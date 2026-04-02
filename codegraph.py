#!/usr/bin/env python3
"""
codegraph — Build a knowledge graph of a codebase for feature identification.

Instead of a flat markdown file, this builds a GRAPH where:
  - Nodes = files, directories, classes, functions, features
  - Edges = imports, contains, calls, co-changes, belongs_to

Given a changed file, you can traverse the graph to find:
  - What feature it belongs to
  - What other files are tightly coupled to it
  - What the blast radius of the change is

Outputs:
  - codegraph.json  — the full graph (queryable)
  - REPO_CONTEXT.md — a compact markdown summary

Usage:
    python codegraph.py /path/to/repo
    python codegraph.py /path/to/repo --llm --api-key sk-...
    python codegraph.py /path/to/repo -o my-output-dir
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import textwrap
from collections import defaultdict
from pathlib import Path
from typing import Optional

# ── Constants ────────────────────────────────────────────────────────────────

MAX_FILE_SIZE = 512_000
MAX_FILES = 10_000
MAX_LINES_SCAN = 300

SKIP_DIRS = {
    "node_modules", ".git", "__pycache__", ".tox", ".mypy_cache",
    ".pytest_cache", "venv", ".venv", "env", ".env", "vendor", "dist",
    "build", "target", ".next", ".nuxt", "coverage", ".cache",
    ".idea", ".vscode", "eggs", ".gradle", ".mvn",
    "Pods", "DerivedData", ".terraform", ".serverless",
}

SKIP_EXTENSIONS = {
    ".min.js", ".min.css", ".map", ".lock", ".svg", ".png", ".jpg",
    ".jpeg", ".gif", ".ico", ".woff", ".woff2", ".ttf", ".eot",
    ".mp3", ".mp4", ".wav", ".zip", ".tar", ".gz", ".bz2", ".rar",
    ".exe", ".dll", ".so", ".dylib", ".o", ".pyc", ".class", ".jar",
    ".db", ".sqlite", ".bin", ".dat", ".pdf",
}

SKIP_FILES = {
    "package-lock.json", "yarn.lock", "pnpm-lock.yaml", "Gemfile.lock",
    "Pipfile.lock", "poetry.lock", "composer.lock", "Cargo.lock",
    "go.sum", ".DS_Store",
}

SOURCE_EXTENSIONS = {
    ".py", ".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs",
    ".go", ".rs", ".java", ".kt", ".cs", ".c", ".cpp", ".h", ".hpp",
    ".rb", ".php", ".swift", ".scala", ".ex", ".exs",
    ".vue", ".svelte", ".dart", ".lua", ".r", ".R",
}

DOC_FILES = {"README.md", "README.rst", "README.txt", "README",
             "ARCHITECTURE.md", "DESIGN.md", "CONTRIBUTING.md"}

MANIFEST_FILES = {"package.json", "requirements.txt", "pyproject.toml",
                  "Cargo.toml", "go.mod", "pom.xml", "build.gradle",
                  "Gemfile", "composer.json", "setup.py", "setup.cfg"}

# Directory name → feature label
FEATURE_KEYWORDS = {
    "auth": "Authentication", "login": "Authentication", "signup": "Registration",
    "user": "User Management", "account": "Account Management",
    "profile": "User Profiles", "admin": "Administration",
    "dashboard": "Dashboard", "api": "API Layer",
    "routes": "Routing", "router": "Routing",
    "middleware": "Middleware", "models": "Data Models",
    "schema": "Data Schema", "migration": "Database Migrations",
    "db": "Database", "database": "Database",
    "store": "State Management", "redux": "Redux State",
    "components": "UI Components", "views": "Views/Pages",
    "pages": "Pages", "layouts": "Layouts",
    "templates": "Templates", "styles": "Styling",
    "utils": "Utilities", "helpers": "Utilities",
    "lib": "Shared Libraries", "common": "Shared Code",
    "core": "Core Logic", "services": "Service Layer",
    "controllers": "Controllers", "handlers": "Handlers",
    "resolvers": "GraphQL Resolvers",
    "config": "Configuration", "settings": "Configuration",
    "tests": "Testing", "test": "Testing", "spec": "Testing",
    "e2e": "E2E Testing", "fixtures": "Test Fixtures",
    "docs": "Documentation", "scripts": "Build Scripts",
    "tools": "Developer Tools", "ci": "CI/CD",
    "deploy": "Deployment", "infra": "Infrastructure",
    "terraform": "Infrastructure", "k8s": "Kubernetes",
    "docker": "Docker", "monitoring": "Monitoring",
    "logging": "Logging", "analytics": "Analytics",
    "i18n": "Internationalization", "locales": "i18n",
    "notifications": "Notifications", "email": "Email",
    "messaging": "Messaging", "chat": "Chat",
    "websocket": "Real-time", "socket": "Real-time",
    "payment": "Payments", "billing": "Billing",
    "checkout": "Checkout", "cart": "Shopping Cart",
    "orders": "Orders", "products": "Product Catalog",
    "search": "Search", "cache": "Caching",
    "queue": "Job Queue", "workers": "Background Workers",
    "jobs": "Background Jobs", "security": "Security",
    "upload": "File Upload", "storage": "File Storage",
    "media": "Media", "plugins": "Plugins",
    "hooks": "Hooks", "graphql": "GraphQL",
    "grpc": "gRPC", "proto": "Protocol Buffers",
}


# ═══════════════════════════════════════════════════════════════════════════
# GRAPH DATA STRUCTURE
# ═══════════════════════════════════════════════════════════════════════════

class CodeGraph:
    """
    A knowledge graph representing a codebase.

    Node types: directory, file, class, function, feature, doc, manifest
    Edge types: contains, imports, calls, exports, co_changes, belongs_to
    """

    def __init__(self, repo_name: str):
        self.repo_name = repo_name
        self.nodes: dict[str, dict] = {}   # id → {type, name, path, ...metadata}
        self.edges: list[dict] = []         # [{source, target, type, ...metadata}]
        self._edge_index: dict[str, list[int]] = defaultdict(list)  # node_id → [edge indices]

    def add_node(self, node_id: str, node_type: str, name: str, **meta) -> str:
        self.nodes[node_id] = {"type": node_type, "name": name, **meta}
        return node_id

    def add_edge(self, source: str, target: str, edge_type: str, **meta):
        idx = len(self.edges)
        self.edges.append({"source": source, "target": target, "type": edge_type, **meta})
        self._edge_index[source].append(idx)
        self._edge_index[target].append(idx)

    def get_neighbors(self, node_id: str, edge_type: str | None = None,
                      direction: str = "both") -> list[dict]:
        """Get neighboring nodes, optionally filtered by edge type and direction."""
        results = []
        for idx in self._edge_index.get(node_id, []):
            edge = self.edges[idx]
            if edge_type and edge["type"] != edge_type:
                continue
            if direction == "outgoing" and edge["source"] != node_id:
                continue
            if direction == "incoming" and edge["target"] != node_id:
                continue
            neighbor_id = edge["target"] if edge["source"] == node_id else edge["source"]
            if neighbor_id in self.nodes:
                results.append({"node": self.nodes[neighbor_id], "id": neighbor_id, "edge": edge})
        return results

    def find_feature(self, file_path: str) -> list[dict]:
        """Find which feature(s) a file belongs to by traversing the graph."""
        file_id = f"file:{file_path}"
        if file_id not in self.nodes:
            # Try partial match
            for nid in self.nodes:
                if nid.endswith(file_path) or file_path.endswith(nid.replace("file:", "")):
                    file_id = nid
                    break
            else:
                return []

        # Direct feature edges
        features = self.get_neighbors(file_id, "belongs_to", "outgoing")
        if features:
            return features

        # Walk up to parent directory and check its feature
        dir_path = str(Path(file_path).parent)
        while dir_path and dir_path != ".":
            dir_id = f"dir:{dir_path}"
            dir_features = self.get_neighbors(dir_id, "belongs_to", "outgoing")
            if dir_features:
                return dir_features
            dir_path = str(Path(dir_path).parent)

        return []

    def blast_radius(self, file_path: str, depth: int = 2) -> dict:
        """
        Find all files that could be affected by a change to the given file.
        Traverses imports, co-changes, and contains edges up to `depth` hops.
        """
        file_id = f"file:{file_path}"
        if file_id not in self.nodes:
            return {"affected": [], "features_touched": set()}

        visited = set()
        frontier = {file_id}
        all_affected = []
        features_touched = set()

        for d in range(depth):
            next_frontier = set()
            for nid in frontier:
                if nid in visited:
                    continue
                visited.add(nid)
                # who imports this file?
                importers = self.get_neighbors(nid, "imports", "incoming")
                for imp in importers:
                    next_frontier.add(imp["id"])
                    if imp["node"]["type"] == "file":
                        all_affected.append({
                            "file": imp["id"].replace("file:", ""),
                            "relationship": "imports_this",
                            "depth": d + 1,
                        })
                # co-change partners
                co_changed = self.get_neighbors(nid, "co_changes", "both")
                for cc in co_changed:
                    if cc["node"]["type"] == "file" and cc["id"] not in visited:
                        all_affected.append({
                            "file": cc["id"].replace("file:", ""),
                            "relationship": "co_changes",
                            "depth": d + 1,
                            "strength": cc["edge"].get("strength", 0),
                        })
                # features
                feats = self.get_neighbors(nid, "belongs_to", "outgoing")
                for f in feats:
                    features_touched.add(f["node"]["name"])

            frontier = next_frontier

        return {"affected": all_affected, "features_touched": features_touched}

    def to_json(self) -> dict:
        return {
            "repo": self.repo_name,
            "node_count": len(self.nodes),
            "edge_count": len(self.edges),
            "nodes": self.nodes,
            "edges": self.edges,
        }

    @classmethod
    def from_json(cls, data: dict) -> "CodeGraph":
        g = cls(data["repo"])
        g.nodes = data["nodes"]
        g.edges = data["edges"]
        # rebuild edge index
        for idx, edge in enumerate(g.edges):
            g._edge_index[edge["source"]].append(idx)
            g._edge_index[edge["target"]].append(idx)
        return g

    def stats(self) -> dict:
        type_counts = defaultdict(int)
        for n in self.nodes.values():
            type_counts[n["type"]] += 1
        edge_type_counts = defaultdict(int)
        for e in self.edges:
            edge_type_counts[e["type"]] += 1
        return {"nodes": dict(type_counts), "edges": dict(edge_type_counts)}


# ═══════════════════════════════════════════════════════════════════════════
# PARSERS — Extract symbols and imports from source files
# ═══════════════════════════════════════════════════════════════════════════

def _read_file(path: Path, max_lines: int = MAX_LINES_SCAN) -> str:
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            lines = []
            for i, line in enumerate(f):
                if i >= max_lines:
                    break
                lines.append(line)
            return "".join(lines)
    except Exception:
        return ""


def _extract_docstring(text: str, ext: str) -> str:
    """Extract the leading docstring or comment block."""
    lines = text.split("\n")

    if ext == ".py":
        stripped = text.strip()
        for delim in ('"""', "'''"):
            if stripped.startswith(delim):
                end = stripped.find(delim, len(delim))
                if end != -1:
                    return stripped[len(delim):end].strip()
                return stripped[len(delim):].strip()

    if ext in (".js", ".jsx", ".ts", ".tsx", ".java", ".kt", ".cs",
               ".go", ".rs", ".c", ".cpp", ".h", ".hpp", ".swift", ".php",
               ".scala", ".dart"):
        stripped = text.strip()
        if stripped.startswith("/*"):
            end = stripped.find("*/")
            if end != -1:
                comment = stripped[2:end]
                cleaned = "\n".join(
                    re.sub(r"^\s*\*\s?", "", l) for l in comment.split("\n")
                )
                return cleaned.strip()

    comment_char = "#" if ext in (".py", ".rb", ".sh", ".yaml", ".yml") else "//"
    block = []
    for line in lines:
        s = line.strip()
        if s.startswith("#!"):
            continue
        if s.startswith(comment_char):
            block.append(s[len(comment_char):].strip())
        elif s == "":
            if block:
                break
            continue
        else:
            break
    return "\n".join(block).strip() if block else ""


# ── Import extraction patterns ──────────────────────────────────────────

IMPORT_PATTERNS = {
    ".py": [
        re.compile(r"^\s*import\s+([\w.]+)"),
        re.compile(r"^\s*from\s+([\w.]+)\s+import"),
    ],
    ".js": [
        re.compile(r"""^\s*import\s+.*?from\s+['"]([@\w./-]+)['"]"""),
        re.compile(r"""^\s*(?:const|let|var)\s+.*?=\s*require\(\s*['"]([@\w./-]+)['"]\s*\)"""),
        re.compile(r"""^\s*import\s+['"]([@\w./-]+)['"]"""),
    ],
    ".go": [
        re.compile(r"""^\s*"([\w./-]+)"\s*$"""),
        re.compile(r"""^\s*\w+\s+"([\w./-]+)"\s*$"""),
    ],
    ".rs": [
        re.compile(r"^\s*use\s+([\w:]+)"),
        re.compile(r"^\s*extern\s+crate\s+(\w+)"),
    ],
    ".java": [
        re.compile(r"^\s*import\s+([\w.]+)"),
    ],
    ".rb": [
        re.compile(r"""^\s*require\s+['"]([\w./-]+)['"]"""),
        re.compile(r"""^\s*require_relative\s+['"]([\w./-]+)['"]"""),
    ],
    ".php": [
        re.compile(r"^\s*(?:use|require|include|require_once|include_once)\s+['\"]?([\w\\/.]+)"),
    ],
}
# aliases
for _ext in (".jsx", ".ts", ".tsx", ".mjs", ".cjs", ".vue", ".svelte"):
    IMPORT_PATTERNS[_ext] = IMPORT_PATTERNS[".js"]
for _ext in (".kt", ".scala"):
    IMPORT_PATTERNS[_ext] = IMPORT_PATTERNS[".java"]
IMPORT_PATTERNS[".cs"] = [re.compile(r"^\s*using\s+([\w.]+)")]
IMPORT_PATTERNS[".swift"] = [re.compile(r"^\s*import\s+(\w+)")]
IMPORT_PATTERNS[".dart"] = [re.compile(r"""^\s*import\s+['"]([\w./:]+)['"]""")]


# ── Symbol extraction patterns ──────────────────────────────────────────

SYMBOL_PATTERNS = {
    ".py": {
        "class": re.compile(r"^\s*class\s+(\w+)"),
        "function": re.compile(r"^\s*(?:async\s+)?def\s+(\w+)"),
    },
    ".js": {
        "class": re.compile(r"^\s*(?:export\s+)?(?:default\s+)?class\s+(\w+)"),
        "function": re.compile(
            r"^\s*(?:export\s+)?(?:default\s+)?(?:async\s+)?function\s+(\w+)"
        ),
        "const_fn": re.compile(
            r"^\s*(?:export\s+)?(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s+)?\("
        ),
    },
    ".go": {
        "function": re.compile(r"^\s*func\s+(?:\(\w+\s+\*?\w+\)\s+)?(\w+)"),
        "type": re.compile(r"^\s*type\s+(\w+)\s+(?:struct|interface)"),
    },
    ".rs": {
        "function": re.compile(r"^\s*(?:pub\s+)?(?:async\s+)?fn\s+(\w+)"),
        "struct": re.compile(r"^\s*(?:pub\s+)?struct\s+(\w+)"),
        "enum": re.compile(r"^\s*(?:pub\s+)?enum\s+(\w+)"),
        "trait": re.compile(r"^\s*(?:pub\s+)?trait\s+(\w+)"),
        "impl": re.compile(r"^\s*impl(?:<[^>]*>)?\s+(\w+)"),
    },
    ".java": {
        "class": re.compile(r"^\s*(?:public|private|protected)?\s*(?:static\s+)?(?:abstract\s+)?(?:final\s+)?(?:class|interface|enum|record)\s+(\w+)"),
        "method": re.compile(r"^\s*(?:public|private|protected)\s+(?:static\s+)?(?:abstract\s+)?(?:final\s+)?\w[\w<>\[\]]*\s+(\w+)\s*\("),
    },
    ".rb": {
        "class": re.compile(r"^\s*class\s+(\w+)"),
        "module": re.compile(r"^\s*module\s+(\w+)"),
        "function": re.compile(r"^\s*def\s+(\w+)"),
    },
    ".php": {
        "class": re.compile(r"^\s*(?:abstract\s+)?class\s+(\w+)"),
        "function": re.compile(r"^\s*(?:public|private|protected|static|\s)*function\s+(\w+)"),
    },
    ".swift": {
        "class": re.compile(r"^\s*(?:class|struct|enum|protocol)\s+(\w+)"),
        "function": re.compile(r"^\s*(?:public|private|internal|open)?\s*(?:static\s+)?func\s+(\w+)"),
    },
}
for _ext in (".jsx", ".ts", ".tsx", ".mjs", ".cjs"):
    SYMBOL_PATTERNS[_ext] = SYMBOL_PATTERNS[".js"]
for _ext in (".kt",):
    SYMBOL_PATTERNS[_ext] = {
        "class": re.compile(r"^\s*(?:data\s+)?class\s+(\w+)"),
        "function": re.compile(r"^\s*(?:fun|suspend\s+fun)\s+(\w+)"),
    }
SYMBOL_PATTERNS[".cs"] = {
    "class": re.compile(r"^\s*(?:public|internal|private)?\s*(?:static\s+)?(?:abstract\s+)?(?:partial\s+)?(?:class|interface|enum|struct|record)\s+(\w+)"),
    "method": re.compile(r"^\s*(?:public|private|protected|internal)\s+(?:static\s+)?(?:async\s+)?(?:virtual\s+)?(?:override\s+)?\w[\w<>\[\]]*\s+(\w+)\s*\("),
}
SYMBOL_PATTERNS[".c"] = {
    "function": re.compile(r"^\s*(?:static\s+|extern\s+|inline\s+)*\w[\w\s*]*\s+(\w+)\s*\([^)]*\)\s*\{"),
    "struct": re.compile(r"^\s*(?:typedef\s+)?struct\s+(\w+)"),
}
SYMBOL_PATTERNS[".cpp"] = SYMBOL_PATTERNS[".c"]
SYMBOL_PATTERNS[".h"] = SYMBOL_PATTERNS[".c"]
SYMBOL_PATTERNS[".hpp"] = SYMBOL_PATTERNS[".c"]


def parse_file(path: Path, ext: str) -> dict:
    """Parse a source file and extract its symbols and imports."""
    text = _read_file(path)
    if not text:
        return {"imports": [], "symbols": [], "docstring": ""}

    # Docstring
    docstring = _extract_docstring(text, ext)

    # Imports
    imports = []
    patterns = IMPORT_PATTERNS.get(ext, [])
    for line in text.split("\n"):
        for pat in patterns:
            m = pat.match(line)
            if m:
                imports.append(m.group(1))
                break

    # Symbols (classes, functions, etc.)
    symbols = []
    sym_patterns = SYMBOL_PATTERNS.get(ext, {})
    for line in text.split("\n"):
        for sym_type, pat in sym_patterns.items():
            m = pat.match(line)
            if m:
                symbols.append({"type": sym_type, "name": m.group(1)})
                break

    return {"imports": imports, "symbols": symbols, "docstring": docstring}


# ═══════════════════════════════════════════════════════════════════════════
# IMPORT → FILE RESOLUTION
# ═══════════════════════════════════════════════════════════════════════════

def build_import_resolver(all_files: list[str]) -> dict[str, str]:
    """
    Build a lookup table that resolves import strings to file paths.
    E.g., "src.auth.login" → "src/auth/login.py"
          "./utils/helpers" → "src/utils/helpers.ts"
    """
    resolver = {}
    for fpath in all_files:
        p = Path(fpath)
        stem = str(p.with_suffix(""))  # e.g., "src/auth/login"

        # Dot-notation (Python style)
        dot_form = stem.replace("/", ".").replace("\\", ".")
        resolver[dot_form] = fpath

        # Slash-notation (JS/Go style)
        resolver[stem] = fpath
        resolver["./" + stem] = fpath
        resolver["../" + stem] = fpath  # rough approximation

        # Just the filename without extension
        resolver[p.stem] = fpath

        # For index files, also register the directory
        if p.stem in ("index", "__init__", "mod"):
            dir_form = str(p.parent)
            resolver[dir_form] = fpath
            resolver[dir_form.replace("/", ".")] = fpath

    return resolver


# ═══════════════════════════════════════════════════════════════════════════
# GIT CO-CHANGE ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════

def get_co_changes(repo_root: Path, min_commits: int = 3) -> list[tuple[str, str, int]]:
    """
    Find files that frequently change together in the same commit.
    Returns [(file_a, file_b, co_commit_count), ...] for pairs above min_commits.
    """
    try:
        result = subprocess.run(
            ["git", "log", "--all", "--name-only", "--pretty=format:---COMMIT---"],
            capture_output=True, text=True, cwd=repo_root, timeout=30,
        )
        if result.returncode != 0:
            return []
    except Exception:
        return []

    # Parse commits
    commits = []
    current: list[str] = []
    for line in result.stdout.split("\n"):
        line = line.strip()
        if line == "---COMMIT---":
            if current:
                commits.append(current)
            current = []
        elif line:
            current.append(line)
    if current:
        commits.append(current)

    # Count co-occurrences
    pair_counts: dict[tuple[str, str], int] = defaultdict(int)
    for files in commits:
        files = sorted(set(files))
        for i in range(len(files)):
            for j in range(i + 1, min(i + 20, len(files))):  # cap pairs per commit
                pair = (files[i], files[j])
                pair_counts[pair] += 1

    return [(a, b, c) for (a, b), c in pair_counts.items() if c >= min_commits]


# ═══════════════════════════════════════════════════════════════════════════
# GRAPH BUILDER
# ═══════════════════════════════════════════════════════════════════════════

def build_graph(repo_root: Path) -> CodeGraph:
    """Walk a repository and build the full code knowledge graph."""

    repo_name = repo_root.resolve().name
    graph = CodeGraph(repo_name)

    # Track all source files for import resolution
    all_source_files: list[str] = []
    file_data: dict[str, dict] = {}  # rel_path → parse results

    # ── Pass 1: Collect all files, build directory and file nodes ─────────
    for root_str, dirs, files in os.walk(repo_root):
        dirs[:] = sorted([d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")])
        root_path = Path(root_str)
        rel_dir = str(root_path.relative_to(repo_root))
        if rel_dir == ".":
            rel_dir = ""

        # Directory node
        if rel_dir:
            dir_id = f"dir:{rel_dir}"
            graph.add_node(dir_id, "directory", rel_dir.split("/")[-1], path=rel_dir)

            # contains edge from parent
            parent = str(Path(rel_dir).parent)
            parent_id = f"dir:{parent}" if parent != "." else f"dir:"
            if parent_id in graph.nodes:
                graph.add_edge(parent_id, dir_id, "contains")

            # Detect feature from directory name
            dir_name_lower = rel_dir.split("/")[-1].lower().replace("-", "").replace("_", "")
            for kw, label in FEATURE_KEYWORDS.items():
                if kw in dir_name_lower:
                    feat_id = f"feature:{label}"
                    if feat_id not in graph.nodes:
                        graph.add_node(feat_id, "feature", label)
                    graph.add_edge(dir_id, feat_id, "belongs_to")
                    break

        for fname in sorted(files):
            fpath = root_path / fname
            rel_file = str(fpath.relative_to(repo_root))

            # Skip unwanted files
            if fname in SKIP_FILES:
                continue
            suffix = fpath.suffix.lower()
            if suffix in SKIP_EXTENSIONS:
                continue
            if fname.endswith(".min.js") or fname.endswith(".min.css"):
                continue
            try:
                if fpath.stat().st_size > MAX_FILE_SIZE:
                    continue
            except OSError:
                continue

            # Doc files
            if fname in DOC_FILES:
                doc_id = f"doc:{rel_file}"
                try:
                    with open(fpath, "r", encoding="utf-8", errors="replace") as f:
                        content = f.read(3000)
                except Exception:
                    content = ""
                graph.add_node(doc_id, "doc", fname, path=rel_file,
                               content=content[:1000])
                if rel_dir:
                    graph.add_edge(f"dir:{rel_dir}", doc_id, "contains")
                continue

            # Manifest files
            if fname in MANIFEST_FILES:
                man_id = f"manifest:{rel_file}"
                try:
                    with open(fpath, "r", encoding="utf-8", errors="replace") as f:
                        raw = f.read(3000)
                    if fname == "package.json":
                        data = json.loads(raw)
                        content = json.dumps({k: data.get(k) for k in
                            ("name", "description", "scripts", "dependencies",
                             "devDependencies") if k in data}, indent=2)
                    else:
                        content = raw
                except Exception:
                    content = ""
                graph.add_node(man_id, "manifest", fname, path=rel_file,
                               content=content[:2000])
                continue

            # Source files
            if suffix in SOURCE_EXTENSIONS:
                file_id = f"file:{rel_file}"
                parsed = parse_file(fpath, suffix)
                file_data[rel_file] = parsed
                all_source_files.append(rel_file)

                graph.add_node(file_id, "file", fname, path=rel_file,
                               language=suffix.lstrip("."),
                               docstring=parsed["docstring"][:300],
                               symbol_count=len(parsed["symbols"]),
                               import_count=len(parsed["imports"]))

                # contains edge from directory
                if rel_dir:
                    graph.add_edge(f"dir:{rel_dir}", file_id, "contains")

                # File inherits feature from parent directory
                if rel_dir:
                    dir_id = f"dir:{rel_dir}"
                    dir_features = graph.get_neighbors(dir_id, "belongs_to", "outgoing")
                    for feat in dir_features:
                        graph.add_edge(file_id, feat["id"], "belongs_to")

                # Add symbol nodes
                for sym in parsed["symbols"][:30]:
                    sym_id = f"symbol:{rel_file}::{sym['name']}"
                    graph.add_node(sym_id, sym["type"], sym["name"],
                                   file=rel_file)
                    graph.add_edge(file_id, sym_id, "contains")

                if len(all_source_files) >= MAX_FILES:
                    break

    # ── Pass 2: Resolve imports to create edges ──────────────────────────
    resolver = build_import_resolver(all_source_files)

    for rel_file, parsed in file_data.items():
        file_id = f"file:{rel_file}"
        file_dir = str(Path(rel_file).parent)

        for imp in parsed["imports"]:
            # Try to resolve the import to a file in the repo
            resolved = None

            # Direct resolution
            if imp in resolver:
                resolved = resolver[imp]

            # Relative resolution (from file's directory)
            if not resolved:
                relative_imp = imp.lstrip("./")
                candidates = [
                    f"{file_dir}/{relative_imp}",
                    f"{file_dir}/{relative_imp}".replace(".", "/"),
                ]
                for c in candidates:
                    if c in resolver:
                        resolved = resolver[c]
                        break

            # Module-level resolution (try removing common prefixes)
            if not resolved:
                parts = imp.replace(".", "/").replace("::", "/").split("/")
                for i in range(len(parts)):
                    partial = "/".join(parts[i:])
                    if partial in resolver:
                        resolved = resolver[partial]
                        break

            if resolved and resolved != rel_file:
                target_id = f"file:{resolved}"
                if target_id in graph.nodes:
                    graph.add_edge(file_id, target_id, "imports",
                                   import_string=imp)

    # ── Pass 3: Git co-change analysis ───────────────────────────────────
    co_changes = get_co_changes(repo_root)
    for file_a, file_b, count in co_changes:
        id_a = f"file:{file_a}"
        id_b = f"file:{file_b}"
        if id_a in graph.nodes and id_b in graph.nodes:
            graph.add_edge(id_a, id_b, "co_changes", strength=count)

    return graph


# ═══════════════════════════════════════════════════════════════════════════
# MARKDOWN EXPORT
# ═══════════════════════════════════════════════════════════════════════════

def graph_to_markdown(graph: CodeGraph) -> str:
    """Convert the graph to a compact, readable markdown file."""
    lines = [
        f"# Code Knowledge Graph: {graph.repo_name}\n",
        "> A graph-based knowledge map for feature identification.\n",
    ]

    stats = graph.stats()

    # ── Overview ─────────────────────────────────────────────────────────
    lines.append("## Overview\n")
    lines.append(f"| Metric | Count |")
    lines.append(f"|--------|-------|")
    for ntype, count in sorted(stats["nodes"].items()):
        lines.append(f"| {ntype} nodes | {count} |")
    for etype, count in sorted(stats["edges"].items()):
        lines.append(f"| {etype} edges | {count} |")
    lines.append("")

    # ── Feature Map ──────────────────────────────────────────────────────
    feature_nodes = {nid: n for nid, n in graph.nodes.items() if n["type"] == "feature"}
    if feature_nodes:
        lines.append("## Feature Map\n")
        for feat_id, feat in sorted(feature_nodes.items(), key=lambda x: x[1]["name"]):
            lines.append(f"### {feat['name']}\n")
            # Directories
            dirs = graph.get_neighbors(feat_id, "belongs_to", "incoming")
            dir_list = [d for d in dirs if d["node"]["type"] == "directory"]
            file_list = [d for d in dirs if d["node"]["type"] == "file"]
            if dir_list:
                lines.append("**Directories:**")
                for d in dir_list:
                    lines.append(f"- `{d['node'].get('path', d['node']['name'])}/`")
            if file_list:
                lines.append("**Key files:**")
                for f in sorted(file_list, key=lambda x: x["node"].get("path", ""))[:20]:
                    doc = f["node"].get("docstring", "")
                    path = f["node"].get("path", f["node"]["name"])
                    if doc:
                        lines.append(f"- `{path}` — {doc[:100]}")
                    else:
                        lines.append(f"- `{path}`")
            lines.append("")

    # ── File Context (with imports and symbols) ──────────────────────────
    lines.append("## File Details\n")
    file_nodes = sorted(
        [(nid, n) for nid, n in graph.nodes.items() if n["type"] == "file"],
        key=lambda x: x[1].get("path", "")
    )
    for file_id, fnode in file_nodes:
        path = fnode.get("path", fnode["name"])
        docstring = fnode.get("docstring", "")
        lines.append(f"### `{path}`")
        if docstring:
            lines.append(f"**Purpose:** {docstring[:200]}")

        # Features
        feats = graph.get_neighbors(file_id, "belongs_to", "outgoing")
        if feats:
            feat_names = ", ".join(f["node"]["name"] for f in feats)
            lines.append(f"**Feature:** {feat_names}")

        # Imports (resolved to internal files only)
        imports = graph.get_neighbors(file_id, "imports", "outgoing")
        if imports:
            imp_paths = [i["node"].get("path", i["node"]["name"]) for i in imports]
            lines.append(f"**Imports:** {', '.join(f'`{p}`' for p in imp_paths[:10])}")

        # Imported by
        importers = graph.get_neighbors(file_id, "imports", "incoming")
        if importers:
            imp_paths = [i["node"].get("path", i["node"]["name"]) for i in importers]
            lines.append(f"**Imported by:** {', '.join(f'`{p}`' for p in imp_paths[:10])}")

        # Symbols
        symbols = graph.get_neighbors(file_id, "contains", "outgoing")
        sym_nodes = [s for s in symbols if s["node"]["type"] in
                     ("class", "function", "const_fn", "method", "struct",
                      "enum", "trait", "impl", "module", "type")]
        if sym_nodes:
            sym_strs = [f"{s['node']['type']}:`{s['node']['name']}`" for s in sym_nodes[:15]]
            lines.append(f"**Symbols:** {', '.join(sym_strs)}")

        # Co-changes
        co = graph.get_neighbors(file_id, "co_changes")
        if co:
            co_sorted = sorted(co, key=lambda x: -x["edge"].get("strength", 0))[:5]
            co_strs = [f"`{c['node'].get('path', c['node']['name'])}` ({c['edge'].get('strength', '?')}x)"
                       for c in co_sorted]
            lines.append(f"**Often changes with:** {', '.join(co_strs)}")

        lines.append("")

    # ── Dependency graph (adjacency list) ────────────────────────────────
    import_edges = [e for e in graph.edges if e["type"] == "imports"]
    if import_edges:
        lines.append("## Import Graph (Adjacency List)\n")
        lines.append("```")
        by_source = defaultdict(list)
        for e in import_edges:
            src = e["source"].replace("file:", "")
            tgt = e["target"].replace("file:", "")
            by_source[src].append(tgt)
        for src, targets in sorted(by_source.items()):
            lines.append(f"{src} → {', '.join(targets)}")
        lines.append("```\n")

    # ── Documentation ────────────────────────────────────────────────────
    doc_nodes = [(nid, n) for nid, n in graph.nodes.items() if n["type"] == "doc"]
    if doc_nodes:
        lines.append("## Documentation\n")
        for doc_id, doc in doc_nodes:
            lines.append(f"### {doc.get('path', doc['name'])}\n")
            content = doc.get("content", "")
            if content:
                lines.append(content)
            lines.append("")

    return "\n".join(lines)


# ═══════════════════════════════════════════════════════════════════════════
# LLM ENRICHMENT
# ═══════════════════════════════════════════════════════════════════════════

def enrich_with_llm(graph: CodeGraph, api_key: str) -> CodeGraph:
    """
    Send the graph summary to an LLM to:
    1. Identify higher-level features that directory naming missed
    2. Group files into semantic clusters
    3. Add feature descriptions
    """
    import urllib.request

    md = graph_to_markdown(graph)

    prompt = textwrap.dedent("""\
        You are a senior software architect analyzing a codebase knowledge graph.

        Below is a graph-based extraction of a repository showing files, their
        imports, symbols, and auto-detected features.

        Your job:
        1. Identify any ADDITIONAL features/domains not already detected
        2. For any files without a feature assignment, determine which feature
           they belong to
        3. Write a description for each feature (1-2 sentences)

        Respond ONLY with a valid JSON object (no markdown fences) like:
        {
            "features": [
                {
                    "name": "Authentication",
                    "description": "Handles user login, registration, JWT tokens, and session management.",
                    "files": ["src/auth/login.py", "src/auth/middleware.py"],
                    "directories": ["src/auth"]
                }
            ],
            "unmapped_file_features": {
                "src/utils/crypto.py": "Authentication",
                "src/lib/validator.ts": "Data Validation"
            }
        }

        --- REPO GRAPH ---
        {context}
        --- END ---
    """).format(context=md[:80_000])

    body = json.dumps({
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 4000,
        "messages": [{"role": "user", "content": prompt}],
    }).encode()

    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=body,
        headers={
            "Content-Type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode())
            text = "".join(b.get("text", "") for b in data.get("content", []))
            # Clean markdown fences if present
            text = re.sub(r"```json\s*", "", text)
            text = re.sub(r"```\s*", "", text)
            enrichment = json.loads(text.strip())
    except Exception as e:
        print(f"[!] LLM enrichment failed: {e}", file=sys.stderr)
        return graph

    # Apply enrichment to graph
    for feat in enrichment.get("features", []):
        feat_id = f"feature:{feat['name']}"
        if feat_id not in graph.nodes:
            graph.add_node(feat_id, "feature", feat["name"],
                           description=feat.get("description", ""))
        elif "description" in feat:
            graph.nodes[feat_id]["description"] = feat["description"]

        for fpath in feat.get("files", []):
            file_id = f"file:{fpath}"
            if file_id in graph.nodes:
                graph.add_edge(file_id, feat_id, "belongs_to", source="llm")

        for dpath in feat.get("directories", []):
            dir_id = f"dir:{dpath}"
            if dir_id in graph.nodes:
                graph.add_edge(dir_id, feat_id, "belongs_to", source="llm")

    for fpath, feat_name in enrichment.get("unmapped_file_features", {}).items():
        feat_id = f"feature:{feat_name}"
        if feat_id not in graph.nodes:
            graph.add_node(feat_id, "feature", feat_name)
        file_id = f"file:{fpath}"
        if file_id in graph.nodes:
            graph.add_edge(file_id, feat_id, "belongs_to", source="llm")

    return graph


# ═══════════════════════════════════════════════════════════════════════════
# QUERY INTERFACE
# ═══════════════════════════════════════════════════════════════════════════

def query_file(graph: CodeGraph, file_path: str) -> dict:
    """Query the graph for everything known about a file."""
    file_path = file_path.strip().lstrip("./")
    file_id = f"file:{file_path}"

    if file_id not in graph.nodes:
        # Try partial match
        matches = [nid for nid in graph.nodes if nid.endswith(file_path)]
        if matches:
            file_id = matches[0]
        else:
            return {"error": f"File '{file_path}' not found in graph"}

    node = graph.nodes[file_id]

    # Features
    features = graph.find_feature(file_path)
    feature_names = [f["node"]["name"] for f in features]

    # Blast radius
    blast = graph.blast_radius(file_path)

    # Imports
    imports_out = graph.get_neighbors(file_id, "imports", "outgoing")
    imports_in = graph.get_neighbors(file_id, "imports", "incoming")

    # Symbols
    symbols = graph.get_neighbors(file_id, "contains", "outgoing")

    return {
        "file": file_path,
        "language": node.get("language", "unknown"),
        "docstring": node.get("docstring", ""),
        "features": feature_names,
        "imports": [i["node"].get("path", "") for i in imports_out],
        "imported_by": [i["node"].get("path", "") for i in imports_in],
        "symbols": [{"type": s["node"]["type"], "name": s["node"]["name"]}
                     for s in symbols if s["node"]["type"] != "file"],
        "blast_radius": {
            "affected_files": blast["affected"][:20],
            "features_touched": list(blast["features_touched"]),
        },
    }


# ═══════════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Build a code knowledge graph from a repository.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", help="Command to run")

    # ── build ────────────────────────────────────────────────────────────
    build_cmd = sub.add_parser("build", help="Build the knowledge graph")
    build_cmd.add_argument("repo", type=Path, help="Path to the repository root")
    build_cmd.add_argument("-o", "--output", type=Path, default=None,
                           help="Output directory (default: <repo>/.codegraph/)")
    build_cmd.add_argument("--llm", action="store_true",
                           help="Enrich with LLM-generated feature summaries")
    build_cmd.add_argument("--api-key", type=str, default=None,
                           help="Anthropic API key (or set ANTHROPIC_API_KEY)")

    # ── query ────────────────────────────────────────────────────────────
    query_cmd = sub.add_parser("query", help="Query a file's feature and context")
    query_cmd.add_argument("file", type=str, help="File path to query")
    query_cmd.add_argument("--graph", type=Path, default=Path("codegraph.json"),
                           help="Path to codegraph.json")

    # ── blast ────────────────────────────────────────────────────────────
    blast_cmd = sub.add_parser("blast", help="Show the blast radius of a file change")
    blast_cmd.add_argument("file", type=str, help="File path to analyze")
    blast_cmd.add_argument("--graph", type=Path, default=Path("codegraph.json"))
    blast_cmd.add_argument("--depth", type=int, default=2, help="Traversal depth")

    # ── Default: treat first arg as repo path for backwards compat ───────
    args = parser.parse_args()

    if args.command is None:
        # If no subcommand but args exist, assume "build"
        if len(sys.argv) > 1 and Path(sys.argv[1]).is_dir():
            sys.argv.insert(1, "build")
            args = parser.parse_args()
        else:
            parser.print_help()
            sys.exit(1)

    if args.command == "build":
        if not args.repo.is_dir():
            print(f"Error: '{args.repo}' is not a directory.", file=sys.stderr)
            sys.exit(1)

        repo_root = args.repo.resolve()
        out_dir = args.output or Path(".")

        print(f"[*] Building knowledge graph: {repo_root}")
        graph = build_graph(repo_root)

        if args.llm:
            api_key = args.api_key or os.environ.get("ANTHROPIC_API_KEY", "")
            if not api_key:
                print("[!] --llm requires ANTHROPIC_API_KEY", file=sys.stderr)
                sys.exit(1)
            print("[*] Enriching with LLM...")
            graph = enrich_with_llm(graph, api_key)

        stats = graph.stats()
        print(f"[✓] Graph built: {sum(stats['nodes'].values())} nodes, "
              f"{sum(stats['edges'].values())} edges")

        # Write JSON graph
        json_path = out_dir / "codegraph.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(graph.to_json(), f, indent=2, default=str)
        json_size = json_path.stat().st_size / 1024
        print(f"    Graph: {json_path} ({json_size:.1f} KB)")

        # Write markdown
        md_path = out_dir / "REPO_CONTEXT.md"
        md_content = graph_to_markdown(graph)
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        md_size = md_path.stat().st_size / 1024
        print(f"    Markdown: {md_path} ({md_size:.1f} KB)")

    elif args.command == "query":
        if not args.graph.exists():
            print(f"Error: '{args.graph}' not found. Run 'codegraph build' first.",
                  file=sys.stderr)
            sys.exit(1)
        with open(args.graph) as f:
            graph = CodeGraph.from_json(json.load(f))
        result = query_file(graph, args.file)
        print(json.dumps(result, indent=2, default=list))

    elif args.command == "blast":
        if not args.graph.exists():
            print(f"Error: '{args.graph}' not found.", file=sys.stderr)
            sys.exit(1)
        with open(args.graph) as f:
            graph = CodeGraph.from_json(json.load(f))
        result = graph.blast_radius(args.file.strip().lstrip("./"), args.depth)
        print(json.dumps({
            "file": args.file,
            "features_touched": list(result["features_touched"]),
            "affected_files": result["affected"],
        }, indent=2, default=list))


if __name__ == "__main__":
    main()
