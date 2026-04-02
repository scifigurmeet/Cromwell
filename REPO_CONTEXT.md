# Code Knowledge Graph: Cromwell

> A graph-based knowledge map for feature identification.

## Overview

| Metric | Count |
|--------|-------|
| class nodes | 236 |
| const_fn nodes | 1095 |
| directory nodes | 392 |
| doc nodes | 14 |
| feature nodes | 35 |
| file nodes | 988 |
| function nodes | 221 |
| manifest nodes | 21 |
| belongs_to edges | 568 |
| co_changes edges | 4648 |
| contains edges | 2945 |
| imports edges | 1575 |

## Feature Map

### API Layer

**Directories:**
- `system/admin/src/pages/api/`
- `system/core/frontend/src/api/`
- `website/api-generator/`
**Key files:**
- `system/admin/src/pages/api/public-env.ts`
- `system/core/frontend/src/api/CGraphQLClient.ts`
- `system/core/frontend/src/api/CRestApiClient.ts`
- `system/core/frontend/src/api/CWebSocketClient.ts`
- `system/core/frontend/src/api/CentralServerClient.ts`
- `website/api-generator/generate.js`

### Account Management

**Directories:**
- `toolkits/commerce/src/base/AccountInfo/`
- `toolkits/commerce/src/base/AccountOrders/`
**Key files:**
- `toolkits/commerce/src/base/AccountInfo/AccountInfo.test.tsx`
- `toolkits/commerce/src/base/AccountInfo/AccountInfo.tsx`
- `toolkits/commerce/src/base/AccountInfo/DefaultElements.tsx`
- `toolkits/commerce/src/base/AccountInfo/actions.ts`
- `toolkits/commerce/src/base/AccountOrders/AccountOrders.test.tsx`
- `toolkits/commerce/src/base/AccountOrders/AccountOrders.tsx`

### Administration

**Directories:**
- `plugins/main-menu/src/admin/`
- `plugins/main-menu/tests/admin/`
- `plugins/marqo/src/admin/`
- `plugins/newsletter/src/admin/`
- `plugins/newsletter/tests/admin/`
- `plugins/paypal/src/admin/`
- `plugins/paypal/tests/admin/`
- `plugins/product-filter/src/admin/`
- `plugins/product-filter/tests/admin/`
- `plugins/product-showcase/src/admin/`
- `plugins/product-showcase/tests/admin/`
- `plugins/stripe/src/admin/`
- `plugins/stripe/tests/admin/`
- `system/admin/`
- `system/core/frontend/src/components/AdminPanelWidget/`
- `themes/store/src/admin-panel/`
**Key files:**
- `plugins/main-menu/src/admin/icons.tsx`
- `plugins/main-menu/src/admin/index.tsx`
- `plugins/main-menu/src/admin/styles.ts`
- `plugins/main-menu/tests/admin/SettingsPage.test.tsx`
- `plugins/marqo/src/admin/index.tsx`
- `plugins/newsletter/src/admin/index.tsx`
- `plugins/newsletter/src/admin/styles.ts`
- `plugins/newsletter/tests/admin/Dashboard.test.tsx`
- `plugins/newsletter/tests/admin/SettingsPage.test.tsx`
- `plugins/paypal/src/admin/index.tsx`
- `plugins/paypal/tests/admin/SettingsPage.test.tsx`
- `plugins/product-filter/src/admin/index.tsx`
- `plugins/product-filter/tests/admin/SettingsPage.test.tsx`
- `plugins/product-showcase/src/admin/index.tsx`
- `plugins/product-showcase/tests/admin/SettingsPage.test.tsx`
- `plugins/stripe/src/admin/index.tsx`
- `plugins/stripe/tests/admin/SettingsPage.test.tsx`
- `system/admin/.eslintrc.js`
- `system/admin/jest.config.ts`
- `system/admin/next-env.d.ts` — / <reference types="next" />
/ <reference types="next/image-types/global" />

### Authentication

**Directories:**
- `system/admin/src/router-pages/login/`
**Key files:**
- `system/admin/src/router-pages/login/LoginPage.test.tsx`
- `system/admin/src/router-pages/login/LoginPage.tsx`

### CI/CD

**Directories:**
- `system/core/frontend/src/components/CImage/`
**Key files:**
- `system/core/frontend/src/components/CImage/CImage.test.tsx`
- `system/core/frontend/src/components/CImage/CImage.tsx`

### Checkout

**Directories:**
- `toolkits/commerce/src/base/Checkout/`
**Key files:**
- `toolkits/commerce/src/base/Checkout/Checkout.test.tsx`
- `toolkits/commerce/src/base/Checkout/Checkout.tsx`
- `toolkits/commerce/src/base/Checkout/Coupons.tsx`
- `toolkits/commerce/src/base/Checkout/DefaultElements.tsx`
- `toolkits/commerce/src/base/Checkout/actions.ts`

### Configuration

**Directories:**
- `system/admin/src/components/pluginSettingsLayout/`
- `system/admin/src/router-pages/settings/`
**Key files:**
- `system/admin/src/components/pluginSettingsLayout/PluginSettingsLayout.tsx`
- `system/admin/src/router-pages/settings/Settings.test.tsx`
- `system/admin/src/router-pages/settings/Settings.tsx`
- `system/admin/src/router-pages/settings/types.ts`

### Controllers

**Directories:**
- `plugins/marqo/src/backend/controllers/`
- `plugins/newsletter/src/backend/controllers/`
- `system/server/src/controllers/`
- `system/server/tests/controllers/`
**Key files:**
- `plugins/marqo/src/backend/controllers/plugin-marqo.controller.ts`
- `plugins/newsletter/src/backend/controllers/plugin-newsletter.controller.ts`
- `system/server/src/controllers/auth.controller.ts`
- `system/server/src/controllers/cms.controller.ts`
- `system/server/src/controllers/mock.controller.ts`
- `system/server/src/controllers/plugin.controller.ts`
- `system/server/src/controllers/renderer.controller.ts`
- `system/server/src/controllers/theme.controller.ts`
- `system/server/tests/controllers/auth.controller.spec.ts`
- `system/server/tests/controllers/cms.controller.spec.ts`
- `system/server/tests/controllers/plugin.controller.spec.ts`
- `system/server/tests/controllers/theme.controller.spec.ts`

### Core Logic

**Directories:**
- `system/core/`
- `website/api-generator/core/`

### Dashboard

**Directories:**
- `system/admin/src/router-pages/dashboard/`
**Key files:**
- `system/admin/src/router-pages/dashboard/Dashboard.test.tsx`
- `system/admin/src/router-pages/dashboard/Dashboard.tsx`

### Data Models

**Directories:**
- `system/core/backend/src/models/`

### Database

**Directories:**
- `docker/cromwell-mariadb/`
- `system/admin/src/components/loadBox/`
- `system/core/frontend/src/components/loadBox/`
- `themes/blog/src/components/loadbox/`
- `themes/store/src/components/loadbox/`
- `toolkits/commerce/src/mui/Loadbox/`
**Key files:**
- `docker/cromwell-mariadb/entrypoint.js`
- `system/admin/src/components/loadBox/LoadBox.tsx`
- `system/admin/src/components/loadBox/Loadbox.test.tsx`
- `system/admin/src/components/loadBox/LoadingStatus.tsx`
- `system/core/frontend/src/components/loadBox/Loadbox.tsx`
- `themes/blog/src/components/loadbox/Loadbox.tsx`
- `themes/store/src/components/loadbox/Loadbox.tsx`
- `toolkits/commerce/src/mui/Loadbox/Loadbox.tsx`

### Database Migrations

**Directories:**
- `plugins/newsletter/migrations/`
- `system/server/migrations/`

### Docker

**Directories:**
- `docker/`
- `system/manager/docker/`

### Documentation

**Directories:**
- `website/docs/`

### Email

**Directories:**
- `system/server/static/emails/`

### GraphQL Resolvers

**Directories:**
- `plugins/marqo/src/backend/resolvers/`
- `plugins/newsletter/src/backend/resolvers/`
- `plugins/product-showcase/src/backend/resolvers/`
- `system/server/src/resolvers/`
- `system/server/tests/resolvers/`
**Key files:**
- `plugins/marqo/src/backend/resolvers/plugin-marqo.resolver.ts`
- `plugins/newsletter/src/backend/resolvers/plugin-newsletter.resolver.ts`
- `plugins/product-showcase/src/backend/resolvers/product-showcase.resolver.ts`
- `system/server/src/resolvers/attribute.resolver.ts`
- `system/server/src/resolvers/coupon.resolver.ts`
- `system/server/src/resolvers/custom-entity.resolver.ts`
- `system/server/src/resolvers/order.resolver.ts`
- `system/server/src/resolvers/post.resolver.ts`
- `system/server/src/resolvers/product-category.resolver.ts`
- `system/server/src/resolvers/product-review.resolver.ts`
- `system/server/src/resolvers/product-variant.resolver.ts`
- `system/server/src/resolvers/product.resolver.ts`
- `system/server/src/resolvers/role.resolver.ts`
- `system/server/src/resolvers/tag.resolver.ts`
- `system/server/src/resolvers/user.resolver.ts`
- `system/server/tests/resolvers/attribute.resolver.spec.ts`
- `system/server/tests/resolvers/coupon.resolver.spec.ts`
- `system/server/tests/resolvers/custom-entity.resolver.spec.ts`
- `system/server/tests/resolvers/generic.resolver.spec.ts`
- `system/server/tests/resolvers/order.resolver.spec.ts`

### Hooks

**Directories:**
- `system/admin/src/components/layout/hooks/`
- `system/admin/src/hooks/`
- `system/admin/src/router-pages/product/hooks/`
- `system/admin/src/router-pages/settings/hooks/`
- `system/admin/src/router-pages/themeEdit/hooks/`
**Key files:**
- `system/admin/src/components/layout/hooks/useAppState.ts`
- `system/admin/src/components/layout/hooks/useTheme.ts`
- `system/admin/src/hooks/useBlocker.ts`
- `system/admin/src/hooks/useDashboard.tsx`
- `system/admin/src/hooks/useDebounce.tsx`
- `system/admin/src/hooks/useLongPress.tsx`
- `system/admin/src/router-pages/product/hooks/useTabs.ts`
- `system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx`
- `system/admin/src/router-pages/themeEdit/hooks/useBlockEvents.tsx`
- `system/admin/src/router-pages/themeEdit/hooks/useBlockFns.tsx`
- `system/admin/src/router-pages/themeEdit/hooks/useDebounce.ts`
- `system/admin/src/router-pages/themeEdit/hooks/useDocumentEvents.tsx`
- `system/admin/src/router-pages/themeEdit/hooks/useEditorUtils.tsx`
- `system/admin/src/router-pages/themeEdit/hooks/useHoveredFrames.tsx`
- `system/admin/src/router-pages/themeEdit/hooks/useKeyPress.ts`
- `system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx`
- `system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx`

### Pages

**Directories:**
- `system/admin/src/pages/`
- `system/admin/src/router-pages/settings/pages/`
- `themes/blog/src/pages/`
- `themes/blog/src/pages/pages/`
- `themes/blog/src/styles/pages/`
- `themes/blog/tests/pages/`
- `themes/store/src/pages/`
- `themes/store/src/pages/pages/`
- `themes/store/src/styles/pages/`
- `themes/store/tests/pages/`
- `website/src/pages/`
**Key files:**
- `system/admin/src/pages/_app.tsx`
- `system/admin/src/pages/_document.tsx`
- `system/admin/src/pages/index.tsx`
- `system/admin/src/router-pages/settings/pages/acl.tsx`
- `system/admin/src/router-pages/settings/pages/code.tsx`
- `system/admin/src/router-pages/settings/pages/customData.tsx`
- `system/admin/src/router-pages/settings/pages/general.tsx`
- `system/admin/src/router-pages/settings/pages/index.tsx`
- `system/admin/src/router-pages/settings/pages/migration.tsx`
- `system/admin/src/router-pages/settings/pages/seo.tsx`
- `system/admin/src/router-pages/settings/pages/store.tsx`
- `themes/blog/src/pages/404.tsx`
- `themes/blog/src/pages/_app.tsx`
- `themes/blog/src/pages/_document.tsx`
- `themes/blog/src/pages/index.tsx`
- `themes/blog/src/pages/pages/[slug].tsx`
- `themes/blog/src/pages/search.tsx`
- `themes/blog/tests/pages/index.test.tsx`
- `themes/blog/tests/pages/pages-slug.test.tsx`
- `themes/blog/tests/pages/post-slug.test.tsx`

### Plugins

**Directories:**
- `plugins/`
- `system/utils/src/plugins/`
**Key files:**
- `system/utils/src/plugins/rollup-globals.ts`
- `system/utils/src/plugins/rollup.ts`

### Product Catalog

**Directories:**
- `plugins/product-showcase/`
- `toolkits/commerce/src/base/ProductSearch/`
**Key files:**
- `plugins/product-showcase/cromwell.config.js`
- `toolkits/commerce/src/base/ProductSearch/ListItem.tsx`
- `toolkits/commerce/src/base/ProductSearch/ProductSearch.test.tsx`
- `toolkits/commerce/src/base/ProductSearch/ProductSearch.tsx`

### Redux State

**Directories:**
- `system/admin/src/redux/`
**Key files:**
- `system/admin/src/redux/helpers.ts`
- `system/admin/src/redux/store.ts`

### Registration

**Directories:**
- `system/core/frontend/src/components/SignUp/`
**Key files:**
- `system/core/frontend/src/components/SignUp/SignUp.test.tsx`
- `system/core/frontend/src/components/SignUp/SignUp.tsx`

### Routing

**Directories:**
- `system/admin/src/router-pages/`

### Search

**Directories:**
- `system/admin/src/components/inputs/Search/`
**Key files:**
- `system/admin/src/components/inputs/Search/ListItem.tsx`
- `system/admin/src/components/inputs/Search/SearchInput.test.tsx`
- `system/admin/src/components/inputs/Search/SearchInput.tsx`

### Service Layer

**Directories:**
- `system/server/src/services/`
**Key files:**
- `system/server/src/services/auth.service.ts`
- `system/server/src/services/cms.service.ts`
- `system/server/src/services/migration.service.ts`
- `system/server/src/services/mock.service.ts`
- `system/server/src/services/plugin.service.ts`
- `system/server/src/services/renderer.service.ts`
- `system/server/src/services/stats.service.ts`
- `system/server/src/services/store.service.ts`
- `system/server/src/services/theme.service.ts`

### Shared Code

**Directories:**
- `system/core/common/`
- `system/server/migrations/common/`
**Key files:**
- `system/core/common/.eslintrc.js`
- `system/core/common/rollup.config.js`
- `system/server/migrations/common/1651054396603-permissions.js`

### Shopping Cart

**Directories:**
- `themes/store/src/components/modals/cart/`
- `toolkits/commerce/src/base/CartList/`
**Key files:**
- `themes/store/src/components/modals/cart/CartModal.tsx`
- `toolkits/commerce/src/base/CartList/CartList.test.tsx`
- `toolkits/commerce/src/base/CartList/CartList.tsx`
- `toolkits/commerce/src/base/CartList/CartListItem.tsx`

### State Management

**Directories:**
- `themes/store/`
**Key files:**
- `themes/store/.eslintrc.js`
- `themes/store/cromwell.config.js`
- `themes/store/next-env.d.ts` — / <reference types="next" />
/ <reference types="next/types/global" />
/ <reference types="next/imag
- `themes/store/next.config.js`
- `themes/store/suppress-hydration-loader.js`

### Styling

**Directories:**
- `system/admin/src/styles/`
- `themes/blog/src/styles/`
- `themes/store/src/styles/`

### Testing

**Directories:**
- `plugins/main-menu/tests/`
- `plugins/newsletter/tests/`
- `plugins/paypal/tests/`
- `plugins/product-filter/tests/`
- `plugins/product-showcase/tests/`
- `plugins/stripe/tests/`
- `system/admin/src/tests/`
- `system/cli/tests/`
- `system/core/backend/tests/`
- `system/core/frontend/tests/`
- `system/server/tests/`
- `system/utils/tests/`
- `themes/blog/tests/`
- `themes/store/tests/`
- `toolkits/commerce/tests/`
**Key files:**
- `plugins/main-menu/tests/jest.config.ts`
- `plugins/main-menu/tests/setup.ts`
- `plugins/newsletter/tests/jest.config.ts`
- `plugins/newsletter/tests/setup.ts`
- `plugins/paypal/tests/jest.config.ts`
- `plugins/paypal/tests/setup.ts`
- `plugins/product-filter/tests/jest.config.ts`
- `plugins/product-filter/tests/setup.ts`
- `plugins/product-showcase/tests/jest.config.ts`
- `plugins/product-showcase/tests/setup.ts`
- `plugins/stripe/tests/jest.config.ts`
- `plugins/stripe/tests/setup.ts`
- `system/admin/src/tests/customEntities.test.tsx`
- `system/admin/src/tests/customFields.test.tsx`
- `system/admin/src/tests/setup.ts`
- `system/cli/tests/cli.test.ts`
- `system/core/backend/tests/helpers.ts`
- `system/core/backend/tests/setup.ts`
- `system/core/backend/tests/teardown.ts`
- `system/core/frontend/tests/helpers.ts`

### UI Components

**Directories:**
- `plugins/main-menu/src/admin/widgets/components/`
- `plugins/marqo/src/frontend/components/`
- `plugins/product-filter/src/frontend/components/`
- `system/admin/src/components/`
- `system/admin/src/components/entity/entityEdit/components/`
- `system/admin/src/components/entity/entityTable/components/`
- `system/admin/src/components/layout/components/`
- `system/admin/src/router-pages/attribute/components/`
- `system/admin/src/router-pages/categoryList/components/`
- `system/admin/src/router-pages/dashboard/components/`
- `system/admin/src/router-pages/login/components/`
- `system/admin/src/router-pages/order/components/`
- `system/admin/src/router-pages/post/components/`
- `system/admin/src/router-pages/product/components/`
- `system/admin/src/router-pages/settings/components/`
- `system/admin/src/router-pages/settings/pages/Themes/components/`
- `system/admin/src/router-pages/themeEdit/pageEditor/components/`
- `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/`
- `system/admin/src/router-pages/welcome/components/`
- `system/core/frontend/src/components/`
- `themes/blog/src/components/`
- `themes/store/src/components/`
- `website/src/components/`
**Key files:**
- `plugins/main-menu/src/admin/widgets/components/MenuItem.tsx`
- `plugins/marqo/src/frontend/components/ProductCard.tsx`
- `plugins/marqo/src/frontend/components/SimilarProducts.tsx`
- `plugins/product-filter/src/frontend/components/Filter.tsx`
- `plugins/product-filter/src/frontend/components/Slider.tsx`
- `system/admin/src/components/entity/entityEdit/components/ElevationScroll.tsx`
- `system/admin/src/components/entity/entityEdit/components/EntityCustomFields.tsx`
- `system/admin/src/components/entity/entityEdit/components/EntityFields.tsx`
- `system/admin/src/components/entity/entityEdit/components/EntityHeader.tsx`
- `system/admin/src/components/entity/entityEdit/components/EntityMetaFields.tsx`
- `system/admin/src/components/entity/entityEdit/components/InputField.tsx`
- `system/admin/src/components/entity/entityTable/components/ColumnConfigureItem.tsx`
- `system/admin/src/components/entity/entityTable/components/DeleteSelectedButton.tsx`
- `system/admin/src/components/entity/entityTable/components/EntityTableItem.tsx`
- `system/admin/src/components/entity/entityTable/components/PageHeader.tsx`
- `system/admin/src/components/entity/entityTable/components/SearchContent.tsx`
- `system/admin/src/components/entity/entityTable/components/TableHeader.tsx`
- `system/admin/src/components/layout/components/BrowserRouter.tsx`
- `system/admin/src/router-pages/attribute/components/AttributeValues.tsx`
- `system/admin/src/router-pages/attribute/components/ValueItem.tsx`

### User Management

**Directories:**
- `system/admin/src/router-pages/user/`
- `system/admin/src/router-pages/userList/`
**Key files:**
- `system/admin/src/router-pages/user/User.test.tsx`
- `system/admin/src/router-pages/user/User.tsx`
- `system/admin/src/router-pages/userList/UserList.test.tsx`
- `system/admin/src/router-pages/userList/UserList.tsx`

### Utilities

**Directories:**
- `plugins/product-filter/src/frontend/utils/`
- `system/admin/src/helpers/`
- `system/cli/src/utils/`
- `system/core/backend/src/helpers/`
- `system/core/backend/tests/helpers/`
- `system/core/frontend/src/helpers/`
- `system/core/frontend/tests/helpers/`
- `system/manager/src/utils/`
- `system/renderer/src/helpers/`
- `system/server/src/helpers/`
- `system/utils/`
- `themes/blog/src/helpers/`
- `themes/store/src/helpers/`
- `toolkits/commerce/src/helpers/`
- `website/src/helpers/`
**Key files:**
- `plugins/product-filter/src/frontend/utils/queries.ts`
- `system/admin/src/helpers/LayoutPortal.tsx`
- `system/admin/src/helpers/NumberFormatCustom.tsx`
- `system/admin/src/helpers/WidgetErrorBoundary.tsx`
- `system/admin/src/helpers/addressParser.tsx`
- `system/admin/src/helpers/customEntities.tsx`
- `system/admin/src/helpers/forceUpdate.ts`
- `system/admin/src/helpers/getPalette.ts`
- `system/admin/src/helpers/importDependencies.tsx`
- `system/admin/src/helpers/loadPlugins.ts`
- `system/admin/src/helpers/navigation.tsx`
- `system/admin/src/helpers/registerThemeEditor.ts`
- `system/admin/src/helpers/slugify.ts`
- `system/admin/src/helpers/time.ts`
- `system/cli/src/utils/cleanup-modules.js`
- `system/cli/src/utils/cleanup.js`
- `system/core/backend/src/helpers/actions.ts`
- `system/core/backend/src/helpers/auth-guards.ts`
- `system/core/backend/src/helpers/auth-roles-permissions.ts`
- `system/core/backend/src/helpers/auth-settings.ts`

### Views/Pages

**Directories:**
- `toolkits/commerce/src/base/ProductReviews/`
**Key files:**
- `toolkits/commerce/src/base/ProductReviews/ProductReviews.test.tsx`
- `toolkits/commerce/src/base/ProductReviews/ProductReviews.tsx`
- `toolkits/commerce/src/base/ProductReviews/ReviewForm.tsx`
- `toolkits/commerce/src/base/ProductReviews/ReviewItem.tsx`

## File Details

### `codegraph.py`
**Symbols:** class:`CodeGraph`, function:`__init__`, function:`add_node`, function:`add_edge`, function:`get_neighbors`, function:`find_feature`, function:`blast_radius`, function:`to_json`, function:`from_json`, function:`stats`, function:`_read_file`, function:`_extract_docstring`

### `docker/cromwell-mariadb/entrypoint.js`
**Feature:** Database
**Symbols:** const_fn:`main`, const_fn:`omMessage`
**Often changes with:** `docker/cromwell/entrypoint.js` (4x)

### `docker/cromwell/entrypoint.js`
**Symbols:** const_fn:`main`
**Often changes with:** `docker/cromwell-mariadb/entrypoint.js` (4x)

### `plugins/main-menu/cromwell.config.js`

### `plugins/main-menu/src/admin/icons.tsx`
**Feature:** Administration
**Often changes with:** `plugins/main-menu/src/admin/widgets/SettingsPage.tsx` (3x), `plugins/main-menu/src/admin/widgets/components/MenuItem.tsx` (3x)

### `plugins/main-menu/src/admin/index.tsx`
**Feature:** Administration
**Imports:** `plugins/main-menu/src/admin/widgets/SettingsPage.tsx`
**Often changes with:** `plugins/newsletter/src/admin/index.tsx` (5x), `plugins/product-filter/src/admin/index.tsx` (5x), `plugins/main-menu/src/admin/styles.ts` (3x), `plugins/main-menu/src/frontend/index.tsx` (3x), `plugins/product-showcase/src/admin/index.tsx` (3x)

### `plugins/main-menu/src/admin/styles.ts`
**Feature:** Administration
**Imports:** `system/admin/src/components/inputs/DateInput/styles.ts`
**Often changes with:** `plugins/main-menu/src/frontend/index.tsx` (4x), `plugins/main-menu/src/admin/index.tsx` (3x), `plugins/main-menu/src/admin/widgets/SettingsPage.tsx` (3x), `plugins/main-menu/src/admin/widgets/components/MenuItem.tsx` (3x)

### `plugins/main-menu/src/admin/widgets/SettingsPage.tsx`
**Imports:** `themes/store/src/types.ts`, `toolkits/commerce/src/base/icons.tsx`, `system/admin/src/components/inputs/DateInput/styles.ts`, `plugins/main-menu/src/admin/widgets/components/MenuItem.tsx`
**Imported by:** `plugins/main-menu/src/admin/index.tsx`
**Symbols:** function:`SettingsPage`, const_fn:`onSave`, const_fn:`updateItems`
**Often changes with:** `plugins/main-menu/src/admin/widgets/components/MenuItem.tsx` (5x), `plugins/main-menu/src/frontend/index.tsx` (4x), `plugins/product-filter/src/admin/widgets/SettingsPage.tsx` (3x), `system/cli/src/cli.ts` (3x), `system/manager/src/index.ts` (3x)

### `plugins/main-menu/src/admin/widgets/components/MenuItem.tsx`
**Feature:** UI Components
**Imports:** `themes/store/src/types.ts`, `toolkits/commerce/src/base/icons.tsx`, `system/admin/src/components/inputs/DateInput/styles.ts`
**Imported by:** `plugins/main-menu/src/admin/widgets/SettingsPage.tsx`
**Symbols:** const_fn:`Item`, const_fn:`handleExpandClick`, const_fn:`handleChange`, const_fn:`handleRemove`
**Often changes with:** `plugins/main-menu/src/admin/widgets/SettingsPage.tsx` (5x), `plugins/main-menu/src/frontend/index.tsx` (4x), `plugins/main-menu/src/admin/icons.tsx` (3x), `plugins/main-menu/src/admin/styles.ts` (3x)

### `plugins/main-menu/src/frontend/DefaultElements.tsx`
**Imports:** `themes/store/src/types.ts`
**Imported by:** `plugins/main-menu/src/frontend/index.tsx`
**Symbols:** const_fn:`DefaultMenuItemTitle`, const_fn:`DefaultIconButton`, const_fn:`DefaultPopover`
**Often changes with:** `plugins/main-menu/src/frontend/index.tsx` (4x), `plugins/main-menu/src/types.ts` (3x)

### `plugins/main-menu/src/frontend/index.tsx`
**Imports:** `themes/store/src/types.ts`, `plugins/main-menu/src/frontend/DefaultElements.tsx`
**Symbols:** const_fn:`MainMenu`, const_fn:`handlePopoverOpen`, const_fn:`handlePopoverClose`, const_fn:`handleItemMouseOver`, const_fn:`handleItemMobileClick`, const_fn:`menuSubitems`, const_fn:`menuTitle`, const_fn:`menuItem`
**Often changes with:** `plugins/product-filter/src/frontend/index.tsx` (7x), `plugins/main-menu/src/types.ts` (5x), `plugins/main-menu/src/frontend/DefaultElements.tsx` (4x), `plugins/main-menu/src/admin/styles.ts` (4x), `plugins/main-menu/src/admin/widgets/SettingsPage.tsx` (4x)

### `plugins/main-menu/src/types.ts`
**Often changes with:** `plugins/main-menu/src/frontend/index.tsx` (5x), `plugins/main-menu/src/frontend/DefaultElements.tsx` (3x)

### `plugins/main-menu/tests/admin/SettingsPage.test.tsx`
**Feature:** Administration
**Imports:** `plugins/stripe/src/admin/widgets/SettingsPage.tsx`

### `plugins/main-menu/tests/frontend/index.test.tsx`
**Imports:** `website/src/theme/Footer/index.tsx`

### `plugins/main-menu/tests/jest.config.ts`
**Feature:** Testing
**Imports:** `themes/store/src/types.ts`

### `plugins/main-menu/tests/setup.ts`
**Feature:** Testing

### `plugins/marqo/cromwell.config.js`

### `plugins/marqo/src/admin/index.tsx`
**Feature:** Administration
**Imports:** `themes/store/src/constants.js`, `plugins/marqo/src/admin/widgets/SettingsPage.tsx`

### `plugins/marqo/src/admin/widgets/SettingsPage.tsx`
**Imports:** `themes/store/src/types.ts`
**Imported by:** `plugins/marqo/src/admin/index.tsx`
**Symbols:** function:`SettingsPage`, const_fn:`syncData`, const_fn:`deleteData`

### `plugins/marqo/src/backend/controllers/plugin-marqo.controller.ts`
**Feature:** Controllers
**Imports:** `plugins/marqo/src/backend/marqo-client.ts`
**Imported by:** `plugins/marqo/src/backend/index.ts`
**Symbols:** class:`PluginMarqoController`

### `plugins/marqo/src/backend/index.ts`
**Imports:** `themes/store/src/types.ts`, `plugins/marqo/src/backend/controllers/plugin-marqo.controller.ts`, `plugins/marqo/src/backend/marqo-client.ts`, `plugins/marqo/src/backend/resolvers/plugin-marqo.resolver.ts`
**Symbols:** const_fn:`indexName`

### `plugins/marqo/src/backend/marqo-client.ts`
**Imports:** `themes/store/src/types.ts`
**Imported by:** `plugins/marqo/src/backend/index.ts`, `plugins/marqo/src/backend/controllers/plugin-marqo.controller.ts`, `plugins/marqo/src/backend/resolvers/plugin-marqo.resolver.ts`
**Symbols:** class:`MarqoClient`

### `plugins/marqo/src/backend/resolvers/plugin-marqo.resolver.ts`
**Feature:** GraphQL Resolvers
**Imports:** `plugins/marqo/src/backend/marqo-client.ts`
**Imported by:** `plugins/marqo/src/backend/index.ts`
**Symbols:** class:`PluginMarqoResolver`

### `plugins/marqo/src/constants.ts`

### `plugins/marqo/src/frontend/components/ProductCard.tsx`
**Feature:** UI Components
**Imported by:** `plugins/marqo/src/frontend/components/SimilarProducts.tsx`
**Symbols:** function:`DefaultProductCard`

### `plugins/marqo/src/frontend/components/SimilarProducts.tsx`
**Feature:** UI Components
**Imports:** `plugins/marqo/src/frontend/components/ProductCard.tsx`, `system/server/src/helpers/utils.ts`
**Imported by:** `plugins/marqo/src/frontend/index.tsx`
**Symbols:** function:`SimilarProducts`, const_fn:`getSimilarProducts`

### `plugins/marqo/src/frontend/index.tsx`
**Imports:** `themes/store/src/types.ts`, `plugins/marqo/src/frontend/components/SimilarProducts.tsx`
**Symbols:** function:`MarqoPlugin`

### `plugins/marqo/src/frontend/utils.ts`
**Imports:** `themes/store/src/constants.js`
**Symbols:** function:`queryMarqo`, function:`queryMarqoWithSessionCache`

### `plugins/marqo/src/types.ts`

### `plugins/newsletter/cromwell.config.js`

### `plugins/newsletter/migrations/mysql/1628509499895-init.js`

### `plugins/newsletter/migrations/postgres/1628509503816-init.js`

### `plugins/newsletter/migrations/sqlite/1628509508009-init.js`

### `plugins/newsletter/src/admin/index.tsx`
**Feature:** Administration
**Imports:** `plugins/newsletter/src/admin/widgets/Dashboard.tsx`, `plugins/newsletter/src/admin/widgets/SettingsPage.tsx`
**Often changes with:** `plugins/main-menu/src/admin/index.tsx` (5x), `plugins/product-filter/src/admin/index.tsx` (5x), `plugins/newsletter/src/admin/styles.ts` (4x), `plugins/newsletter/src/frontend/index.tsx` (4x), `plugins/product-showcase/src/admin/index.tsx` (4x)

### `plugins/newsletter/src/admin/styles.ts`
**Feature:** Administration
**Imports:** `system/admin/src/components/inputs/DateInput/styles.ts`
**Often changes with:** `plugins/newsletter/src/admin/index.tsx` (4x), `plugins/newsletter/src/frontend/index.tsx` (4x), `plugins/newsletter/src/frontend/styles.ts` (4x), `plugins/newsletter/src/types.ts` (3x), `plugins/main-menu/src/admin/index.tsx` (3x)

### `plugins/newsletter/src/admin/widgets/Dashboard.tsx`
**Imports:** `system/admin/src/components/inputs/DateInput/styles.ts`
**Imported by:** `plugins/newsletter/src/admin/index.tsx`
**Symbols:** const_fn:`Dashboard`, const_fn:`getStats`
**Often changes with:** `plugins/newsletter/src/backend/controllers/plugin-newsletter.controller.ts` (3x), `plugins/newsletter/tests/admin/Dashboard.test.tsx` (3x)

### `plugins/newsletter/src/admin/widgets/SettingsPage.tsx`
**Imports:** `themes/store/src/types.ts`, `system/admin/src/components/inputs/DateInput/styles.ts`
**Imported by:** `plugins/newsletter/src/admin/index.tsx`
**Symbols:** function:`SettingsPage`, const_fn:`exportData`, function:`downloadFile`

### `plugins/newsletter/src/backend/auth.ts`

### `plugins/newsletter/src/backend/controllers/plugin-newsletter.controller.ts`
**Feature:** Controllers
**Imports:** `system/core/common/src/auth.ts`
**Imported by:** `plugins/newsletter/src/backend/index.ts`
**Symbols:** class:`PluginNewsletterSubscription`, class:`PluginNewsletterController`
**Often changes with:** `plugins/newsletter/src/backend/resolvers/plugin-newsletter.resolver.ts` (4x), `plugins/newsletter/src/admin/widgets/Dashboard.tsx` (3x), `plugins/newsletter/tests/backend/newsletter.controller.test.ts` (3x), `plugins/newsletter/tests/backend/newsletter.resolver.test.ts` (3x)

### `plugins/newsletter/src/backend/entities/newsletter-form.entity.ts`
**Imports:** `themes/store/src/types.ts`
**Imported by:** `plugins/newsletter/src/backend/index.ts`
**Symbols:** class:`PluginNewsletter_NewsletterForm`

### `plugins/newsletter/src/backend/index.ts`
**Imports:** `plugins/newsletter/src/backend/controllers/plugin-newsletter.controller.ts`, `plugins/newsletter/src/backend/entities/newsletter-form.entity.ts`, `plugins/newsletter/src/backend/resolvers/plugin-newsletter.resolver.ts`

### `plugins/newsletter/src/backend/resolvers/plugin-newsletter.resolver.ts`
**Feature:** GraphQL Resolvers
**Imports:** `system/core/common/src/auth.ts`
**Imported by:** `plugins/newsletter/src/backend/index.ts`
**Symbols:** class:`PluginNewsletterResolver`
**Often changes with:** `plugins/newsletter/src/backend/controllers/plugin-newsletter.controller.ts` (4x), `plugins/newsletter/tests/backend/newsletter.controller.test.ts` (3x), `plugins/newsletter/tests/backend/newsletter.resolver.test.ts` (3x)

### `plugins/newsletter/src/frontend/index.tsx`
**Imports:** `plugins/newsletter/src/frontend/styles.ts`
**Symbols:** function:`NewsletterPlugin`, const_fn:`validateEmail`, const_fn:`submit`, function:`CustomAlert`
**Often changes with:** `plugins/newsletter/src/admin/index.tsx` (4x), `plugins/newsletter/src/admin/styles.ts` (4x), `plugins/newsletter/src/frontend/styles.ts` (4x), `plugins/newsletter/src/types.ts` (3x), `system/core/backend/src/helpers/constants.ts` (3x)

### `plugins/newsletter/src/frontend/styles.ts`
**Imports:** `system/admin/src/components/inputs/DateInput/styles.ts`
**Imported by:** `plugins/newsletter/src/frontend/index.tsx`
**Often changes with:** `plugins/newsletter/src/admin/styles.ts` (4x), `plugins/newsletter/src/frontend/index.tsx` (4x), `plugins/newsletter/src/admin/index.tsx` (3x)

### `plugins/newsletter/src/types.ts`
**Often changes with:** `plugins/newsletter/src/admin/index.tsx` (3x), `plugins/newsletter/src/admin/styles.ts` (3x), `plugins/newsletter/src/frontend/index.tsx` (3x)

### `plugins/newsletter/tests/admin/Dashboard.test.tsx`
**Feature:** Administration
**Imports:** `system/admin/src/router-pages/dashboard/Dashboard.tsx`
**Often changes with:** `plugins/newsletter/src/admin/widgets/Dashboard.tsx` (3x)

### `plugins/newsletter/tests/admin/SettingsPage.test.tsx`
**Feature:** Administration
**Imports:** `plugins/stripe/src/admin/widgets/SettingsPage.tsx`

### `plugins/newsletter/tests/backend/newsletter.controller.test.ts`
**Often changes with:** `plugins/newsletter/src/backend/controllers/plugin-newsletter.controller.ts` (3x), `plugins/newsletter/src/backend/resolvers/plugin-newsletter.resolver.ts` (3x), `plugins/newsletter/tests/backend/newsletter.resolver.test.ts` (3x)

### `plugins/newsletter/tests/backend/newsletter.resolver.test.ts`
**Often changes with:** `plugins/newsletter/src/backend/controllers/plugin-newsletter.controller.ts` (3x), `plugins/newsletter/src/backend/resolvers/plugin-newsletter.resolver.ts` (3x), `plugins/newsletter/tests/backend/newsletter.controller.test.ts` (3x)

### `plugins/newsletter/tests/frontend/index.test.tsx`
**Imports:** `website/src/theme/Footer/index.tsx`

### `plugins/newsletter/tests/jest.config.ts`
**Feature:** Testing
**Imports:** `themes/store/src/types.ts`

### `plugins/newsletter/tests/setup.ts`
**Feature:** Testing

### `plugins/paypal/cromwell.config.js`
**Often changes with:** `plugins/paypal/src/admin/widgets/SettingsPage.tsx` (3x), `plugins/paypal/src/backend/actions/create-payment.action.ts` (3x), `plugins/paypal/src/types.ts` (3x)

### `plugins/paypal/src/admin/index.tsx`
**Feature:** Administration
**Imports:** `themes/store/src/constants.js`, `plugins/paypal/src/admin/widgets/SettingsPage.tsx`

### `plugins/paypal/src/admin/widgets/SettingsPage.tsx`
**Imports:** `themes/store/src/types.ts`
**Imported by:** `plugins/paypal/src/admin/index.tsx`
**Symbols:** function:`SettingsPage`
**Often changes with:** `plugins/paypal/cromwell.config.js` (3x), `plugins/paypal/src/backend/actions/create-payment.action.ts` (3x), `plugins/paypal/src/types.ts` (3x)

### `plugins/paypal/src/backend/actions/create-payment.action.ts`
**Imports:** `themes/store/src/constants.js`, `themes/store/src/types.ts`
**Imported by:** `plugins/paypal/src/backend/index.ts`
**Symbols:** const_fn:`createPayment`, const_fn:`cart`, const_fn:`currency`, const_fn:`convertPrice`
**Often changes with:** `plugins/stripe/src/backend/actions/create-payment.action.ts` (4x), `plugins/paypal/cromwell.config.js` (3x), `plugins/paypal/src/admin/widgets/SettingsPage.tsx` (3x), `plugins/paypal/src/types.ts` (3x)

### `plugins/paypal/src/backend/index.ts`
**Imports:** `themes/store/src/constants.js`, `plugins/paypal/src/backend/actions/create-payment.action.ts`

### `plugins/paypal/src/constants.ts`

### `plugins/paypal/src/types.ts`
**Often changes with:** `plugins/paypal/cromwell.config.js` (3x), `plugins/paypal/src/admin/widgets/SettingsPage.tsx` (3x), `plugins/paypal/src/backend/actions/create-payment.action.ts` (3x)

### `plugins/paypal/tests/admin/SettingsPage.test.tsx`
**Feature:** Administration
**Imports:** `plugins/stripe/src/admin/widgets/SettingsPage.tsx`

### `plugins/paypal/tests/backend/create-payment.action.test.ts`
**Imports:** `themes/store/src/types.ts`

### `plugins/paypal/tests/jest.config.ts`
**Feature:** Testing
**Imports:** `themes/store/src/types.ts`

### `plugins/paypal/tests/setup.ts`
**Feature:** Testing

### `plugins/product-filter/cromwell.config.js`
**Often changes with:** `plugins/product-filter/src/types.ts` (3x)

### `plugins/product-filter/src/admin/index.tsx`
**Feature:** Administration
**Imports:** `plugins/product-filter/src/admin/widgets/SettingsPage.tsx`, `plugins/product-filter/src/admin/widgets/ThemeEditor.tsx`
**Often changes with:** `plugins/product-showcase/src/admin/index.tsx` (6x), `plugins/main-menu/src/admin/index.tsx` (5x), `plugins/newsletter/src/admin/index.tsx` (5x), `plugins/product-filter/src/frontend/index.tsx` (4x), `plugins/product-filter/src/types.ts` (3x)

### `plugins/product-filter/src/admin/widgets/SettingsPage.tsx`
**Imports:** `themes/store/src/constants.js`, `themes/store/src/types.ts`
**Imported by:** `plugins/product-filter/src/admin/index.tsx`
**Symbols:** function:`SettingsPage`, const_fn:`onSave`
**Often changes with:** `plugins/product-showcase/src/admin/widgets/SettingsPage.tsx` (5x), `plugins/main-menu/src/admin/widgets/SettingsPage.tsx` (3x), `plugins/product-filter/src/frontend/components/Filter.tsx` (3x), `plugins/product-filter/src/frontend/index.tsx` (3x), `plugins/product-filter/tests/admin/SettingsPage.test.tsx` (3x)

### `plugins/product-filter/src/admin/widgets/ThemeEditor.tsx`
**Imported by:** `plugins/product-filter/src/admin/index.tsx`
**Symbols:** function:`ThemeEditor`, const_fn:`handleChangeListId`

### `plugins/product-filter/src/constants.ts`
**Imports:** `plugins/product-filter/src/types.ts`
**Often changes with:** `plugins/product-filter/src/types.ts` (4x), `plugins/product-filter/src/frontend/index.tsx` (3x)

### `plugins/product-filter/src/frontend/components/Filter.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/components/inputs/DateInput/styles.ts`, `themes/store/src/constants.js`, `themes/store/src/types.ts`, `system/admin/src/components/inputs/DateInput/styles.ts`, `plugins/product-filter/src/frontend/utils/queries.ts`, `plugins/product-filter/src/frontend/components/Slider.tsx`
**Imported by:** `plugins/product-filter/src/frontend/index.tsx`, `system/admin/src/router-pages/productList/ProductList.tsx`
**Symbols:** class:`ProductFilter`
**Often changes with:** `plugins/product-filter/src/types.ts` (5x), `plugins/product-filter/src/frontend/index.tsx` (4x), `plugins/product-showcase/src/frontend/index.tsx` (4x), `plugins/product-filter/src/frontend/components/Slider.tsx` (3x), `plugins/product-filter/src/admin/widgets/SettingsPage.tsx` (3x)

### `plugins/product-filter/src/frontend/components/Slider.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/components/inputs/DateInput/styles.ts`
**Imported by:** `plugins/product-filter/src/frontend/components/Filter.tsx`, `system/admin/src/helpers/editor/fontSize/InputSlider.tsx`
**Symbols:** const_fn:`getPriceText`, function:`useForceUpdate`, const_fn:`Slider`, const_fn:`handlePriceRangeChange`
**Often changes with:** `plugins/product-filter/src/frontend/components/Filter.tsx` (3x)

### `plugins/product-filter/src/frontend/index.tsx`
**Imports:** `plugins/product-filter/src/frontend/components/Filter.tsx`, `themes/store/src/types.ts`
**Often changes with:** `plugins/product-filter/src/types.ts` (8x), `plugins/product-filter/src/frontend/styles.ts` (8x), `system/core/common/src/types/data.ts` (7x), `plugins/main-menu/src/frontend/index.tsx` (7x), `system/core/common/src/types/blocks.ts` (7x)

### `plugins/product-filter/src/frontend/styles.ts`
**Imports:** `system/admin/src/components/inputs/DateInput/styles.ts`
**Often changes with:** `plugins/product-filter/src/frontend/index.tsx` (8x), `plugins/product-filter/src/types.ts` (5x)

### `plugins/product-filter/src/frontend/utils/queries.ts`
**Feature:** Utilities
**Imported by:** `plugins/product-filter/src/frontend/components/Filter.tsx`
**Symbols:** function:`getCategoryBySlug`, function:`getFilteredProducts`, function:`getAttributes`

### `plugins/product-filter/src/types.ts`
**Imported by:** `plugins/product-filter/src/constants.ts`
**Often changes with:** `plugins/product-filter/src/frontend/index.tsx` (8x), `plugins/product-filter/src/frontend/components/Filter.tsx` (5x), `plugins/product-filter/src/frontend/styles.ts` (5x), `plugins/product-filter/src/constants.ts` (4x), `system/core/common/src/types/data.ts` (3x)

### `plugins/product-filter/tests/admin/SettingsPage.test.tsx`
**Feature:** Administration
**Imports:** `plugins/stripe/src/admin/widgets/SettingsPage.tsx`
**Often changes with:** `plugins/product-filter/src/admin/widgets/SettingsPage.tsx` (3x), `plugins/product-filter/src/frontend/index.tsx` (3x), `plugins/product-filter/tests/frontend/index.test.tsx` (3x), `plugins/product-showcase/src/admin/widgets/SettingsPage.tsx` (3x)

### `plugins/product-filter/tests/frontend/index.test.tsx`
**Imports:** `website/src/theme/Footer/index.tsx`
**Often changes with:** `plugins/product-filter/src/admin/widgets/SettingsPage.tsx` (3x), `plugins/product-filter/src/frontend/index.tsx` (3x), `plugins/product-filter/tests/admin/SettingsPage.test.tsx` (3x), `plugins/product-showcase/src/admin/widgets/SettingsPage.tsx` (3x)

### `plugins/product-filter/tests/jest.config.ts`
**Feature:** Testing
**Imports:** `themes/store/src/types.ts`

### `plugins/product-filter/tests/setup.ts`
**Feature:** Testing

### `plugins/product-showcase/cromwell.config.js`
**Feature:** Product Catalog

### `plugins/product-showcase/src/admin/index.tsx`
**Feature:** Administration
**Imports:** `plugins/product-showcase/src/admin/widgets/SettingsPage.tsx`
**Often changes with:** `plugins/product-filter/src/admin/index.tsx` (6x), `plugins/product-showcase/src/frontend/index.tsx` (4x), `plugins/newsletter/src/admin/index.tsx` (4x), `plugins/product-filter/src/frontend/index.tsx` (3x), `plugins/main-menu/src/admin/index.tsx` (3x)

### `plugins/product-showcase/src/admin/widgets/SettingsPage.tsx`
**Imports:** `system/admin/src/components/inputs/DateInput/styles.ts`, `themes/store/src/types.ts`
**Imported by:** `plugins/product-showcase/src/admin/index.tsx`
**Symbols:** function:`SettingsPage`, const_fn:`onSave`, const_fn:`handleChangeSize`
**Often changes with:** `plugins/product-filter/src/admin/widgets/SettingsPage.tsx` (5x), `plugins/product-filter/src/frontend/index.tsx` (3x), `plugins/product-filter/tests/admin/SettingsPage.test.tsx` (3x), `plugins/product-filter/tests/frontend/index.test.tsx` (3x), `plugins/stripe/tests/admin/SettingsPage.test.tsx` (3x)

### `plugins/product-showcase/src/backend/entities/page-data.entity.ts`
**Symbols:** class:`PluginProductShowcase_PageData`

### `plugins/product-showcase/src/backend/index.ts`
**Imports:** `plugins/product-showcase/src/backend/resolvers/product-showcase.resolver.ts`

### `plugins/product-showcase/src/backend/resolvers/product-showcase.resolver.ts`
**Feature:** GraphQL Resolvers
**Imports:** `themes/store/src/types.ts`
**Imported by:** `plugins/product-showcase/src/backend/index.ts`
**Symbols:** class:`PluginProductShowcaseResolver`
**Often changes with:** `plugins/product-showcase/src/frontend/index.tsx` (3x), `plugins/stripe/src/backend/actions/create-payment.action.ts` (3x)

### `plugins/product-showcase/src/frontend/ProductCard.tsx`
**Imported by:** `plugins/product-showcase/src/frontend/index.tsx`
**Symbols:** function:`DefaultProductCard`

### `plugins/product-showcase/src/frontend/index.tsx`
**Imports:** `plugins/product-showcase/src/frontend/ProductCard.tsx`
**Symbols:** const_fn:`ProductShowcase`, const_fn:`getData`
**Often changes with:** `system/core/common/src/types/blocks.ts` (9x), `plugins/product-filter/src/frontend/index.tsx` (5x), `system/core/frontend/src/api/CGraphQLClient.ts` (5x), `system/core/backend/src/helpers/constants.ts` (4x), `plugins/product-filter/src/frontend/components/Filter.tsx` (4x)

### `plugins/product-showcase/src/types.ts`

### `plugins/product-showcase/tests/admin/SettingsPage.test.tsx`
**Feature:** Administration
**Imports:** `plugins/stripe/src/admin/widgets/SettingsPage.tsx`

### `plugins/product-showcase/tests/backend/newsletter.resolver.test.ts`

### `plugins/product-showcase/tests/frontend/index.test.tsx`
**Imports:** `website/src/theme/Footer/index.tsx`

### `plugins/product-showcase/tests/jest.config.ts`
**Feature:** Testing
**Imports:** `themes/store/src/types.ts`

### `plugins/product-showcase/tests/setup.ts`
**Feature:** Testing

### `plugins/stripe/cromwell.config.js`
**Often changes with:** `plugins/stripe/src/types.ts` (3x)

### `plugins/stripe/src/admin/index.tsx`
**Feature:** Administration
**Imports:** `themes/store/src/constants.js`, `plugins/stripe/src/admin/widgets/SettingsPage.tsx`
**Often changes with:** `plugins/stripe/src/backend/index.ts` (3x)

### `plugins/stripe/src/admin/widgets/SettingsPage.tsx`
**Imports:** `themes/store/src/types.ts`
**Imported by:** `plugins/main-menu/tests/admin/SettingsPage.test.tsx`, `plugins/newsletter/tests/admin/SettingsPage.test.tsx`, `plugins/paypal/tests/admin/SettingsPage.test.tsx`, `plugins/product-filter/tests/admin/SettingsPage.test.tsx`, `plugins/product-showcase/tests/admin/SettingsPage.test.tsx`, `plugins/stripe/src/admin/index.tsx`, `plugins/stripe/tests/admin/SettingsPage.test.tsx`
**Symbols:** function:`SettingsPage`
**Often changes with:** `plugins/stripe/src/backend/actions/create-payment.action.ts` (3x)

### `plugins/stripe/src/backend/actions/create-payment.action.ts`
**Imports:** `themes/store/src/constants.js`, `themes/store/src/types.ts`
**Imported by:** `plugins/stripe/src/backend/index.ts`
**Symbols:** const_fn:`createPayment`, const_fn:`cart`, const_fn:`convertPrice`
**Often changes with:** `plugins/paypal/src/backend/actions/create-payment.action.ts` (4x), `plugins/stripe/src/admin/widgets/SettingsPage.tsx` (3x), `system/admin/startup.js` (3x), `system/core/common/src/types/data.ts` (3x), `plugins/product-showcase/src/backend/resolvers/product-showcase.resolver.ts` (3x)

### `plugins/stripe/src/backend/index.ts`
**Imports:** `themes/store/src/constants.js`, `plugins/stripe/src/backend/actions/create-payment.action.ts`
**Often changes with:** `plugins/stripe/src/admin/index.tsx` (3x)

### `plugins/stripe/src/constants.ts`

### `plugins/stripe/src/types.ts`
**Often changes with:** `plugins/stripe/cromwell.config.js` (3x)

### `plugins/stripe/tests/admin/SettingsPage.test.tsx`
**Feature:** Administration
**Imports:** `plugins/stripe/src/admin/widgets/SettingsPage.tsx`
**Often changes with:** `plugins/product-showcase/src/admin/widgets/SettingsPage.tsx` (3x)

### `plugins/stripe/tests/backend/create-payment.action.test.ts`
**Often changes with:** `plugins/stripe/src/backend/actions/create-payment.action.ts` (3x)

### `plugins/stripe/tests/jest.config.ts`
**Feature:** Testing
**Imports:** `themes/store/src/types.ts`

### `plugins/stripe/tests/setup.ts`
**Feature:** Testing

### `startup.js`
**Symbols:** const_fn:`isCoreBuilt`, const_fn:`hasNodeModules`, const_fn:`buildAllPackagesInDir`
**Often changes with:** `system/core/common/src/types/data.ts` (12x), `system/cli/src/cli.ts` (10x), `system/core/backend/src/helpers/paths.ts` (10x), `system/manager/src/managers/baseManager.ts` (7x), `system/renderer/src/generator.ts` (7x)

### `system/admin/.eslintrc.js`
**Feature:** Administration

### `system/admin/jest.config.ts`
**Feature:** Administration
**Imports:** `themes/store/src/types.ts`

### `system/admin/next-env.d.ts`
**Purpose:** / <reference types="next" />
/ <reference types="next/image-types/global" />
**Feature:** Administration

### `system/admin/next.config.js`
**Feature:** Administration
**Often changes with:** `system/admin/startup.js` (3x), `system/admin/src/components/entity/entityTable/components/EntityTableItem.tsx` (3x)

### `system/admin/postcss.config.js`
**Feature:** Administration
**Imports:** `system/core/backend/src/helpers/paths.ts`

### `system/admin/src/components/actionButton/index.tsx`
**Symbols:** const_fn:`ActionButton`

### `system/admin/src/components/breadcrumbs/index.tsx`
**Symbols:** const_fn:`TBreadcrumbs`, const_fn:`content`
**Often changes with:** `system/admin/src/components/entity/entityEdit/EntityEdit.tsx` (4x), `system/admin/src/components/entity/entityTable/components/EntityTableItem.tsx` (4x), `system/admin/src/components/entity/entityTable/components/TableHeader.tsx` (3x), `system/admin/src/components/entity/types.ts` (3x), `system/admin/src/components/fileManager/FileManager.tsx` (3x)

### `system/admin/src/components/buttons/IconButton.tsx`
**Imported by:** `system/admin/src/components/draggableList/DraggableList.tsx`, `system/admin/src/components/entity/entityEdit/components/EntityHeader.tsx`, `system/admin/src/components/entity/entityTable/components/DeleteSelectedButton.tsx`, `system/admin/src/components/entity/entityTable/components/EntityTableItem.tsx`, `system/admin/src/components/entity/entityTable/components/PageHeader.tsx`, `system/admin/src/components/fileManager/FileItem.tsx`, `system/admin/src/components/fileManager/FileManager.tsx`, `system/admin/src/components/pluginSettingsLayout/PluginSettingsLayout.tsx`, `system/admin/src/components/sideNav/ResponsiveSideNav.tsx`, `system/admin/src/components/textFieldWithTooltip/TextFieldWithTooltip.tsx`

### `system/admin/src/components/buttons/TextButton.tsx`
**Imported by:** `system/admin/src/components/entity/entityEdit/components/EntityHeader.tsx`, `system/admin/src/components/entity/entityTable/components/PageHeader.tsx`, `system/admin/src/components/entity/entityTable/components/TableHeader.tsx`, `system/admin/src/components/fileManager/FileManager.tsx`, `system/admin/src/components/modal/Confirmation.tsx`, `system/admin/src/components/pluginSettingsLayout/PluginSettingsLayout.tsx`, `system/admin/src/components/transferList/TransferList.tsx`, `system/admin/src/router-pages/dashboard/Dashboard.tsx`, `system/admin/src/router-pages/post/components/HeaderActions.tsx`, `system/admin/src/router-pages/post/components/PostSettings.tsx`

### `system/admin/src/components/cmsInfo/CmsInfo.tsx`
**Imports:** `themes/store/src/components/modals/baseModal/Modal.tsx`
**Imported by:** `system/admin/src/components/topbar/Topbar.tsx`
**Symbols:** function:`CmsInfo`

### `system/admin/src/components/draggableList/DraggableList.tsx`
**Imports:** `system/admin/src/components/buttons/IconButton.tsx`
**Imported by:** `system/admin/src/components/entity/entityTable/components/TableHeader.tsx`
**Symbols:** class:`DraggableList`

### `system/admin/src/components/entity/entityEdit/EntityEdit.test.tsx`
**Imports:** `system/admin/src/components/entity/entityEdit/EntityEdit.tsx`

### `system/admin/src/components/entity/entityEdit/EntityEdit.tsx`
**Imports:** `themes/store/src/components/toast/toast.tsx`, `themes/store/src/types.ts`, `system/server/src/helpers/utils.ts`, `system/admin/src/components/entity/entityEdit/components/EntityFields.tsx`, `system/admin/src/components/entity/entityEdit/components/EntityHeader.tsx`, `system/admin/src/components/entity/entityEdit/helpers.tsx`, `system/admin/src/components/entity/entityEdit/type.ts`
**Imported by:** `system/admin/src/components/entity/entityEdit/EntityEdit.test.tsx`, `system/admin/src/helpers/customEntities.tsx`, `system/admin/src/router-pages/attribute/AttributePage.tsx`, `system/admin/src/router-pages/category/CategoryPage.tsx`, `system/admin/src/router-pages/coupon/Coupon.tsx`, `system/admin/src/router-pages/order/Order.tsx`, `system/admin/src/router-pages/post/Post.tsx`, `system/admin/src/router-pages/product/Product.tsx`, `system/admin/src/router-pages/tag/Tag.tsx`, `system/admin/src/router-pages/user/User.tsx`
**Symbols:** class:`EntityEdit`, const_fn:`value`, function:`ComponentWithRouterProp`
**Often changes with:** `system/admin/src/components/entity/types.ts` (5x), `system/admin/src/components/breadcrumbs/index.tsx` (4x), `system/admin/src/components/entity/entityTable/components/EntityTableItem.tsx` (4x), `system/admin/src/components/entity/entityTable/components/TableHeader.tsx` (4x), `system/admin/src/components/fileManager/FileItem.tsx` (3x)

### `system/admin/src/components/entity/entityEdit/components/ElevationScroll.tsx`
**Feature:** UI Components
**Imported by:** `system/admin/src/components/entity/entityEdit/components/EntityHeader.tsx`
**Symbols:** function:`ElevationScroll`

### `system/admin/src/components/entity/entityEdit/components/EntityCustomFields.tsx`
**Feature:** UI Components
**Imports:** `toolkits/commerce/tests/helpers.ts`
**Imported by:** `system/admin/src/components/entity/entityEdit/components/EntityFields.tsx`, `system/admin/src/router-pages/order/components/PageContent.tsx`, `system/admin/src/router-pages/product/components/PageContent.tsx`
**Symbols:** function:`CustomFieldWrapper`, function:`EntityCustomFields`

### `system/admin/src/components/entity/entityEdit/components/EntityFields.tsx`
**Feature:** UI Components
**Imports:** `toolkits/commerce/tests/helpers.ts`, `system/admin/src/components/entity/entityEdit/components/EntityCustomFields.tsx`, `system/admin/src/components/entity/entityEdit/components/EntityMetaFields.tsx`, `system/admin/src/components/entity/entityEdit/components/InputField.tsx`
**Imported by:** `system/admin/src/components/entity/entityEdit/EntityEdit.tsx`
**Symbols:** function:`EntityFields`

### `system/admin/src/components/entity/entityEdit/components/EntityHeader.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/components/buttons/IconButton.tsx`, `system/admin/src/components/buttons/TextButton.tsx`, `toolkits/commerce/tests/helpers.ts`, `system/admin/src/components/entity/entityEdit/components/ElevationScroll.tsx`
**Imported by:** `system/admin/src/components/entity/entityEdit/EntityEdit.tsx`, `system/admin/src/router-pages/settings/Settings.tsx`
**Symbols:** function:`EntityHeader`, function:`PageStickyHeader`
**Often changes with:** `system/admin/src/components/entity/entityTable/components/EntityTableItem.tsx` (3x), `system/admin/src/components/entity/types.ts` (3x)

### `system/admin/src/components/entity/entityEdit/components/EntityMetaFields.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/components/inputs/AutocompleteInput.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx`, `toolkits/commerce/tests/helpers.ts`
**Imported by:** `system/admin/src/components/entity/entityEdit/components/EntityFields.tsx`, `system/admin/src/router-pages/product/components/PageContent.tsx`
**Symbols:** function:`EntityMetaFields`

### `system/admin/src/components/entity/entityEdit/components/InputField.tsx`
**Feature:** UI Components
**Imports:** `themes/store/src/helpers/forceUpdate.ts`, `themes/store/src/types.ts`
**Imported by:** `system/admin/src/components/entity/entityEdit/components/EntityFields.tsx`
**Symbols:** function:`InputField`

### `system/admin/src/components/entity/entityEdit/helpers.tsx`
**Imports:** `themes/store/src/types.ts`, `system/admin/src/components/entity/entityEdit/type.ts`
**Imported by:** `system/admin/src/components/entity/entityEdit/EntityEdit.tsx`
**Symbols:** const_fn:`setValueOfTextEditorField`, const_fn:`getInitialValueOfTextEditorField`, function:`EntityEditContextProvider`, function:`getIdFromField`, function:`getCachedField`

### `system/admin/src/components/entity/entityEdit/type.ts`
**Imports:** `themes/store/src/types.ts`
**Imported by:** `system/admin/src/components/entity/entityEdit/EntityEdit.tsx`, `system/admin/src/components/entity/entityEdit/helpers.tsx`

### `system/admin/src/components/entity/entityTable/EntityTable.test.tsx`
**Imports:** `system/admin/src/router-pages/settings/pages/store.tsx`, `themes/store/src/types.ts`, `system/admin/src/components/entity/entityTable/EntityTable.tsx`

### `system/admin/src/components/entity/entityTable/EntityTable.tsx`
**Imports:** `toolkits/commerce/tests/helpers.ts`, `system/admin/src/components/modal/Confirmation.tsx`, `toolkits/commerce/src/mui/Pagination/Pagination.tsx`, `system/admin/src/components/skeleton/SkeletonPreloader.tsx`, `themes/store/src/components/toast/toast.tsx`, `themes/store/src/types.ts`, `system/server/src/helpers/utils.ts`, `system/admin/src/components/entity/entityTable/components/EntityTableItem.tsx`, `system/admin/src/components/entity/entityTable/components/PageHeader.tsx`, `system/admin/src/components/entity/entityTable/components/TableHeader.tsx`
**Imported by:** `system/admin/src/components/entity/entityTable/EntityTable.test.tsx`, `system/admin/src/components/entity/entityTable/components/TableHeader.tsx`, `system/admin/src/helpers/customEntities.tsx`, `system/admin/src/router-pages/attributeList/AttributesList.tsx`, `system/admin/src/router-pages/categoryList/CategoryList.tsx`, `system/admin/src/router-pages/couponList/CouponList.tsx`, `system/admin/src/router-pages/orderList/OrderList.tsx`, `system/admin/src/router-pages/pluginList/PluginList.tsx`, `system/admin/src/router-pages/postList/PostList.tsx`, `system/admin/src/router-pages/productList/ProductList.tsx`
**Symbols:** class:`EntityTable`
**Often changes with:** `system/admin/src/components/entity/entityTable/components/EntityTableItem.tsx` (3x), `system/admin/src/components/entity/types.ts` (3x), `system/admin/src/components/fileManager/FileManager.tsx` (3x)

### `system/admin/src/components/entity/entityTable/components/ColumnConfigureItem.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/components/inputs/SwitchInput/SwitchInput.tsx`, `themes/store/src/types.ts`
**Imported by:** `system/admin/src/components/entity/entityTable/components/TableHeader.tsx`
**Symbols:** const_fn:`ColumnConfigureItem`, const_fn:`toggleVisibility`

### `system/admin/src/components/entity/entityTable/components/DeleteSelectedButton.tsx`
**Feature:** UI Components
**Imports:** `toolkits/commerce/tests/helpers.ts`, `system/admin/src/router-pages/settings/pages/store.tsx`, `system/admin/src/components/buttons/IconButton.tsx`
**Imported by:** `system/admin/src/components/entity/entityTable/components/PageHeader.tsx`
**Symbols:** const_fn:`mapStateToProps`, const_fn:`DeleteSelectedButton`
**Often changes with:** `system/admin/src/components/entity/entityTable/components/EntityTableItem.tsx` (3x)

### `system/admin/src/components/entity/entityTable/components/EntityTableItem.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/helpers/time.ts`, `system/admin/src/router-pages/settings/pages/store.tsx`, `system/admin/src/components/buttons/IconButton.tsx`, `system/admin/src/components/inputs/CheckboxInput.tsx`, `themes/store/src/types.ts`
**Imported by:** `system/admin/src/components/entity/entityTable/EntityTable.tsx`
**Symbols:** const_fn:`mapStateToProps`, function:`EntityTableItem`, const_fn:`TooltipContent`
**Often changes with:** `system/admin/src/components/entity/types.ts` (6x), `system/admin/src/components/fileManager/FileItem.tsx` (5x), `system/admin/src/components/fileManager/FileManager.tsx` (5x), `system/admin/src/components/breadcrumbs/index.tsx` (4x), `system/admin/src/components/entity/entityEdit/EntityEdit.tsx` (4x)

### `system/admin/src/components/entity/entityTable/components/PageHeader.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/components/sideNav/ResponsiveSideNav.tsx`, `system/admin/src/components/buttons/IconButton.tsx`, `system/admin/src/components/buttons/TextButton.tsx`, `system/admin/src/components/icons/clearFilter.tsx`, `themes/store/src/types.ts`, `system/admin/src/components/entity/entityTable/components/DeleteSelectedButton.tsx`
**Imported by:** `system/admin/src/components/entity/entityTable/EntityTable.tsx`
**Symbols:** function:`PageHeader`, const_fn:`handleCreate`
**Often changes with:** `system/admin/src/components/entity/entityTable/components/EntityTableItem.tsx` (3x)

### `system/admin/src/components/entity/entityTable/components/SearchContent.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/components/inputs/AutocompleteInput.tsx`, `system/admin/src/components/inputs/DateInput/DateInput.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx`, `system/admin/src/components/entity/entityTable/components/TableHeader.tsx`
**Imported by:** `system/admin/src/components/entity/entityTable/components/TableHeader.tsx`
**Symbols:** function:`SearchContent`

### `system/admin/src/components/entity/entityTable/components/TableHeader.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/components/inputs/DateInput/styles.ts`, `themes/store/src/helpers/forceUpdate.ts`, `toolkits/commerce/tests/helpers.ts`, `system/admin/src/router-pages/settings/pages/store.tsx`, `system/admin/src/components/buttons/TextButton.tsx`, `system/admin/src/components/draggableList/DraggableList.tsx`, `system/admin/src/components/inputs/CheckboxInput.tsx`, `themes/store/src/types.ts`, `system/admin/src/components/entity/entityTable/EntityTable.tsx`, `system/admin/src/components/entity/entityTable/components/ColumnConfigureItem.tsx`
**Imported by:** `system/admin/src/components/entity/entityTable/EntityTable.tsx`, `system/admin/src/components/entity/entityTable/components/SearchContent.tsx`
**Symbols:** const_fn:`mapStateToProps`, function:`TableHeader`, const_fn:`handleToggleSelectAll`, const_fn:`openColumnSearch`, const_fn:`closeColumnSearch`, const_fn:`getFilter`, const_fn:`clearColumnSearch`, const_fn:`toggleOrderBy`, const_fn:`changeColumnsOrder`, const_fn:`saveConfiguredColumns`, const_fn:`toggleConfigureColumns`, const_fn:`resetConfiguredColumns`
**Often changes with:** `system/admin/src/components/entity/entityEdit/EntityEdit.tsx` (4x), `system/admin/src/components/breadcrumbs/index.tsx` (3x), `system/admin/src/components/entity/entityTable/components/EntityTableItem.tsx` (3x), `system/admin/src/components/entity/types.ts` (3x), `system/admin/src/components/fileManager/FileItem.tsx` (3x)

### `system/admin/src/components/entity/types.ts`
**Often changes with:** `system/admin/src/components/entity/entityTable/components/EntityTableItem.tsx` (6x), `system/admin/src/components/entity/entityEdit/EntityEdit.tsx` (5x), `system/admin/src/components/fileManager/FileManager.tsx` (4x), `system/admin/src/components/entity/entityTable/EntityTable.tsx` (3x), `system/admin/src/components/breadcrumbs/index.tsx` (3x)

### `system/admin/src/components/entity/utils.ts`
**Symbols:** const_fn:`customGraphQlPropertyToFragment`, const_fn:`addProperty`

### `system/admin/src/components/errorBoundaries/PageErrorBoundary.tsx`
**Imported by:** `system/admin/src/components/layout/Layout.tsx`
**Symbols:** class:`PageErrorBoundary`

### `system/admin/src/components/fileManager/FileItem.tsx`
**Imports:** `system/admin/src/components/buttons/IconButton.tsx`, `system/admin/src/components/fileManager/types.ts`
**Imported by:** `system/admin/src/components/fileManager/FileManager.tsx`
**Symbols:** const_fn:`FileItem`
**Often changes with:** `system/admin/src/components/entity/entityTable/components/EntityTableItem.tsx` (5x), `system/admin/src/components/fileManager/FileManager.tsx` (3x), `system/admin/src/components/entity/entityEdit/EntityEdit.tsx` (3x), `system/admin/src/components/entity/entityTable/components/TableHeader.tsx` (3x)

### `system/admin/src/components/fileManager/FileManager.test.tsx`
**Imports:** `system/admin/src/components/fileManager/FileManager.tsx`, `system/admin/src/components/fileManager/helpers.ts`

### `system/admin/src/components/fileManager/FileManager.tsx`
**Imports:** `system/admin/src/components/buttons/IconButton.tsx`, `system/admin/src/components/buttons/TextButton.tsx`, `system/admin/src/components/loadBox/LoadingStatus.tsx`, `system/admin/src/components/modal/Confirmation.tsx`, `themes/store/src/components/modals/baseModal/Modal.tsx`, `toolkits/commerce/src/mui/Pagination/Pagination.tsx`, `themes/store/src/components/toast/toast.tsx`, `system/admin/src/components/fileManager/FileItem.tsx`, `system/admin/src/components/fileManager/types.ts`
**Imported by:** `system/admin/src/components/fileManager/FileManager.test.tsx`, `system/admin/src/components/layout/Layout.tsx`
**Symbols:** class:`FileManager`
**Often changes with:** `system/admin/src/components/entity/entityTable/components/EntityTableItem.tsx` (5x), `system/admin/src/components/entity/types.ts` (4x), `system/admin/src/components/fileManager/FileItem.tsx` (3x), `system/admin/src/components/inputs/TextInput/RegisteredTextInput.tsx` (3x), `system/admin/src/components/inputs/TextInput/TextInput.tsx` (3x)

### `system/admin/src/components/fileManager/helpers.ts`
**Imported by:** `system/admin/src/components/fileManager/FileManager.test.tsx`
**Symbols:** const_fn:`getFileManager`

### `system/admin/src/components/fileManager/types.ts`
**Imported by:** `system/admin/src/components/fileManager/FileItem.tsx`, `system/admin/src/components/fileManager/FileManager.tsx`

### `system/admin/src/components/framePortal/FramePortal.tsx`
**Symbols:** class:`FramePortal`, const_fn:`updateHead`, const_fn:`observeDOM`
**Often changes with:** `system/admin/src/components/entity/entityTable/components/TableHeader.tsx` (3x), `system/admin/src/components/entity/types.ts` (3x)

### `system/admin/src/components/icons/clearFilter.tsx`
**Imported by:** `system/admin/src/components/entity/entityTable/components/PageHeader.tsx`
**Symbols:** function:`ClearFilterIcon`

### `system/admin/src/components/icons/grabIcon.tsx`
**Imported by:** `system/admin/src/components/inputs/GalleryInput/GalleryInput.tsx`, `system/admin/src/router-pages/settings/components/draggableCurrencies.tsx`, `system/admin/src/router-pages/settings/components/draggableEntityFields.tsx`, `system/admin/src/router-pages/settings/pages/store.tsx`
**Symbols:** const_fn:`GrabIcon`

### `system/admin/src/components/icons/marketicon.tsx`
**Imported by:** `system/admin/src/router-pages/settings/pages/index.tsx`
**Symbols:** const_fn:`MarketIcon`

### `system/admin/src/components/icons/spyIcon.tsx`
**Imported by:** `system/admin/src/router-pages/settings/pages/acl.tsx`
**Symbols:** const_fn:`SpyIcon`

### `system/admin/src/components/icons/stackIcon.tsx`
**Imported by:** `system/admin/src/router-pages/settings/pages/index.tsx`
**Symbols:** const_fn:`StackIcon`

### `system/admin/src/components/icons/toolsIcon.tsx`
**Symbols:** const_fn:`ToolsIcon`

### `system/admin/src/components/inputs/AutocompleteInput.tsx`
**Imports:** `toolkits/commerce/src/mui/Popper/Popper.tsx`, `system/admin/src/components/inputs/DateInput/styles.ts`, `system/admin/src/components/inputs/TextInput/TextInput.tsx`
**Imported by:** `system/admin/src/components/entity/entityEdit/components/EntityMetaFields.tsx`, `system/admin/src/components/entity/entityTable/components/SearchContent.tsx`, `system/admin/src/router-pages/order/components/PageContent.tsx`, `system/admin/src/router-pages/post/components/PostSettings.tsx`
**Symbols:** function:`AutocompleteInput`

### `system/admin/src/components/inputs/CheckboxInput.tsx`
**Imported by:** `system/admin/src/components/entity/entityTable/components/EntityTableItem.tsx`, `system/admin/src/components/entity/entityTable/components/TableHeader.tsx`, `system/admin/src/components/inputs/Search/ListItem.tsx`, `system/admin/src/components/transferList/CheckList.tsx`, `system/admin/src/helpers/customFields/fields.tsx`, `system/admin/src/router-pages/categoryList/components/CategoryItem.tsx`
**Symbols:** const_fn:`input`

### `system/admin/src/components/inputs/CodeEditor.tsx`
**Imported by:** `system/admin/src/router-pages/settings/pages/code.tsx`, `system/admin/src/router-pages/settings/pages/seo.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/HTMLBlockEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PageSettings.tsx`
**Symbols:** const_fn:`CodeEditor`

### `system/admin/src/components/inputs/ColorInput.tsx`
**Imports:** `themes/store/src/helpers/forceUpdate.ts`, `system/admin/src/components/inputs/TextInput/TextInput.tsx`
**Imported by:** `system/admin/src/helpers/customFields/fields.tsx`
**Symbols:** function:`ColorInput`, const_fn:`handleChange`, const_fn:`handleClose`, const_fn:`handleApply`, const_fn:`handleInputChange`

### `system/admin/src/components/inputs/DateInput/DateInput.tsx`
**Imports:** `system/admin/src/components/inputs/DateInput/styles.ts`
**Imported by:** `system/admin/src/components/entity/entityTable/components/SearchContent.tsx`, `system/admin/src/helpers/customFields/fields.tsx`, `system/admin/src/router-pages/post/components/PostSettings.tsx`
**Symbols:** function:`DateInput`, const_fn:`onCommonChange`, const_fn:`handleChange`, const_fn:`dateRangeValue`

### `system/admin/src/components/inputs/DateInput/index.ts`

### `system/admin/src/components/inputs/DateInput/styles.ts`
**Imports:** `system/admin/src/helpers/getPalette.ts`
**Imported by:** `plugins/main-menu/src/admin/styles.ts`, `plugins/main-menu/src/admin/widgets/SettingsPage.tsx`, `plugins/main-menu/src/admin/widgets/components/MenuItem.tsx`, `plugins/newsletter/src/admin/styles.ts`, `plugins/newsletter/src/admin/widgets/Dashboard.tsx`, `plugins/newsletter/src/admin/widgets/SettingsPage.tsx`, `plugins/newsletter/src/frontend/styles.ts`, `plugins/product-filter/src/frontend/styles.ts`, `plugins/product-filter/src/frontend/components/Filter.tsx`, `plugins/product-filter/src/frontend/components/Filter.tsx`
**Symbols:** const_fn:`mainColor`
**Often changes with:** `system/admin/src/components/layout/Layout.tsx` (3x)

### `system/admin/src/components/inputs/GalleryInput/GalleryInput.tsx`
**Imports:** `system/admin/src/components/icons/grabIcon.tsx`, `system/admin/src/components/inputs/Image/ImageInput.tsx`, `system/admin/src/components/inputs/GalleryInput/ImageItem.tsx`
**Imported by:** `system/admin/src/helpers/customFields/fields.tsx`, `system/admin/src/router-pages/product/components/MainInfoCard.tsx`
**Symbols:** class:`GalleryPicker`, const_fn:`images`, const_fn:`images`
**Often changes with:** `system/admin/src/components/inputs/Image/ImageInput.tsx` (4x), `system/admin/src/components/fileManager/FileManager.tsx` (3x)

### `system/admin/src/components/inputs/GalleryInput/ImageItem.tsx`
**Imports:** `system/admin/src/components/inputs/Image/ImageInput.tsx`
**Imported by:** `system/admin/src/components/inputs/GalleryInput/GalleryInput.tsx`
**Symbols:** const_fn:`ImageItem`, const_fn:`onSrcChange`

### `system/admin/src/components/inputs/Image/ImageInput.tsx`
**Imports:** `toolkits/commerce/tests/helpers.ts`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx`
**Imported by:** `system/admin/src/components/inputs/GalleryInput/GalleryInput.tsx`, `system/admin/src/components/inputs/GalleryInput/ImageItem.tsx`, `system/admin/src/components/inputs/Image/RegisteredImageInput.tsx`, `system/admin/src/helpers/customFields/fields.tsx`, `system/admin/src/router-pages/post/components/PostSettings.tsx`, `system/admin/src/router-pages/settings/components/newEntityForm.tsx`, `system/admin/src/router-pages/settings/pages/custom/CustomEntity/index.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/ImageBlockEditor.tsx`, `system/admin/src/router-pages/welcome/components/UserForm.tsx`
**Symbols:** const_fn:`ImageInput`, const_fn:`onMaximizeImage`
**Often changes with:** `system/admin/src/components/inputs/GalleryInput/GalleryInput.tsx` (4x), `system/admin/src/components/fileManager/FileManager.tsx` (3x)

### `system/admin/src/components/inputs/Image/RegisteredImageInput.tsx`
**Imports:** `system/admin/src/components/inputs/Image/ImageInput.tsx`
**Symbols:** function:`RegisteredImageInput`

### `system/admin/src/components/inputs/Image/index.tsx`

### `system/admin/src/components/inputs/Search/ListItem.tsx`
**Feature:** Search
**Imports:** `system/admin/src/components/inputs/CheckboxInput.tsx`, `themes/store/src/helpers/forceUpdate.ts`
**Imported by:** `system/admin/src/components/inputs/Search/SearchInput.tsx`

### `system/admin/src/components/inputs/Search/SearchInput.test.tsx`
**Feature:** Search
**Imports:** `system/admin/src/components/inputs/Search/SearchInput.tsx`

### `system/admin/src/components/inputs/Search/SearchInput.tsx`
**Feature:** Search
**Imports:** `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx`, `system/admin/src/components/inputs/Search/ListItem.tsx`
**Imported by:** `system/admin/src/components/inputs/Search/SearchInput.test.tsx`, `system/admin/src/router-pages/category/CategoryPage.tsx`, `system/admin/src/router-pages/coupon/Coupon.tsx`, `system/admin/src/router-pages/product/components/PageContent.tsx`
**Symbols:** class:`SearchInput`

### `system/admin/src/components/inputs/SelectInput/RegisteredSelectInput.tsx`
**Imports:** `system/admin/src/components/inputs/SelectInput/SelectInput.tsx`

### `system/admin/src/components/inputs/SelectInput/SelectInput.tsx`
**Imported by:** `system/admin/src/components/inputs/SelectInput/RegisteredSelectInput.tsx`, `system/admin/src/helpers/customFields/fields.tsx`, `system/admin/src/router-pages/product/components/MainInfoCard.tsx`, `system/admin/src/router-pages/product/components/VariantsTab.tsx`, `system/admin/src/router-pages/settings/components/draggableEntityFields.tsx`, `system/admin/src/router-pages/settings/pages/general.tsx`

### `system/admin/src/components/inputs/SelectInput/index.tsx`

### `system/admin/src/components/inputs/SwitchInput/RegisteredSwitchInput.tsx`
**Imports:** `system/admin/src/components/inputs/SwitchInput/SwitchInput.tsx`
**Symbols:** function:`RegisteredSwitchInput`

### `system/admin/src/components/inputs/SwitchInput/SwitchInput.tsx`
**Imported by:** `system/admin/src/components/entity/entityTable/components/ColumnConfigureItem.tsx`, `system/admin/src/components/inputs/SwitchInput/RegisteredSwitchInput.tsx`, `system/admin/src/router-pages/post/components/PostSettings.tsx`, `system/admin/src/router-pages/product/components/MainInfoCard.tsx`, `system/admin/src/router-pages/product/components/VariantsTab.tsx`, `system/admin/src/router-pages/settings/components/newRoleForm.tsx`, `system/admin/src/router-pages/settings/pages/general.tsx`, `system/admin/src/router-pages/settings/pages/store.tsx`, `system/admin/src/router-pages/settings/pages/custom/CustomRole/index.tsx`, `system/admin/src/router-pages/welcome/components/CmsSettingsForm.tsx`
**Symbols:** const_fn:`SwitchInput`

### `system/admin/src/components/inputs/SwitchInput/index.tsx`

### `system/admin/src/components/inputs/TextEditor/TextEditor.tsx`
**Imports:** `system/admin/src/helpers/editor/editor.ts`
**Imported by:** `system/admin/src/helpers/customFields/fields.tsx`
**Symbols:** class:`TextEditor`

### `system/admin/src/components/inputs/TextEditor/index.tsx`

### `system/admin/src/components/inputs/TextInput/RegisteredTextInput.tsx`
**Imports:** `system/server/src/helpers/utils.ts`, `system/admin/src/components/inputs/TextInput/TextInput.tsx`
**Symbols:** function:`RegisteredTextInput`
**Often changes with:** `system/admin/src/components/entity/entityTable/components/EntityTableItem.tsx` (3x), `system/admin/src/components/fileManager/FileManager.tsx` (3x), `system/admin/src/components/inputs/TextInput/TextInput.tsx` (3x), `system/admin/src/router-pages/settings/Settings.tsx` (3x)

### `system/admin/src/components/inputs/TextInput/TextInput.tsx`
**Imports:** `system/admin/src/helpers/NumberFormatCustom.tsx`
**Imported by:** `system/admin/src/components/inputs/AutocompleteInput.tsx`, `system/admin/src/components/inputs/ColorInput.tsx`, `system/admin/src/components/inputs/TextInput/RegisteredTextInput.tsx`
**Symbols:** const_fn:`inputField`
**Often changes with:** `system/admin/src/router-pages/settings/Settings.tsx` (4x), `system/admin/src/components/fileManager/FileManager.tsx` (3x), `system/admin/src/components/inputs/TextInput/RegisteredTextInput.tsx` (3x)

### `system/admin/src/components/inputs/TextInput/index.ts`

### `system/admin/src/components/inputs/utils.ts`
**Symbols:** const_fn:`getFieldErrorFromState`, const_fn:`getFieldErrorMessageFromState`

### `system/admin/src/components/layout/Layout.tsx`
**Imports:** `system/admin/src/components/sideNav/ResponsiveSideNav.tsx`, `system/admin/src/helpers/LayoutPortal.tsx`, `system/admin/src/helpers/navigation.tsx`, `system/admin/src/router-pages/settings/pages/store.tsx`, `system/admin/src/router-pages/404/404page.tsx`, `system/admin/src/components/errorBoundaries/PageErrorBoundary.tsx`, `system/admin/src/components/fileManager/FileManager.tsx`, `system/admin/src/components/modal/Confirmation.tsx`, `system/admin/src/components/layout/components/BrowserRouter.tsx`, `system/admin/src/components/layout/hooks/useAppState.ts`
**Symbols:** function:`Layout`
**Often changes with:** `system/admin/src/components/entity/entityTable/components/EntityTableItem.tsx` (3x), `system/admin/src/components/entity/entityTable/components/TableHeader.tsx` (3x), `system/admin/src/components/entity/types.ts` (3x), `system/admin/src/components/inputs/DateInput/styles.ts` (3x), `system/admin/src/components/sideNav/SideNav.tsx` (3x)

### `system/admin/src/components/layout/components/BrowserRouter.tsx`
**Feature:** UI Components
**Imported by:** `system/admin/src/components/layout/Layout.tsx`
**Symbols:** function:`BrowserRouter`

### `system/admin/src/components/layout/hooks/useAppState.ts`
**Feature:** Hooks
**Imports:** `themes/store/src/components/toast/toast.tsx`, `system/admin/src/constants/PageInfos.ts`, `system/admin/src/helpers/customEntities.tsx`, `themes/store/src/helpers/forceUpdate.ts`, `system/admin/src/helpers/loadPlugins.ts`, `system/admin/src/router-pages/settings/pages/store.tsx`
**Imported by:** `system/admin/src/components/layout/Layout.tsx`
**Symbols:** const_fn:`initApp`, const_fn:`onUnauthorized`, const_fn:`onRestApiError`, const_fn:`onGraphQlError`, const_fn:`onUserLogged`, function:`useAppState`
**Often changes with:** `system/admin/startup.js` (3x), `system/admin/src/components/layout/Layout.tsx` (3x)

### `system/admin/src/components/layout/hooks/useTheme.ts`
**Feature:** Hooks
**Imports:** `system/admin/src/helpers/getPalette.ts`, `system/admin/src/components/inputs/DateInput/styles.ts`
**Imported by:** `system/admin/src/components/layout/Layout.tsx`
**Symbols:** function:`useTheme`

### `system/admin/src/components/loadBox/LoadBox.tsx`
**Feature:** Database
**Imported by:** `system/admin/src/components/loadBox/Loadbox.test.tsx`, `system/admin/src/components/loadBox/LoadingStatus.tsx`, `system/admin/src/components/pluginSettingsLayout/PluginSettingsLayout.tsx`, `system/admin/src/components/systemMonitor/SystemMonitor.tsx`, `system/admin/src/router-pages/coupon/Coupon.tsx`
**Symbols:** const_fn:`LoadBox`

### `system/admin/src/components/loadBox/Loadbox.test.tsx`
**Feature:** Database
**Imports:** `system/admin/src/components/loadBox/LoadBox.tsx`

### `system/admin/src/components/loadBox/LoadingStatus.tsx`
**Feature:** Database
**Imports:** `system/admin/src/components/loadBox/LoadBox.tsx`
**Imported by:** `system/admin/src/components/fileManager/FileManager.tsx`, `system/admin/src/router-pages/login/LoginPage.tsx`, `system/admin/src/router-pages/settings/Settings.tsx`, `system/admin/src/router-pages/settings/pages/migration.tsx`, `system/admin/src/router-pages/settings/pages/seo.tsx`, `system/admin/src/router-pages/welcome/components/CmsSettingsForm.tsx`
**Symbols:** const_fn:`LoadingStatus`

### `system/admin/src/components/managerLogger/ManagerLogger.tsx`
**Symbols:** const_fn:`ManagerLogger`, const_fn:`handleOpenModal`, const_fn:`Notification`

### `system/admin/src/components/market/MarketItem.tsx`
**Imported by:** `system/admin/src/router-pages/pluginMarket/PluginMarket.tsx`, `system/admin/src/router-pages/themeMarket/ThemeMarket.tsx`
**Symbols:** function:`MarketItem`, const_fn:`installModule`

### `system/admin/src/components/market/MarketModal.tsx`
**Imported by:** `system/admin/src/components/pluginSettingsLayout/PluginSettingsLayout.tsx`, `system/admin/src/router-pages/pluginMarket/PluginMarket.tsx`, `system/admin/src/router-pages/themeMarket/ThemeMarket.tsx`
**Symbols:** function:`MarketModal`, const_fn:`installModule`

### `system/admin/src/components/modal/Confirmation.test.tsx`
**Imports:** `system/admin/src/components/modal/Confirmation.tsx`

### `system/admin/src/components/modal/Confirmation.tsx`
**Imports:** `system/admin/src/components/buttons/TextButton.tsx`, `system/admin/src/components/modal/Modal.tsx`
**Imported by:** `system/admin/src/components/entity/entityTable/EntityTable.tsx`, `system/admin/src/components/fileManager/FileManager.tsx`, `system/admin/src/components/layout/Layout.tsx`, `system/admin/src/components/modal/Confirmation.test.tsx`, `system/admin/src/components/notificationCenter/NotificationCenter.tsx`, `system/admin/src/components/topbar/Topbar.tsx`, `system/admin/src/router-pages/product/components/VariantsTab.tsx`, `system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx`
**Symbols:** const_fn:`ConfirmationModal`, class:`ConfirmPrompt`, const_fn:`askConfirmation`

### `system/admin/src/components/modal/Modal.tsx`
**Imported by:** `system/admin/src/components/modal/Confirmation.tsx`
**Symbols:** const_fn:`Modal`, const_fn:`setBlur`

### `system/admin/src/components/modal/index.tsx`

### `system/admin/src/components/modeSwitch/ModeSwitch.tsx`
**Imports:** `system/admin/src/components/inputs/DateInput/styles.ts`
**Symbols:** const_fn:`AdminModeSwitch`

### `system/admin/src/components/notificationCenter/NotificationCenter.tsx`
**Imports:** `toolkits/commerce/tests/helpers.ts`, `system/admin/src/router-pages/settings/pages/store.tsx`, `system/admin/src/components/modal/Confirmation.tsx`, `themes/store/src/components/toast/toast.tsx`, `system/admin/src/components/notificationCenter/UpdateInfoCard.tsx`
**Symbols:** const_fn:`mapStateToProps`, function:`NotificationCenter`, const_fn:`handleOpen`, const_fn:`handleStartUpdate`

### `system/admin/src/components/notificationCenter/UpdateInfoCard.tsx`
**Imported by:** `system/admin/src/components/notificationCenter/NotificationCenter.tsx`
**Symbols:** function:`UpdateInfoCard`, const_fn:`toggleChangelog`

### `system/admin/src/components/pagination/Pagination.tsx`
**Symbols:** const_fn:`Pagination`

### `system/admin/src/components/pluginSettingsLayout/PluginSettingsLayout.tsx`
**Feature:** Configuration
**Imports:** `themes/store/src/components/toast/toast.tsx`, `system/admin/src/constants/PageInfos.ts`, `system/admin/src/components/loadBox/LoadBox.tsx`, `system/admin/src/components/market/MarketModal.tsx`, `themes/store/src/components/modals/baseModal/Modal.tsx`, `system/admin/src/components/buttons/TextButton.tsx`, `system/admin/src/components/buttons/IconButton.tsx`
**Symbols:** function:`PluginSettingsLayout`, const_fn:`handleSave`, const_fn:`toggleOpenInfo`

### `system/admin/src/components/select/Select.tsx`
**Symbols:** function:`Select`, const_fn:`openLink`

### `system/admin/src/components/sideNav/ResponsiveSideNav.tsx`
**Imports:** `system/admin/src/components/buttons/IconButton.tsx`, `system/admin/src/helpers/navigation.tsx`, `system/admin/src/components/sideNav/SideNav.tsx`, `system/admin/src/components/sideNav/SwipeableTemporaryDrawer.tsx`
**Imported by:** `system/admin/src/components/entity/entityTable/components/PageHeader.tsx`, `system/admin/src/components/layout/Layout.tsx`, `system/admin/src/components/sideNav/SideNavLink.tsx`, `system/admin/src/router-pages/dashboard/Dashboard.tsx`, `system/admin/src/router-pages/settings/Settings.tsx`, `system/admin/src/router-pages/themeEdit/ThemeEdit.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PageActions.tsx`
**Symbols:** function:`LayoutSideNav`, function:`SwipeableSideNav`, function:`SideNavMobileButton`, function:`SideNavToggleButton`

### `system/admin/src/components/sideNav/SideNav.tsx`
**Imports:** `themes/store/src/helpers/forceUpdate.ts`, `system/admin/src/helpers/navigation.tsx`, `system/admin/src/router-pages/settings/pages/store.tsx`, `system/admin/src/components/topbar/Topbar.tsx`, `system/admin/src/components/sideNav/SideNavLink.tsx`
**Imported by:** `system/admin/src/components/sideNav/ResponsiveSideNav.tsx`
**Symbols:** const_fn:`SideNav`, const_fn:`toggleSubMenu`
**Often changes with:** `system/admin/src/components/layout/Layout.tsx` (3x), `system/admin/src/components/topbar/Topbar.tsx` (3x), `system/admin/src/components/sideNav/SideNavLink.tsx` (3x)

### `system/admin/src/components/sideNav/SideNavLink.tsx`
**Imports:** `system/admin/src/constants/PageInfos.ts`, `system/admin/src/components/sideNav/ResponsiveSideNav.tsx`
**Imported by:** `system/admin/src/components/sideNav/SideNav.tsx`
**Symbols:** const_fn:`SideNavLink`, const_fn:`hasPermission`, const_fn:`onLinkClick`
**Often changes with:** `system/admin/src/components/sideNav/SideNav.tsx` (3x)

### `system/admin/src/components/sideNav/SwipeableTemporaryDrawer.tsx`
**Imported by:** `system/admin/src/components/sideNav/ResponsiveSideNav.tsx`
**Symbols:** function:`SwipeableTemporaryDrawer`, const_fn:`toggleDrawer`

### `system/admin/src/components/skeleton/SkeletonPreloader.tsx`
**Imported by:** `system/admin/src/components/entity/entityTable/EntityTable.tsx`
**Symbols:** const_fn:`SkeletonPreloader`

### `system/admin/src/components/systemMonitor/SystemMonitor.tsx`
**Imports:** `system/admin/src/components/loadBox/LoadBox.tsx`, `themes/store/src/components/modals/baseModal/Modal.tsx`, `system/admin/src/components/systemMonitor/chartOptions.ts`
**Imported by:** `system/admin/src/components/topbar/Topbar.tsx`
**Symbols:** class:`SystemMonitor`

### `system/admin/src/components/systemMonitor/chartOptions.ts`
**Imported by:** `system/admin/src/components/systemMonitor/SystemMonitor.tsx`
**Symbols:** const_fn:`getCpuUsageOption`, const_fn:`getCmsCpuUsageOption`, const_fn:`getCmsMemoryUsageOption`, const_fn:`getPieOption`

### `system/admin/src/components/textFieldWithTooltip/TextFieldWithTooltip.tsx`
**Imports:** `system/admin/src/components/buttons/IconButton.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx`
**Symbols:** function:`TextFieldWithTooltip`, const_fn:`openLink`

### `system/admin/src/components/toast/index.tsx`

### `system/admin/src/components/toast/toast.tsx`
**Symbols:** class:`Toast`

### `system/admin/src/components/topbar/Topbar.tsx`
**Imports:** `system/admin/src/constants/PageInfos.ts`, `themes/store/src/helpers/forceUpdate.ts`, `toolkits/commerce/tests/helpers.ts`, `system/admin/src/router-pages/settings/pages/store.tsx`, `system/admin/src/components/cmsInfo/CmsInfo.tsx`, `toolkits/commerce/tests/helpers.ts`, `system/admin/src/components/modal/Confirmation.tsx`, `system/admin/src/components/systemMonitor/SystemMonitor.tsx`, `themes/store/src/components/toast/toast.tsx`
**Imported by:** `system/admin/src/components/sideNav/SideNav.tsx`
**Symbols:** const_fn:`Topbar`, const_fn:`handleLogout`, const_fn:`openFileManager`, const_fn:`openCmsInfo`, const_fn:`openDocs`, const_fn:`mapStateToProps`, const_fn:`handleStartUpdate`, const_fn:`UserMenu`
**Often changes with:** `system/admin/src/components/sideNav/SideNav.tsx` (3x), `system/admin/src/constants/PageInfos.ts` (3x)

### `system/admin/src/components/topbar/context.tsx`
**Symbols:** const_fn:`useContextBar`

### `system/admin/src/components/transferList/CheckList.tsx`
**Imports:** `system/admin/src/components/inputs/CheckboxInput.tsx`, `system/admin/src/components/transferList/helpers.ts`
**Imported by:** `system/admin/src/components/transferList/TransferList.tsx`, `system/admin/src/router-pages/attribute/components/AttributeValues.tsx`
**Symbols:** const_fn:`CheckList`, const_fn:`handleToggle`, const_fn:`numberOfChecked`, const_fn:`handleToggleAll`

### `system/admin/src/components/transferList/TransferList.tsx`
**Imports:** `system/admin/src/components/buttons/TextButton.tsx`, `system/admin/src/components/transferList/CheckList.tsx`, `system/admin/src/components/transferList/helpers.ts`
**Imported by:** `system/admin/src/router-pages/product/components/AttributesTab.tsx`
**Symbols:** function:`TransferList`, const_fn:`handleCheckedRight`, const_fn:`handleCheckedLeft`

### `system/admin/src/components/transferList/helpers.ts`
**Imported by:** `system/admin/src/components/transferList/CheckList.tsx`, `system/admin/src/components/transferList/TransferList.tsx`
**Symbols:** function:`not`, function:`intersection`, function:`union`

### `system/admin/src/components/virtualList/infiniteLoader.ts`
**Imports:** `system/admin/src/components/virtualList/isRangeVisible.ts`, `system/admin/src/components/virtualList/scanForUnloadedRanges.ts`, `system/admin/src/components/virtualList/types.ts`
**Symbols:** const_fn:`InfiniteLoader`

### `system/admin/src/components/virtualList/isInteger.ts`
**Symbols:** function:`isInteger`

### `system/admin/src/components/virtualList/isRangeVisible.ts`
**Imported by:** `system/admin/src/components/virtualList/infiniteLoader.ts`
**Symbols:** function:`isRangeVisible`

### `system/admin/src/components/virtualList/scanForUnloadedRanges.ts`
**Imports:** `system/admin/src/components/virtualList/types.ts`
**Imported by:** `system/admin/src/components/virtualList/infiniteLoader.ts`
**Symbols:** function:`scanForUnloadedRanges`

### `system/admin/src/components/virtualList/types.ts`
**Imported by:** `system/admin/src/components/virtualList/infiniteLoader.ts`, `system/admin/src/components/virtualList/scanForUnloadedRanges.ts`

### `system/admin/src/constants/PageInfos.ts`
**Imported by:** `system/admin/src/components/layout/hooks/useAppState.ts`, `system/admin/src/components/pluginSettingsLayout/PluginSettingsLayout.tsx`, `system/admin/src/components/sideNav/SideNavLink.tsx`, `system/admin/src/components/topbar/Topbar.tsx`, `system/admin/src/helpers/customEntities.tsx`, `system/admin/src/router-pages/attribute/AttributePage.tsx`, `system/admin/src/router-pages/attributeList/AttributesList.tsx`, `system/admin/src/router-pages/category/CategoryPage.tsx`, `system/admin/src/router-pages/categoryList/CategoryList.tsx`, `system/admin/src/router-pages/categoryList/components/CategoryItem.tsx`
**Often changes with:** `system/admin/src/components/topbar/Topbar.tsx` (3x), `system/admin/src/helpers/navigation.tsx` (3x), `system/admin/src/helpers/editor/editor.ts` (3x)

### `system/admin/src/constants/icons.tsx`
**Symbols:** const_fn:`PluginIcon`

### `system/admin/src/constants/languages.ts`
**Imported by:** `system/admin/src/router-pages/settings/Settings.test.tsx`, `system/admin/src/router-pages/settings/pages/general.tsx`

### `system/admin/src/constants/order.ts`
**Imported by:** `system/admin/src/router-pages/order/components/PageContent.tsx`, `system/admin/src/router-pages/orderList/OrderList.tsx`

### `system/admin/src/constants/timezones.ts`
**Imported by:** `system/admin/src/router-pages/settings/pages/general.tsx`

### `system/admin/src/declarations.d.ts`

### `system/admin/src/exports.ts`
**Imports:** `system/admin/src/redux/store.ts`

### `system/admin/src/helpers/Draggable/Draggable.ts`
**Imported by:** `system/admin/src/redux/store.ts`, `system/admin/src/router-pages/themeEdit/hooks/useBlockEvents.tsx`, `system/admin/src/router-pages/themeEdit/hooks/useHoveredFrames.tsx`, `system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx`
**Symbols:** class:`Draggable`

### `system/admin/src/helpers/LayoutPortal.tsx`
**Feature:** Utilities
**Imports:** `system/admin/src/helpers/forceUpdate.ts`
**Imported by:** `system/admin/src/components/layout/Layout.tsx`, `system/admin/src/helpers/editor/fontSize/FontSize.tsx`
**Symbols:** const_fn:`LayoutPortal`

### `system/admin/src/helpers/NumberFormatCustom.tsx`
**Feature:** Utilities
**Imported by:** `system/admin/src/components/inputs/TextInput/TextInput.tsx`, `system/admin/src/helpers/customFields/fields.tsx`
**Symbols:** function:`NumberFormatCustom`

### `system/admin/src/helpers/WidgetErrorBoundary.tsx`
**Feature:** Utilities
**Symbols:** class:`WidgetErrorBoundary`

### `system/admin/src/helpers/addressParser.tsx`
**Feature:** Utilities
**Imported by:** `system/admin/src/router-pages/order/components/PageContent.tsx`, `system/admin/src/router-pages/orderList/OrderList.tsx`, `system/admin/src/router-pages/user/User.tsx`, `system/admin/src/router-pages/userList/UserList.tsx`
**Symbols:** const_fn:`getValueView`, const_fn:`getTooltipValueView`, const_fn:`parseAddress`

### `system/admin/src/helpers/customEntities.tsx`
**Feature:** Utilities
**Imports:** `system/admin/src/components/entity/entityEdit/EntityEdit.tsx`, `system/admin/src/components/entity/entityTable/EntityTable.tsx`, `themes/store/src/types.ts`, `system/admin/src/constants/PageInfos.ts`, `system/admin/src/router-pages/settings/pages/store.tsx`, `system/admin/src/helpers/time.ts`
**Imported by:** `system/admin/src/components/layout/hooks/useAppState.ts`, `system/admin/src/helpers/navigation.tsx`, `system/admin/src/router-pages/attributeList/AttributesList.tsx`, `system/admin/src/router-pages/categoryList/CategoryList.tsx`, `system/admin/src/router-pages/couponList/CouponList.tsx`, `system/admin/src/router-pages/postList/PostList.tsx`, `system/admin/src/router-pages/productList/ProductList.tsx`, `system/admin/src/router-pages/settings/components/newEntityForm.tsx`, `system/admin/src/router-pages/tagList/TagList.tsx`, `system/admin/src/router-pages/userList/UserList.tsx`
**Symbols:** const_fn:`registerCustomEntity`, const_fn:`unregisterCustomEntity`, const_fn:`getCustomEntities`, const_fn:`getEntityRoutes`, const_fn:`entityBaseRoute`, const_fn:`entityListRoute`, const_fn:`getCustomEntityPages`, const_fn:`ListComp`, const_fn:`EntityComp`, const_fn:`getCustomEntitySidebarLinks`

### `system/admin/src/helpers/customFields/RenderCustomFields.tsx`
**Imports:** `themes/store/src/helpers/forceUpdate.ts`, `system/admin/src/helpers/customFields/helpers.ts`, `system/admin/src/helpers/customFields/state.ts`, `system/admin/src/helpers/customFields/types.ts`
**Symbols:** const_fn:`RenderCustomFields`, const_fn:`content`

### `system/admin/src/helpers/customFields/fields.tsx`
**Imports:** `system/admin/src/components/inputs/CheckboxInput.tsx`, `system/admin/src/components/inputs/ColorInput.tsx`, `system/admin/src/components/inputs/DateInput/DateInput.tsx`, `system/admin/src/components/inputs/GalleryInput/GalleryInput.tsx`, `system/admin/src/components/inputs/Image/ImageInput.tsx`, `system/admin/src/components/inputs/SelectInput/SelectInput.tsx`, `system/admin/src/components/inputs/TextEditor/TextEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx`, `system/admin/src/helpers/editor/editor.ts`, `system/admin/src/helpers/NumberFormatCustom.tsx`
**Symbols:** const_fn:`getCustomField`, const_fn:`getSimpleTextField`, const_fn:`registerSimpleTextCustomField`, const_fn:`getTextEditorField`, const_fn:`registerTextEditorCustomField`, const_fn:`getSelectField`, const_fn:`registerSelectCustomField`, const_fn:`getImageField`

### `system/admin/src/helpers/customFields/helpers.ts`
**Imports:** `system/admin/src/helpers/customFields/state.ts`, `system/admin/src/helpers/customFields/types.ts`
**Imported by:** `system/admin/src/helpers/customFields/RenderCustomFields.tsx`, `system/admin/src/helpers/customFields/fields.tsx`
**Symbols:** const_fn:`registerCustomField`, const_fn:`unregisterCustomField`, const_fn:`addOnFieldRegisterEventListener`, const_fn:`removeOnFieldRegisterEventListener`, const_fn:`getCustomMetaFor`, const_fn:`getCustomMetaKeysFor`, const_fn:`getCustomFieldsFor`

### `system/admin/src/helpers/customFields/hooks.ts`
**Imported by:** `system/admin/src/helpers/customFields/fields.tsx`
**Symbols:** const_fn:`useInitialValue`

### `system/admin/src/helpers/customFields/index.tsx`

### `system/admin/src/helpers/customFields/state.ts`
**Imports:** `system/admin/src/helpers/customFields/types.ts`
**Imported by:** `system/admin/src/helpers/customFields/RenderCustomFields.tsx`, `system/admin/src/helpers/customFields/fields.tsx`, `system/admin/src/helpers/customFields/helpers.ts`

### `system/admin/src/helpers/customFields/types.ts`
**Imported by:** `system/admin/src/helpers/customFields/RenderCustomFields.tsx`, `system/admin/src/helpers/customFields/helpers.ts`, `system/admin/src/helpers/customFields/state.ts`

### `system/admin/src/helpers/editor/customHtml/CustomHtml.ts`
**Imported by:** `system/admin/src/helpers/editor/editor.ts`
**Symbols:** const_fn:`getCustomHtmlClass`, class:`CustomHtml`

### `system/admin/src/helpers/editor/editor.ts`
**Imports:** `toolkits/commerce/tests/helpers.ts`, `themes/store/src/components/toast/toast.tsx`, `system/admin/src/helpers/editor/customHtml/CustomHtml.ts`, `system/admin/src/helpers/editor/fontSize/FontSize.tsx`
**Imported by:** `system/admin/src/components/inputs/TextEditor/TextEditor.tsx`, `system/admin/src/helpers/customFields/fields.tsx`, `system/admin/src/router-pages/post/components/PageContent.tsx`, `system/admin/src/router-pages/product/components/MainInfoCard.tsx`, `system/admin/src/router-pages/settings/components/customTextEditorInputField.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/EditorBlockEditor.tsx`
**Symbols:** const_fn:`importDependencies`, const_fn:`getTools`, const_fn:`initTextEditor`, const_fn:`getEditorHtml`, const_fn:`getEditorData`, const_fn:`destroyEditor`
**Often changes with:** `system/admin/src/constants/PageInfos.ts` (3x), `system/admin/src/helpers/navigation.tsx` (3x)

### `system/admin/src/helpers/editor/fontSize/FontSize.tsx`
**Imports:** `system/admin/src/helpers/LayoutPortal.tsx`, `system/admin/src/helpers/editor/fontSize/InputSlider.tsx`
**Imported by:** `system/admin/src/helpers/editor/editor.ts`
**Symbols:** class:`FontSize`, const_fn:`text`

### `system/admin/src/helpers/editor/fontSize/InputSlider.tsx`
**Imports:** `plugins/product-filter/src/frontend/components/Slider.tsx`
**Imported by:** `system/admin/src/helpers/editor/fontSize/FontSize.tsx`
**Symbols:** function:`InputSlider`, const_fn:`changeValue`, const_fn:`handleSliderChange`, const_fn:`handleInputChange`, const_fn:`handleBlur`

### `system/admin/src/helpers/editor/index.tsx`

### `system/admin/src/helpers/forceUpdate.ts`
**Feature:** Utilities
**Imported by:** `system/admin/src/helpers/LayoutPortal.tsx`
**Symbols:** function:`useForceUpdate`

### `system/admin/src/helpers/getPalette.ts`
**Feature:** Utilities
**Imported by:** `system/admin/src/components/inputs/DateInput/styles.ts`, `system/admin/src/components/layout/hooks/useTheme.ts`

### `system/admin/src/helpers/importDependencies.tsx`
**Feature:** Utilities
**Imports:** `system/utils/src/exports.ts`, `system/admin/src/components/inputs/DateInput/styles.ts`
**Imported by:** `system/admin/src/pages/_app.tsx`
**Symbols:** const_fn:`interopDefault`

### `system/admin/src/helpers/loadPlugins.ts`
**Feature:** Utilities
**Imported by:** `system/admin/src/components/layout/hooks/useAppState.ts`
**Symbols:** const_fn:`loadPlugin`, const_fn:`loadPlugins`

### `system/admin/src/helpers/navigation.tsx`
**Feature:** Utilities
**Imports:** `system/admin/src/helpers/customEntities.tsx`, `system/admin/src/router-pages/settings/pages/store.tsx`
**Imported by:** `system/admin/src/components/layout/Layout.tsx`, `system/admin/src/components/sideNav/ResponsiveSideNav.tsx`, `system/admin/src/components/sideNav/SideNav.tsx`, `system/admin/src/router-pages/login/LoginPage.tsx`
**Symbols:** const_fn:`registerPageInfoModifier`, const_fn:`registerSidebarLinkModifier`, const_fn:`getPageInfos`, const_fn:`getSideBarLinks`, const_fn:`getSideBarLinksFlat`, const_fn:`pushLinks`, const_fn:`getLinkByInfo`, const_fn:`getFromLinks`
**Often changes with:** `system/admin/src/constants/PageInfos.ts` (3x), `system/admin/src/helpers/editor/editor.ts` (3x)

### `system/admin/src/helpers/registerThemeEditor.ts`
**Feature:** Utilities
**Symbols:** const_fn:`getPluginBlockId`, const_fn:`registerThemeEditorPluginBlock`, const_fn:`onPluginBlockRegister`, const_fn:`getPluginBlocks`

### `system/admin/src/helpers/slugify.ts`
**Feature:** Utilities
**Imported by:** `system/admin/src/router-pages/settings/components/draggableEntityFields.tsx`, `system/admin/src/router-pages/settings/components/newEntityForm.tsx`, `system/admin/src/router-pages/settings/components/newRoleForm.tsx`, `system/admin/src/router-pages/settings/pages/custom/CustomEntity/index.tsx`, `system/admin/src/router-pages/settings/pages/custom/CustomRole/index.tsx`
**Symbols:** function:`slugify`

### `system/admin/src/helpers/time.ts`
**Feature:** Utilities
**Imported by:** `system/admin/src/components/entity/entityTable/components/EntityTableItem.tsx`, `system/admin/src/helpers/customEntities.tsx`, `system/admin/src/router-pages/order/components/PageContent.tsx`, `system/admin/src/router-pages/orderList/OrderList.tsx`, `system/admin/src/router-pages/postList/PostList.tsx`, `system/admin/src/router-pages/reviewList/ReviewList.tsx`
**Symbols:** const_fn:`toLocaleDateTimeString`, const_fn:`toLocaleDateString`, const_fn:`toLocaleTimeString`, const_fn:`timeSince`, const_fn:`formatTimeAgo`

### `system/admin/src/hooks/useBlocker.ts`
**Feature:** Hooks
**Imported by:** `system/admin/src/router-pages/post/contexts/PostContext.tsx`
**Symbols:** function:`useBlocker`, function:`usePrompt`

### `system/admin/src/hooks/useDashboard.tsx`
**Feature:** Hooks
**Imports:** `system/core/frontend/src/components/AdminPanelWidget/WidgetErrorBoundary.tsx`
**Imported by:** `system/admin/src/router-pages/dashboard/Dashboard.tsx`, `system/admin/src/router-pages/dashboard/components/addWidgetMenu.tsx`, `system/admin/src/router-pages/dashboard/widgets/ordersLastWeek.tsx`, `system/admin/src/router-pages/dashboard/widgets/pageViews.tsx`, `system/admin/src/router-pages/dashboard/widgets/pageViewsList.tsx`, `system/admin/src/router-pages/dashboard/widgets/productRating.tsx`, `system/admin/src/router-pages/dashboard/widgets/productReviews.tsx`, `system/admin/src/router-pages/dashboard/widgets/salesLastWeek.tsx`, `system/admin/src/router-pages/dashboard/widgets/salesValue.tsx`, `system/admin/src/router-pages/dashboard/widgets/widgetPanel.tsx`
**Symbols:** const_fn:`useDashboardContext`, const_fn:`useDashboard`, const_fn:`DashboardContextProvider`

### `system/admin/src/hooks/useDebounce.tsx`
**Feature:** Hooks
**Symbols:** function:`useDebounceFn`, function:`useDebounce`

### `system/admin/src/hooks/useLongPress.tsx`
**Feature:** Hooks
**Imported by:** `system/admin/src/router-pages/dashboard/Dashboard.tsx`
**Symbols:** const_fn:`useLongPress`, const_fn:`isTouchEvent`, const_fn:`preventDefault`

### `system/admin/src/pages/_app.tsx`
**Feature:** Pages
**Imports:** `system/admin/src/helpers/importDependencies.tsx`
**Symbols:** function:`CustomApp`

### `system/admin/src/pages/_document.tsx`
**Feature:** Pages
**Imports:** `system/renderer/src/helpers/document.tsx`
**Symbols:** function:`Document`

### `system/admin/src/pages/api/public-env.ts`
**Feature:** API Layer
**Symbols:** function:`handler`

### `system/admin/src/pages/index.tsx`
**Feature:** Pages
**Symbols:** function:`Index`

### `system/admin/src/redux/helpers.ts`
**Feature:** Redux State
**Imports:** `system/admin/src/redux/store.ts`
**Imported by:** `system/admin/src/redux/store.ts`
**Symbols:** const_fn:`toggleItemSelection`, const_fn:`toggleSelectAll`, const_fn:`countSelectedItems`, const_fn:`resetSelected`, const_fn:`getSelectedInput`, const_fn:`updateStatus`, const_fn:`startUpdateChecker`, const_fn:`updateChecker`

### `system/admin/src/redux/store.ts`
**Feature:** Redux State
**Imports:** `system/admin/src/helpers/Draggable/Draggable.ts`, `system/admin/src/redux/helpers.ts`
**Imported by:** `system/admin/src/exports.ts`, `system/admin/src/redux/helpers.ts`

### `system/admin/src/router-pages/404/404page.tsx`
**Imported by:** `system/admin/src/components/layout/Layout.tsx`
**Symbols:** function:`Page404`

### `system/admin/src/router-pages/attribute/AttributePage.tsx`
**Imports:** `system/admin/src/components/entity/entityEdit/EntityEdit.tsx`, `system/admin/src/constants/PageInfos.ts`, `system/admin/src/router-pages/attribute/components/AttributeValues.tsx`
**Symbols:** function:`AttributePage`

### `system/admin/src/router-pages/attribute/components/AttributeValues.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/components/buttons/IconButton.tsx`, `system/admin/src/components/transferList/CheckList.tsx`, `system/admin/src/router-pages/attribute/components/ValueItem.tsx`
**Imported by:** `system/admin/src/router-pages/attribute/AttributePage.tsx`
**Symbols:** const_fn:`AttributeValues`, const_fn:`handleAddValue`, const_fn:`handleCheckedValuesChange`, const_fn:`handleDeleteAttribute`

### `system/admin/src/router-pages/attribute/components/ValueItem.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/components/buttons/IconButton.tsx`, `toolkits/commerce/tests/helpers.ts`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx`
**Imported by:** `system/admin/src/router-pages/attribute/components/AttributeValues.tsx`
**Symbols:** const_fn:`ValueItem`, const_fn:`handleChangeIcon`, const_fn:`handleDeleteValue`, const_fn:`handleValueNameChange`

### `system/admin/src/router-pages/attributeList/AttributesList.tsx`
**Imports:** `system/admin/src/components/entity/entityTable/EntityTable.tsx`, `system/admin/src/constants/PageInfos.ts`, `system/admin/src/helpers/customEntities.tsx`
**Imported by:** `system/admin/src/router-pages/attributeList/AttributesPage.test.tsx`
**Symbols:** function:`AttributesList`

### `system/admin/src/router-pages/attributeList/AttributesPage.test.tsx`
**Imports:** `system/admin/src/router-pages/attributeList/AttributesList.tsx`

### `system/admin/src/router-pages/category/CategoryPage.test.tsx`
**Imports:** `system/admin/src/router-pages/category/CategoryPage.tsx`

### `system/admin/src/router-pages/category/CategoryPage.tsx`
**Imports:** `system/admin/src/components/inputs/Search/SearchInput.tsx`, `system/admin/src/components/entity/entityEdit/EntityEdit.tsx`, `system/admin/src/constants/PageInfos.ts`
**Imported by:** `system/admin/src/router-pages/category/CategoryPage.test.tsx`
**Symbols:** function:`CategoryPage`, const_fn:`handleSearchRequest`, const_fn:`handleParentCategoryChange`, const_fn:`getParentCategory`

### `system/admin/src/router-pages/categoryList/CategoryList.test.tsx`
**Imports:** `system/admin/src/router-pages/categoryList/CategoryList.tsx`, `system/admin/src/router-pages/settings/pages/store.tsx`

### `system/admin/src/router-pages/categoryList/CategoryList.tsx`
**Imports:** `system/admin/src/components/entity/entityTable/EntityTable.tsx`, `themes/store/src/types.ts`, `system/admin/src/constants/PageInfos.ts`, `system/admin/src/helpers/customEntities.tsx`, `themes/store/src/helpers/forceUpdate.ts`, `system/admin/src/router-pages/categoryList/components/HeaderActions.tsx`, `system/admin/src/router-pages/categoryList/components/TreeView.tsx`
**Imported by:** `system/admin/src/router-pages/categoryList/CategoryList.test.tsx`
**Symbols:** function:`CategoryList`, const_fn:`handleCollapseAll`, const_fn:`handleExpandAll`

### `system/admin/src/router-pages/categoryList/components/CategoryItem.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/components/buttons/IconButton.tsx`, `system/admin/src/components/inputs/CheckboxInput.tsx`, `system/admin/src/constants/PageInfos.ts`, `themes/store/src/helpers/forceUpdate.ts`, `system/admin/src/router-pages/settings/pages/store.tsx`, `toolkits/commerce/src/base/CategoryList/CategoryList.tsx`
**Imported by:** `system/admin/src/router-pages/categoryList/components/TreeView.tsx`
**Symbols:** const_fn:`mapStateToProps`, const_fn:`CategoryItem`, const_fn:`setExpanded`, const_fn:`handleToggleCollapse`, const_fn:`togglePrimary`, const_fn:`loadChildren`, const_fn:`handleDelete`, function:`TransitionComponent`

### `system/admin/src/router-pages/categoryList/components/HeaderActions.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/components/buttons/IconButton.tsx`, `toolkits/commerce/src/base/CategoryList/CategoryList.tsx`
**Imported by:** `system/admin/src/router-pages/categoryList/CategoryList.tsx`
**Symbols:** function:`HeaderActions`

### `system/admin/src/router-pages/categoryList/components/TreeView.tsx`
**Feature:** UI Components
**Imports:** `themes/store/src/types.ts`, `toolkits/commerce/tests/helpers.ts`, `system/admin/src/router-pages/categoryList/components/CategoryItem.tsx`
**Imported by:** `system/admin/src/router-pages/categoryList/CategoryList.tsx`
**Symbols:** function:`TreeView`, const_fn:`handleDeleteCategory`, const_fn:`getRootCategories`, const_fn:`handleToggleItemSelection`

### `system/admin/src/router-pages/coupon/Coupon.test.tsx`
**Imports:** `system/admin/src/router-pages/coupon/Coupon.tsx`

### `system/admin/src/router-pages/coupon/Coupon.tsx`
**Imports:** `system/admin/src/components/buttons/IconButton.tsx`, `system/admin/src/components/entity/entityEdit/EntityEdit.tsx`, `system/admin/src/components/inputs/Search/SearchInput.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx`, `system/admin/src/components/loadBox/LoadBox.tsx`, `system/admin/src/constants/PageInfos.ts`
**Imported by:** `system/admin/src/router-pages/coupon/Coupon.test.tsx`
**Symbols:** function:`CouponPage`, const_fn:`handleGenerateCode`, const_fn:`handleSearchCategory`, const_fn:`init`, const_fn:`handleSearchProduct`, const_fn:`init`

### `system/admin/src/router-pages/couponList/CouponList.test.tsx`
**Imports:** `system/admin/src/router-pages/couponList/CouponList.tsx`, `system/admin/src/router-pages/settings/pages/store.tsx`

### `system/admin/src/router-pages/couponList/CouponList.tsx`
**Imports:** `system/admin/src/components/entity/entityTable/EntityTable.tsx`, `system/admin/src/constants/PageInfos.ts`, `system/admin/src/helpers/customEntities.tsx`
**Imported by:** `system/admin/src/router-pages/couponList/CouponList.test.tsx`
**Symbols:** function:`CouponList`

### `system/admin/src/router-pages/dashboard/Dashboard.test.tsx`
**Feature:** Dashboard
**Imports:** `system/admin/src/router-pages/dashboard/Dashboard.tsx`
**Symbols:** class:`CountUp`

### `system/admin/src/router-pages/dashboard/Dashboard.tsx`
**Feature:** Dashboard
**Imports:** `system/admin/src/components/buttons/TextButton.tsx`, `system/admin/src/components/sideNav/ResponsiveSideNav.tsx`, `system/admin/src/hooks/useDashboard.tsx`, `system/admin/src/hooks/useLongPress.tsx`, `system/admin/src/router-pages/dashboard/components/addWidgetMenu.tsx`, `system/admin/src/router-pages/dashboard/widgets/ordersLastWeek.tsx`, `system/admin/src/router-pages/dashboard/widgets/pageViews.tsx`, `system/admin/src/router-pages/dashboard/widgets/pageViewsList.tsx`, `system/admin/src/router-pages/dashboard/widgets/productRating.tsx`, `system/admin/src/router-pages/dashboard/widgets/productReviews.tsx`
**Imported by:** `plugins/newsletter/tests/admin/Dashboard.test.tsx`, `system/admin/src/router-pages/dashboard/Dashboard.test.tsx`
**Symbols:** const_fn:`Dashboard`, const_fn:`DashboardLoader`, const_fn:`DashboardWrapper`
**Often changes with:** `system/admin/src/components/layout/Layout.tsx` (3x)

### `system/admin/src/router-pages/dashboard/components/StarRating.tsx`
**Feature:** UI Components
**Imported by:** `system/admin/src/router-pages/dashboard/widgets/productRating.tsx`, `system/admin/src/router-pages/dashboard/widgets/productReviews.tsx`
**Symbols:** const_fn:`StarRating`

### `system/admin/src/router-pages/dashboard/components/addWidgetMenu.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/hooks/useDashboard.tsx`
**Imported by:** `system/admin/src/router-pages/dashboard/Dashboard.tsx`
**Symbols:** const_fn:`AddWidgetMenu`

### `system/admin/src/router-pages/dashboard/widgets/areachart.tsx`

### `system/admin/src/router-pages/dashboard/widgets/ordersLastWeek.tsx`
**Imports:** `system/admin/src/hooks/useDashboard.tsx`, `system/admin/src/router-pages/dashboard/widgets/widgetPanel.tsx`
**Imported by:** `system/admin/src/router-pages/dashboard/Dashboard.tsx`
**Symbols:** function:`numFormat`, const_fn:`OrdersLastWeekWidget`

### `system/admin/src/router-pages/dashboard/widgets/pageViews.tsx`
**Imports:** `system/admin/src/hooks/useDashboard.tsx`, `system/admin/src/router-pages/dashboard/widgets/widgetPanel.tsx`
**Imported by:** `system/admin/src/router-pages/dashboard/Dashboard.tsx`
**Symbols:** const_fn:`PageViewsWidget`

### `system/admin/src/router-pages/dashboard/widgets/pageViewsList.tsx`
**Imports:** `system/admin/src/hooks/useDashboard.tsx`, `system/admin/src/router-pages/dashboard/widgets/widgetPanel.tsx`
**Imported by:** `system/admin/src/router-pages/dashboard/Dashboard.tsx`
**Symbols:** const_fn:`PageViewsList`

### `system/admin/src/router-pages/dashboard/widgets/productRating.tsx`
**Imports:** `system/admin/src/hooks/useDashboard.tsx`, `system/admin/src/router-pages/dashboard/components/StarRating.tsx`, `system/admin/src/router-pages/dashboard/widgets/widgetPanel.tsx`
**Imported by:** `system/admin/src/router-pages/dashboard/Dashboard.tsx`
**Symbols:** const_fn:`ProductRatingWidget`

### `system/admin/src/router-pages/dashboard/widgets/productReviews.tsx`
**Imports:** `system/admin/src/hooks/useDashboard.tsx`, `system/admin/src/router-pages/dashboard/components/StarRating.tsx`, `system/admin/src/router-pages/dashboard/widgets/widgetPanel.tsx`
**Imported by:** `system/admin/src/router-pages/dashboard/Dashboard.tsx`
**Symbols:** const_fn:`ProductReviewsList`

### `system/admin/src/router-pages/dashboard/widgets/salesLastWeek.tsx`
**Imports:** `system/admin/src/hooks/useDashboard.tsx`, `system/admin/src/router-pages/dashboard/widgets/widgetPanel.tsx`
**Imported by:** `system/admin/src/router-pages/dashboard/Dashboard.tsx`
**Symbols:** function:`numFormat`, const_fn:`SalesLastWeekWidget`

### `system/admin/src/router-pages/dashboard/widgets/salesValue.tsx`
**Imports:** `system/admin/src/hooks/useDashboard.tsx`, `system/admin/src/router-pages/dashboard/widgets/widgetPanel.tsx`
**Imported by:** `system/admin/src/router-pages/dashboard/Dashboard.tsx`
**Symbols:** const_fn:`SalesValueWidget`

### `system/admin/src/router-pages/dashboard/widgets/widgetPanel.tsx`
**Imports:** `system/admin/src/hooks/useDashboard.tsx`
**Imported by:** `system/admin/src/router-pages/dashboard/Dashboard.tsx`, `system/admin/src/router-pages/dashboard/widgets/ordersLastWeek.tsx`, `system/admin/src/router-pages/dashboard/widgets/pageViews.tsx`, `system/admin/src/router-pages/dashboard/widgets/pageViewsList.tsx`, `system/admin/src/router-pages/dashboard/widgets/productRating.tsx`, `system/admin/src/router-pages/dashboard/widgets/productReviews.tsx`, `system/admin/src/router-pages/dashboard/widgets/salesLastWeek.tsx`, `system/admin/src/router-pages/dashboard/widgets/salesValue.tsx`
**Symbols:** const_fn:`randomNumber`, const_fn:`WidgetPanel`

### `system/admin/src/router-pages/login/LoginPage.test.tsx`
**Feature:** Authentication
**Imports:** `system/admin/src/router-pages/login/LoginPage.tsx`

### `system/admin/src/router-pages/login/LoginPage.tsx`
**Feature:** Authentication
**Imports:** `system/admin/src/components/loadBox/LoadingStatus.tsx`, `themes/store/src/components/toast/toast.tsx`, `system/admin/src/helpers/navigation.tsx`, `system/admin/src/router-pages/login/components/ForgotPassForm.tsx`, `system/admin/src/router-pages/login/components/ResetPassForm.tsx`, `system/admin/src/router-pages/login/components/SignInForm.tsx`
**Imported by:** `system/admin/src/router-pages/login/LoginPage.test.tsx`
**Symbols:** const_fn:`LoginPage`, const_fn:`checkAuth`, const_fn:`loginSuccess`, const_fn:`handleGoToForgotPass`

### `system/admin/src/router-pages/login/components/ForgotPassForm.tsx`
**Feature:** UI Components
**Imports:** `themes/store/src/components/toast/toast.tsx`
**Imported by:** `system/admin/src/router-pages/login/LoginPage.tsx`
**Symbols:** const_fn:`ForgotPassForm`, const_fn:`handleForgotPass`

### `system/admin/src/router-pages/login/components/ResetPassForm.tsx`
**Feature:** UI Components
**Imports:** `themes/store/src/components/toast/toast.tsx`
**Imported by:** `system/admin/src/router-pages/login/LoginPage.tsx`
**Symbols:** const_fn:`ResetPassForm`, const_fn:`handleResetPass`

### `system/admin/src/router-pages/login/components/SignInForm.tsx`
**Feature:** UI Components
**Imports:** `themes/store/src/components/toast/toast.tsx`
**Imported by:** `system/admin/src/router-pages/login/LoginPage.tsx`
**Symbols:** const_fn:`SignInForm`, const_fn:`handleLoginClick`

### `system/admin/src/router-pages/order/Order.test.tsx`
**Imports:** `system/admin/src/router-pages/order/Order.tsx`

### `system/admin/src/router-pages/order/Order.tsx`
**Imports:** `system/admin/src/components/entity/entityEdit/EntityEdit.tsx`, `system/admin/src/constants/PageInfos.ts`, `system/admin/src/router-pages/order/components/PageContent.tsx`
**Imported by:** `system/admin/src/router-pages/order/Order.test.tsx`
**Symbols:** function:`OrderPage`
**Often changes with:** `system/admin/src/router-pages/post/components/PageContent.tsx` (3x)

### `system/admin/src/router-pages/order/components/PageContent.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/components/entity/entityEdit/components/EntityCustomFields.tsx`, `themes/store/src/types.ts`, `system/admin/src/components/inputs/AutocompleteInput.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx`, `system/admin/src/constants/order.ts`, `system/admin/src/constants/PageInfos.ts`, `system/admin/src/helpers/addressParser.tsx`, `themes/store/src/helpers/forceUpdate.ts`, `system/admin/src/helpers/time.ts`
**Imported by:** `system/admin/src/router-pages/order/Order.tsx`
**Symbols:** function:`PageContent`, const_fn:`updateCart`, const_fn:`products`, const_fn:`handleDeleteFromCart`, const_fn:`handleInputChange`, const_fn:`onPriceChange`

### `system/admin/src/router-pages/orderList/OrderList.test.tsx`
**Imports:** `system/admin/src/router-pages/orderList/OrderList.tsx`, `system/admin/src/router-pages/settings/pages/store.tsx`

### `system/admin/src/router-pages/orderList/OrderList.tsx`
**Imports:** `system/admin/src/components/entity/entityTable/EntityTable.tsx`, `system/admin/src/constants/order.ts`, `system/admin/src/constants/PageInfos.ts`, `system/admin/src/helpers/addressParser.tsx`, `system/admin/src/helpers/time.ts`
**Imported by:** `system/admin/src/router-pages/orderList/OrderList.test.tsx`
**Symbols:** function:`OrderTable`

### `system/admin/src/router-pages/plugin/PluginPage.test.tsx`
**Imports:** `system/admin/src/router-pages/plugin/PluginPage.tsx`

### `system/admin/src/router-pages/plugin/PluginPage.tsx`
**Imported by:** `system/admin/src/router-pages/plugin/PluginPage.test.tsx`
**Symbols:** const_fn:`PluginPage`, const_fn:`getInfos`, const_fn:`getSettings`
**Often changes with:** `system/admin/src/router-pages/pluginList/PluginList.tsx` (3x)

### `system/admin/src/router-pages/pluginList/PluginList.test.tsx`
**Imports:** `system/admin/src/router-pages/pluginList/PluginList.tsx`

### `system/admin/src/router-pages/pluginList/PluginList.tsx`
**Imports:** `system/admin/src/components/buttons/IconButton.tsx`, `system/admin/src/components/entity/entityTable/EntityTable.tsx`, `themes/store/src/types.ts`, `themes/store/src/components/toast/toast.tsx`, `system/admin/src/constants/PageInfos.ts`
**Imported by:** `system/admin/src/router-pages/pluginList/PluginList.test.tsx`
**Symbols:** function:`PluginList`, const_fn:`getPlugins`, const_fn:`pluginEntity`, const_fn:`reloadPlugins`, const_fn:`handleActivatePlugin`, const_fn:`handleDeletePlugin`
**Often changes with:** `system/admin/src/router-pages/settings/Settings.tsx` (3x), `system/admin/startup.js` (3x), `system/admin/src/components/layout/Layout.tsx` (3x), `system/admin/src/router-pages/plugin/PluginPage.tsx` (3x)

### `system/admin/src/router-pages/pluginMarket/PluginMarket.test.tsx`
**Imports:** `system/admin/src/router-pages/pluginMarket/PluginMarket.tsx`

### `system/admin/src/router-pages/pluginMarket/PluginMarket.tsx`
**Imports:** `system/admin/src/components/market/MarketItem.tsx`, `system/admin/src/components/market/MarketModal.tsx`, `themes/store/src/components/modals/baseModal/Modal.tsx`, `toolkits/commerce/src/mui/Pagination/Pagination.tsx`, `themes/store/src/components/toast/toast.tsx`
**Imported by:** `system/admin/src/router-pages/pluginMarket/PluginMarket.test.tsx`
**Symbols:** class:`PluginMarket`, const_fn:`preloader`

### `system/admin/src/router-pages/post/Post.test.tsx`
**Imports:** `system/admin/src/router-pages/post/Post.tsx`

### `system/admin/src/router-pages/post/Post.tsx`
**Imports:** `system/admin/src/components/entity/entityEdit/EntityEdit.tsx`, `system/admin/src/constants/PageInfos.ts`, `system/admin/src/router-pages/post/components/HeaderActions.tsx`, `system/admin/src/router-pages/post/components/PageContent.tsx`, `system/admin/src/router-pages/post/contexts/PostContext.tsx`
**Imported by:** `system/admin/src/router-pages/post/Post.test.tsx`
**Symbols:** function:`PostPage`, function:`PostEdit`
**Often changes with:** `system/admin/src/router-pages/product/Product.tsx` (3x)

### `system/admin/src/router-pages/post/components/HeaderActions.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/components/buttons/IconButton.tsx`, `system/admin/src/components/buttons/TextButton.tsx`, `themes/store/src/helpers/forceUpdate.ts`, `themes/store/src/types.ts`, `system/admin/src/router-pages/post/contexts/PostContext.tsx`, `system/admin/src/router-pages/post/components/PostSettings.tsx`
**Imported by:** `system/admin/src/router-pages/post/Post.tsx`
**Symbols:** function:`HeaderActions`, const_fn:`getPostTags`, const_fn:`data`, const_fn:`handleToggleSettings`, const_fn:`handleUnpublish`, const_fn:`handlePublish`, const_fn:`handleChangeTitle`

### `system/admin/src/router-pages/post/components/PageContent.tsx`
**Feature:** UI Components
**Imports:** `themes/store/src/types.ts`, `system/admin/src/helpers/editor/editor.ts`, `themes/store/src/helpers/forceUpdate.ts`, `system/admin/src/router-pages/post/contexts/PostContext.tsx`
**Imported by:** `system/admin/src/router-pages/post/Post.tsx`
**Symbols:** function:`PageContent`, const_fn:`_initEditor`
**Often changes with:** `system/admin/src/router-pages/order/Order.tsx` (3x)

### `system/admin/src/router-pages/post/components/PostSettings.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/components/buttons/IconButton.tsx`, `system/admin/src/components/buttons/TextButton.tsx`, `system/admin/src/components/inputs/AutocompleteInput.tsx`, `system/admin/src/components/inputs/DateInput/DateInput.tsx`, `system/admin/src/components/inputs/SwitchInput/SwitchInput.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx`, `system/admin/src/components/inputs/Image/ImageInput.tsx`, `themes/store/src/helpers/forceUpdate.ts`, `system/admin/src/router-pages/post/contexts/PostContext.tsx`
**Imported by:** `system/admin/src/router-pages/post/components/HeaderActions.tsx`
**Symbols:** const_fn:`PostSettings`, const_fn:`handleChangeTags`, const_fn:`handleChangeKeywords`, const_fn:`handleClose`, const_fn:`handleChangePublishDate`

### `system/admin/src/router-pages/post/contexts/PostContext.tsx`
**Imports:** `system/admin/src/hooks/useBlocker.ts`
**Imported by:** `system/admin/src/router-pages/post/Post.tsx`, `system/admin/src/router-pages/post/components/HeaderActions.tsx`, `system/admin/src/router-pages/post/components/PageContent.tsx`, `system/admin/src/router-pages/post/components/PostSettings.tsx`
**Symbols:** const_fn:`PostContextProvider`, const_fn:`getInput`

### `system/admin/src/router-pages/postList/PostList.test.tsx`
**Imports:** `system/admin/src/router-pages/settings/pages/store.tsx`, `system/admin/src/router-pages/postList/PostList.tsx`

### `system/admin/src/router-pages/postList/PostList.tsx`
**Imports:** `system/admin/src/components/entity/entityTable/EntityTable.tsx`, `system/admin/src/constants/PageInfos.ts`, `system/admin/src/helpers/customEntities.tsx`, `system/admin/src/helpers/time.ts`
**Imported by:** `system/admin/src/router-pages/postList/PostList.test.tsx`
**Symbols:** function:`PostTable`, const_fn:`getUsers`, const_fn:`getPostTags`, const_fn:`data`

### `system/admin/src/router-pages/product/Product.test.tsx`
**Imports:** `system/admin/src/router-pages/product/Product.tsx`

### `system/admin/src/router-pages/product/Product.tsx`
**Imports:** `system/admin/src/components/entity/entityEdit/EntityEdit.tsx`, `system/admin/src/constants/PageInfos.ts`, `system/admin/src/router-pages/product/components/Header.tsx`, `system/admin/src/router-pages/product/components/PageContent.tsx`, `system/admin/src/router-pages/product/contexts/Product.ts`, `system/admin/src/router-pages/product/hooks/useTabs.ts`
**Imported by:** `system/admin/src/router-pages/product/Product.test.tsx`
**Symbols:** function:`ProductPage`
**Often changes with:** `system/admin/src/router-pages/product/components/PageContent.tsx` (4x), `system/admin/src/router-pages/product/components/VariantsTab.tsx` (3x), `system/admin/src/router-pages/product/hooks/useTabs.ts` (3x), `system/admin/src/router-pages/post/Post.tsx` (3x)

### `system/admin/src/router-pages/product/components/AttributesTab.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/components/buttons/IconButton.tsx`, `system/admin/src/components/buttons/TextButton.tsx`, `system/admin/src/components/transferList/TransferList.tsx`
**Imported by:** `system/admin/src/router-pages/product/components/PageContent.tsx`
**Symbols:** function:`AttributesTab`, const_fn:`addAttribute`, const_fn:`deleteAttribute`, const_fn:`setRight`

### `system/admin/src/router-pages/product/components/Header.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/router-pages/product/hooks/useTabs.ts`
**Imported by:** `system/admin/src/router-pages/product/Product.tsx`
**Symbols:** function:`Header`, const_fn:`handleTabChange`

### `system/admin/src/router-pages/product/components/MainInfoCard.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/components/inputs/GalleryInput/GalleryInput.tsx`, `system/admin/src/components/inputs/SelectInput/SelectInput.tsx`, `system/admin/src/components/inputs/SwitchInput/SwitchInput.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx`, `system/admin/src/helpers/editor/editor.ts`, `themes/store/src/helpers/forceUpdate.ts`
**Imported by:** `system/admin/src/router-pages/product/components/PageContent.tsx`, `system/admin/src/router-pages/product/components/VariantsTab.tsx`
**Symbols:** const_fn:`MainInfoCard`, const_fn:`setProdData`, const_fn:`init`, const_fn:`handleChange`
**Often changes with:** `system/admin/src/router-pages/product/components/VariantsTab.tsx` (3x)

### `system/admin/src/router-pages/product/components/PageContent.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/components/entity/entityEdit/components/EntityCustomFields.tsx`, `system/admin/src/components/entity/entityEdit/components/EntityMetaFields.tsx`, `themes/store/src/types.ts`, `system/admin/src/components/inputs/Search/SearchInput.tsx`, `themes/store/src/helpers/forceUpdate.ts`, `system/admin/src/constants/PageInfos.ts`, `system/admin/src/router-pages/product/contexts/Product.ts`, `system/admin/src/router-pages/product/hooks/useTabs.ts`, `system/admin/src/router-pages/product/components/AttributesTab.tsx`, `system/admin/src/router-pages/product/components/MainInfoCard.tsx`
**Imported by:** `system/admin/src/router-pages/product/Product.tsx`
**Symbols:** const_fn:`PageContent`, const_fn:`setProdData`, const_fn:`handleSearchCategory`, const_fn:`handleChangeCategories`, const_fn:`handleMainCategoryChange`, const_fn:`getMainCategory`, const_fn:`getAttributes`
**Often changes with:** `system/admin/src/router-pages/product/Product.tsx` (4x), `system/admin/src/router-pages/product/hooks/useTabs.ts` (4x), `system/admin/src/router-pages/product/components/VariantsTab.tsx` (3x), `system/admin/src/router-pages/settings/Settings.tsx` (3x), `system/admin/src/router-pages/reviewList/ReviewList.tsx` (3x)

### `system/admin/src/router-pages/product/components/VariantsTab.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/components/buttons/IconButton.tsx`, `system/admin/src/components/buttons/TextButton.tsx`, `system/admin/src/components/inputs/SelectInput/SelectInput.tsx`, `system/admin/src/components/inputs/SwitchInput/SwitchInput.tsx`, `system/admin/src/components/modal/Confirmation.tsx`, `system/admin/src/router-pages/product/components/MainInfoCard.tsx`
**Imported by:** `system/admin/src/router-pages/product/components/PageContent.tsx`
**Symbols:** function:`VariantsTab`, const_fn:`handleAddProductVariant`, const_fn:`expandVariant`, const_fn:`getScrollParent`, const_fn:`handleDeleteVariant`, const_fn:`onAttributeChange`, const_fn:`handleEditAttributes`, const_fn:`onUsedAttributeChange`
**Often changes with:** `system/admin/src/router-pages/settings/Settings.tsx` (4x), `system/admin/src/router-pages/product/Product.tsx` (3x), `system/admin/src/router-pages/product/components/MainInfoCard.tsx` (3x), `system/admin/src/router-pages/product/components/PageContent.tsx` (3x), `system/admin/src/router-pages/settings/components/draggableCurrencies.tsx` (3x)

### `system/admin/src/router-pages/product/contexts/Product.ts`
**Imported by:** `system/admin/src/router-pages/product/Product.tsx`, `system/admin/src/router-pages/product/components/PageContent.tsx`, `system/admin/src/router-pages/product/hooks/useTabs.ts`

### `system/admin/src/router-pages/product/hooks/useTabs.ts`
**Feature:** Hooks
**Imports:** `system/admin/src/router-pages/product/contexts/Product.ts`
**Imported by:** `system/admin/src/router-pages/product/Product.tsx`, `system/admin/src/router-pages/product/components/Header.tsx`, `system/admin/src/router-pages/product/components/PageContent.tsx`
**Symbols:** function:`useTabs`
**Often changes with:** `system/admin/src/router-pages/product/components/PageContent.tsx` (4x), `system/admin/src/router-pages/product/Product.tsx` (3x), `system/admin/src/router-pages/reviewList/ReviewList.tsx` (3x)

### `system/admin/src/router-pages/productList/ProductList.test.tsx`
**Imports:** `system/admin/src/router-pages/settings/pages/store.tsx`, `system/admin/src/router-pages/productList/ProductList.tsx`

### `system/admin/src/router-pages/productList/ProductList.tsx`
**Imports:** `plugins/product-filter/src/frontend/components/Filter.tsx`, `themes/store/src/types.ts`, `system/admin/src/components/entity/entityTable/EntityTable.tsx`, `themes/store/src/types.ts`, `system/admin/src/constants/PageInfos.ts`, `system/admin/src/helpers/customEntities.tsx`, `themes/store/src/helpers/forceUpdate.ts`
**Imported by:** `system/admin/src/router-pages/productList/ProductList.test.tsx`
**Symbols:** function:`ProductListPage`, const_fn:`init`, const_fn:`handleToggleFilter`, const_fn:`onFilterMount`, const_fn:`onFilterChange`

### `system/admin/src/router-pages/reviewList/ProductListItem.tsx`
**Imports:** `system/admin/src/constants/PageInfos.ts`, `system/admin/src/router-pages/settings/pages/store.tsx`
**Imported by:** `system/admin/src/router-pages/reviewList/ReviewList.tsx`
**Symbols:** const_fn:`mapStateToProps`, const_fn:`ProductListItem`

### `system/admin/src/router-pages/reviewList/ReviewList.test.tsx`
**Imports:** `system/admin/src/router-pages/reviewList/ReviewList.tsx`, `system/admin/src/router-pages/settings/pages/store.tsx`

### `system/admin/src/router-pages/reviewList/ReviewList.tsx`
**Imports:** `system/admin/src/components/buttons/IconButton.tsx`, `system/admin/src/components/entity/entityTable/EntityTable.tsx`, `themes/store/src/types.ts`, `themes/store/src/components/modals/baseModal/Modal.tsx`, `themes/store/src/components/toast/toast.tsx`, `system/admin/src/constants/PageInfos.ts`, `system/admin/src/helpers/time.ts`, `system/admin/src/router-pages/reviewList/ProductListItem.tsx`
**Imported by:** `system/admin/src/router-pages/reviewList/ReviewList.test.tsx`
**Symbols:** function:`ProductReviewTable`, const_fn:`handleApproveReview`, const_fn:`handleOpenReview`
**Often changes with:** `system/admin/src/router-pages/product/components/PageContent.tsx` (3x), `system/admin/src/router-pages/product/hooks/useTabs.ts` (3x)

### `system/admin/src/router-pages/settings/Settings.test.tsx`
**Feature:** Configuration
**Imports:** `system/admin/src/constants/languages.ts`, `system/admin/src/router-pages/settings/Settings.tsx`

### `system/admin/src/router-pages/settings/Settings.tsx`
**Feature:** Configuration
**Imports:** `system/admin/src/components/entity/entityEdit/components/EntityHeader.tsx`, `system/admin/src/components/loadBox/LoadingStatus.tsx`, `system/admin/src/components/sideNav/ResponsiveSideNav.tsx`, `system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx`, `system/admin/src/router-pages/settings/pages/index.tsx`, `system/admin/src/router-pages/settings/pages/acl.tsx`, `system/admin/src/router-pages/settings/pages/code.tsx`, `system/admin/src/router-pages/settings/pages/custom/CustomEntity/index.tsx`, `system/admin/src/router-pages/settings/pages/custom/CustomRole/index.tsx`, `system/admin/src/router-pages/settings/pages/custom/DefaultEntity/index.tsx`
**Imported by:** `system/admin/src/router-pages/settings/Settings.test.tsx`
**Symbols:** const_fn:`SettingsPage`, const_fn:`SettingsPageLoader`, const_fn:`SettingsPageWithProvider`
**Often changes with:** `system/admin/src/router-pages/settings/pages/code.tsx` (5x), `system/admin/src/router-pages/settings/pages/customData.tsx` (5x), `system/admin/src/router-pages/settings/pages/general.tsx` (5x), `system/admin/src/router-pages/settings/pages/migration.tsx` (5x), `system/admin/src/router-pages/settings/pages/seo.tsx` (5x)

### `system/admin/src/router-pages/settings/components/SettingCategory.tsx`
**Feature:** UI Components
**Imported by:** `system/admin/src/router-pages/settings/pages/acl.tsx`, `system/admin/src/router-pages/settings/pages/code.tsx`, `system/admin/src/router-pages/settings/pages/customData.tsx`, `system/admin/src/router-pages/settings/pages/general.tsx`, `system/admin/src/router-pages/settings/pages/migration.tsx`, `system/admin/src/router-pages/settings/pages/seo.tsx`, `system/admin/src/router-pages/settings/pages/store.tsx`, `system/admin/src/router-pages/settings/pages/custom/CustomEntity/index.tsx`, `system/admin/src/router-pages/settings/pages/custom/CustomRole/index.tsx`, `system/admin/src/router-pages/settings/pages/custom/DefaultEntity/index.tsx`
**Symbols:** function:`SettingCategory`

### `system/admin/src/router-pages/settings/components/customTextEditorInputField.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/helpers/editor/editor.ts`
**Symbols:** const_fn:`CustomTextEditorInputField`, const_fn:`initEditor`

### `system/admin/src/router-pages/settings/components/draggableCurrencies.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/components/icons/grabIcon.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx`, `themes/store/src/types.ts`
**Imported by:** `system/admin/src/router-pages/settings/pages/store.tsx`
**Symbols:** function:`CurrencyItem`, const_fn:`DraggableCurrenciesList`, function:`handleDragEnd`
**Often changes with:** `system/admin/src/router-pages/product/components/VariantsTab.tsx` (3x), `system/admin/src/router-pages/settings/Settings.tsx` (3x), `system/admin/src/router-pages/settings/components/draggableEntityFields.tsx` (3x), `system/admin/src/router-pages/settings/components/newEntityForm.tsx` (3x), `system/admin/src/router-pages/settings/components/newRoleForm.tsx` (3x)

### `system/admin/src/router-pages/settings/components/draggableEntityFields.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/components/icons/grabIcon.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx`, `system/admin/src/helpers/slugify.ts`, `themes/store/src/types.ts`, `system/admin/src/components/inputs/SelectInput/SelectInput.tsx`
**Imported by:** `system/admin/src/router-pages/settings/pages/custom/CustomEntity/index.tsx`, `system/admin/src/router-pages/settings/pages/custom/DefaultEntity/index.tsx`
**Symbols:** function:`EntityFieldItem`, const_fn:`DraggableEntityFields`, const_fn:`handleDragEnd`
**Often changes with:** `system/admin/src/router-pages/product/components/VariantsTab.tsx` (3x), `system/admin/src/router-pages/settings/Settings.tsx` (3x), `system/admin/src/router-pages/settings/components/draggableCurrencies.tsx` (3x), `system/admin/src/router-pages/settings/components/newEntityForm.tsx` (3x), `system/admin/src/router-pages/settings/components/newRoleForm.tsx` (3x)

### `system/admin/src/router-pages/settings/components/newEntityForm.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/components/buttons/TextButton.tsx`, `system/admin/src/components/inputs/Image/ImageInput.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx`, `system/admin/src/helpers/customEntities.tsx`, `system/admin/src/helpers/slugify.ts`, `system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx`
**Imported by:** `system/admin/src/router-pages/settings/pages/customData.tsx`
**Symbols:** const_fn:`NewEntityForm`, const_fn:`onSubmit`
**Often changes with:** `system/admin/src/router-pages/product/components/VariantsTab.tsx` (3x), `system/admin/src/router-pages/settings/Settings.tsx` (3x), `system/admin/src/router-pages/settings/components/draggableCurrencies.tsx` (3x), `system/admin/src/router-pages/settings/components/draggableEntityFields.tsx` (3x), `system/admin/src/router-pages/settings/components/newRoleForm.tsx` (3x)

### `system/admin/src/router-pages/settings/components/newRoleForm.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/components/buttons/TextButton.tsx`, `system/admin/src/components/inputs/SwitchInput/SwitchInput.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx`, `themes/store/src/components/toast/toast.tsx`, `system/admin/src/helpers/slugify.ts`, `system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx`
**Imported by:** `system/admin/src/router-pages/settings/pages/acl.tsx`
**Symbols:** const_fn:`NewRoleForm`, const_fn:`onSubmit`
**Often changes with:** `system/admin/src/router-pages/settings/Settings.tsx` (3x), `system/admin/src/router-pages/settings/components/draggableCurrencies.tsx` (3x), `system/admin/src/router-pages/settings/components/draggableEntityFields.tsx` (3x), `system/admin/src/router-pages/settings/components/newEntityForm.tsx` (3x), `system/admin/src/router-pages/settings/pages/code.tsx` (3x)

### `system/admin/src/router-pages/settings/components/settingItem.tsx`
**Feature:** UI Components
**Imported by:** `system/admin/src/router-pages/settings/pages/acl.tsx`, `system/admin/src/router-pages/settings/pages/customData.tsx`, `system/admin/src/router-pages/settings/pages/index.tsx`
**Symbols:** const_fn:`SettingItem`
**Often changes with:** `system/admin/src/router-pages/settings/Settings.tsx` (3x), `system/admin/src/router-pages/settings/pages/acl.tsx` (3x), `system/admin/src/router-pages/settings/pages/code.tsx` (3x), `system/admin/src/router-pages/settings/pages/customData.tsx` (3x), `system/admin/src/router-pages/settings/pages/general.tsx` (3x)

### `system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx`
**Feature:** Hooks
**Imports:** `themes/store/src/components/toast/toast.tsx`, `themes/store/src/types.ts`
**Imported by:** `system/admin/src/router-pages/settings/Settings.tsx`, `system/admin/src/router-pages/settings/components/newEntityForm.tsx`, `system/admin/src/router-pages/settings/components/newRoleForm.tsx`, `system/admin/src/router-pages/settings/pages/acl.tsx`, `system/admin/src/router-pages/settings/pages/code.tsx`, `system/admin/src/router-pages/settings/pages/customData.tsx`, `system/admin/src/router-pages/settings/pages/general.tsx`, `system/admin/src/router-pages/settings/pages/index.tsx`, `system/admin/src/router-pages/settings/pages/migration.tsx`, `system/admin/src/router-pages/settings/pages/seo.tsx`
**Symbols:** const_fn:`uniqBy`, const_fn:`useAdminSettingsStore`, const_fn:`useAdminSettingsContext`, const_fn:`useAdminSettings`, const_fn:`AdminSettingsContextProvider`
**Often changes with:** `system/admin/src/router-pages/settings/Settings.tsx` (3x), `system/admin/src/router-pages/settings/pages/code.tsx` (3x), `system/admin/src/router-pages/settings/pages/customData.tsx` (3x), `system/admin/src/router-pages/settings/pages/general.tsx` (3x), `system/admin/src/router-pages/settings/pages/seo.tsx` (3x)

### `system/admin/src/router-pages/settings/pages/Themes/components/ThemePackage.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/components/buttons/TextButton.tsx`, `system/admin/src/constants/PageInfos.ts`
**Imported by:** `system/admin/src/router-pages/settings/pages/Themes/index.tsx`
**Symbols:** const_fn:`ThemePackage`, const_fn:`ThemePackageSkeleton`

### `system/admin/src/router-pages/settings/pages/Themes/index.tsx`
**Imports:** `themes/store/src/components/toast/toast.tsx`, `system/admin/src/constants/PageInfos.ts`, `system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx`, `system/admin/src/router-pages/settings/pages/Themes/components/ThemePackage.tsx`
**Imported by:** `system/admin/src/router-pages/settings/Settings.tsx`
**Symbols:** const_fn:`getThemeList`, const_fn:`getThemeUpdates`, const_fn:`checkUpdates`, const_fn:`init`, const_fn:`handleDeleteTheme`, const_fn:`handleChangeTheme`, const_fn:`handleUpdateTheme`

### `system/admin/src/router-pages/settings/pages/acl.tsx`
**Feature:** Pages
**Imports:** `system/admin/src/components/icons/spyIcon.tsx`, `system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx`, `system/admin/src/router-pages/settings/components/newRoleForm.tsx`, `system/admin/src/router-pages/settings/components/settingItem.tsx`, `system/admin/src/router-pages/settings/components/SettingCategory.tsx`
**Imported by:** `system/admin/src/router-pages/settings/Settings.tsx`
**Symbols:** const_fn:`ACLSettingsPage`
**Often changes with:** `system/admin/src/router-pages/settings/Settings.tsx` (4x), `system/admin/src/router-pages/settings/pages/code.tsx` (4x), `system/admin/src/router-pages/settings/pages/customData.tsx` (4x), `system/admin/src/router-pages/settings/pages/general.tsx` (4x), `system/admin/src/router-pages/settings/pages/migration.tsx` (4x)

### `system/admin/src/router-pages/settings/pages/code.tsx`
**Feature:** Pages
**Imports:** `system/admin/src/components/inputs/CodeEditor.tsx`, `system/admin/src/router-pages/settings/components/SettingCategory.tsx`, `system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx`, `themes/store/src/types.ts`
**Imported by:** `system/admin/src/router-pages/settings/Settings.tsx`
**Symbols:** const_fn:`CodeSettingsPage`, const_fn:`onSubmit`
**Often changes with:** `system/admin/src/router-pages/settings/Settings.tsx` (5x), `system/admin/src/router-pages/settings/pages/customData.tsx` (5x), `system/admin/src/router-pages/settings/pages/general.tsx` (5x), `system/admin/src/router-pages/settings/pages/seo.tsx` (5x), `system/admin/src/router-pages/settings/pages/store.tsx` (5x)

### `system/admin/src/router-pages/settings/pages/custom/CustomEntity/index.tsx`
**Imports:** `system/admin/src/components/inputs/Image/ImageInput.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx`, `system/admin/src/constants/PageInfos.ts`, `system/admin/src/helpers/slugify.ts`, `system/admin/src/router-pages/settings/components/SettingCategory.tsx`, `themes/store/src/types.ts`, `system/admin/src/router-pages/settings/components/draggableEntityFields.tsx`, `system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx`
**Imported by:** `system/admin/src/router-pages/settings/Settings.tsx`
**Symbols:** const_fn:`CustomEntitySettingsPage`, const_fn:`CustomEntityForm`, const_fn:`onSubmit`
**Often changes with:** `system/admin/src/router-pages/settings/Settings.tsx` (3x), `system/admin/src/router-pages/settings/pages/code.tsx` (3x), `system/admin/src/router-pages/settings/pages/custom/CustomRole/index.tsx` (3x), `system/admin/src/router-pages/settings/pages/custom/DefaultEntity/index.tsx` (3x), `system/admin/src/router-pages/settings/pages/customData.tsx` (3x)

### `system/admin/src/router-pages/settings/pages/custom/CustomRole/PermissionCategory.tsx`
**Imported by:** `system/admin/src/router-pages/settings/pages/custom/CustomRole/index.tsx`
**Symbols:** const_fn:`ControlledPermissionCategory`, const_fn:`onChange`

### `system/admin/src/router-pages/settings/pages/custom/CustomRole/PermissionOption.tsx`
**Imported by:** `system/admin/src/router-pages/settings/pages/custom/CustomRole/index.tsx`
**Symbols:** const_fn:`ControlledPermissionOption`, const_fn:`PermissionOption`

### `system/admin/src/router-pages/settings/pages/custom/CustomRole/index.tsx`
**Imports:** `system/admin/src/components/inputs/SwitchInput/SwitchInput.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx`, `themes/store/src/components/toast/toast.tsx`, `system/admin/src/helpers/slugify.ts`, `system/admin/src/router-pages/settings/components/SettingCategory.tsx`, `system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx`, `system/admin/src/router-pages/settings/pages/custom/CustomRole/PermissionCategory.tsx`, `system/admin/src/router-pages/settings/pages/custom/CustomRole/PermissionOption.tsx`
**Imported by:** `system/admin/src/router-pages/settings/Settings.tsx`
**Symbols:** const_fn:`CustomRoleSettingsPage`, const_fn:`onSubmit`
**Often changes with:** `system/admin/src/router-pages/settings/Settings.tsx` (3x), `system/admin/src/router-pages/settings/pages/code.tsx` (3x), `system/admin/src/router-pages/settings/pages/custom/CustomEntity/index.tsx` (3x), `system/admin/src/router-pages/settings/pages/custom/DefaultEntity/index.tsx` (3x), `system/admin/src/router-pages/settings/pages/customData.tsx` (3x)

### `system/admin/src/router-pages/settings/pages/custom/DefaultEntity/constants.ts`
**Imported by:** `system/admin/src/router-pages/settings/pages/custom/DefaultEntity/index.tsx`

### `system/admin/src/router-pages/settings/pages/custom/DefaultEntity/index.tsx`
**Imports:** `system/admin/src/router-pages/settings/components/SettingCategory.tsx`, `themes/store/src/types.ts`, `system/admin/src/router-pages/settings/components/draggableEntityFields.tsx`, `system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx`, `system/admin/src/router-pages/settings/pages/custom/DefaultEntity/constants.ts`
**Imported by:** `system/admin/src/router-pages/settings/Settings.tsx`
**Symbols:** const_fn:`DefaultEntitySettingsPage`, const_fn:`DefaultEntityForm`, const_fn:`onSubmit`
**Often changes with:** `system/admin/src/router-pages/settings/Settings.tsx` (3x), `system/admin/src/router-pages/settings/pages/code.tsx` (3x), `system/admin/src/router-pages/settings/pages/custom/CustomEntity/index.tsx` (3x), `system/admin/src/router-pages/settings/pages/custom/CustomRole/index.tsx` (3x), `system/admin/src/router-pages/settings/pages/customData.tsx` (3x)

### `system/admin/src/router-pages/settings/pages/customData.tsx`
**Feature:** Pages
**Imports:** `system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx`, `system/admin/src/router-pages/settings/components/newEntityForm.tsx`, `system/admin/src/router-pages/settings/components/settingItem.tsx`, `system/admin/src/router-pages/settings/components/SettingCategory.tsx`
**Imported by:** `system/admin/src/router-pages/settings/Settings.tsx`
**Symbols:** const_fn:`CustomDataPage`
**Often changes with:** `system/admin/src/router-pages/settings/Settings.tsx` (5x), `system/admin/src/router-pages/settings/pages/code.tsx` (5x), `system/admin/src/router-pages/settings/pages/general.tsx` (5x), `system/admin/src/router-pages/settings/pages/seo.tsx` (5x), `system/admin/src/router-pages/settings/pages/store.tsx` (5x)

### `system/admin/src/router-pages/settings/pages/general.tsx`
**Feature:** Pages
**Imports:** `system/admin/src/components/inputs/SelectInput/SelectInput.tsx`, `system/admin/src/components/inputs/SwitchInput/SwitchInput.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx`, `system/admin/src/constants/languages.ts`, `system/admin/src/constants/timezones.ts`, `system/admin/src/router-pages/settings/components/SettingCategory.tsx`, `system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx`, `themes/store/src/types.ts`
**Imported by:** `system/admin/src/router-pages/settings/Settings.tsx`
**Symbols:** const_fn:`getLangLabel`, const_fn:`getTZLabel`, const_fn:`getTZValue`, const_fn:`getLangValue`, const_fn:`GeneralSettingsPage`, const_fn:`onSubmit`
**Often changes with:** `system/admin/src/router-pages/settings/pages/store.tsx` (6x), `system/admin/src/router-pages/settings/Settings.tsx` (5x), `system/admin/src/router-pages/settings/pages/code.tsx` (5x), `system/admin/src/router-pages/settings/pages/customData.tsx` (5x), `system/admin/src/router-pages/settings/pages/seo.tsx` (5x)

### `system/admin/src/router-pages/settings/pages/index.tsx`
**Feature:** Pages
**Imports:** `toolkits/commerce/tests/helpers.ts`, `system/admin/src/components/icons/marketicon.tsx`, `system/admin/src/components/icons/stackIcon.tsx`, `system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx`, `system/admin/src/router-pages/settings/components/settingItem.tsx`
**Imported by:** `system/admin/src/router-pages/settings/Settings.tsx`
**Symbols:** const_fn:`SettingsIndexPage`
**Often changes with:** `system/admin/src/router-pages/settings/Settings.tsx` (3x), `system/admin/src/router-pages/settings/components/settingItem.tsx` (3x), `system/admin/src/router-pages/settings/pages/acl.tsx` (3x), `system/admin/src/router-pages/settings/pages/code.tsx` (3x), `system/admin/src/router-pages/settings/pages/customData.tsx` (3x)

### `system/admin/src/router-pages/settings/pages/migration.tsx`
**Feature:** Pages
**Imports:** `system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx`, `system/admin/src/components/loadBox/LoadingStatus.tsx`, `themes/store/src/components/toast/toast.tsx`, `system/admin/src/router-pages/settings/components/SettingCategory.tsx`
**Imported by:** `system/admin/src/router-pages/settings/Settings.tsx`
**Symbols:** const_fn:`ControlledBackupOption`, const_fn:`BackupOption`, const_fn:`MigrationSettingsPage`, const_fn:`onSubmit`
**Often changes with:** `system/admin/src/router-pages/settings/Settings.tsx` (5x), `system/admin/src/router-pages/settings/pages/acl.tsx` (4x), `system/admin/src/router-pages/settings/pages/code.tsx` (4x), `system/admin/src/router-pages/settings/pages/customData.tsx` (4x), `system/admin/src/router-pages/settings/pages/general.tsx` (4x)

### `system/admin/src/router-pages/settings/pages/seo.tsx`
**Feature:** Pages
**Imports:** `system/admin/src/components/inputs/CodeEditor.tsx`, `system/utils/src/exports.ts`, `system/admin/src/components/loadBox/LoadingStatus.tsx`, `themes/store/src/components/toast/toast.tsx`, `system/admin/src/router-pages/settings/components/SettingCategory.tsx`, `system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx`, `themes/store/src/types.ts`
**Imported by:** `system/admin/src/router-pages/settings/Settings.tsx`
**Symbols:** const_fn:`SEOSettingsPage`, const_fn:`onSubmit`, const_fn:`buildSitemap`
**Often changes with:** `system/admin/src/router-pages/settings/Settings.tsx` (5x), `system/admin/src/router-pages/settings/pages/code.tsx` (5x), `system/admin/src/router-pages/settings/pages/customData.tsx` (5x), `system/admin/src/router-pages/settings/pages/general.tsx` (5x), `system/admin/src/router-pages/settings/pages/store.tsx` (5x)

### `system/admin/src/router-pages/settings/pages/store.tsx`
**Feature:** Pages
**Imports:** `system/admin/src/components/inputs/SwitchInput/SwitchInput.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx`, `system/admin/src/components/icons/grabIcon.tsx`, `system/admin/src/router-pages/settings/components/draggableCurrencies.tsx`, `system/admin/src/router-pages/settings/components/SettingCategory.tsx`, `system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx`, `themes/store/src/types.ts`
**Imported by:** `system/admin/src/components/entity/entityTable/EntityTable.test.tsx`, `system/admin/src/components/entity/entityTable/components/DeleteSelectedButton.tsx`, `system/admin/src/components/entity/entityTable/components/EntityTableItem.tsx`, `system/admin/src/components/entity/entityTable/components/TableHeader.tsx`, `system/admin/src/components/layout/Layout.tsx`, `system/admin/src/components/layout/hooks/useAppState.ts`, `system/admin/src/components/notificationCenter/NotificationCenter.tsx`, `system/admin/src/components/sideNav/SideNav.tsx`, `system/admin/src/components/topbar/Topbar.tsx`, `system/admin/src/helpers/customEntities.tsx`
**Symbols:** const_fn:`StoreSettingsPage`, const_fn:`onSubmit`
**Often changes with:** `system/admin/src/router-pages/settings/pages/general.tsx` (6x), `system/admin/src/router-pages/settings/pages/code.tsx` (5x), `system/admin/src/router-pages/settings/pages/customData.tsx` (5x), `system/admin/src/router-pages/settings/pages/seo.tsx` (5x), `system/admin/src/router-pages/settings/pages/acl.tsx` (4x)

### `system/admin/src/router-pages/settings/types.ts`
**Feature:** Configuration

### `system/admin/src/router-pages/tag/Tag.test.tsx`
**Imports:** `system/admin/src/router-pages/tag/Tag.tsx`

### `system/admin/src/router-pages/tag/Tag.tsx`
**Imports:** `system/admin/src/components/entity/entityEdit/EntityEdit.tsx`, `system/admin/src/constants/PageInfos.ts`
**Imported by:** `system/admin/src/router-pages/tag/Tag.test.tsx`
**Symbols:** function:`TagPage`

### `system/admin/src/router-pages/tagList/TagList.test.tsx`
**Imports:** `system/admin/src/router-pages/tagList/TagList.tsx`, `system/admin/src/router-pages/settings/pages/store.tsx`

### `system/admin/src/router-pages/tagList/TagList.tsx`
**Imports:** `system/admin/src/components/entity/entityTable/EntityTable.tsx`, `system/admin/src/constants/PageInfos.ts`, `system/admin/src/helpers/customEntities.tsx`
**Imported by:** `system/admin/src/router-pages/tagList/TagList.test.tsx`
**Symbols:** function:`TagTable`

### `system/admin/src/router-pages/themeEdit/ThemeEdit.test.tsx`

### `system/admin/src/router-pages/themeEdit/ThemeEdit.tsx`
**Imports:** `system/admin/src/components/sideNav/ResponsiveSideNav.tsx`, `system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx`, `system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditor/PageEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PageActions.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/PageEditorSidebar.tsx`, `system/admin/src/router-pages/themeEdit/pageList/PageList.tsx`
**Imported by:** `system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx`, `system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PageSettings.tsx`, `system/admin/src/router-pages/themeEdit/pageList/PageItem.tsx`

### `system/admin/src/router-pages/themeEdit/hooks/useBlockEvents.tsx`
**Feature:** Hooks
**Imports:** `system/admin/src/helpers/Draggable/Draggable.ts`
**Imported by:** `system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx`
**Symbols:** const_fn:`useBlockEvents`, const_fn:`onMouseUp`, const_fn:`onTryToInsert`, const_fn:`onBlockDeSelected`, const_fn:`onBlockSelected`, const_fn:`deselectBlock`, const_fn:`deselectCurrentBlock`, const_fn:`selectBlock`, const_fn:`canDeselectBlock`, const_fn:`canDragBlock`, const_fn:`addBlock`, const_fn:`onBlockInserted`

### `system/admin/src/router-pages/themeEdit/hooks/useBlockFns.tsx`
**Feature:** Hooks
**Imported by:** `system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx`
**Symbols:** const_fn:`useBlockFns`

### `system/admin/src/router-pages/themeEdit/hooks/useDebounce.ts`
**Feature:** Hooks
**Imported by:** `system/admin/src/router-pages/themeEdit/pageEditor/components/NewBlockMenu.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/ColorPickerField.tsx`
**Symbols:** function:`useDebounceFn`, function:`useDebounce`

### `system/admin/src/router-pages/themeEdit/hooks/useDocumentEvents.tsx`
**Feature:** Hooks
**Imported by:** `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/ColorPickerField.tsx`
**Symbols:** const_fn:`useDocumentEvent`, function:`useDropdown`

### `system/admin/src/router-pages/themeEdit/hooks/useEditorUtils.tsx`
**Feature:** Hooks
**Imported by:** `system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx`
**Symbols:** const_fn:`useEditorUtils`, const_fn:`isGlobalElem`, const_fn:`findEditableParent`, const_fn:`getFrameColor`, const_fn:`checkBlockDataGlobal`

### `system/admin/src/router-pages/themeEdit/hooks/useHoveredFrames.tsx`
**Feature:** Hooks
**Imports:** `system/admin/src/helpers/Draggable/Draggable.ts`
**Imported by:** `system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx`
**Symbols:** const_fn:`useEditorFrames`, const_fn:`createBlockFrame`, const_fn:`onBlockHoverStart`, const_fn:`onBlockHoverEnd`, const_fn:`setFramePosition`, const_fn:`updateFramesPosition`, const_fn:`onAnyElementScroll`

### `system/admin/src/router-pages/themeEdit/hooks/useKeyPress.ts`
**Feature:** Hooks
**Symbols:** const_fn:`useKeyPress`

### `system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx`
**Feature:** Hooks
**Imports:** `system/admin/src/components/modal/Confirmation.tsx`, `system/utils/src/exports.ts`, `system/admin/src/helpers/Draggable/Draggable.ts`, `system/admin/src/router-pages/themeEdit/pageEditor/components/BlockMenu.tsx`, `system/admin/src/router-pages/themeEdit/ThemeEdit.tsx`, `system/admin/src/router-pages/themeEdit/hooks/useBlockEvents.tsx`, `system/admin/src/router-pages/themeEdit/hooks/useBlockFns.tsx`, `system/admin/src/router-pages/themeEdit/hooks/useEditorUtils.tsx`, `system/admin/src/router-pages/themeEdit/hooks/useHoveredFrames.tsx`, `system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx`
**Imported by:** `system/admin/src/router-pages/themeEdit/ThemeEdit.tsx`, `system/admin/src/router-pages/themeEdit/pageEditor/PageEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditor/components/BlockMenu.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/PageEditorSidebar.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/EditorBlockEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/HTMLBlockEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/ImageBlockEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PageActions.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PageDesignEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PageSettings.tsx`
**Symbols:** const_fn:`usePageBuilderContext`, const_fn:`canInsertBlock`, const_fn:`updateChangedModifications`, function:`modifyBlock`, function:`updateDraggable`, function:`addToModifications`, function:`getCurrentModificationsState`, function:`saveCurrentState`, function:`rerenderBlocks`, function:`applyHistory`, function:`undoModification`, const_fn:`resetModifications`, function:`redoModification`, function:`deleteBlock`

### `system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx`
**Feature:** Hooks
**Imports:** `system/admin/src/router-pages/themeEdit/ThemeEdit.tsx`
**Imported by:** `system/admin/src/router-pages/themeEdit/ThemeEdit.tsx`, `system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx`, `system/admin/src/router-pages/themeEdit/pageEditor/PageEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditor/components/BlockMenu.tsx`, `system/admin/src/router-pages/themeEdit/pageEditor/components/NewBlockMenu.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/PageEditorSidebar.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/HTMLBlockEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/ImageBlockEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PageActions.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PageDesignEditor.tsx`
**Symbols:** const_fn:`useThemeEditorContext`, const_fn:`forceUpdate`, const_fn:`useThemeEditor`, const_fn:`ThemeEditorProvider`

### `system/admin/src/router-pages/themeEdit/pageEditor/PageEditor.tsx`
**Imports:** `system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx`, `system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditor/components/BlockMenu.tsx`
**Imported by:** `system/admin/src/router-pages/themeEdit/ThemeEdit.tsx`
**Symbols:** const_fn:`InnerPageFrame`, const_fn:`PageFrame`

### `system/admin/src/router-pages/themeEdit/pageEditor/components/BlockMenu.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx`, `system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditor/components/NewBlockMenu.tsx`
**Imported by:** `system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx`, `system/admin/src/router-pages/themeEdit/pageEditor/PageEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditor/components/NewBlockMenu.tsx`
**Symbols:** const_fn:`BlockMenu`, const_fn:`addNewBlock`, const_fn:`BlockIcon`

### `system/admin/src/router-pages/themeEdit/pageEditor/components/NewBlockMenu.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/router-pages/themeEdit/hooks/useDebounce.ts`, `system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditor/components/BlockMenu.tsx`
**Imported by:** `system/admin/src/router-pages/themeEdit/pageEditor/components/BlockMenu.tsx`
**Symbols:** const_fn:`NewBlockMenu`

### `system/admin/src/router-pages/themeEdit/pageEditorSidebar/PageEditorSidebar.tsx`
**Imports:** `themes/store/src/helpers/forceUpdate.ts`, `system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx`, `system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PageDesignEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PageSettings.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PluginEditor.tsx`
**Imported by:** `system/admin/src/router-pages/themeEdit/ThemeEdit.tsx`
**Symbols:** const_fn:`BlockSubViews`, const_fn:`PageEditorSidebar`, const_fn:`onUpdate`, const_fn:`posX`, const_fn:`onEnd`

### `system/admin/src/router-pages/themeEdit/pageEditorSidebar/SlideableNumberInput.tsx`
**Imported by:** `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/StyleNumberField.tsx`
**Symbols:** function:`ResizeIcon`, const_fn:`DragLabel`, const_fn:`onUpdate`, const_fn:`onEnd`, const_fn:`SlideableNumberInput`

### `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/BackgroundEditor.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/ColorPickerField.tsx`
**Imported by:** `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PageDesignEditor.tsx`
**Symbols:** const_fn:`BackgroundEditor`

### `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/ColorPickerField.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/router-pages/themeEdit/hooks/useDocumentEvents.tsx`, `system/admin/src/router-pages/themeEdit/hooks/useDebounce.ts`
**Imported by:** `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/BackgroundEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/FontEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/ShadowEditor.tsx`
**Symbols:** const_fn:`ColorPickerField`

### `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/DimensionsEditor.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/MarginEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PaddingEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/StyleNumberField.tsx`
**Imported by:** `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PageDesignEditor.tsx`
**Symbols:** const_fn:`DimensionsEditor`

### `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/EditorBlockEditor.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/helpers/editor/editor.ts`, `system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx`
**Imported by:** `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PluginEditor.tsx`
**Symbols:** const_fn:`EditorBlockEditor`, const_fn:`init`, const_fn:`handler`

### `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/FontEditor.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/ColorPickerField.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/SelectableField.tsx`
**Imported by:** `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PageDesignEditor.tsx`
**Symbols:** const_fn:`MenuCenterIcon`, const_fn:`FontEditor`

### `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/HTMLBlockEditor.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/components/inputs/CodeEditor.tsx`, `system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx`, `system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx`
**Imported by:** `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PluginEditor.tsx`
**Symbols:** const_fn:`HTMLBlockEditor`, const_fn:`setBlockValue`

### `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/ImageBlockEditor.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/components/inputs/Image/ImageInput.tsx`, `system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx`, `system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/SelectableField.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/StyleNumberField.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx`
**Imported by:** `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PluginEditor.tsx`
**Symbols:** const_fn:`ImageBlockEditor`, const_fn:`handleChange`, const_fn:`handleTextInput`

### `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/MarginEditor.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/StyleNumberField.tsx`
**Imported by:** `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/DimensionsEditor.tsx`
**Symbols:** const_fn:`MarginEditor`
**Often changes with:** `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PageActions.tsx` (3x)

### `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PaddingEditor.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/StyleNumberField.tsx`
**Imported by:** `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/DimensionsEditor.tsx`
**Symbols:** const_fn:`PaddingEditor`

### `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PageActions.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/components/sideNav/ResponsiveSideNav.tsx`, `system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx`, `system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx`
**Imported by:** `system/admin/src/router-pages/themeEdit/ThemeEdit.tsx`
**Symbols:** const_fn:`PageActions`, const_fn:`handleChangeUrl`, const_fn:`onURLBlur`, const_fn:`handleChange`, const_fn:`changeLayout`, const_fn:`DeviceSwitcher`
**Often changes with:** `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/MarginEditor.tsx` (3x)

### `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PageDesignEditor.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx`, `system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/BackgroundEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/DimensionsEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/FontEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/ShadowEditor.tsx`
**Imported by:** `system/admin/src/router-pages/themeEdit/pageEditorSidebar/PageEditorSidebar.tsx`
**Symbols:** const_fn:`PageDesignEditor`

### `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PageSettings.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/components/inputs/CodeEditor.tsx`, `system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx`, `system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx`, `system/admin/src/router-pages/themeEdit/ThemeEdit.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx`
**Imported by:** `system/admin/src/router-pages/themeEdit/pageEditorSidebar/PageEditorSidebar.tsx`
**Symbols:** const_fn:`PageMetaSettings`, const_fn:`PageSettings`, const_fn:`handleChange`, const_fn:`handleDeleteCurrentPage`

### `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PluginEditor.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/EditorBlockEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/HTMLBlockEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/ImageBlockEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextBlockEditor.tsx`
**Imported by:** `system/admin/src/router-pages/themeEdit/pageEditorSidebar/PageEditorSidebar.tsx`
**Symbols:** const_fn:`PluginEditor`

### `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/SelectableField.tsx`
**Feature:** UI Components
**Imported by:** `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/FontEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/ImageBlockEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/ShadowEditor.tsx`
**Symbols:** const_fn:`SelectableField`

### `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/ShadowEditor.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/ColorPickerField.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/SelectableField.tsx`
**Imported by:** `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PageDesignEditor.tsx`
**Symbols:** const_fn:`extractColor`, const_fn:`extractCurrentValue`, const_fn:`getDefaultColor`, const_fn:`swapColor`, const_fn:`ShadowEditor`, const_fn:`colorUpdate`, const_fn:`shadowUpdate`

### `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/StyleNumberField.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/router-pages/themeEdit/pageEditorSidebar/SlideableNumberInput.tsx`
**Imported by:** `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/DimensionsEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/ImageBlockEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/MarginEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PaddingEditor.tsx`
**Symbols:** const_fn:`getUnit`, const_fn:`getWithoutUnit`, const_fn:`StyleNumberField`

### `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextBlockEditor.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx`, `system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx`
**Imported by:** `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PluginEditor.tsx`
**Symbols:** const_fn:`TextBlockEditor`, const_fn:`setBlockValue`

### `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx`
**Feature:** UI Components
**Imported by:** `system/admin/src/components/entity/entityEdit/components/EntityMetaFields.tsx`, `system/admin/src/components/entity/entityTable/components/SearchContent.tsx`, `system/admin/src/components/inputs/Image/ImageInput.tsx`, `system/admin/src/components/inputs/Search/SearchInput.tsx`, `system/admin/src/components/textFieldWithTooltip/TextFieldWithTooltip.tsx`, `system/admin/src/helpers/customFields/fields.tsx`, `system/admin/src/router-pages/attribute/components/ValueItem.tsx`, `system/admin/src/router-pages/coupon/Coupon.tsx`, `system/admin/src/router-pages/order/components/PageContent.tsx`, `system/admin/src/router-pages/post/components/PostSettings.tsx`
**Symbols:** const_fn:`TextInput`, const_fn:`TextAreaInput`

### `system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/ThirdPartyPluginEditor.tsx`
**Feature:** UI Components
**Symbols:** const_fn:`ThirdPartyPluginEditor`

### `system/admin/src/router-pages/themeEdit/pageList/PageItem.tsx`
**Imports:** `system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx`, `system/admin/src/router-pages/themeEdit/ThemeEdit.tsx`
**Imported by:** `system/admin/src/router-pages/themeEdit/pageList/PageList.tsx`
**Symbols:** const_fn:`PageItem`

### `system/admin/src/router-pages/themeEdit/pageList/PageList.tsx`
**Imports:** `system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx`, `system/admin/src/router-pages/themeEdit/pageList/PageItem.tsx`
**Imported by:** `system/admin/src/router-pages/themeEdit/ThemeEdit.tsx`
**Symbols:** const_fn:`PageList`, const_fn:`openNewPage`, const_fn:`handleAddCustomPage`

### `system/admin/src/router-pages/themeMarket/ThemeMarket.test.tsx`
**Imports:** `system/admin/src/router-pages/themeMarket/ThemeMarket.tsx`

### `system/admin/src/router-pages/themeMarket/ThemeMarket.tsx`
**Imports:** `system/admin/src/components/market/MarketItem.tsx`, `system/admin/src/components/market/MarketModal.tsx`, `themes/store/src/components/modals/baseModal/Modal.tsx`, `toolkits/commerce/src/mui/Pagination/Pagination.tsx`, `themes/store/src/components/toast/toast.tsx`
**Imported by:** `system/admin/src/router-pages/themeMarket/ThemeMarket.test.tsx`
**Symbols:** class:`ThemeMarket`, const_fn:`preloader`

### `system/admin/src/router-pages/user/User.test.tsx`
**Feature:** User Management
**Imports:** `system/admin/src/router-pages/user/User.tsx`

### `system/admin/src/router-pages/user/User.tsx`
**Feature:** User Management
**Imports:** `system/admin/src/components/entity/entityEdit/EntityEdit.tsx`, `system/admin/src/constants/PageInfos.ts`, `system/admin/src/helpers/addressParser.tsx`
**Imported by:** `system/admin/src/router-pages/user/User.test.tsx`
**Symbols:** function:`UserPage`, const_fn:`init`

### `system/admin/src/router-pages/userList/UserList.test.tsx`
**Feature:** User Management
**Imports:** `system/admin/src/router-pages/userList/UserList.tsx`, `system/admin/src/router-pages/settings/pages/store.tsx`

### `system/admin/src/router-pages/userList/UserList.tsx`
**Feature:** User Management
**Imports:** `system/admin/src/components/entity/entityTable/EntityTable.tsx`, `system/admin/src/constants/PageInfos.ts`, `system/admin/src/helpers/addressParser.tsx`, `system/admin/src/helpers/customEntities.tsx`
**Imported by:** `system/admin/src/router-pages/userList/UserList.test.tsx`
**Symbols:** function:`UserTable`, const_fn:`init`

### `system/admin/src/router-pages/welcome/Welcome.test.tsx`
**Imports:** `system/admin/src/router-pages/welcome/Welcome.tsx`

### `system/admin/src/router-pages/welcome/Welcome.tsx`
**Imports:** `system/admin/src/router-pages/welcome/components/CmsSettingsForm.tsx`, `system/admin/src/router-pages/welcome/components/UserForm.tsx`
**Imported by:** `system/admin/src/router-pages/welcome/Welcome.test.tsx`
**Symbols:** function:`WelcomePage`, const_fn:`onAccountSuccess`, const_fn:`onSettingsSuccess`

### `system/admin/src/router-pages/welcome/components/CmsSettingsForm.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/components/inputs/SwitchInput/SwitchInput.tsx`, `system/admin/src/components/loadBox/LoadingStatus.tsx`
**Imported by:** `system/admin/src/router-pages/welcome/Welcome.tsx`
**Symbols:** function:`CmsSettingsForm`, const_fn:`handleSubmitClick`

### `system/admin/src/router-pages/welcome/components/UserForm.tsx`
**Feature:** UI Components
**Imports:** `system/admin/src/components/inputs/Image/ImageInput.tsx`
**Imported by:** `system/admin/src/router-pages/welcome/Welcome.tsx`
**Symbols:** function:`UserForm`, const_fn:`init`, const_fn:`checkAuth`, const_fn:`handleSubmitClick`

### `system/admin/src/startup/server.ts`
**Imports:** `system/core/backend/src/helpers/cms-settings.ts`, `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/helpers/shell.ts`, `system/core/frontend/src/api/CRestApiClient.ts`, `system/utils/src/static.ts`
**Symbols:** const_fn:`start`, const_fn:`linkFiles`, const_fn:`outputEnv`, const_fn:`startProdServer`
**Often changes with:** `system/admin/startup.js` (3x)

### `system/admin/src/tests/customEntities.test.tsx`
**Feature:** Testing

### `system/admin/src/tests/customFields.test.tsx`
**Feature:** Testing

### `system/admin/src/tests/setup.ts`
**Feature:** Testing

### `system/admin/startup.js`
**Feature:** Administration
**Imports:** `system/core/backend/src/helpers/paths.ts`, `themes/store/src/constants.js`, `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/helpers/shell.ts`
**Symbols:** const_fn:`main`, const_fn:`isServerBuilt`, const_fn:`isAdminBuilt`, const_fn:`buildServerScript`, const_fn:`buildWebApp`, const_fn:`outputDeclarations`, const_fn:`runDev`, const_fn:`buffToText`, const_fn:`runProd`
**Often changes with:** `system/core/common/src/types/entities.ts` (5x), `system/manager/src/managers/baseManager.ts` (4x), `system/core/common/src/types/data.ts` (4x), `system/cli/src/cli.ts` (3x), `system/manager/src/managers/adminPanelManager.ts` (3x)

### `system/admin/tailwind.config.js`
**Feature:** Administration
**Imports:** `system/core/backend/src/helpers/paths.ts`

### `system/cli/jest.config.ts`
**Imports:** `themes/store/src/types.ts`

### `system/cli/rollup.config.js`
**Symbols:** const_fn:`external`
**Often changes with:** `system/core/backend/rollup.config.js` (6x), `system/core/common/rollup.config.js` (4x), `system/core/frontend/rollup.config.js` (4x), `system/manager/rollup.config.js` (4x), `system/core/frontend/src/components/CImage/CImage.tsx` (3x)

### `system/cli/src/cli.ts`
**Imports:** `system/core/backend/src/helpers/shell.ts`, `system/cli/src/tasks/create.ts`, `system/utils/src/downloader.ts`
**Symbols:** const_fn:`getManager`
**Often changes with:** `system/manager/src/managers/baseManager.ts` (17x), `system/manager/src/managers/rendererManager.ts` (15x), `system/manager/src/managers/adminPanelManager.ts` (12x), `system/manager/src/managers/serverManager.ts` (12x), `startup.js` (10x)

### `system/cli/src/tasks/create.ts`
**Imported by:** `system/cli/src/cli.ts`, `system/core/backend/src/repositories/product-category.repository.ts`
**Symbols:** const_fn:`sleep`, const_fn:`createTask`
**Often changes with:** `system/cli/src/cli.ts` (9x), `system/manager/src/managers/rendererManager.ts` (5x), `system/manager/src/managers/baseManager.ts` (4x), `startup.js` (4x), `system/cli/tests/cli.test.ts` (3x)

### `system/cli/src/utils/cleanup-modules.js`
**Feature:** Utilities

### `system/cli/src/utils/cleanup.js`
**Feature:** Utilities
**Symbols:** const_fn:`addFolder`
**Often changes with:** `system/manager/src/tasks/buildTask.ts` (5x), `system/cli/src/cli.ts` (5x), `system/manager/src/managers/baseManager.ts` (4x), `system/core/backend/rollup.config.js` (4x), `system/core/backend/src/helpers/paths.ts` (3x)

### `system/cli/startup.js`
**Imports:** `system/core/backend/src/helpers/shell.ts`
**Symbols:** const_fn:`main`
**Often changes with:** `system/cli/src/cli.ts` (4x), `system/manager/startup.js` (3x), `startup.js` (3x)

### `system/cli/tests/cli.test.ts`
**Feature:** Testing
**Often changes with:** `system/cli/src/cli.ts` (4x), `system/cli/src/tasks/create.ts` (3x)

### `system/core/backend/.eslintrc.js`

### `system/core/backend/jest.config.ts`
**Imports:** `themes/store/src/types.ts`
**Often changes with:** `system/core/backend/src/helpers/paths.ts` (4x), `system/core/backend/src/helpers/actions.ts` (3x), `system/core/backend/src/helpers/cms-settings.ts` (3x), `system/core/backend/src/helpers/constants.ts` (3x), `system/core/backend/src/helpers/emailing.ts` (3x)

### `system/core/backend/rollup.config.js`
**Symbols:** const_fn:`external`, const_fn:`getOutput`, const_fn:`getPlugins`
**Often changes with:** `system/core/common/rollup.config.js` (9x), `system/core/frontend/rollup.config.js` (8x), `system/renderer/rollup.config.js` (7x), `system/cli/rollup.config.js` (6x), `system/core/backend/src/helpers/paths.ts` (6x)

### `system/core/backend/src/_index.ts`
**Often changes with:** `system/core/backend/src/helpers/constants.ts` (13x), `system/core/backend/src/helpers/entity-meta.ts` (8x), `system/core/common/src/types/entities.ts` (8x), `system/core/backend/src/helpers/base-queries.ts` (6x), `system/core/backend/src/repositories/user.repository.ts` (6x)

### `system/core/backend/src/helpers/actions.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/helpers/types.ts`
**Often changes with:** `system/core/backend/src/helpers/paths.ts` (5x), `system/core/backend/jest.config.ts` (3x), `system/core/backend/src/helpers/auth-guards.ts` (3x), `system/core/backend/src/helpers/constants.ts` (3x), `system/core/backend/src/helpers/logger.ts` (3x)

### `system/core/backend/src/helpers/auth-guards.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/auth-roles-permissions.ts`, `system/core/backend/src/helpers/types.ts`
**Imported by:** `system/core/backend/tests/helpers/auth-guards.test.ts`
**Symbols:** const_fn:`checkRegisteredPermissions`, const_fn:`AuthGuard`, const_fn:`graphQlAuthChecker`
**Often changes with:** `system/core/backend/src/_index.ts` (4x), `system/core/backend/src/helpers/constants.ts` (4x), `system/core/backend/src/helpers/create-generic-entity.ts` (4x), `system/core/backend/src/helpers/base-queries.ts` (4x), `system/core/backend/src/helpers/auth-roles-permissions.ts` (3x)

### `system/core/backend/src/helpers/auth-roles-permissions.ts`
**Feature:** Utilities
**Imported by:** `system/core/backend/src/helpers/auth-guards.ts`, `system/core/backend/src/repositories/role.repository.ts`, `system/server/src/main.ts`, `system/server/src/filters/auth.interceptor.ts`
**Symbols:** const_fn:`onRolesChange`, const_fn:`checkRoles`, const_fn:`getCurrentRoles`, const_fn:`getUserRole`, const_fn:`registerPermission`, const_fn:`registerPermissionCategory`, const_fn:`registerDefaultPermission`, const_fn:`getPermissions`
**Often changes with:** `system/core/backend/src/_index.ts` (5x), `system/core/common/src/types/entities.ts` (4x), `system/server/src/controllers/cms.controller.ts` (4x), `system/core/backend/src/helpers/constants.ts` (4x), `system/core/backend/src/helpers/logger.ts` (3x)

### `system/core/backend/src/helpers/auth-settings.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/cms-settings.ts`, `system/core/backend/src/helpers/paths.ts`
**Imported by:** `system/core/backend/src/repositories/user.repository.ts`, `system/renderer/src/server.ts`, `system/renderer/src/helpers/cacheManager.ts`
**Symbols:** const_fn:`getAuthSettings`
**Often changes with:** `system/core/backend/src/_index.ts` (3x), `system/core/backend/src/helpers/constants.ts` (3x)

### `system/core/backend/src/helpers/base-queries.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/entity-meta.ts`
**Imported by:** `system/core/backend/src/repositories/attribute.repository.ts`, `system/core/backend/src/repositories/base.repository.ts`, `system/core/backend/src/repositories/coupon.repository.ts`, `system/core/backend/src/repositories/custom-entity.repository.ts`, `system/core/backend/src/repositories/order.repository.ts`, `system/core/backend/src/repositories/plugin.repository.ts`, `system/core/backend/src/repositories/post.repository.ts`, `system/core/backend/src/repositories/product-review.repository.ts`, `system/core/backend/src/repositories/product-variant.repository.ts`, `system/core/backend/src/repositories/role.repository.ts`
**Symbols:** const_fn:`handleBaseInput`, const_fn:`isSimpleString`, const_fn:`getSqlBoolStr`, const_fn:`getSqlLike`, const_fn:`wrapInQuotes`, const_fn:`getRangeValue`
**Often changes with:** `system/core/backend/src/helpers/constants.ts` (8x), `system/core/common/src/types/entities.ts` (8x), `system/core/backend/src/repositories/base.repository.ts` (8x), `system/core/backend/src/helpers/entity-meta.ts` (7x), `system/core/backend/src/models/entities/order.entity.ts` (7x)

### `system/core/backend/src/helpers/cms-modules.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/constants.ts`, `system/core/backend/src/helpers/paths.ts`
**Imported by:** `system/core/backend/src/helpers/plugin-exports.ts`, `system/core/backend/tests/helpers/cms-modules.test.ts`
**Symbols:** const_fn:`readCmsModules`, const_fn:`readPackageCmsModules`
**Often changes with:** `system/core/backend/src/helpers/constants.ts` (3x), `system/core/backend/src/helpers/plugin-exports.ts` (3x), `system/core/backend/src/helpers/service-versions.ts` (3x), `system/core/backend/src/helpers/theme-config.ts` (3x)

### `system/core/backend/src/helpers/cms-settings.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/constants.ts`, `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/helpers/paths.ts`
**Imported by:** `system/admin/src/startup/server.ts`, `system/core/backend/src/helpers/auth-settings.ts`, `system/core/backend/src/helpers/connect-database.ts`, `system/core/backend/src/helpers/emailing.ts`, `system/core/backend/src/helpers/service-versions.ts`, `system/core/backend/tests/helpers/cms-settings.test.ts`, `system/core/backend/tests/helpers/theme-config.test.ts`, `system/manager/src/index.ts`, `system/manager/src/managers/adminPanelManager.ts`, `system/manager/src/managers/baseManager.ts`
**Symbols:** const_fn:`getEnvConfig`, const_fn:`readCMSConfigSync`, const_fn:`readCMSConfig`, const_fn:`getCmsEntity`, const_fn:`getCmsConfig`, const_fn:`getCmsSettings`, const_fn:`getCmsInfo`
**Often changes with:** `system/core/backend/src/helpers/constants.ts` (11x), `system/core/common/src/types/entities.ts` (10x), `system/core/common/src/types/data.ts` (8x), `system/core/backend/src/helpers/paths.ts` (7x), `system/server/src/controllers/cms.controller.ts` (7x)

### `system/core/backend/src/helpers/connect-database.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/cms-settings.ts`, `system/core/backend/src/helpers/constants.ts`, `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/helpers/paths.ts`, `system/core/backend/src/helpers/plugin-exports.ts`
**Symbols:** const_fn:`connectDatabase`, const_fn:`setDbConnected`, const_fn:`awaitDbConnection`
**Often changes with:** `system/core/backend/src/_index.ts` (4x), `system/core/backend/src/helpers/constants.ts` (4x), `system/server/src/helpers/connect-database.ts` (3x), `system/core/backend/src/helpers/auth-roles-permissions.ts` (3x)

### `system/core/backend/src/helpers/constants.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/logger.ts`
**Imported by:** `system/core/backend/src/helpers/cms-modules.ts`, `system/core/backend/src/helpers/cms-settings.ts`, `system/core/backend/src/helpers/connect-database.ts`, `system/core/backend/src/helpers/plugin-exports.ts`
**Often changes with:** `system/core/common/src/types/data.ts` (23x), `system/core/common/src/types/entities.ts` (22x), `system/core/backend/src/helpers/paths.ts` (15x), `system/core/backend/src/_index.ts` (13x), `system/core/common/src/constants.ts` (12x)

### `system/core/backend/src/helpers/create-generic-entity.ts`
**Feature:** Utilities
**Imported by:** `system/core/backend/src/helpers/generic-entities.ts`, `system/core/backend/tests/helpers/create-generic-entity.test.ts`
**Symbols:** class:`GenericRepository`, class:`PagedEntity`, class:`CreateArgs`, class:`UpdateArgs`
**Often changes with:** `system/core/backend/src/helpers/constants.ts` (6x), `system/core/backend/src/helpers/base-queries.ts` (6x), `system/core/backend/src/_index.ts` (5x), `system/core/backend/src/helpers/auth-guards.ts` (4x), `system/core/backend/src/repositories/base.repository.ts` (4x)

### `system/core/backend/src/helpers/data-filters.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/types.ts`
**Often changes with:** `system/core/backend/src/helpers/plugin-settings.ts` (3x)

### `system/core/backend/src/helpers/emailing.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/cms-settings.ts`, `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/helpers/paths.ts`
**Imported by:** `system/core/backend/tests/helpers/emailing.test.ts`
**Symbols:** const_fn:`getEmailTemplate`, const_fn:`sendEmail`
**Often changes with:** `system/core/backend/src/helpers/paths.ts` (5x), `system/core/common/src/types/entities.ts` (5x), `system/core/backend/src/helpers/cms-settings.ts` (5x), `system/core/backend/src/helpers/constants.ts` (5x), `system/core/backend/src/helpers/logger.ts` (4x)

### `system/core/backend/src/helpers/entity-meta.ts`
**Feature:** Utilities
**Imported by:** `system/core/backend/src/helpers/base-queries.ts`, `system/core/backend/src/repositories/base.repository.ts`, `system/core/backend/src/repositories/product-category.repository.ts`
**Symbols:** class:`EntityMetaRepository`
**Often changes with:** `system/core/backend/src/_index.ts` (8x), `system/core/backend/src/helpers/base-queries.ts` (7x), `system/core/backend/src/helpers/constants.ts` (6x), `system/core/common/src/types/entities.ts` (6x), `system/core/backend/src/repositories/product.repository.ts` (6x)

### `system/core/backend/src/helpers/generic-entities.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/create-generic-entity.ts`
**Imported by:** `system/core/backend/src/helpers/plugin-settings.ts`, `system/core/backend/src/helpers/theme-config.ts`
**Symbols:** class:`GenericThemeResolver`, class:`GenericPluginResolver`
**Often changes with:** `system/core/backend/src/helpers/cms-settings.ts` (3x), `system/core/backend/src/helpers/constants.ts` (3x), `system/core/backend/src/models/entities/cms.entity.ts` (3x)

### `system/core/backend/src/helpers/logger.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/paths.ts`
**Imported by:** `system/admin/startup.js`, `system/admin/src/startup/server.ts`, `system/core/backend/src/helpers/actions.ts`, `system/core/backend/src/helpers/cms-settings.ts`, `system/core/backend/src/helpers/connect-database.ts`, `system/core/backend/src/helpers/constants.ts`, `system/core/backend/src/helpers/emailing.ts`, `system/core/backend/src/helpers/paths.ts`, `system/core/backend/src/helpers/plugin-exports.ts`, `system/core/backend/src/helpers/plugin-settings.ts`
**Symbols:** const_fn:`getLogger`
**Often changes with:** `system/core/backend/src/helpers/paths.ts` (5x), `system/core/frontend/src/api/CGraphQLClient.ts` (5x), `system/core/backend/src/helpers/emailing.ts` (4x), `system/core/common/src/types/data.ts` (4x), `system/core/common/src/types/entities.ts` (4x)

### `system/core/backend/src/helpers/paths.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/logger.ts`
**Imported by:** `system/admin/postcss.config.js`, `system/admin/startup.js`, `system/admin/tailwind.config.js`, `system/core/backend/src/helpers/auth-settings.ts`, `system/core/backend/src/helpers/cms-modules.ts`, `system/core/backend/src/helpers/cms-settings.ts`, `system/core/backend/src/helpers/connect-database.ts`, `system/core/backend/src/helpers/emailing.ts`, `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/helpers/shell.ts`
**Symbols:** const_fn:`getTempDir`, const_fn:`resolvePackageJsonPath`, const_fn:`getNodeModuleDirSync`, const_fn:`getNodeModuleDir`, const_fn:`getCmsConfigPath`, const_fn:`getUp`, const_fn:`getCmsConfigPathSync`, const_fn:`getUp`, const_fn:`getCoreCommonDir`, const_fn:`getCoreFrontendDir`, const_fn:`getCoreBackendDir`, const_fn:`getLogsDir`, const_fn:`getErrorLogPath`, const_fn:`getManagerDir`, const_fn:`getManagerTempDir`
**Often changes with:** `system/core/common/src/types/data.ts` (33x), `system/core/backend/src/helpers/constants.ts` (15x), `system/server/src/controllers/cms.controller.ts` (13x), `system/core/common/src/types/entities.ts` (12x), `system/renderer/src/generator.ts` (12x)

### `system/core/backend/src/helpers/plugin-exports.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/cms-modules.ts`, `system/core/backend/src/helpers/constants.ts`, `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/helpers/types.ts`
**Imported by:** `system/core/backend/src/helpers/connect-database.ts`, `system/core/backend/tests/helpers/plugin-exports.test.ts`
**Symbols:** const_fn:`readPluginsExports`, const_fn:`collectPlugins`
**Often changes with:** `system/core/backend/src/helpers/cms-modules.ts` (3x), `system/core/backend/src/helpers/constants.ts` (3x)

### `system/core/backend/src/helpers/plugin-settings.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/generic-entities.ts`, `system/core/backend/src/helpers/logger.ts`
**Imported by:** `system/core/backend/tests/helpers/plugin-settings.test.ts`
**Symbols:** const_fn:`findPlugin`, const_fn:`savePlugin`, const_fn:`entityToSettings`, const_fn:`savePluginSettings`
**Often changes with:** `system/core/backend/src/helpers/data-filters.ts` (3x), `system/core/backend/src/helpers/base-queries.ts` (3x), `system/core/backend/src/helpers/theme-config.ts` (3x)

### `system/core/backend/src/helpers/service-versions.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/cms-settings.ts`, `system/core/backend/src/helpers/logger.ts`
**Imported by:** `system/core/backend/tests/helpers/service-versions.test.ts`, `system/manager/src/managers/baseManager.ts`
**Symbols:** const_fn:`extractServiceVersion`, const_fn:`incrementServiceVersion`, const_fn:`getServiceVersion`
**Often changes with:** `system/core/backend/src/helpers/base-queries.ts` (3x), `system/core/backend/src/helpers/cms-modules.ts` (3x), `system/core/backend/src/helpers/cms-settings.ts` (3x), `system/core/backend/src/helpers/constants.ts` (3x), `system/core/backend/src/models/entities/cms.entity.ts` (3x)

### `system/core/backend/src/helpers/shell.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/helpers/paths.ts`
**Imported by:** `system/admin/startup.js`, `system/admin/src/startup/server.ts`, `system/cli/startup.js`, `system/cli/src/cli.ts`, `system/manager/startup.js`, `system/manager/src/index.ts`, `system/renderer/startup.js`, `system/renderer/src/generator.ts`, `system/renderer/src/server.ts`, `system/server/startup.js`
**Symbols:** const_fn:`runShellCommand`, function:`dataToKey`, function:`keyToData`, const_fn:`reportProcessPid`, const_fn:`getAllProcessPids`, const_fn:`pids`
**Often changes with:** `system/core/backend/src/helpers/paths.ts` (4x), `system/core/common/src/types/data.ts` (3x), `system/core/common/src/types/entities.ts` (3x), `system/core/backend/src/helpers/actions.ts` (3x), `system/core/backend/src/helpers/cms-settings.ts` (3x)

### `system/core/backend/src/helpers/theme-config.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/generic-entities.ts`, `system/core/backend/src/helpers/logger.ts`
**Imported by:** `system/core/backend/tests/helpers/theme-config.test.ts`
**Symbols:** const_fn:`findTheme`, const_fn:`getThemeConfigs`
**Often changes with:** `system/core/backend/src/helpers/cms-settings.ts` (4x), `system/core/backend/src/helpers/base-queries.ts` (3x), `system/core/backend/src/helpers/cms-modules.ts` (3x), `system/core/backend/src/helpers/plugin-settings.ts` (3x)

### `system/core/backend/src/helpers/types.ts`
**Feature:** Utilities
**Imported by:** `system/core/backend/src/helpers/actions.ts`, `system/core/backend/src/helpers/auth-guards.ts`, `system/core/backend/src/helpers/data-filters.ts`, `system/core/backend/src/helpers/plugin-exports.ts`
**Often changes with:** `system/core/backend/src/helpers/constants.ts` (7x), `system/core/common/src/types/data.ts` (7x), `system/core/common/src/types/entities.ts` (5x), `system/core/backend/src/_index.ts` (5x), `system/core/common/src/constants.ts` (5x)

### `system/core/backend/src/helpers/validation.ts`
**Feature:** Utilities
**Imported by:** `system/core/backend/src/repositories/order.repository.ts`, `system/core/backend/src/repositories/user.repository.ts`, `system/core/backend/tests/helpers/validation.test.ts`
**Symbols:** const_fn:`validateEmail`

### `system/core/backend/src/models/entities/attribute-product.entity.ts`
**Imports:** `system/core/backend/src/models/entities/attribute-value.entity.ts`, `system/core/backend/src/models/entities/product.entity.ts`
**Imported by:** `system/core/backend/src/models/entities/attribute-value.entity.ts`, `system/core/backend/src/models/entities/product.entity.ts`
**Symbols:** class:`AttributeToProduct`
**Often changes with:** `system/core/backend/src/helpers/entity-meta.ts` (3x), `system/core/backend/src/models/entities/attribute-value.entity.ts` (3x), `system/core/backend/src/models/entities/attribute.entity.ts` (3x), `system/core/backend/src/models/entities/cms.entity.ts` (3x), `system/core/backend/src/models/entities/meta/attribute-meta.entity.ts` (3x)

### `system/core/backend/src/models/entities/attribute-value.entity.ts`
**Imports:** `system/core/backend/src/models/entities/attribute.entity.ts`, `system/core/backend/src/models/entities/base-page.entity.ts`, `system/core/backend/src/models/entities/attribute-product.entity.ts`
**Imported by:** `system/core/backend/src/models/entities/attribute-product.entity.ts`, `system/core/backend/src/models/entities/attribute.entity.ts`
**Symbols:** class:`AttributeValue`
**Often changes with:** `system/core/backend/src/helpers/entity-meta.ts` (3x), `system/core/backend/src/models/entities/attribute-product.entity.ts` (3x), `system/core/backend/src/models/entities/attribute.entity.ts` (3x), `system/core/backend/src/models/entities/cms.entity.ts` (3x), `system/core/backend/src/models/entities/meta/attribute-meta.entity.ts` (3x)

### `system/core/backend/src/models/entities/attribute.entity.ts`
**Imports:** `system/core/backend/src/models/entities/attribute-value.entity.ts`, `system/core/backend/src/models/entities/base-page.entity.ts`, `system/core/backend/src/models/entities/meta/attribute-meta.entity.ts`
**Imported by:** `system/core/backend/src/models/entities/attribute-value.entity.ts`
**Symbols:** class:`Attribute`
**Often changes with:** `system/core/backend/src/models/entities/order.entity.ts` (5x), `system/core/backend/src/helpers/entity-meta.ts` (4x), `system/core/backend/src/models/entities/base-page.entity.ts` (4x), `system/core/backend/src/models/entities/cms.entity.ts` (4x), `system/core/backend/src/models/entities/post.entity.ts` (4x)

### `system/core/backend/src/models/entities/base-page.entity.ts`
**Imported by:** `system/core/backend/src/models/entities/attribute-value.entity.ts`, `system/core/backend/src/models/entities/attribute.entity.ts`, `system/core/backend/src/models/entities/coupon.entity.ts`, `system/core/backend/src/models/entities/custom-entity.entity.ts`, `system/core/backend/src/models/entities/plugin.entity.ts`, `system/core/backend/src/models/entities/post-comment.entity.ts`, `system/core/backend/src/models/entities/post.entity.ts`, `system/core/backend/src/models/entities/product-category.entity.ts`, `system/core/backend/src/models/entities/product-review.entity.ts`, `system/core/backend/src/models/entities/product-variant.entity.ts`
**Symbols:** class:`BasePageMeta`, class:`BasePageEntity`
**Often changes with:** `system/core/backend/src/models/entities/order.entity.ts` (8x), `system/core/backend/src/helpers/base-queries.ts` (6x), `system/core/backend/src/models/entities/product.entity.ts` (6x), `system/core/backend/src/models/entities/cms.entity.ts` (5x), `system/core/backend/src/models/entities/plugin.entity.ts` (5x)

### `system/core/backend/src/models/entities/cms.entity.ts`
**Symbols:** class:`CmsEntity`
**Often changes with:** `system/core/backend/src/helpers/constants.ts` (7x), `system/core/backend/src/models/entities/order.entity.ts` (6x), `system/core/backend/src/models/entities/user.entity.ts` (6x), `system/core/backend/src/models/entities/base-page.entity.ts` (5x), `system/core/backend/src/helpers/cms-settings.ts` (5x)

### `system/core/backend/src/models/entities/coupon.entity.ts`
**Imports:** `system/core/backend/src/models/entities/base-page.entity.ts`, `system/core/backend/src/models/entities/meta/coupon-meta.entity.ts`
**Imported by:** `system/core/backend/src/models/entities/order.entity.ts`
**Symbols:** class:`Coupon`

### `system/core/backend/src/models/entities/custom-entity.entity.ts`
**Imports:** `system/core/backend/src/models/entities/base-page.entity.ts`, `system/core/backend/src/models/entities/meta/custom-entity-meta.entity.ts`
**Symbols:** class:`CustomEntity`
**Often changes with:** `system/core/backend/src/helpers/entity-meta.ts` (3x)

### `system/core/backend/src/models/entities/dashboard-entity.entity.ts`
**Imports:** `system/core/backend/src/models/entities/user.entity.ts`
**Imported by:** `system/core/backend/src/models/entities/user.entity.ts`
**Symbols:** class:`DashboardEntity`

### `system/core/backend/src/models/entities/meta/attribute-meta.entity.ts`
**Imports:** `system/core/backend/src/models/entities/meta/base-meta.entity.ts`
**Imported by:** `system/core/backend/src/models/entities/attribute.entity.ts`
**Symbols:** class:`AttributeMeta`
**Often changes with:** `system/core/backend/src/helpers/entity-meta.ts` (3x), `system/core/backend/src/models/entities/attribute-product.entity.ts` (3x), `system/core/backend/src/models/entities/attribute-value.entity.ts` (3x), `system/core/backend/src/models/entities/attribute.entity.ts` (3x), `system/core/backend/src/models/entities/cms.entity.ts` (3x)

### `system/core/backend/src/models/entities/meta/base-meta.entity.ts`
**Imported by:** `system/core/backend/src/models/entities/meta/attribute-meta.entity.ts`, `system/core/backend/src/models/entities/meta/coupon-meta.entity.ts`, `system/core/backend/src/models/entities/meta/custom-entity-meta.entity.ts`, `system/core/backend/src/models/entities/meta/order-meta.entity.ts`, `system/core/backend/src/models/entities/meta/post-meta.entity.ts`, `system/core/backend/src/models/entities/meta/product-category-meta.entity.ts`, `system/core/backend/src/models/entities/meta/product-meta.entity.ts`, `system/core/backend/src/models/entities/meta/product-variant-meta.entity.ts`, `system/core/backend/src/models/entities/meta/role-meta.entity.ts`, `system/core/backend/src/models/entities/meta/tag-meta.entity.ts`
**Symbols:** class:`BaseEntityMeta`

### `system/core/backend/src/models/entities/meta/coupon-meta.entity.ts`
**Imports:** `system/core/backend/src/models/entities/meta/base-meta.entity.ts`
**Imported by:** `system/core/backend/src/models/entities/coupon.entity.ts`
**Symbols:** class:`CouponMeta`

### `system/core/backend/src/models/entities/meta/custom-entity-meta.entity.ts`
**Imports:** `system/core/backend/src/models/entities/meta/base-meta.entity.ts`
**Imported by:** `system/core/backend/src/models/entities/custom-entity.entity.ts`
**Symbols:** class:`CustomEntityMeta`

### `system/core/backend/src/models/entities/meta/order-meta.entity.ts`
**Imports:** `system/core/backend/src/models/entities/meta/base-meta.entity.ts`
**Imported by:** `system/core/backend/src/models/entities/order.entity.ts`
**Symbols:** class:`OrderMeta`
**Often changes with:** `system/core/backend/src/models/entities/attribute-product.entity.ts` (3x), `system/core/backend/src/models/entities/attribute-value.entity.ts` (3x), `system/core/backend/src/models/entities/attribute.entity.ts` (3x), `system/core/backend/src/models/entities/cms.entity.ts` (3x), `system/core/backend/src/models/entities/meta/attribute-meta.entity.ts` (3x)

### `system/core/backend/src/models/entities/meta/post-meta.entity.ts`
**Imports:** `system/core/backend/src/models/entities/meta/base-meta.entity.ts`
**Imported by:** `system/core/backend/src/models/entities/post.entity.ts`
**Symbols:** class:`PostMeta`
**Often changes with:** `system/core/backend/src/models/entities/attribute-product.entity.ts` (3x), `system/core/backend/src/models/entities/attribute-value.entity.ts` (3x), `system/core/backend/src/models/entities/attribute.entity.ts` (3x), `system/core/backend/src/models/entities/cms.entity.ts` (3x), `system/core/backend/src/models/entities/meta/attribute-meta.entity.ts` (3x)

### `system/core/backend/src/models/entities/meta/product-category-meta.entity.ts`
**Imports:** `system/core/backend/src/models/entities/meta/base-meta.entity.ts`
**Imported by:** `system/core/backend/src/models/entities/product-category.entity.ts`
**Symbols:** class:`ProductCategoryMeta`
**Often changes with:** `system/core/backend/src/models/entities/attribute-product.entity.ts` (3x), `system/core/backend/src/models/entities/attribute-value.entity.ts` (3x), `system/core/backend/src/models/entities/attribute.entity.ts` (3x), `system/core/backend/src/models/entities/cms.entity.ts` (3x), `system/core/backend/src/models/entities/meta/attribute-meta.entity.ts` (3x)

### `system/core/backend/src/models/entities/meta/product-meta.entity.ts`
**Imports:** `system/core/backend/src/models/entities/meta/base-meta.entity.ts`
**Imported by:** `system/core/backend/src/models/entities/product.entity.ts`
**Symbols:** class:`ProductMeta`
**Often changes with:** `system/core/backend/src/models/entities/attribute-product.entity.ts` (3x), `system/core/backend/src/models/entities/attribute-value.entity.ts` (3x), `system/core/backend/src/models/entities/attribute.entity.ts` (3x), `system/core/backend/src/models/entities/cms.entity.ts` (3x), `system/core/backend/src/models/entities/meta/attribute-meta.entity.ts` (3x)

### `system/core/backend/src/models/entities/meta/product-variant-meta.entity.ts`
**Imports:** `system/core/backend/src/models/entities/meta/base-meta.entity.ts`
**Imported by:** `system/core/backend/src/models/entities/product-variant.entity.ts`
**Symbols:** class:`ProductVariantMeta`

### `system/core/backend/src/models/entities/meta/role-meta.entity.ts`
**Imports:** `system/core/backend/src/models/entities/meta/base-meta.entity.ts`
**Imported by:** `system/core/backend/src/models/entities/role.entity.ts`
**Symbols:** class:`RoleMeta`

### `system/core/backend/src/models/entities/meta/tag-meta.entity.ts`
**Imports:** `system/core/backend/src/models/entities/meta/base-meta.entity.ts`
**Imported by:** `system/core/backend/src/models/entities/tag.entity.ts`
**Symbols:** class:`TagMeta`
**Often changes with:** `system/core/backend/src/models/entities/attribute-product.entity.ts` (3x), `system/core/backend/src/models/entities/attribute-value.entity.ts` (3x), `system/core/backend/src/models/entities/attribute.entity.ts` (3x), `system/core/backend/src/models/entities/cms.entity.ts` (3x), `system/core/backend/src/models/entities/meta/attribute-meta.entity.ts` (3x)

### `system/core/backend/src/models/entities/meta/user-meta.entity.ts`
**Imports:** `system/core/backend/src/models/entities/meta/base-meta.entity.ts`
**Imported by:** `system/core/backend/src/models/entities/user.entity.ts`
**Symbols:** class:`UserMeta`
**Often changes with:** `system/core/backend/src/models/entities/attribute-product.entity.ts` (3x), `system/core/backend/src/models/entities/attribute-value.entity.ts` (3x), `system/core/backend/src/models/entities/attribute.entity.ts` (3x), `system/core/backend/src/models/entities/cms.entity.ts` (3x), `system/core/backend/src/models/entities/meta/attribute-meta.entity.ts` (3x)

### `system/core/backend/src/models/entities/order.entity.ts`
**Imports:** `system/core/backend/src/models/entities/meta/order-meta.entity.ts`, `system/core/backend/src/models/entities/coupon.entity.ts`
**Symbols:** class:`Order`
**Often changes with:** `system/core/common/src/types/entities.ts` (9x), `system/core/backend/src/models/entities/base-page.entity.ts` (8x), `system/core/backend/src/models/entities/product.entity.ts` (8x), `system/core/backend/src/models/inputs/order.input.ts` (8x), `system/core/backend/src/models/entities/post.entity.ts` (7x)

### `system/core/backend/src/models/entities/page-stats.entity.ts`
**Symbols:** class:`PageStats`
**Often changes with:** `system/core/backend/src/models/entities/base-page.entity.ts` (4x), `system/core/backend/src/models/entities/cms.entity.ts` (4x), `system/core/backend/src/models/entities/order.entity.ts` (4x), `system/core/backend/src/models/entities/plugin.entity.ts` (4x), `system/core/backend/src/models/entities/post-comment.entity.ts` (4x)

### `system/core/backend/src/models/entities/plugin.entity.ts`
**Imports:** `system/core/backend/src/models/entities/base-page.entity.ts`
**Symbols:** class:`PluginEntity`
**Often changes with:** `system/core/backend/src/models/entities/base-page.entity.ts` (5x), `system/core/backend/src/models/entities/order.entity.ts` (5x), `system/core/backend/src/models/entities/post.entity.ts` (5x), `system/core/backend/src/models/entities/product-category.entity.ts` (5x), `system/core/backend/src/models/entities/product-review.entity.ts` (5x)

### `system/core/backend/src/models/entities/post-comment.entity.ts`
**Imports:** `system/core/backend/src/models/entities/base-page.entity.ts`, `system/core/backend/src/models/entities/post.entity.ts`
**Imported by:** `system/core/backend/src/models/entities/post.entity.ts`
**Symbols:** class:`PostComment`
**Often changes with:** `system/core/backend/src/models/entities/cms.entity.ts` (4x), `system/core/backend/src/models/entities/order.entity.ts` (4x), `system/core/backend/src/models/entities/page-stats.entity.ts` (4x), `system/core/backend/src/models/entities/plugin.entity.ts` (4x), `system/core/backend/src/models/entities/post.entity.ts` (4x)

### `system/core/backend/src/models/entities/post.entity.ts`
**Imports:** `system/core/backend/src/models/entities/base-page.entity.ts`, `system/core/backend/src/models/entities/meta/post-meta.entity.ts`, `system/core/backend/src/models/entities/post-comment.entity.ts`, `system/core/backend/src/models/entities/tag.entity.ts`, `system/core/backend/src/models/entities/user.entity.ts`
**Imported by:** `system/core/backend/src/models/entities/post-comment.entity.ts`, `system/core/backend/src/models/entities/user.entity.ts`
**Symbols:** class:`Post`
**Often changes with:** `system/core/backend/src/models/entities/user.entity.ts` (8x), `system/core/backend/src/models/entities/order.entity.ts` (7x), `system/core/backend/src/models/entities/product.entity.ts` (7x), `system/core/backend/src/models/entities/product-category.entity.ts` (6x), `system/core/backend/src/models/entities/tag.entity.ts` (6x)

### `system/core/backend/src/models/entities/product-category.entity.ts`
**Imports:** `system/core/backend/src/models/entities/base-page.entity.ts`, `system/core/backend/src/models/entities/meta/product-category-meta.entity.ts`, `system/core/backend/src/models/entities/product.entity.ts`
**Imported by:** `system/core/backend/src/models/entities/product.entity.ts`
**Symbols:** class:`ProductCategory`
**Often changes with:** `system/core/backend/src/models/entities/product.entity.ts` (7x), `system/core/backend/src/models/entities/order.entity.ts` (6x), `system/core/backend/src/models/entities/post.entity.ts` (6x), `system/core/backend/src/models/entities/tag.entity.ts` (6x), `system/core/backend/src/models/entities/user.entity.ts` (6x)

### `system/core/backend/src/models/entities/product-review.entity.ts`
**Imports:** `system/core/backend/src/models/entities/base-page.entity.ts`, `system/core/backend/src/models/entities/product.entity.ts`
**Imported by:** `system/core/backend/src/models/entities/product.entity.ts`
**Symbols:** class:`ProductReview`
**Often changes with:** `system/core/backend/src/models/entities/order.entity.ts` (5x), `system/core/backend/src/models/entities/plugin.entity.ts` (5x), `system/core/backend/src/models/entities/post.entity.ts` (5x), `system/core/backend/src/models/entities/product-category.entity.ts` (5x), `system/core/backend/src/models/entities/product.entity.ts` (5x)

### `system/core/backend/src/models/entities/product-variant.entity.ts`
**Imports:** `system/core/backend/src/models/entities/base-page.entity.ts`, `system/core/backend/src/models/entities/meta/product-variant-meta.entity.ts`, `system/core/backend/src/models/entities/product.entity.ts`
**Imported by:** `system/core/backend/src/models/entities/product.entity.ts`
**Symbols:** class:`ProductVariant`

### `system/core/backend/src/models/entities/product.entity.ts`
**Imports:** `system/core/backend/src/models/entities/attribute-product.entity.ts`, `system/core/backend/src/models/entities/base-page.entity.ts`, `system/core/backend/src/models/entities/meta/product-meta.entity.ts`, `system/core/backend/src/models/entities/product-category.entity.ts`, `system/core/backend/src/models/entities/product-review.entity.ts`, `system/core/backend/src/models/entities/product-variant.entity.ts`
**Imported by:** `system/core/backend/src/models/entities/attribute-product.entity.ts`, `system/core/backend/src/models/entities/product-category.entity.ts`, `system/core/backend/src/models/entities/product-review.entity.ts`, `system/core/backend/src/models/entities/product-variant.entity.ts`
**Symbols:** class:`Product`, class:`ProductRating`
**Often changes with:** `system/core/backend/src/repositories/product.repository.ts` (9x), `system/core/backend/src/models/entities/order.entity.ts` (8x), `system/core/backend/src/models/entities/post.entity.ts` (7x), `system/core/backend/src/models/entities/product-category.entity.ts` (7x), `system/core/backend/src/models/entities/user.entity.ts` (7x)

### `system/core/backend/src/models/entities/role.entity.ts`
**Imports:** `system/core/backend/src/models/entities/base-page.entity.ts`, `system/core/backend/src/models/entities/user.entity.ts`, `system/core/backend/src/models/entities/meta/role-meta.entity.ts`
**Imported by:** `system/core/backend/src/models/entities/user.entity.ts`
**Symbols:** class:`Role`
**Often changes with:** `system/core/backend/src/models/entities/user.entity.ts` (3x), `system/core/backend/src/_index.ts` (3x), `system/core/backend/src/helpers/auth-roles-permissions.ts` (3x), `system/core/backend/src/repositories/role.repository.ts` (3x), `system/core/common/src/types/entities.ts` (3x)

### `system/core/backend/src/models/entities/tag.entity.ts`
**Imports:** `system/core/backend/src/models/entities/base-page.entity.ts`, `system/core/backend/src/models/entities/meta/tag-meta.entity.ts`
**Imported by:** `system/core/backend/src/models/entities/post.entity.ts`
**Symbols:** class:`Tag`
**Often changes with:** `system/core/backend/src/models/entities/order.entity.ts` (6x), `system/core/backend/src/models/entities/post.entity.ts` (6x), `system/core/backend/src/models/entities/product-category.entity.ts` (6x), `system/core/backend/src/models/entities/product.entity.ts` (6x), `system/core/backend/src/models/entities/user.entity.ts` (6x)

### `system/core/backend/src/models/entities/theme.entity.ts`
**Imports:** `system/core/backend/src/models/entities/base-page.entity.ts`
**Symbols:** class:`ThemeEntity`
**Often changes with:** `system/core/backend/src/models/entities/plugin.entity.ts` (5x), `system/core/backend/src/models/entities/order.entity.ts` (4x), `system/core/backend/src/models/entities/post.entity.ts` (4x), `system/core/backend/src/models/entities/product-category.entity.ts` (4x), `system/core/backend/src/models/entities/product-review.entity.ts` (4x)

### `system/core/backend/src/models/entities/user.entity.ts`
**Imports:** `system/core/backend/src/models/entities/base-page.entity.ts`, `system/core/backend/src/models/entities/dashboard-entity.entity.ts`, `system/core/backend/src/models/entities/meta/user-meta.entity.ts`, `system/core/backend/src/models/entities/post.entity.ts`, `system/core/backend/src/models/entities/role.entity.ts`
**Imported by:** `system/core/backend/src/models/entities/dashboard-entity.entity.ts`, `system/core/backend/src/models/entities/post.entity.ts`, `system/core/backend/src/models/entities/role.entity.ts`
**Symbols:** class:`User`
**Often changes with:** `system/core/backend/src/models/entities/post.entity.ts` (8x), `system/core/backend/src/models/entities/order.entity.ts` (7x), `system/core/backend/src/models/entities/product.entity.ts` (7x), `system/core/common/src/types/entities.ts` (7x), `system/core/backend/src/models/entities/product-category.entity.ts` (6x)

### `system/core/backend/src/models/filters/base-filter.filter.ts`
**Imported by:** `system/core/backend/src/models/filters/custom-entity.filter.ts`, `system/core/backend/src/models/filters/order.filter.ts`, `system/core/backend/src/models/filters/post.filter.ts`, `system/core/backend/src/models/filters/product-category.filter.ts`, `system/core/backend/src/models/filters/product-review.filter.ts`, `system/core/backend/src/models/filters/product.filter.ts`, `system/core/backend/src/models/filters/user.filter.ts`
**Symbols:** class:`BaseFilterInput`, class:`PropertySearch`, class:`SortByOptions`
**Often changes with:** `system/core/backend/src/helpers/base-queries.ts` (5x), `system/core/common/src/types/entities.ts` (5x), `system/core/backend/src/helpers/constants.ts` (3x), `system/core/backend/src/models/entities/order.entity.ts` (3x), `system/core/backend/src/models/entities/post.entity.ts` (3x)

### `system/core/backend/src/models/filters/custom-entity.filter.ts`
**Imports:** `system/core/backend/src/models/filters/base-filter.filter.ts`
**Symbols:** class:`CustomEntityFilterInput`
**Often changes with:** `system/core/backend/src/models/entities/product.entity.ts` (3x), `system/core/common/src/types/entities.ts` (3x)

### `system/core/backend/src/models/filters/order.filter.ts`
**Imports:** `system/core/backend/src/models/filters/base-filter.filter.ts`
**Symbols:** class:`OrderFilterInput`
**Often changes with:** `system/core/backend/src/models/filters/post.filter.ts` (3x), `system/core/backend/src/models/filters/product-category.filter.ts` (3x), `system/core/backend/src/models/filters/product-review.filter.ts` (3x), `system/core/backend/src/models/filters/product.filter.ts` (3x), `system/core/backend/src/models/filters/user.filter.ts` (3x)

### `system/core/backend/src/models/filters/post.filter.ts`
**Imports:** `system/core/backend/src/models/filters/base-filter.filter.ts`
**Symbols:** class:`PostFilterInput`
**Often changes with:** `system/core/backend/src/models/filters/product-review.filter.ts` (4x), `system/core/backend/src/models/entities/post.entity.ts` (3x), `system/core/backend/src/models/entities/product.entity.ts` (3x), `system/core/backend/src/models/filters/order.filter.ts` (3x), `system/core/backend/src/models/filters/product-category.filter.ts` (3x)

### `system/core/backend/src/models/filters/product-category.filter.ts`
**Imports:** `system/core/backend/src/models/filters/base-filter.filter.ts`
**Symbols:** class:`ProductCategoryFilterInput`
**Often changes with:** `system/core/common/src/types/entities.ts` (4x), `system/core/backend/src/repositories/product-category.repository.ts` (3x), `system/core/backend/src/models/filters/order.filter.ts` (3x), `system/core/backend/src/models/filters/post.filter.ts` (3x), `system/core/backend/src/models/filters/product-review.filter.ts` (3x)

### `system/core/backend/src/models/filters/product-review.filter.ts`
**Imports:** `system/core/backend/src/models/filters/base-filter.filter.ts`
**Symbols:** class:`ProductReviewFilter`
**Often changes with:** `system/core/backend/src/models/filters/post.filter.ts` (4x), `system/core/backend/src/models/entities/post.entity.ts` (3x), `system/core/backend/src/models/entities/product.entity.ts` (3x), `system/core/backend/src/models/filters/order.filter.ts` (3x), `system/core/backend/src/models/filters/product-category.filter.ts` (3x)

### `system/core/backend/src/models/filters/product.filter.ts`
**Imports:** `system/core/backend/src/models/filters/base-filter.filter.ts`
**Symbols:** class:`ProductFilterMeta`, class:`FilteredProduct`, class:`ProductFilterAttributes`, class:`ProductFilterInput`
**Often changes with:** `system/core/backend/src/repositories/product.repository.ts` (4x), `system/core/common/src/types/entities.ts` (4x), `system/core/backend/src/models/entities/order.entity.ts` (3x), `system/core/backend/src/models/entities/post.entity.ts` (3x), `system/core/backend/src/models/entities/product.entity.ts` (3x)

### `system/core/backend/src/models/filters/user.filter.ts`
**Imports:** `system/core/backend/src/models/filters/base-filter.filter.ts`
**Symbols:** class:`UserFilterInput`
**Often changes with:** `system/core/backend/src/models/filters/order.filter.ts` (3x), `system/core/backend/src/models/filters/post.filter.ts` (3x), `system/core/backend/src/models/filters/product-category.filter.ts` (3x), `system/core/backend/src/models/filters/product-review.filter.ts` (3x), `system/core/backend/src/models/filters/product.filter.ts` (3x)

### `system/core/backend/src/models/inputs/attribute.input.ts`
**Imports:** `system/core/backend/src/models/inputs/base-page.input.ts`
**Symbols:** class:`AttributeInput`, class:`AttributeValueInput`

### `system/core/backend/src/models/inputs/base-page.input.ts`
**Imported by:** `system/core/backend/src/models/inputs/attribute.input.ts`, `system/core/backend/src/models/inputs/coupon.input.ts`, `system/core/backend/src/models/inputs/custom-entity.input.ts`, `system/core/backend/src/models/inputs/order.input.ts`, `system/core/backend/src/models/inputs/plugin.input.ts`, `system/core/backend/src/models/inputs/post.create.ts`, `system/core/backend/src/models/inputs/post.update.ts`, `system/core/backend/src/models/inputs/product-category.create.ts`, `system/core/backend/src/models/inputs/product-category.update.ts`, `system/core/backend/src/models/inputs/product-variant.input.ts`
**Symbols:** class:`BasePageMetaInput`, class:`BasePageInput`
**Often changes with:** `system/core/backend/src/models/entities/product.entity.ts` (5x), `system/core/backend/src/models/entities/user.entity.ts` (5x), `system/core/backend/src/models/inputs/order.input.ts` (5x), `system/core/backend/src/models/entities/order.entity.ts` (5x), `system/core/backend/src/models/entities/post.entity.ts` (4x)

### `system/core/backend/src/models/inputs/coupon.input.ts`
**Imports:** `system/core/backend/src/models/inputs/base-page.input.ts`
**Symbols:** class:`CouponInput`

### `system/core/backend/src/models/inputs/custom-entity.input.ts`
**Imports:** `system/core/backend/src/models/inputs/base-page.input.ts`
**Symbols:** class:`CustomEntityInput`

### `system/core/backend/src/models/inputs/delete-many.input.ts`
**Symbols:** class:`DeleteManyInput`
**Often changes with:** `system/core/backend/src/models/entities/product-review.entity.ts` (3x), `system/core/backend/src/models/entities/product.entity.ts` (3x), `system/core/backend/src/models/entities/tag.entity.ts` (3x), `system/core/backend/src/models/entities/user.entity.ts` (3x), `system/core/backend/src/models/inputs/order.input.ts` (3x)

### `system/core/backend/src/models/inputs/order.input.ts`
**Imports:** `system/core/backend/src/models/inputs/base-page.input.ts`
**Symbols:** class:`OrderInput`
**Often changes with:** `system/core/common/src/types/entities.ts` (9x), `system/core/backend/src/models/entities/order.entity.ts` (8x), `system/core/backend/src/repositories/product.repository.ts` (8x), `system/core/backend/src/models/entities/product.entity.ts` (6x), `system/core/backend/src/models/inputs/product.update.ts` (6x)

### `system/core/backend/src/models/inputs/paged-params.input.ts`
**Symbols:** class:`PagedParamsInput`

### `system/core/backend/src/models/inputs/plugin.input.ts`
**Imports:** `system/core/backend/src/models/inputs/base-page.input.ts`
**Symbols:** class:`PluginInput`

### `system/core/backend/src/models/inputs/post.create.ts`
**Imports:** `system/core/backend/src/models/inputs/base-page.input.ts`
**Symbols:** class:`CreatePost`
**Often changes with:** `system/core/backend/src/models/inputs/post.update.ts` (5x), `system/core/backend/src/models/inputs/product.create.ts` (4x), `system/core/backend/src/models/inputs/product.update.ts` (4x), `system/core/backend/src/models/entities/post.entity.ts` (4x), `system/core/backend/src/models/entities/tag.entity.ts` (3x)

### `system/core/backend/src/models/inputs/post.update.ts`
**Imports:** `system/core/backend/src/models/inputs/base-page.input.ts`
**Symbols:** class:`UpdatePost`
**Often changes with:** `system/core/backend/src/models/inputs/post.create.ts` (5x), `system/core/backend/src/models/inputs/product.create.ts` (4x), `system/core/backend/src/models/inputs/product.update.ts` (4x), `system/core/backend/src/repositories/order.repository.ts` (4x), `system/core/backend/src/models/entities/user.entity.ts` (3x)

### `system/core/backend/src/models/inputs/product-category.create.ts`
**Imports:** `system/core/backend/src/models/inputs/base-page.input.ts`
**Symbols:** class:`CreateProductCategory`
**Often changes with:** `system/core/backend/src/models/entities/user.entity.ts` (4x), `system/core/backend/src/models/inputs/order.input.ts` (4x), `system/core/backend/src/models/inputs/product-category.update.ts` (4x), `system/core/backend/src/models/inputs/product.update.ts` (4x), `system/core/backend/src/models/inputs/base-page.input.ts` (3x)

### `system/core/backend/src/models/inputs/product-category.update.ts`
**Imports:** `system/core/backend/src/models/inputs/base-page.input.ts`
**Symbols:** class:`UpdateProductCategory`
**Often changes with:** `system/core/backend/src/models/inputs/order.input.ts` (4x), `system/core/backend/src/models/inputs/product-category.create.ts` (4x), `system/core/backend/src/models/inputs/product.update.ts` (4x), `system/core/backend/src/models/inputs/base-page.input.ts` (3x), `system/core/backend/src/models/inputs/delete-many.input.ts` (3x)

### `system/core/backend/src/models/inputs/product-review.input.ts`
**Symbols:** class:`ProductReviewInput`
**Often changes with:** `system/core/backend/src/models/inputs/delete-many.input.ts` (3x), `system/core/backend/src/models/inputs/order.input.ts` (3x), `system/core/backend/src/models/inputs/post.create.ts` (3x), `system/core/backend/src/models/inputs/post.update.ts` (3x), `system/core/backend/src/models/inputs/product-category.create.ts` (3x)

### `system/core/backend/src/models/inputs/product-variant.input.ts`
**Imports:** `system/core/backend/src/models/inputs/base-page.input.ts`
**Imported by:** `system/core/backend/src/models/inputs/product.create.ts`, `system/core/backend/src/models/inputs/product.update.ts`
**Symbols:** class:`ProductVariantInput`

### `system/core/backend/src/models/inputs/product.create.ts`
**Imports:** `system/core/backend/src/models/inputs/base-page.input.ts`, `system/core/backend/src/models/inputs/product-variant.input.ts`
**Symbols:** class:`CreateProduct`
**Often changes with:** `system/core/backend/src/models/inputs/product.update.ts` (8x), `system/core/backend/src/models/entities/product.entity.ts` (6x), `system/core/backend/src/repositories/product.repository.ts` (6x), `system/core/common/src/types/entities.ts` (6x), `system/core/backend/src/models/inputs/order.input.ts` (4x)

### `system/core/backend/src/models/inputs/product.update.ts`
**Imports:** `system/core/backend/src/models/inputs/base-page.input.ts`, `system/core/backend/src/models/inputs/product-variant.input.ts`
**Symbols:** class:`UpdateProduct`
**Often changes with:** `system/core/backend/src/models/inputs/product.create.ts` (8x), `system/core/backend/src/repositories/product.repository.ts` (8x), `system/core/common/src/types/entities.ts` (8x), `system/core/backend/src/models/entities/product.entity.ts` (7x), `system/core/backend/src/models/inputs/order.input.ts` (6x)

### `system/core/backend/src/models/inputs/role.input.ts`
**Imports:** `system/core/backend/src/models/inputs/base-page.input.ts`
**Symbols:** class:`RoleInput`

### `system/core/backend/src/models/inputs/tag.input.ts`
**Imports:** `system/core/backend/src/models/inputs/base-page.input.ts`
**Symbols:** class:`TagInput`
**Often changes with:** `system/core/backend/src/models/inputs/user.create.ts` (3x), `system/core/backend/src/models/inputs/user.update.ts` (3x)

### `system/core/backend/src/models/inputs/user.create.ts`
**Imports:** `system/core/backend/src/models/inputs/base-page.input.ts`
**Symbols:** class:`CreateUser`
**Often changes with:** `system/core/backend/src/models/inputs/tag.input.ts` (3x), `system/core/backend/src/models/inputs/user.update.ts` (3x)

### `system/core/backend/src/models/inputs/user.update.ts`
**Imports:** `system/core/backend/src/models/inputs/base-page.input.ts`
**Symbols:** class:`UpdateUser`
**Often changes with:** `system/core/backend/src/models/inputs/tag.input.ts` (3x), `system/core/backend/src/models/inputs/user.create.ts` (3x)

### `system/core/backend/src/models/objects/attribute-instance.object.ts`
**Symbols:** class:`AttributeInstanceValue`, class:`AttributeInstance`
**Often changes with:** `system/core/backend/src/models/inputs/product.create.ts` (3x), `system/core/backend/src/models/inputs/product.update.ts` (3x), `system/core/backend/src/repositories/attribute.repository.ts` (3x)

### `system/core/backend/src/models/objects/custom-date.scalar.ts`
**Often changes with:** `system/core/backend/src/models/inputs/product.create.ts` (3x), `system/core/backend/src/models/inputs/product.update.ts` (3x)

### `system/core/backend/src/models/objects/stringified-value.scalar.ts`
**Symbols:** const_fn:`parseStringifiedValue`

### `system/core/backend/src/models/paged/attribute.paged.ts`
**Imports:** `system/core/backend/src/models/paged/meta.paged.ts`
**Symbols:** class:`PagedAttribute`

### `system/core/backend/src/models/paged/coupon.paged.ts`
**Imports:** `system/core/backend/src/models/paged/meta.paged.ts`
**Symbols:** class:`PagedCoupon`

### `system/core/backend/src/models/paged/custom-entity.paged.ts`
**Imports:** `system/core/backend/src/models/paged/meta.paged.ts`
**Symbols:** class:`PagedCustomEntity`

### `system/core/backend/src/models/paged/meta.paged.ts`
**Imported by:** `system/core/backend/src/models/paged/attribute.paged.ts`, `system/core/backend/src/models/paged/coupon.paged.ts`, `system/core/backend/src/models/paged/custom-entity.paged.ts`, `system/core/backend/src/models/paged/order.paged.ts`, `system/core/backend/src/models/paged/post.paged.ts`, `system/core/backend/src/models/paged/product-category.paged.ts`, `system/core/backend/src/models/paged/product-review.paged.ts`, `system/core/backend/src/models/paged/product.paged.ts`, `system/core/backend/src/models/paged/role.paged.ts`, `system/core/backend/src/models/paged/tag.paged.ts`
**Symbols:** class:`PagedMeta`
**Often changes with:** `system/core/backend/src/models/inputs/post.create.ts` (3x), `system/core/backend/src/models/inputs/post.update.ts` (3x), `system/core/backend/src/models/inputs/product-category.create.ts` (3x), `system/core/backend/src/models/inputs/product-category.update.ts` (3x), `system/core/backend/src/models/inputs/product-review.input.ts` (3x)

### `system/core/backend/src/models/paged/order.paged.ts`
**Imports:** `system/core/backend/src/models/paged/meta.paged.ts`
**Symbols:** class:`PagedOrder`

### `system/core/backend/src/models/paged/post.paged.ts`
**Imports:** `system/core/backend/src/models/paged/meta.paged.ts`
**Symbols:** class:`PagedPost`

### `system/core/backend/src/models/paged/product-category.paged.ts`
**Imports:** `system/core/backend/src/models/paged/meta.paged.ts`
**Symbols:** class:`PagedProductCategory`

### `system/core/backend/src/models/paged/product-review.paged.ts`
**Imports:** `system/core/backend/src/models/paged/meta.paged.ts`
**Symbols:** class:`PagedProductReview`

### `system/core/backend/src/models/paged/product.paged.ts`
**Imports:** `system/core/backend/src/models/paged/meta.paged.ts`
**Symbols:** class:`PagedProduct`

### `system/core/backend/src/models/paged/role.paged.ts`
**Imports:** `system/core/backend/src/models/paged/meta.paged.ts`
**Symbols:** class:`PagedRole`

### `system/core/backend/src/models/paged/tag.paged.ts`
**Imports:** `system/core/backend/src/models/paged/meta.paged.ts`
**Symbols:** class:`PagedTag`

### `system/core/backend/src/models/paged/user.paged.ts`
**Imports:** `system/core/backend/src/models/paged/meta.paged.ts`
**Symbols:** class:`PagedUser`

### `system/core/backend/src/repositories/attribute.repository.ts`
**Imports:** `system/core/backend/src/helpers/base-queries.ts`, `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/repositories/base.repository.ts`
**Imported by:** `system/core/backend/src/repositories/product.repository.ts`
**Symbols:** class:`AttributeRepository`
**Often changes with:** `system/core/backend/src/repositories/product.repository.ts` (11x), `system/core/backend/src/repositories/tag.repository.ts` (11x), `system/core/backend/src/repositories/user.repository.ts` (11x), `system/core/backend/src/repositories/product-review.repository.ts` (10x), `system/core/backend/src/repositories/order.repository.ts` (9x)

### `system/core/backend/src/repositories/base.repository.ts`
**Imports:** `system/core/backend/src/helpers/base-queries.ts`, `system/core/backend/src/helpers/entity-meta.ts`, `system/core/backend/src/helpers/logger.ts`
**Imported by:** `system/core/backend/src/repositories/attribute.repository.ts`, `system/core/backend/src/repositories/coupon.repository.ts`, `system/core/backend/src/repositories/custom-entity.repository.ts`, `system/core/backend/src/repositories/order.repository.ts`, `system/core/backend/src/repositories/page-stats.repository.ts`, `system/core/backend/src/repositories/plugin.repository.ts`, `system/core/backend/src/repositories/post.repository.ts`, `system/core/backend/src/repositories/product-review.repository.ts`, `system/core/backend/src/repositories/product-variant.repository.ts`, `system/core/backend/src/repositories/product.repository.ts`
**Symbols:** class:`BaseRepository`
**Often changes with:** `system/core/backend/src/repositories/product.repository.ts` (13x), `system/core/backend/src/repositories/post.repository.ts` (11x), `system/core/backend/src/repositories/product-category.repository.ts` (11x), `system/core/backend/src/repositories/order.repository.ts` (10x), `system/core/backend/src/repositories/user.repository.ts` (10x)

### `system/core/backend/src/repositories/coupon.repository.ts`
**Imports:** `system/core/backend/src/helpers/base-queries.ts`, `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/repositories/base.repository.ts`
**Imported by:** `system/core/backend/src/repositories/order.repository.ts`
**Symbols:** class:`CouponRepository`
**Often changes with:** `system/core/backend/src/repositories/base.repository.ts` (5x), `system/core/backend/src/repositories/order.repository.ts` (5x), `system/core/backend/src/repositories/product.repository.ts` (5x), `system/core/backend/src/repositories/attribute.repository.ts` (4x), `system/core/backend/src/repositories/custom-entity.repository.ts` (4x)

### `system/core/backend/src/repositories/custom-entity.repository.ts`
**Imports:** `system/core/backend/src/helpers/base-queries.ts`, `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/repositories/base.repository.ts`
**Symbols:** class:`CustomEntityRepository`
**Often changes with:** `system/core/backend/src/repositories/product.repository.ts` (9x), `system/core/backend/src/repositories/post.repository.ts` (8x), `system/core/backend/src/repositories/attribute.repository.ts` (7x), `system/core/backend/src/repositories/product-review.repository.ts` (7x), `system/core/backend/src/repositories/tag.repository.ts` (7x)

### `system/core/backend/src/repositories/order.repository.ts`
**Imports:** `system/core/backend/src/helpers/base-queries.ts`, `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/helpers/validation.ts`, `system/core/backend/src/repositories/base.repository.ts`, `system/core/backend/src/repositories/coupon.repository.ts`
**Symbols:** class:`OrderRepository`
**Often changes with:** `system/core/backend/src/repositories/product.repository.ts` (13x), `system/core/backend/src/repositories/post.repository.ts` (12x), `system/core/backend/src/repositories/product-category.repository.ts` (12x), `system/core/backend/src/repositories/user.repository.ts` (12x), `system/core/backend/src/repositories/product-review.repository.ts` (11x)

### `system/core/backend/src/repositories/page-stats.repository.ts`
**Imports:** `system/core/backend/src/repositories/base.repository.ts`
**Symbols:** class:`PageStatsRepository`

### `system/core/backend/src/repositories/plugin.repository.ts`
**Imports:** `system/core/backend/src/helpers/base-queries.ts`, `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/repositories/base.repository.ts`
**Symbols:** class:`PluginRepository`
**Often changes with:** `system/core/backend/src/repositories/attribute.repository.ts` (8x), `system/core/backend/src/repositories/base.repository.ts` (8x), `system/core/backend/src/repositories/order.repository.ts` (8x), `system/core/backend/src/repositories/post.repository.ts` (8x), `system/core/backend/src/repositories/product-category.repository.ts` (8x)

### `system/core/backend/src/repositories/post.repository.ts`
**Imports:** `system/core/backend/src/helpers/base-queries.ts`, `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/repositories/base.repository.ts`, `system/core/backend/src/repositories/tag.repository.ts`, `system/core/backend/src/repositories/user.repository.ts`
**Symbols:** class:`PostRepository`
**Often changes with:** `system/core/backend/src/repositories/product.repository.ts` (15x), `system/core/backend/src/repositories/user.repository.ts` (14x), `system/core/backend/src/repositories/product-category.repository.ts` (13x), `system/core/backend/src/repositories/order.repository.ts` (12x), `system/core/backend/src/repositories/product-review.repository.ts` (12x)

### `system/core/backend/src/repositories/product-category.repository.ts`
**Imports:** `system/core/backend/src/helpers/entity-meta.ts`, `system/core/backend/src/helpers/logger.ts`, `system/cli/src/tasks/create.ts`, `system/core/backend/src/repositories/product.repository.ts`
**Imported by:** `system/core/backend/src/repositories/product.repository.ts`
**Symbols:** class:`ProductCategoryRepository`
**Often changes with:** `system/core/common/src/types/entities.ts` (13x), `system/core/backend/src/repositories/post.repository.ts` (13x), `system/core/backend/src/repositories/product.repository.ts` (13x), `system/core/backend/src/repositories/user.repository.ts` (13x), `system/core/backend/src/repositories/order.repository.ts` (12x)

### `system/core/backend/src/repositories/product-review.repository.ts`
**Imports:** `system/core/backend/src/helpers/base-queries.ts`, `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/repositories/base.repository.ts`, `system/core/backend/src/repositories/product.repository.ts`
**Imported by:** `system/core/backend/src/repositories/product.repository.ts`
**Symbols:** class:`ProductReviewRepository`
**Often changes with:** `system/core/backend/src/repositories/user.repository.ts` (13x), `system/core/backend/src/repositories/post.repository.ts` (12x), `system/core/backend/src/repositories/product.repository.ts` (12x), `system/core/backend/src/repositories/order.repository.ts` (11x), `system/core/backend/src/repositories/product-category.repository.ts` (11x)

### `system/core/backend/src/repositories/product-variant.repository.ts`
**Imports:** `system/core/backend/src/helpers/base-queries.ts`, `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/repositories/base.repository.ts`, `system/core/backend/src/repositories/product.repository.ts`
**Imported by:** `system/core/backend/src/repositories/product.repository.ts`
**Symbols:** class:`ProductVariantRepository`, const_fn:`updatedVariants`
**Often changes with:** `system/core/backend/src/repositories/product.repository.ts` (5x), `system/core/backend/src/repositories/attribute.repository.ts` (4x), `system/core/backend/src/repositories/base.repository.ts` (4x), `system/core/backend/src/repositories/coupon.repository.ts` (4x), `system/core/backend/src/repositories/custom-entity.repository.ts` (4x)

### `system/core/backend/src/repositories/product.repository.ts`
**Imports:** `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/repositories/attribute.repository.ts`, `system/core/backend/src/repositories/base.repository.ts`, `system/core/backend/src/repositories/product-category.repository.ts`, `system/core/backend/src/repositories/product-review.repository.ts`, `system/core/backend/src/repositories/product-variant.repository.ts`
**Imported by:** `system/core/backend/src/repositories/product-category.repository.ts`, `system/core/backend/src/repositories/product-review.repository.ts`, `system/core/backend/src/repositories/product-variant.repository.ts`
**Symbols:** class:`ProductRepository`
**Often changes with:** `system/core/common/src/types/entities.ts` (19x), `system/core/backend/src/repositories/post.repository.ts` (15x), `system/server/src/services/migration.service.ts` (15x), `system/core/backend/src/repositories/base.repository.ts` (13x), `system/core/backend/src/repositories/order.repository.ts` (13x)

### `system/core/backend/src/repositories/role.repository.ts`
**Imports:** `system/core/backend/src/helpers/auth-roles-permissions.ts`, `system/core/backend/src/helpers/base-queries.ts`, `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/repositories/base.repository.ts`
**Imported by:** `system/core/backend/src/repositories/user.repository.ts`
**Symbols:** class:`RoleRepository`
**Often changes with:** `system/core/backend/src/repositories/user.repository.ts` (5x), `system/server/src/controllers/cms.controller.ts` (5x), `system/core/backend/src/_index.ts` (4x), `system/core/common/src/types/entities.ts` (4x), `system/core/backend/src/helpers/types.ts` (3x)

### `system/core/backend/src/repositories/tag.repository.ts`
**Imports:** `system/core/backend/src/helpers/base-queries.ts`, `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/repositories/base.repository.ts`
**Imported by:** `system/core/backend/src/repositories/post.repository.ts`
**Symbols:** class:`TagRepository`
**Often changes with:** `system/core/backend/src/repositories/attribute.repository.ts` (11x), `system/core/backend/src/repositories/product-review.repository.ts` (10x), `system/core/backend/src/repositories/product.repository.ts` (10x), `system/core/backend/src/repositories/user.repository.ts` (10x), `system/core/backend/src/repositories/order.repository.ts` (9x)

### `system/core/backend/src/repositories/user.repository.ts`
**Imports:** `system/core/backend/src/helpers/auth-settings.ts`, `themes/store/src/constants.js`, `system/core/backend/src/helpers/base-queries.ts`, `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/helpers/validation.ts`, `system/core/backend/src/repositories/base.repository.ts`, `system/core/backend/src/repositories/role.repository.ts`
**Imported by:** `system/core/backend/src/repositories/post.repository.ts`
**Symbols:** class:`UserRepository`
**Often changes with:** `system/core/backend/src/repositories/post.repository.ts` (14x), `system/core/common/src/types/entities.ts` (14x), `system/core/backend/src/repositories/product-category.repository.ts` (13x), `system/core/backend/src/repositories/product-review.repository.ts` (13x), `system/core/backend/src/repositories/product.repository.ts` (13x)

### `system/core/backend/tests/helpers.ts`
**Feature:** Testing
**Imports:** `themes/store/src/constants.js`
**Imported by:** `system/core/backend/tests/teardown.ts`
**Symbols:** const_fn:`mockWorkingDirectory`, const_fn:`connectDatabase`, const_fn:`clearTestDir`
**Often changes with:** `system/core/backend/tests/helpers/paths.test.ts` (4x), `system/core/backend/tests/helpers/emailing.test.ts` (3x), `system/core/backend/jest.config.ts` (3x), `system/manager/src/managers/baseManager.ts` (3x)

### `system/core/backend/tests/helpers/actions.test.ts`
**Feature:** Utilities
**Imports:** `toolkits/commerce/src/base/Checkout/actions.ts`

### `system/core/backend/tests/helpers/auth-guards.test.ts`
**Feature:** Utilities
**Imports:** `themes/store/src/types.ts`, `system/core/backend/src/helpers/auth-guards.ts`
**Symbols:** const_fn:`test`, const_fn:`test`
**Often changes with:** `system/core/backend/src/repositories/user.repository.ts` (4x), `system/core/backend/src/repositories/base.repository.ts` (3x), `system/core/backend/src/repositories/product.repository.ts` (3x), `system/core/backend/src/repositories/role.repository.ts` (3x), `system/server/src/services/cms.service.ts` (3x)

### `system/core/backend/tests/helpers/base-queries.test.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/base-queries.ts`

### `system/core/backend/tests/helpers/cms-modules.test.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/cms-modules.ts`, `toolkits/commerce/tests/helpers.ts`

### `system/core/backend/tests/helpers/cms-settings.test.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/cms-settings.ts`, `themes/store/src/constants.js`, `toolkits/commerce/tests/helpers.ts`
**Often changes with:** `system/core/backend/src/helpers/constants.ts` (4x), `system/core/backend/src/helpers/paths.ts` (4x), `system/core/common/src/types/data.ts` (4x), `system/manager/src/managers/baseManager.ts` (4x), `system/renderer/src/generator.ts` (4x)

### `system/core/backend/tests/helpers/create-generic-entity.test.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/create-generic-entity.ts`

### `system/core/backend/tests/helpers/emailing.test.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/emailing.ts`, `system/core/backend/src/helpers/paths.ts`, `toolkits/commerce/tests/helpers.ts`
**Often changes with:** `system/core/backend/tests/helpers.ts` (3x), `system/core/backend/tests/helpers/paths.test.ts` (3x)

### `system/core/backend/tests/helpers/logger.test.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/helpers/paths.ts`, `toolkits/commerce/tests/helpers.ts`

### `system/core/backend/tests/helpers/paths.test.ts`
**Feature:** Utilities
**Imports:** `toolkits/commerce/tests/helpers.ts`
**Often changes with:** `system/core/backend/tests/helpers.ts` (4x), `system/core/backend/tests/helpers/emailing.test.ts` (3x)

### `system/core/backend/tests/helpers/plugin-exports.test.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/plugin-exports.ts`, `toolkits/commerce/tests/helpers.ts`

### `system/core/backend/tests/helpers/plugin-settings.test.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/plugin-settings.ts`, `toolkits/commerce/tests/helpers.ts`

### `system/core/backend/tests/helpers/service-versions.test.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/service-versions.ts`, `toolkits/commerce/tests/helpers.ts`

### `system/core/backend/tests/helpers/theme-config.test.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/theme-config.ts`, `system/core/backend/src/helpers/cms-settings.ts`, `toolkits/commerce/tests/helpers.ts`

### `system/core/backend/tests/helpers/validation.test.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/validation.ts`

### `system/core/backend/tests/setup.ts`
**Feature:** Testing
**Often changes with:** `system/core/backend/src/helpers/paths.ts` (4x), `system/manager/src/managers/baseManager.ts` (4x), `system/core/backend/src/helpers/constants.ts` (3x), `system/core/backend/tests/helpers/cms-settings.test.ts` (3x), `system/core/frontend/src/api/CGraphQLClient.ts` (3x)

### `system/core/backend/tests/teardown.ts`
**Feature:** Testing
**Imports:** `system/core/backend/tests/helpers.ts`

### `system/core/common/.eslintrc.js`
**Feature:** Shared Code
**Often changes with:** `system/core/frontend/.eslintrc.js` (3x)

### `system/core/common/rollup.config.js`
**Feature:** Shared Code
**Symbols:** const_fn:`external`, const_fn:`getOutput`, const_fn:`getPlugins`
**Often changes with:** `system/core/frontend/rollup.config.js` (12x), `system/core/backend/rollup.config.js` (9x), `system/manager/rollup.config.js` (6x), `system/renderer/rollup.config.js` (6x), `system/core/frontend/src/components/CImage/CImage.tsx` (5x)

### `system/core/common/src/_index.ts`
**Often changes with:** `system/core/common/src/types/blocks.ts` (4x), `system/core/common/src/types/data.ts` (3x), `system/server/src/controllers/cms.controller.ts` (3x)

### `system/core/common/src/auth.ts`
**Imports:** `system/core/common/src/types/data.ts`, `system/core/common/src/types/entities.ts`
**Imported by:** `plugins/newsletter/src/backend/controllers/plugin-newsletter.controller.ts`, `plugins/newsletter/src/backend/resolvers/plugin-newsletter.resolver.ts`
**Symbols:** const_fn:`matchPermissions`
**Often changes with:** `system/core/common/src/constants.ts` (3x), `system/core/common/src/types/data.ts` (3x), `system/core/common/src/types/entities.ts` (3x), `system/core/frontend/src/api/CGraphQLClient.ts` (3x)

### `system/core/common/src/constants.ts`
**Imports:** `system/core/common/src/types/data.ts`, `system/core/common/src/types/entities.ts`
**Symbols:** const_fn:`nodeRequire`
**Often changes with:** `system/core/common/src/types/data.ts` (38x), `system/core/frontend/src/api/CGraphQLClient.ts` (38x), `system/core/common/src/types/entities.ts` (35x), `system/manager/src/managers/rendererManager.ts` (14x), `system/server/src/controllers/cms.controller.ts` (13x)

### `system/core/common/src/global-store.ts`
**Imports:** `system/core/common/src/helpers.ts`, `system/core/common/src/types/blocks.ts`, `system/core/common/src/types/data.ts`, `system/core/common/src/types/entities.ts`
**Imported by:** `system/core/common/src/helpers.ts`, `system/core/common/src/redirects.ts`, `system/core/common/src/service-locator.ts`
**Symbols:** const_fn:`getStore`, const_fn:`getPageCustomConfig`, const_fn:`getCmsSettings`, const_fn:`getThemeCustomConfig`, const_fn:`getThemeCustomConfigProp`, const_fn:`getProp`, const_fn:`registerRedirect`, const_fn:`registerRewrite`
**Often changes with:** `system/core/common/src/constants.ts` (5x), `system/core/common/src/helpers.ts` (5x), `system/core/common/src/types/data.ts` (5x), `system/core/frontend/src/_index.ts` (5x), `system/core/common/src/types/entities.ts` (4x)

### `system/core/common/src/helpers.ts`
**Imports:** `system/core/common/src/global-store.ts`, `system/core/common/src/types/data.ts`
**Imported by:** `system/core/common/src/global-store.ts`, `system/core/common/src/service-locator.ts`
**Symbols:** const_fn:`isServer`, const_fn:`getRandStr`, const_fn:`sleep`, const_fn:`resolvePageRoute`, const_fn:`processArray`
**Often changes with:** `system/core/common/src/types/data.ts` (6x), `system/core/common/src/types/entities.ts` (6x), `system/core/common/src/global-store.ts` (5x), `system/core/frontend/src/api/CGraphQLClient.ts` (4x), `system/core/common/src/constants.ts` (4x)

### `system/core/common/src/redirects.ts`
**Imports:** `system/core/common/src/global-store.ts`, `system/core/common/src/types/entities.ts`
**Symbols:** const_fn:`findRedirect`

### `system/core/common/src/service-locator.ts`
**Imports:** `system/core/common/src/global-store.ts`, `system/core/common/src/helpers.ts`, `system/core/common/src/types/data.ts`
**Symbols:** const_fn:`getBaseUrl`, const_fn:`url`
**Often changes with:** `system/core/common/src/types/data.ts` (4x), `system/core/frontend/src/api/CGraphQLClient.ts` (4x), `system/core/common/src/constants.ts` (3x)

### `system/core/common/src/types/blocks.ts`
**Imports:** `system/core/common/src/types/data.ts`, `system/renderer/src/helpers/document.tsx`
**Imported by:** `system/core/common/src/global-store.ts`, `system/core/common/src/types/data.ts`
**Often changes with:** `system/core/common/src/types/data.ts` (32x), `system/core/frontend/src/api/CGraphQLClient.ts` (22x), `system/core/common/src/types/entities.ts` (20x), `system/core/frontend/src/components/CPlugin/CPlugin.tsx` (20x), `system/core/frontend/src/components/CGallery/CGallery.tsx` (16x)

### `system/core/common/src/types/data.ts`
**Imports:** `themes/store/src/constants.js`, `system/core/common/src/types/blocks.ts`
**Imported by:** `system/core/common/src/auth.ts`, `system/core/common/src/constants.ts`, `system/core/common/src/global-store.ts`, `system/core/common/src/helpers.ts`, `system/core/common/src/service-locator.ts`, `system/core/common/src/types/blocks.ts`, `system/core/common/src/types/entities.ts`
**Often changes with:** `system/core/common/src/types/entities.ts` (51x), `system/core/frontend/src/api/CGraphQLClient.ts` (39x), `system/core/common/src/constants.ts` (38x), `system/server/src/controllers/cms.controller.ts` (35x), `system/core/backend/src/helpers/paths.ts` (33x)

### `system/core/common/src/types/entities.ts`
**Imports:** `system/core/common/src/types/data.ts`
**Imported by:** `system/core/common/src/auth.ts`, `system/core/common/src/constants.ts`, `system/core/common/src/global-store.ts`, `system/core/common/src/redirects.ts`
**Often changes with:** `system/core/frontend/src/api/CGraphQLClient.ts` (55x), `system/core/common/src/types/data.ts` (51x), `system/server/src/controllers/cms.controller.ts` (40x), `system/core/common/src/constants.ts` (35x), `system/server/src/services/cms.service.ts` (33x)

### `system/core/frontend/.eslintrc.js`
**Often changes with:** `system/core/common/src/types/data.ts` (4x), `system/core/frontend/src/components/CList/CList.tsx` (3x), `system/core/common/.eslintrc.js` (3x), `system/core/common/src/types/blocks.ts` (3x), `system/core/frontend/src/components/CPlugin/CPlugin.tsx` (3x)

### `system/core/frontend/jest.config.ts`
**Imports:** `themes/store/src/types.ts`
**Often changes with:** `system/core/common/src/constants.ts` (4x), `system/core/common/src/types/data.ts` (3x)

### `system/core/frontend/rollup.config.js`
**Symbols:** const_fn:`external`, const_fn:`getOutput`, const_fn:`getPlugins`
**Often changes with:** `system/core/common/rollup.config.js` (12x), `system/core/backend/rollup.config.js` (8x), `system/renderer/rollup.config.js` (8x), `system/core/common/src/types/data.ts` (7x), `system/manager/rollup.config.js` (7x)

### `system/core/frontend/src/_index.ts`
**Often changes with:** `system/core/common/src/types/blocks.ts` (9x), `system/core/frontend/src/api/CRestApiClient.ts` (7x), `system/core/frontend/src/components/CGallery/CGallery.tsx` (7x), `system/server/src/services/cms.service.ts` (7x), `system/core/common/src/types/data.ts` (6x)

### `system/core/frontend/src/api/CGraphQLClient.ts`
**Feature:** API Layer
**Imports:** `system/core/frontend/src/helpers/getServiceSecret.ts`, `system/core/frontend/src/helpers/isomorphicFetch.ts`
**Imported by:** `system/core/frontend/src/helpers/CStore.ts`
**Symbols:** const_fn:`getGraphQLErrorInfo`, class:`CGraphQLClient`
**Often changes with:** `system/core/common/src/types/entities.ts` (55x), `system/core/common/src/types/data.ts` (39x), `system/core/common/src/constants.ts` (38x), `system/server/src/controllers/cms.controller.ts` (29x), `system/server/src/services/cms.service.ts` (24x)

### `system/core/frontend/src/api/CRestApiClient.ts`
**Feature:** API Layer
**Imports:** `system/core/frontend/src/helpers/getServiceSecret.ts`, `system/core/frontend/src/helpers/isomorphicFetch.ts`
**Imported by:** `system/admin/src/startup/server.ts`, `system/core/frontend/src/api/CentralServerClient.ts`, `system/core/frontend/src/components/CPlugin/CPlugin.tsx`, `system/core/frontend/src/helpers/AuthClient.ts`, `system/manager/src/managers/baseManager.ts`, `system/manager/src/managers/rendererManager.ts`, `system/renderer/src/generator.ts`, `system/utils/src/static.ts`
**Symbols:** class:`CRestApiClient`, const_fn:`getCookie`
**Often changes with:** `system/core/common/src/types/data.ts` (13x), `system/server/src/controllers/cms.controller.ts` (11x), `system/core/common/src/types/entities.ts` (10x), `system/core/frontend/src/api/CGraphQLClient.ts` (10x), `system/server/src/services/cms.service.ts` (10x)

### `system/core/frontend/src/api/CWebSocketClient.ts`
**Feature:** API Layer
**Symbols:** class:`CWebSocketClient`, const_fn:`getWebSocketClient`
**Often changes with:** `system/core/common/src/constants.ts` (4x), `system/core/common/src/types/data.ts` (4x), `system/core/frontend/src/api/CGraphQLClient.ts` (4x), `system/core/common/src/types/blocks.ts` (3x), `system/core/backend/src/helpers/constants.ts` (3x)

### `system/core/frontend/src/api/CentralServerClient.ts`
**Feature:** API Layer
**Imports:** `system/core/frontend/src/helpers/isomorphicFetch.ts`, `system/core/frontend/src/api/CRestApiClient.ts`
**Symbols:** class:`CentralServerClient`, const_fn:`getCentralServerClient`
**Often changes with:** `system/core/common/src/types/data.ts` (7x), `system/core/common/src/types/entities.ts` (6x), `system/core/common/src/constants.ts` (5x), `system/core/frontend/src/api/CGraphQLClient.ts` (5x), `system/renderer/src/generator.ts` (5x)

### `system/core/frontend/src/components/AdminPanelWidget/AdminPanelWidgetPlace.test.tsx`
**Feature:** Administration
**Imports:** `system/core/frontend/src/components/AdminPanelWidget/AdminPanelWidgetPlace.tsx`, `system/core/frontend/src/helpers/registerWidget.ts`

### `system/core/frontend/src/components/AdminPanelWidget/AdminPanelWidgetPlace.tsx`
**Feature:** Administration
**Imports:** `system/core/frontend/src/widget-types.ts`, `system/core/frontend/src/helpers/registerWidget.ts`, `system/core/frontend/src/components/AdminPanelWidget/WidgetErrorBoundary.tsx`, `themes/store/src/helpers/forceUpdate.ts`
**Imported by:** `system/core/frontend/src/components/AdminPanelWidget/AdminPanelWidgetPlace.test.tsx`
**Often changes with:** `system/core/common/src/types/blocks.ts` (3x)

### `system/core/frontend/src/components/AdminPanelWidget/WidgetErrorBoundary.tsx`
**Feature:** Administration
**Imported by:** `system/admin/src/hooks/useDashboard.tsx`, `system/core/frontend/src/components/AdminPanelWidget/AdminPanelWidgetPlace.tsx`
**Symbols:** class:`WidgetErrorBoundary`
**Often changes with:** `system/core/common/src/types/blocks.ts` (4x), `system/core/frontend/src/components/CGallery/CGallery.tsx` (4x), `system/core/frontend/src/api/CGraphQLClient.ts` (3x), `system/core/frontend/src/components/CContainer/CContainer.tsx` (3x), `system/core/frontend/src/components/CHTML/CHTML.tsx` (3x)

### `system/core/frontend/src/components/BaseElements/BaseButton.tsx`
**Imported by:** `system/core/frontend/src/components/SignIn/SignIn.tsx`, `system/core/frontend/src/components/SignUp/SignUp.tsx`

### `system/core/frontend/src/components/BaseElements/BaseTextField.tsx`
**Imported by:** `system/core/frontend/src/components/SignIn/SignIn.tsx`, `system/core/frontend/src/components/SignUp/SignUp.tsx`

### `system/core/frontend/src/components/CBlock/CBlock.test.tsx`
**Imports:** `system/core/frontend/src/components/CBlock/CBlock.tsx`

### `system/core/frontend/src/components/CBlock/CBlock.tsx`
**Imports:** `system/core/frontend/src/components/CContainer/CContainer.tsx`, `system/core/frontend/src/components/CEditor/CEditor.tsx`, `system/core/frontend/src/components/CGallery/CGallery.tsx`, `system/core/frontend/src/components/CHTML/CHTML.tsx`, `system/core/frontend/src/components/CImage/CImage.tsx`, `system/core/frontend/src/components/CPlugin/CPlugin.tsx`, `system/core/frontend/src/components/CText/CText.tsx`
**Imported by:** `system/core/frontend/src/components/CBlock/CBlock.test.tsx`, `system/core/frontend/src/components/CContainer/CContainer.tsx`, `system/core/frontend/src/components/CEditor/CEditor.tsx`, `system/core/frontend/src/components/CGallery/CGallery.tsx`, `system/core/frontend/src/components/CHTML/CHTML.tsx`, `system/core/frontend/src/components/CImage/CImage.tsx`, `system/core/frontend/src/components/CList/CList.tsx`, `system/core/frontend/src/components/CPlugin/CPlugin.tsx`, `system/core/frontend/src/components/CText/CText.tsx`
**Symbols:** class:`CBlock`
**Often changes with:** `system/core/common/src/types/blocks.ts` (5x), `system/core/frontend/src/api/CGraphQLClient.ts` (4x), `system/core/frontend/src/_index.ts` (4x), `system/core/frontend/src/components/CEditor/CEditor.tsx` (3x), `system/core/frontend/src/components/CGallery/CGallery.tsx` (3x)

### `system/core/frontend/src/components/CContainer/CContainer.test.tsx`
**Imports:** `system/core/frontend/src/components/CContainer/CContainer.tsx`

### `system/core/frontend/src/components/CContainer/CContainer.tsx`
**Imports:** `system/core/frontend/src/components/CBlock/CBlock.tsx`
**Imported by:** `system/core/frontend/src/components/CBlock/CBlock.tsx`, `system/core/frontend/src/components/CContainer/CContainer.test.tsx`
**Symbols:** class:`CContainer`
**Often changes with:** `system/core/frontend/src/components/CHTML/CHTML.tsx` (8x), `system/core/frontend/src/components/CImage/CImage.tsx` (8x), `system/core/frontend/src/components/CPlugin/CPlugin.tsx` (8x), `system/core/frontend/src/components/CText/CText.tsx` (8x), `system/core/frontend/src/components/CGallery/CGallery.tsx` (7x)

### `system/core/frontend/src/components/CEditor/CEditor.test.tsx`
**Imports:** `system/core/frontend/src/components/CEditor/CEditor.tsx`

### `system/core/frontend/src/components/CEditor/CEditor.tsx`
**Imports:** `system/core/frontend/src/helpers/parserTransform.tsx`, `system/core/frontend/src/components/CBlock/CBlock.tsx`
**Imported by:** `system/core/frontend/src/components/CBlock/CBlock.tsx`, `system/core/frontend/src/components/CEditor/CEditor.test.tsx`
**Symbols:** class:`CEditor`
**Often changes with:** `system/core/frontend/src/components/CBlock/CBlock.tsx` (3x), `system/core/frontend/src/components/CGallery/CGallery.tsx` (3x), `system/core/frontend/src/components/CHTML/CHTML.tsx` (3x)

### `system/core/frontend/src/components/CGallery/CGallery.test.tsx`
**Imports:** `system/core/frontend/src/components/CGallery/CGallery.tsx`
**Often changes with:** `system/core/frontend/src/components/CGallery/CGallery.tsx` (3x)

### `system/core/frontend/src/components/CGallery/CGallery.tsx`
**Imports:** `system/core/frontend/src/components/CBlock/CBlock.tsx`, `system/core/frontend/src/components/Link/Link.tsx`, `system/core/frontend/src/components/CGallery/Lightbox.tsx`, `system/core/frontend/src/components/CGallery/Thumbs.tsx`
**Imported by:** `system/core/frontend/src/components/CBlock/CBlock.tsx`, `system/core/frontend/src/components/CGallery/CGallery.test.tsx`, `system/core/frontend/src/components/CGallery/Thumbs.tsx`
**Symbols:** class:`CarouselStoreSetterRaw`, class:`CGallery`, const_fn:`Image`, const_fn:`galleryJsx`, const_fn:`imgItem`
**Often changes with:** `system/core/common/src/types/blocks.ts` (16x), `system/core/common/src/types/data.ts` (11x), `system/core/frontend/src/components/CList/CList.tsx` (11x), `system/core/frontend/src/components/CImage/CImage.tsx` (10x), `system/core/frontend/src/api/CGraphQLClient.ts` (9x)

### `system/core/frontend/src/components/CGallery/Lightbox.tsx`
**Imported by:** `system/core/frontend/src/components/CGallery/CGallery.tsx`
**Symbols:** class:`Lightbox`
**Often changes with:** `system/core/frontend/src/components/CGallery/CGallery.tsx` (4x), `system/core/frontend/src/components/CList/CList.tsx` (3x), `system/core/frontend/src/components/CText/CText.tsx` (3x), `system/core/frontend/src/components/CGallery/Thumbs.tsx` (3x)

### `system/core/frontend/src/components/CGallery/Thumbs.tsx`
**Imports:** `system/core/frontend/src/helpers/thumbs.ts`, `system/core/frontend/src/components/CGallery/CGallery.tsx`
**Imported by:** `system/core/frontend/src/components/CGallery/CGallery.tsx`
**Symbols:** class:`Thumbs`, const_fn:`thumbDesiredWidth`, const_fn:`thumbvisibleSlides`
**Often changes with:** `system/core/frontend/src/components/CGallery/CGallery.tsx` (5x), `system/core/frontend/src/api/CentralServerClient.ts` (3x), `system/core/frontend/src/components/CGallery/Lightbox.tsx` (3x)

### `system/core/frontend/src/components/CHTML/CHTML.test.tsx`
**Imports:** `system/core/frontend/src/components/CHTML/CHTML.tsx`
**Often changes with:** `system/core/frontend/src/components/CGallery/CGallery.tsx` (3x), `system/core/frontend/src/components/CImage/CImage.tsx` (3x)

### `system/core/frontend/src/components/CHTML/CHTML.tsx`
**Imports:** `system/core/frontend/src/helpers/parserTransform.tsx`, `system/core/frontend/src/components/CBlock/CBlock.tsx`
**Imported by:** `system/core/frontend/src/components/CBlock/CBlock.tsx`, `system/core/frontend/src/components/CHTML/CHTML.test.tsx`
**Symbols:** class:`CHTML`
**Often changes with:** `system/core/frontend/src/components/CPlugin/CPlugin.tsx` (9x), `system/core/frontend/src/components/CContainer/CContainer.tsx` (8x), `system/core/frontend/src/components/CImage/CImage.tsx` (8x), `system/core/frontend/src/components/CText/CText.tsx` (8x), `system/core/frontend/src/components/CGallery/CGallery.tsx` (7x)

### `system/core/frontend/src/components/CImage/CImage.test.tsx`
**Feature:** CI/CD
**Imports:** `system/core/frontend/src/components/CImage/CImage.tsx`

### `system/core/frontend/src/components/CImage/CImage.tsx`
**Feature:** CI/CD
**Imports:** `system/core/frontend/src/components/CBlock/CBlock.tsx`, `system/core/frontend/src/components/Link/Link.tsx`
**Imported by:** `system/core/frontend/src/components/CBlock/CBlock.tsx`, `system/core/frontend/src/components/CImage/CImage.test.tsx`
**Symbols:** class:`CImage`, const_fn:`imgEl`
**Often changes with:** `system/core/common/src/types/blocks.ts` (13x), `system/core/frontend/src/components/CGallery/CGallery.tsx` (10x), `system/core/frontend/src/components/CPlugin/CPlugin.tsx` (9x), `system/core/frontend/src/components/CText/CText.tsx` (9x), `system/core/frontend/src/components/CContainer/CContainer.tsx` (8x)

### `system/core/frontend/src/components/CList/CList.test.tsx`
**Imports:** `system/core/frontend/src/components/CList/CList.tsx`

### `system/core/frontend/src/components/CList/CList.tsx`
**Imports:** `system/core/frontend/src/components/CBlock/CBlock.tsx`, `toolkits/commerce/src/mui/Loadbox/Loadbox.tsx`, `system/core/frontend/src/components/throbber.ts`, `system/core/frontend/src/components/CList/CListPagination.tsx`, `system/core/frontend/src/components/CList/helpers.ts`, `system/core/frontend/src/components/CList/types.ts`
**Imported by:** `system/core/frontend/src/components/CList/CList.test.tsx`
**Symbols:** class:`CList`
**Often changes with:** `system/core/common/src/types/blocks.ts` (12x), `system/core/frontend/src/components/CGallery/CGallery.tsx` (11x), `system/core/common/src/types/data.ts` (10x), `system/core/frontend/src/components/CList/types.ts` (9x), `system/core/frontend/src/components/CPlugin/CPlugin.tsx` (9x)

### `system/core/frontend/src/components/CList/CListPagination.tsx`
**Imports:** `system/core/frontend/src/components/CList/helpers.ts`, `system/core/frontend/src/components/CList/types.ts`
**Imported by:** `system/core/frontend/src/components/CList/CList.tsx`
**Symbols:** class:`Pagination`
**Often changes with:** `system/core/frontend/src/components/CList/CList.tsx` (7x), `system/core/common/src/types/blocks.ts` (5x), `system/core/frontend/src/components/CGallery/CGallery.tsx` (4x), `system/core/frontend/src/components/CImage/CImage.tsx` (4x), `system/core/frontend/src/components/CList/helpers.ts` (4x)

### `system/core/frontend/src/components/CList/helpers.ts`
**Imported by:** `system/core/frontend/src/components/CList/CList.tsx`, `system/core/frontend/src/components/CList/CListPagination.tsx`
**Symbols:** const_fn:`getPageId`, const_fn:`getPageNumsAround`, const_fn:`getPagedUrl`, const_fn:`getPageNumberFromUrl`
**Often changes with:** `system/core/frontend/src/components/CList/CList.tsx` (7x), `system/core/frontend/src/components/CList/CListPagination.tsx` (4x), `system/core/frontend/src/components/CPlugin/CPlugin.tsx` (4x), `system/core/frontend/src/api/CGraphQLClient.ts` (4x), `system/core/frontend/src/components/CGallery/CGallery.tsx` (3x)

### `system/core/frontend/src/components/CList/types.ts`
**Imported by:** `system/core/frontend/src/components/CList/CList.tsx`, `system/core/frontend/src/components/CList/CListPagination.tsx`
**Often changes with:** `system/core/frontend/src/components/CList/CList.tsx` (9x), `system/core/common/src/types/entities.ts` (4x), `system/core/frontend/src/_index.ts` (3x), `system/core/frontend/src/components/CGallery/CGallery.tsx` (3x), `system/core/frontend/src/components/CText/CText.tsx` (3x)

### `system/core/frontend/src/components/CPlugin/CPlugin.test.tsx`
**Imports:** `system/core/frontend/src/components/CPlugin/CPlugin.tsx`
**Often changes with:** `system/core/frontend/src/components/CPlugin/CPlugin.tsx` (3x), `system/core/frontend/src/components/Link/Link.tsx` (3x), `system/core/frontend/src/constants.ts` (3x)

### `system/core/frontend/src/components/CPlugin/CPlugin.tsx`
**Imports:** `system/core/frontend/src/api/CRestApiClient.ts`, `themes/store/src/constants.js`, `system/core/frontend/src/helpers/loadFrontendBundle.ts`, `system/core/frontend/src/components/CBlock/CBlock.tsx`
**Imported by:** `system/core/frontend/src/components/CBlock/CBlock.tsx`, `system/core/frontend/src/components/CPlugin/CPlugin.test.tsx`
**Symbols:** const_fn:`fallbackComponent`, class:`CPlugin`, class:`ErrorBoundary`
**Often changes with:** `system/core/common/src/types/blocks.ts` (20x), `system/core/common/src/types/data.ts` (14x), `system/core/frontend/src/helpers/loadFrontendBundle.ts` (10x), `system/core/frontend/src/components/CGallery/CGallery.tsx` (9x), `system/core/frontend/src/components/CHTML/CHTML.tsx` (9x)

### `system/core/frontend/src/components/CText/CText.test.tsx`
**Imports:** `system/core/frontend/src/components/CText/CText.tsx`

### `system/core/frontend/src/components/CText/CText.tsx`
**Imports:** `system/core/frontend/src/components/CBlock/CBlock.tsx`, `system/core/frontend/src/components/Link/Link.tsx`
**Imported by:** `system/core/frontend/src/components/CBlock/CBlock.tsx`, `system/core/frontend/src/components/CText/CText.test.tsx`
**Symbols:** class:`CText`
**Often changes with:** `system/core/frontend/src/components/CImage/CImage.tsx` (9x), `system/core/common/src/types/blocks.ts` (8x), `system/core/frontend/src/components/CGallery/CGallery.tsx` (8x), `system/core/frontend/src/components/CList/CList.tsx` (8x), `system/core/frontend/src/components/CContainer/CContainer.tsx` (8x)

### `system/core/frontend/src/components/EntityHead/EntityHead.tsx`
**Imports:** `themes/store/src/constants.js`
**Symbols:** function:`EntityHead`
**Often changes with:** `system/core/frontend/src/constants.ts` (3x)

### `system/core/frontend/src/components/Link/Link.test.tsx`
**Imports:** `system/core/frontend/src/components/Link/Link.tsx`
**Often changes with:** `system/core/frontend/src/components/CGallery/CGallery.tsx` (3x), `system/core/frontend/src/components/Link/Link.tsx` (3x)

### `system/core/frontend/src/components/Link/Link.tsx`
**Imported by:** `system/core/frontend/src/components/CGallery/CGallery.tsx`, `system/core/frontend/src/components/CImage/CImage.tsx`, `system/core/frontend/src/components/CText/CText.tsx`, `system/core/frontend/src/components/Link/Link.test.tsx`, `website/src/pages/index.tsx`, `website/src/pages/latest-frontend-dependencies.tsx`, `website/src/theme/Footer/index.tsx`
**Symbols:** const_fn:`Link`
**Often changes with:** `system/core/frontend/src/constants.ts` (8x), `system/core/frontend/src/components/CPlugin/CPlugin.tsx` (6x), `system/core/common/src/types/blocks.ts` (5x), `system/renderer/src/generator.ts` (5x), `system/core/frontend/src/components/CGallery/CGallery.tsx` (4x)

### `system/core/frontend/src/components/SignIn/SignIn.test.tsx`
**Imports:** `system/core/frontend/src/components/SignIn/SignIn.tsx`
**Often changes with:** `system/core/frontend/src/helpers/hooks.ts` (3x)

### `system/core/frontend/src/components/SignIn/SignIn.tsx`
**Imports:** `system/core/frontend/src/helpers/AuthClient.ts`, `system/core/frontend/src/components/BaseElements/BaseButton.tsx`, `system/core/frontend/src/components/BaseElements/BaseTextField.tsx`
**Imported by:** `system/core/frontend/src/components/SignIn/SignIn.test.tsx`
**Symbols:** function:`SignIn`, const_fn:`handleSigIn`, const_fn:`handleForgotPass`, const_fn:`handleResetPass`, const_fn:`onSubmit`
**Often changes with:** `system/core/frontend/src/components/SignUp/SignUp.tsx` (3x), `system/core/frontend/src/helpers/AuthClient.ts` (3x), `system/core/frontend/src/helpers/hooks.ts` (3x)

### `system/core/frontend/src/components/SignUp/SignUp.test.tsx`
**Feature:** Registration
**Imports:** `system/core/frontend/src/components/SignUp/SignUp.tsx`

### `system/core/frontend/src/components/SignUp/SignUp.tsx`
**Feature:** Registration
**Imports:** `system/core/frontend/src/helpers/AuthClient.ts`, `system/core/frontend/src/components/BaseElements/BaseButton.tsx`, `system/core/frontend/src/components/BaseElements/BaseTextField.tsx`
**Imported by:** `system/core/frontend/src/components/SignUp/SignUp.test.tsx`
**Symbols:** function:`SignUp`, const_fn:`handleSignUp`
**Often changes with:** `system/core/frontend/src/helpers/AuthClient.ts` (4x), `system/core/frontend/src/components/SignIn/SignIn.tsx` (3x), `system/core/frontend/src/helpers/hooks.ts` (3x)

### `system/core/frontend/src/components/loadBox/Loadbox.tsx`
**Feature:** Database
**Imports:** `system/core/frontend/src/components/throbber.ts`
**Symbols:** const_fn:`LoadBox`

### `system/core/frontend/src/components/throbber.ts`
**Purpose:** @internal
**Feature:** UI Components
**Imported by:** `system/core/frontend/src/components/CList/CList.tsx`, `system/core/frontend/src/components/loadBox/Loadbox.tsx`

### `system/core/frontend/src/constants.ts`
**Symbols:** const_fn:`getBlockHtmlId`, const_fn:`getBlockIdFromHtml`, const_fn:`getBlockHtmlType`, const_fn:`getBlockTypeFromHtml`, const_fn:`getHtmlPluginBlockName`, const_fn:`getBlockById`, const_fn:`getBlockDataById`, const_fn:`getBlockData`, const_fn:`id`, const_fn:`getBlockElementById`, const_fn:`isAdminPanel`, const_fn:`awaitImporter`, const_fn:`usePageCmsProps`
**Often changes with:** `system/core/common/src/types/blocks.ts` (14x), `system/core/frontend/src/components/CPlugin/CPlugin.tsx` (9x), `system/renderer/src/generator.ts` (8x), `system/core/frontend/src/components/Link/Link.tsx` (8x), `system/core/frontend/src/components/CGallery/CGallery.tsx` (7x)

### `system/core/frontend/src/declarations.d.ts`

### `system/core/frontend/src/helpers/AuthClient.ts`
**Feature:** Utilities
**Imports:** `system/core/frontend/src/api/CRestApiClient.ts`, `system/core/frontend/src/helpers/forceUpdate.ts`
**Imported by:** `system/core/frontend/src/components/SignIn/SignIn.tsx`, `system/core/frontend/src/components/SignUp/SignUp.tsx`
**Symbols:** class:`AuthClient`
**Often changes with:** `system/core/frontend/src/components/SignUp/SignUp.tsx` (4x), `system/core/frontend/src/helpers/hooks.ts` (4x), `system/server/src/services/cms.service.ts` (4x), `system/core/frontend/src/components/SignIn/SignIn.tsx` (3x), `system/core/frontend/src/_index.ts` (3x)

### `system/core/frontend/src/helpers/CStore.ts`
**Feature:** Utilities
**Imports:** `system/core/frontend/src/api/CGraphQLClient.ts`
**Imported by:** `system/core/frontend/src/helpers/hooks.ts`, `system/core/frontend/tests/helpers/CStore.spec.ts`
**Symbols:** class:`CStore`, const_fn:`areEqual`, const_fn:`filter`
**Often changes with:** `system/core/common/src/types/entities.ts` (10x), `system/core/backend/src/repositories/product.repository.ts` (7x), `system/core/frontend/tests/helpers/CStore.spec.ts` (5x), `system/core/common/src/types/blocks.ts` (5x), `system/core/common/src/types/data.ts` (5x)

### `system/core/frontend/src/helpers/contentGetters.ts`
**Feature:** Utilities
**Symbols:** const_fn:`getPluginStaticUrl`

### `system/core/frontend/src/helpers/forceUpdate.ts`
**Feature:** Utilities
**Imported by:** `system/core/frontend/src/helpers/AuthClient.ts`
**Symbols:** function:`useForceUpdate`

### `system/core/frontend/src/helpers/getServiceSecret.ts`
**Feature:** Utilities
**Imported by:** `system/core/frontend/src/api/CGraphQLClient.ts`, `system/core/frontend/src/api/CRestApiClient.ts`
**Symbols:** const_fn:`getServiceSecret`, const_fn:`nodeRequire`

### `system/core/frontend/src/helpers/hooks.ts`
**Feature:** Utilities
**Imports:** `system/core/frontend/src/helpers/CStore.ts`
**Symbols:** const_fn:`useCart`, const_fn:`useWishlist`, const_fn:`useViewedItems`, const_fn:`onChange`
**Often changes with:** `system/core/frontend/src/helpers/AuthClient.ts` (4x), `themes/store/src/components/header/Header.tsx` (4x), `system/core/frontend/src/components/SignIn/SignIn.test.tsx` (3x), `system/core/frontend/src/components/SignIn/SignIn.tsx` (3x), `system/core/frontend/src/components/SignUp/SignUp.tsx` (3x)

### `system/core/frontend/src/helpers/iconFromPath.tsx`
**Feature:** Utilities
**Symbols:** const_fn:`iconFromPath`
**Often changes with:** `system/core/frontend/src/constants.ts` (3x)

### `system/core/frontend/src/helpers/importer.ts`
**Feature:** Utilities
**Imports:** `system/core/frontend/src/helpers/isomorphicFetch.ts`
**Imported by:** `system/core/frontend/src/helpers/loadFrontendBundle.ts`, `system/core/frontend/tests/helpers/importer.spec.ts`
**Symbols:** class:`Importer`, const_fn:`checkLib`, const_fn:`useImporter`, const_fn:`importAllNamed`

### `system/core/frontend/src/helpers/isomorphicFetch.ts`
**Feature:** Utilities
**Imported by:** `system/core/frontend/src/api/CGraphQLClient.ts`, `system/core/frontend/src/api/CRestApiClient.ts`, `system/core/frontend/src/api/CentralServerClient.ts`, `system/core/frontend/src/helpers/importer.ts`
**Symbols:** const_fn:`fetch`
**Often changes with:** `system/core/frontend/src/helpers/loadFrontendBundle.ts` (5x), `system/core/common/src/types/data.ts` (5x), `system/core/frontend/src/components/CPlugin/CPlugin.tsx` (5x), `system/core/frontend/src/components/Link/Link.tsx` (4x), `system/core/frontend/src/constants.ts` (4x)

### `system/core/frontend/src/helpers/loadFrontendBundle.ts`
**Feature:** Utilities
**Imports:** `themes/store/src/constants.js`, `system/core/frontend/src/helpers/importer.ts`
**Imported by:** `system/core/frontend/src/components/CPlugin/CPlugin.tsx`
**Symbols:** const_fn:`loadFrontendBundle`, const_fn:`evalCode`, const_fn:`getLoadableFrontendBundle`
**Often changes with:** `system/core/frontend/src/components/CPlugin/CPlugin.tsx` (10x), `system/core/common/src/types/blocks.ts` (7x), `system/core/frontend/src/constants.ts` (6x), `system/renderer/src/generator.ts` (6x), `system/core/frontend/src/helpers/isomorphicFetch.ts` (5x)

### `system/core/frontend/src/helpers/parserTransform.tsx`
**Feature:** Utilities
**Imported by:** `system/core/frontend/src/components/CEditor/CEditor.tsx`, `system/core/frontend/src/components/CHTML/CHTML.tsx`
**Symbols:** const_fn:`ScriptTag`, const_fn:`makeParserContext`, const_fn:`cleanParseContext`, const_fn:`getParserTransform`, const_fn:`childContent`, const_fn:`parseHtml`
**Often changes with:** `system/core/frontend/src/components/CHTML/CHTML.tsx` (3x)

### `system/core/frontend/src/helpers/registerPlugin.ts`
**Purpose:** Registers a Plugin on a specific page for frontend (Next.js server)
so a plugin will be able to receive its server-side props. If you don't
need those props, then you can just use CPlugin without regi
**Feature:** Utilities
**Symbols:** const_fn:`registerPluginSSR`, const_fn:`getRegisteredPluginsAtPage`
**Often changes with:** `system/renderer/src/helpers/pluginsDataFetcher.ts` (3x)

### `system/core/frontend/src/helpers/registerWidget.ts`
**Feature:** Utilities
**Imports:** `system/core/frontend/src/widget-types.ts`
**Imported by:** `system/core/frontend/src/components/AdminPanelWidget/AdminPanelWidgetPlace.test.tsx`, `system/core/frontend/src/components/AdminPanelWidget/AdminPanelWidgetPlace.tsx`

### `system/core/frontend/src/helpers/thumbs.ts`
**Feature:** Utilities
**Imported by:** `system/core/frontend/src/components/CGallery/Thumbs.tsx`
**Symbols:** function:`getThumbnailSrc`

### `system/core/frontend/src/widget-types.ts`
**Imported by:** `system/core/frontend/src/components/AdminPanelWidget/AdminPanelWidgetPlace.tsx`, `system/core/frontend/src/helpers/registerWidget.ts`
**Often changes with:** `system/core/common/src/types/blocks.ts` (4x)

### `system/core/frontend/tests/helpers.ts`
**Feature:** Testing
**Symbols:** const_fn:`mockWorkingDirectory`, const_fn:`tearDown`

### `system/core/frontend/tests/helpers/CStore.spec.ts`
**Feature:** Utilities
**Imports:** `system/core/frontend/src/helpers/CStore.ts`, `toolkits/commerce/tests/helpers.ts`
**Symbols:** const_fn:`getLocalCStore`
**Often changes with:** `system/core/frontend/src/helpers/CStore.ts` (5x), `system/core/backend/src/repositories/product.repository.ts` (3x), `system/core/common/src/types/entities.ts` (3x), `system/core/common/src/constants.ts` (3x), `system/core/common/src/types/data.ts` (3x)

### `system/core/frontend/tests/helpers/importer.spec.ts`
**Feature:** Utilities
**Imports:** `system/core/frontend/src/helpers/importer.ts`, `toolkits/commerce/tests/helpers.ts`

### `system/core/frontend/tests/setup.ts`
**Feature:** Testing
**Often changes with:** `system/core/common/src/types/data.ts` (3x)

### `system/manager/.eslintrc.js`

### `system/manager/rollup.config.js`
**Symbols:** const_fn:`external`
**Often changes with:** `system/renderer/rollup.config.js` (9x), `system/manager/src/managers/baseManager.ts` (8x), `system/manager/src/managers/rendererManager.ts` (8x), `system/core/frontend/rollup.config.js` (7x), `system/core/backend/rollup.config.js` (6x)

### `system/manager/src/config.ts`
**Imports:** `system/core/backend/src/helpers/paths.ts`
**Imported by:** `system/manager/src/managers/adminPanelManager.ts`, `system/manager/src/managers/baseManager.ts`, `system/manager/src/managers/rendererManager.ts`, `system/manager/src/managers/serverManager.ts`, `system/manager/src/utils/cacheManager.js`, `website/src/theme/prism-include-languages.js`
**Often changes with:** `system/manager/src/managers/baseManager.ts` (5x), `system/manager/src/managers/adminPanelManager.ts` (4x), `system/manager/src/managers/serverManager.ts` (4x), `system/manager/startup.js` (3x), `system/manager/src/constants.ts` (3x)

### `system/manager/src/constants.ts`
**Often changes with:** `system/manager/src/managers/baseManager.ts` (9x), `system/manager/src/managers/rendererManager.ts` (7x), `system/manager/src/managers/adminPanelManager.ts` (6x), `system/manager/rollup.config.js` (5x), `system/manager/src/managers/serverManager.ts` (5x)

### `system/manager/src/index.ts`
**Imports:** `system/core/backend/src/helpers/cms-settings.ts`, `system/core/backend/src/helpers/shell.ts`
**Often changes with:** `system/manager/src/managers/baseManager.ts` (10x), `system/manager/src/managers/rendererManager.ts` (10x), `system/manager/src/managers/adminPanelManager.ts` (8x), `system/manager/src/managers/serverManager.ts` (8x), `system/cli/src/cli.ts` (7x)

### `system/manager/src/managers/adminPanelManager.ts`
**Imports:** `system/core/backend/src/helpers/cms-settings.ts`, `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/helpers/paths.ts`, `system/manager/src/config.ts`, `themes/store/src/constants.js`, `system/manager/src/managers/baseManager.ts`
**Imported by:** `system/manager/src/managers/baseManager.ts`
**Symbols:** const_fn:`startAdminPanel`, const_fn:`closeAdminPanel`, const_fn:`closeAdminPanelManager`
**Often changes with:** `system/manager/src/managers/baseManager.ts` (24x), `system/manager/src/managers/rendererManager.ts` (23x), `system/manager/src/managers/serverManager.ts` (22x), `system/renderer/src/generator.ts` (13x), `system/cli/src/cli.ts` (12x)

### `system/manager/src/managers/baseManager.ts`
**Imports:** `system/core/backend/src/helpers/cms-settings.ts`, `themes/store/src/constants.js`, `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/helpers/service-versions.ts`, `system/core/frontend/src/api/CRestApiClient.ts`, `system/manager/src/config.ts`, `themes/store/src/constants.js`, `system/manager/src/tasks/checkModules.ts`, `system/renderer/src/helpers/cacheManager.ts`, `system/manager/src/managers/adminPanelManager.ts`
**Imported by:** `system/manager/src/managers/adminPanelManager.ts`, `system/manager/src/managers/rendererManager.ts`, `system/manager/src/managers/serverManager.ts`
**Symbols:** function:`getProcessPid`, const_fn:`closeService`, const_fn:`kill`, const_fn:`closeServiceAndManager`, const_fn:`startService`, const_fn:`isServiceRunning`, const_fn:`isPortUsed`, const_fn:`startSystem`, const_fn:`startServiceByName`, const_fn:`closeServiceByName`
**Often changes with:** `system/manager/src/managers/rendererManager.ts` (34x), `system/manager/src/managers/adminPanelManager.ts` (24x), `system/manager/src/managers/serverManager.ts` (24x), `system/renderer/src/generator.ts` (20x), `system/cli/src/cli.ts` (17x)

### `system/manager/src/managers/dockerManager.ts`
**Imports:** `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/helpers/paths.ts`
**Imported by:** `system/manager/src/managers/baseManager.ts`
**Symbols:** const_fn:`startNginx`, const_fn:`closeNginx`
**Often changes with:** `system/manager/src/managers/baseManager.ts` (5x), `system/manager/src/tasks/checkModules.ts` (5x), `system/manager/src/managers/rendererManager.ts` (4x), `system/renderer/src/generator.ts` (4x), `system/manager/src/managers/adminPanelManager.ts` (3x)

### `system/manager/src/managers/rendererManager.ts`
**Imports:** `system/core/backend/src/helpers/cms-settings.ts`, `themes/store/src/constants.js`, `system/core/backend/src/helpers/logger.ts`, `system/core/frontend/src/api/CRestApiClient.ts`, `system/manager/src/config.ts`, `themes/store/src/constants.js`, `system/manager/src/managers/baseManager.ts`
**Imported by:** `system/manager/src/managers/baseManager.ts`, `system/manager/src/tasks/buildTask.ts`
**Symbols:** const_fn:`startRenderer`, const_fn:`onMessage`, const_fn:`isRendererRunning`, const_fn:`rendererRunBuild`, const_fn:`rendererStartWatchDev`, const_fn:`isThemeBuilt`, const_fn:`pollPages`, const_fn:`startRendererAliveWatcher`, const_fn:`rendererAliveWatcher`, const_fn:`closeRenderer`, const_fn:`closeRendererManager`
**Often changes with:** `system/manager/src/managers/baseManager.ts` (34x), `system/renderer/src/generator.ts` (24x), `system/manager/src/managers/adminPanelManager.ts` (23x), `system/manager/src/managers/serverManager.ts` (23x), `system/core/common/src/types/data.ts` (19x)

### `system/manager/src/managers/serverManager.ts`
**Imports:** `system/core/backend/src/helpers/cms-settings.ts`, `themes/store/src/constants.js`, `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/helpers/paths.ts`, `system/manager/src/config.ts`, `themes/store/src/constants.js`, `system/manager/src/managers/baseManager.ts`
**Imported by:** `system/manager/src/managers/baseManager.ts`
**Symbols:** const_fn:`startServer`, const_fn:`onMessage`, const_fn:`closeServer`, const_fn:`closeServerManager`
**Often changes with:** `system/manager/src/managers/baseManager.ts` (24x), `system/manager/src/managers/rendererManager.ts` (23x), `system/manager/src/managers/adminPanelManager.ts` (22x), `system/cli/src/cli.ts` (12x), `system/renderer/src/generator.ts` (12x)

### `system/manager/src/tasks/buildTask.ts`
**Imports:** `system/core/backend/src/helpers/logger.ts`, `system/renderer/src/server.ts`, `system/utils/src/plugins/rollup.ts`, `system/manager/src/managers/rendererManager.ts`, `system/manager/src/tasks/checkModules.ts`, `system/manager/src/utils/buildUtils.ts`, `system/utils/src/plugins/rollup.ts`, `system/server/src/helpers/utils.ts`
**Symbols:** const_fn:`buildTask`, const_fn:`rendererBuildAndSaveTheme`, const_fn:`rollupBuild`, const_fn:`requireDevDeps`, const_fn:`onRollupEvent`, const_fn:`input`, const_fn:`onRollupEventShort`
**Often changes with:** `system/renderer/src/generator.ts` (14x), `system/manager/src/managers/rendererManager.ts` (12x), `system/core/backend/src/helpers/paths.ts` (10x), `system/manager/src/managers/baseManager.ts` (9x), `system/server/src/main.ts` (7x)

### `system/manager/src/tasks/checkModules.ts`
**Imports:** `system/core/backend/src/helpers/logger.ts`, `system/server/src/helpers/utils.ts`, `system/utils/src/downloader.ts`, `system/utils/src/shared.ts`
**Imported by:** `system/manager/src/managers/baseManager.ts`, `system/manager/src/tasks/buildTask.ts`
**Symbols:** const_fn:`checkModules`, const_fn:`checkDependencies`, const_fn:`defaultDeps`, const_fn:`checkConfigs`
**Often changes with:** `system/manager/src/managers/baseManager.ts` (7x), `system/manager/src/tasks/buildTask.ts` (7x), `system/manager/src/managers/rendererManager.ts` (6x), `system/renderer/src/generator.ts` (6x), `system/manager/src/managers/dockerManager.ts` (5x)

### `system/manager/src/utils/buildUtils.ts`
**Feature:** Utilities
**Imported by:** `system/manager/src/tasks/buildTask.ts`
**Symbols:** const_fn:`init`, const_fn:`raw`, function:`isAbsolute`, function:`relativeId`, function:`handleError`, const_fn:`message`

### `system/manager/src/utils/cacheManager.js`
**Feature:** Utilities
**Imports:** `system/manager/src/config.ts`
**Symbols:** const_fn:`getRunTimeCache`, const_fn:`getCacheKey`, const_fn:`saveProcessPid`, const_fn:`saveServiceName`, const_fn:`getProcessPid`, const_fn:`getAllServices`, const_fn:`loadServiceNames`, const_fn:`loadCache`, const_fn:`cleanCache`
**Often changes with:** `system/manager/src/managers/rendererManager.ts` (5x), `system/manager/src/managers/serverManager.ts` (5x), `system/manager/src/managers/adminPanelManager.ts` (4x), `system/manager/src/managers/baseManager.ts` (4x), `system/manager/rollup.config.js` (3x)

### `system/manager/src/utils/herokuStart.js`
**Feature:** Utilities
**Often changes with:** `system/manager/src/managers/adminPanelManager.ts` (3x), `system/manager/src/managers/baseManager.ts` (3x), `system/manager/src/managers/rendererManager.ts` (3x), `system/manager/src/managers/serverManager.ts` (3x)

### `system/manager/src/utils/winUtils.js`
**Feature:** Utilities
**Symbols:** const_fn:`winKillPid`

### `system/manager/startup.js`
**Imports:** `system/core/backend/src/helpers/shell.ts`, `website/src/theme/Footer/index.tsx`
**Symbols:** const_fn:`main`
**Often changes with:** `system/manager/src/managers/baseManager.ts` (11x), `system/renderer/src/generator.ts` (8x), `system/cli/src/cli.ts` (7x), `system/manager/src/managers/adminPanelManager.ts` (6x), `system/manager/src/managers/rendererManager.ts` (6x)

### `system/renderer/.eslintrc.js`
**Often changes with:** `system/server/.eslintrc.js` (3x), `system/core/common/src/types/data.ts` (3x), `system/core/common/src/types/entities.ts` (3x), `system/server/src/controllers/cms.controller.ts` (3x)

### `system/renderer/next-env.d.ts`
**Purpose:** / <reference types="next" />
/ <reference types="next/types/global" />

### `system/renderer/postcss-build.js`

### `system/renderer/rollup.config.js`
**Often changes with:** `system/renderer/src/generator.ts` (13x), `system/manager/rollup.config.js` (9x), `system/renderer/src/index.ts` (8x), `system/renderer/startup.js` (8x), `system/core/frontend/rollup.config.js` (8x)

### `system/renderer/src/generator.ts`
**Imports:** `system/core/backend/src/helpers/cms-settings.ts`, `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/helpers/shell.ts`, `system/core/frontend/src/api/CRestApiClient.ts`, `system/utils/src/shared.ts`, `system/renderer/src/helpers/defaultContents.tsx`, `system/renderer/src/helpers/helpers.ts`
**Symbols:** const_fn:`generator`, const_fn:`devGenerate`, const_fn:`checkDidDefaultImport`, const_fn:`makeProperties`, const_fn:`generateDefaultApp`
**Often changes with:** `system/renderer/startup.js` (25x), `system/manager/src/managers/rendererManager.ts` (24x), `system/core/common/src/types/data.ts` (22x), `system/manager/src/managers/baseManager.ts` (20x), `system/core/common/src/types/entities.ts` (16x)

### `system/renderer/src/helpers/cacheManager.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/auth-settings.ts`, `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/helpers/paths.ts`
**Imported by:** `system/manager/src/managers/baseManager.ts`, `system/renderer/src/server.ts`
**Symbols:** const_fn:`processCacheRequest`, const_fn:`checkAuth`, const_fn:`purgePageCache`, const_fn:`purgeEntireCache`, const_fn:`purgeNextJsFileCache`
**Often changes with:** `system/renderer/src/generator.ts` (5x), `system/renderer/src/server.ts` (4x), `system/renderer/src/wrappers/appWrapper.tsx` (4x), `system/manager/src/tasks/buildTask.ts` (4x), `system/renderer/src/wrappers/getPropsWrapper.ts` (3x)

### `system/renderer/src/helpers/defaultContents.tsx`
**Feature:** Utilities
**Imported by:** `system/renderer/src/generator.ts`
**Symbols:** function:`GenericPage`, const_fn:`getStaticProps`, const_fn:`getStaticPaths`
**Often changes with:** `system/manager/src/managers/rendererManager.ts` (4x), `system/renderer/src/generator.ts` (4x), `system/renderer/src/server.ts` (3x), `system/renderer/src/wrappers/appWrapper.tsx` (3x), `system/renderer/src/wrappers/getPropsWrapper.ts` (3x)

### `system/renderer/src/helpers/document.tsx`
**Feature:** Utilities
**Imported by:** `system/admin/src/pages/_document.tsx`, `system/core/common/src/types/blocks.ts`, `system/renderer/src/wrappers/appWrapper.tsx`, `themes/blog/src/pages/_document.tsx`, `themes/store/src/pages/_document.tsx`
**Symbols:** const_fn:`patchDocument`
**Often changes with:** `system/renderer/src/server.ts` (3x)

### `system/renderer/src/helpers/getThemeStaticProps.ts`
**Feature:** Utilities
**Imported by:** `system/renderer/src/wrappers/getPropsWrapper.ts`
**Symbols:** const_fn:`getThemeStaticProps`

### `system/renderer/src/helpers/helpers.ts`
**Feature:** Utilities
**Imported by:** `system/renderer/src/generator.ts`
**Symbols:** function:`useForceUpdate`
**Often changes with:** `system/renderer/rollup.config.js` (3x), `system/renderer/src/generator.ts` (3x)

### `system/renderer/src/helpers/initRenderer.ts`
**Feature:** Utilities
**Imported by:** `system/renderer/src/helpers/pluginsDataFetcher.ts`, `system/renderer/src/wrappers/appWrapper.tsx`
**Symbols:** const_fn:`checkBackendModules`, const_fn:`initRenderer`, const_fn:`getPluginCjsPath`, const_fn:`fsRequire`, const_fn:`str`

### `system/renderer/src/helpers/pluginsDataFetcher.ts`
**Feature:** Utilities
**Imports:** `system/renderer/src/helpers/initRenderer.ts`
**Imported by:** `system/renderer/src/wrappers/getPropsWrapper.ts`
**Symbols:** const_fn:`pluginsDataFetcher`
**Often changes with:** `system/renderer/src/wrappers/getPropsWrapper.ts` (6x), `system/renderer/src/wrappers/appWrapper.tsx` (5x), `system/core/common/src/types/blocks.ts` (5x), `system/renderer/src/generator.ts` (4x), `system/core/frontend/src/api/CRestApiClient.ts` (4x)

### `system/renderer/src/helpers/readThemeExports.ts`
**Feature:** Utilities
**Symbols:** const_fn:`readThemeExports`
**Often changes with:** `system/renderer/src/generator.ts` (3x)

### `system/renderer/src/helpers/redirects.ts`
**Feature:** Utilities
**Imported by:** `system/renderer/src/wrappers/appWrapper.tsx`
**Symbols:** const_fn:`usePatchForRedirects`, const_fn:`logInfo`, const_fn:`handleChange`, const_fn:`handleChange`
**Often changes with:** `system/renderer/src/generator.ts` (3x)

### `system/renderer/src/index.ts`
**Often changes with:** `system/renderer/src/generator.ts` (14x), `system/renderer/rollup.config.js` (8x), `system/renderer/startup.js` (7x), `system/renderer/src/server.ts` (5x), `system/renderer/src/wrappers/appWrapper.tsx` (5x)

### `system/renderer/src/server.ts`
**Imports:** `system/core/backend/src/helpers/auth-settings.ts`, `system/core/backend/src/helpers/cms-settings.ts`, `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/helpers/shell.ts`, `system/utils/src/static.ts`, `system/renderer/src/helpers/cacheManager.ts`, `system/server/src/helpers/connect-database.ts`
**Imported by:** `system/manager/src/tasks/buildTask.ts`, `system/server/src/main.ts`
**Symbols:** const_fn:`startNextServer`
**Often changes with:** `system/renderer/src/generator.ts` (9x), `system/core/common/src/types/data.ts` (8x), `system/renderer/src/wrappers/appWrapper.tsx` (7x), `system/renderer/startup.js` (7x), `system/manager/src/managers/rendererManager.ts` (6x)

### `system/renderer/src/types.ts`

### `system/renderer/src/wrappers/appWrapper.tsx`
**Imports:** `system/renderer/src/helpers/document.tsx`, `toolkits/commerce/tests/helpers.ts`, `system/renderer/src/helpers/initRenderer.ts`, `system/renderer/src/helpers/redirects.ts`
**Symbols:** const_fn:`DefaultRootComp`, const_fn:`nodeRequire`, const_fn:`withCromwellApp`, const_fn:`forceUpdatePage`, const_fn:`getChildAppProps`, const_fn:`content`
**Often changes with:** `system/renderer/src/generator.ts` (9x), `system/renderer/src/server.ts` (7x), `system/renderer/src/wrappers/getPropsWrapper.ts` (6x), `themes/store/cromwell.config.js` (6x), `themes/store/src/components/header/Header.tsx` (6x)

### `system/renderer/src/wrappers/getPropsWrapper.ts`
**Imports:** `system/renderer/src/helpers/getThemeStaticProps.ts`, `system/renderer/src/helpers/pluginsDataFetcher.ts`
**Symbols:** const_fn:`wrapGetProps`, const_fn:`wrapGetStaticProps`, const_fn:`wrapGetInitialProps`, const_fn:`wrapGetServerSideProps`, const_fn:`wrapGetStaticPaths`, const_fn:`createGetServerSideProps`, const_fn:`createGetInitialProps`, const_fn:`createGetStaticProps`, const_fn:`createGetStaticPaths`
**Often changes with:** `system/renderer/src/wrappers/appWrapper.tsx` (6x), `system/renderer/src/helpers/pluginsDataFetcher.ts` (6x), `system/server/src/services/cms.service.ts` (4x), `system/renderer/src/generator.ts` (4x), `system/core/common/src/types/blocks.ts` (4x)

### `system/renderer/startup.js`
**Imports:** `system/core/backend/src/helpers/cms-settings.ts`, `themes/store/src/constants.js`, `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/helpers/shell.ts`
**Symbols:** const_fn:`main`, const_fn:`isServiceBuilt`, const_fn:`buildService`, const_fn:`gen`, const_fn:`build`, const_fn:`start`
**Often changes with:** `system/renderer/src/generator.ts` (25x), `system/manager/src/managers/rendererManager.ts` (15x), `system/manager/src/managers/baseManager.ts` (14x), `system/core/common/src/types/data.ts` (9x), `system/core/frontend/src/api/CGraphQLClient.ts` (9x)

### `system/server/.eslintrc.js`
**Often changes with:** `system/renderer/.eslintrc.js` (3x)

### `system/server/migrations/common/1651054396603-permissions.js`
**Feature:** Shared Code
**Symbols:** const_fn:`migrationStart`, const_fn:`migrationEnd`, const_fn:`mockRoles`

### `system/server/migrations/mysql/1636584474808-init.js`
**Often changes with:** `system/server/migrations/postgres/1636584481105-init.js` (3x), `system/server/migrations/sqlite/1636584487669-init.js` (3x), `system/server/src/controllers/cms.controller.ts` (3x)

### `system/server/migrations/mysql/1638975054101-coupons.js`

### `system/server/migrations/mysql/1640287891928-product-variants.js`

### `system/server/migrations/mysql/1643375768211-extend-address.js`

### `system/server/migrations/mysql/1651054391643-permissions.js`
**Imports:** `system/server/migrations/sqlite/1651054396603-permissions.js`

### `system/server/migrations/mysql/1685500029070-add_dashboard.js`

### `system/server/migrations/postgres/1636584481105-init.js`
**Often changes with:** `system/server/migrations/mysql/1636584474808-init.js` (3x), `system/server/migrations/sqlite/1636584487669-init.js` (3x), `system/server/src/controllers/cms.controller.ts` (3x)

### `system/server/migrations/postgres/1638975061796-coupons.js`

### `system/server/migrations/postgres/1640287895984-product-variants.js`

### `system/server/migrations/postgres/1643375773990-extend-address.js`

### `system/server/migrations/postgres/1651054394231-permissions.js`
**Imports:** `system/server/migrations/sqlite/1651054396603-permissions.js`

### `system/server/migrations/postgres/1685500033086-add_dashboard.js`

### `system/server/migrations/sqlite/1636584487669-init.js`
**Often changes with:** `system/server/src/controllers/cms.controller.ts` (4x), `system/server/migrations/mysql/1636584474808-init.js` (3x), `system/server/migrations/postgres/1636584481105-init.js` (3x), `system/core/common/src/types/entities.ts` (3x), `system/server/src/services/migration.service.ts` (3x)

### `system/server/migrations/sqlite/1638975069604-coupons.js`

### `system/server/migrations/sqlite/1640287902615-product-variants.js`

### `system/server/migrations/sqlite/1643376896650-extend-address.js`

### `system/server/migrations/sqlite/1651054396603-permissions.js`
**Imported by:** `system/server/migrations/mysql/1651054391643-permissions.js`, `system/server/migrations/postgres/1651054394231-permissions.js`

### `system/server/migrations/sqlite/1685500246809-add_dashboard.js`

### `system/server/rollup-dev.config.js`
**Symbols:** const_fn:`external`, const_fn:`getPlugins`

### `system/server/rollup-prod.config.js`
**Symbols:** const_fn:`external`, const_fn:`getPlugins`

### `system/server/src/controllers/auth.controller.ts`
**Feature:** Controllers
**Imports:** `themes/store/src/constants.js`, `system/server/src/helpers/utils.ts`
**Symbols:** class:`AuthController`
**Often changes with:** `system/server/src/controllers/cms.controller.ts` (20x), `system/server/src/services/auth.service.ts` (15x), `system/core/common/src/types/data.ts` (15x), `system/server/src/main.ts` (12x), `system/core/common/src/types/entities.ts` (12x)

### `system/server/src/controllers/cms.controller.ts`
**Feature:** Controllers
**Imports:** `themes/store/src/constants.js`, `system/server/src/helpers/reset-page.ts`, `system/server/src/helpers/utils.ts`
**Symbols:** class:`CmsController`
**Often changes with:** `system/core/common/src/types/entities.ts` (40x), `system/server/src/services/cms.service.ts` (38x), `system/core/common/src/types/data.ts` (35x), `system/core/frontend/src/api/CGraphQLClient.ts` (29x), `system/server/src/main.ts` (28x)

### `system/server/src/controllers/mock.controller.ts`
**Feature:** Controllers
**Imports:** `system/server/src/helpers/utils.ts`
**Symbols:** class:`MockController`
**Often changes with:** `system/server/src/controllers/cms.controller.ts` (10x), `system/server/src/controllers/plugin.controller.ts` (9x), `system/server/src/controllers/theme.controller.ts` (9x), `system/core/common/src/types/entities.ts` (8x), `system/server/src/controllers/auth.controller.ts` (7x)

### `system/server/src/controllers/plugin.controller.ts`
**Feature:** Controllers
**Imports:** `system/server/src/helpers/data-filters.ts`, `system/server/src/helpers/utils.ts`
**Symbols:** class:`PluginController`
**Often changes with:** `system/server/src/controllers/cms.controller.ts` (24x), `system/server/src/controllers/theme.controller.ts` (19x), `system/core/common/src/types/data.ts` (15x), `system/server/src/services/cms.service.ts` (13x), `system/server/src/main.ts` (13x)

### `system/server/src/controllers/renderer.controller.ts`
**Feature:** Controllers
**Imports:** `system/server/src/helpers/utils.ts`
**Symbols:** class:`RendererController`
**Often changes with:** `system/server/src/controllers/theme.controller.ts` (7x), `system/server/src/controllers/cms.controller.ts` (5x), `system/server/src/controllers/plugin.controller.ts` (5x), `system/core/frontend/src/api/CRestApiClient.ts` (5x), `system/server/src/controllers/auth.controller.ts` (4x)

### `system/server/src/controllers/theme.controller.ts`
**Feature:** Controllers
**Imports:** `system/server/src/helpers/utils.ts`
**Symbols:** class:`ThemeController`
**Often changes with:** `system/server/src/controllers/cms.controller.ts` (27x), `system/server/src/services/theme.service.ts` (24x), `system/core/common/src/types/data.ts` (20x), `system/server/src/controllers/plugin.controller.ts` (19x), `system/server/src/services/cms.service.ts` (18x)

### `system/server/src/dto/access-tokens.dto.ts`
**Imports:** `system/server/src/dto/user.dto.ts`
**Symbols:** class:`AccessTokensDto`, class:`UpdateAccessTokenDto`, class:`UpdateAccessTokenResponseDto`

### `system/server/src/dto/admin-cms-settings.dto.ts`
**Imports:** `system/server/src/dto/cms-settings.dto.ts`
**Symbols:** class:`AdminCmsSettingsDto`
**Often changes with:** `system/core/common/src/types/entities.ts` (4x), `system/server/src/controllers/cms.controller.ts` (4x), `system/server/src/services/cms.service.ts` (4x), `system/server/src/dto/cms-settings.dto.ts` (3x)

### `system/server/src/dto/cms-settings.dto.ts`
**Imports:** `system/server/src/dto/currency.dto.ts`
**Imported by:** `system/server/src/dto/admin-cms-settings.dto.ts`
**Symbols:** class:`CmsSettingsDto`
**Often changes with:** `system/server/src/controllers/cms.controller.ts` (3x), `system/server/src/dto/admin-cms-settings.dto.ts` (3x)

### `system/server/src/dto/cms-stats.dto.ts`
**Imports:** `system/server/src/dto/page-stats.dto.ts`
**Symbols:** class:`SalePerDayDto`, class:`CmsStatsDto`
**Often changes with:** `system/server/src/controllers/cms.controller.ts` (3x)

### `system/server/src/dto/cms-status.dto.ts`
**Imports:** `system/server/src/dto/update-info.dto.ts`
**Symbols:** class:`NotificationDto`, class:`CmsStatusDto`

### `system/server/src/dto/create-order.dto.ts`
**Symbols:** class:`CreateOrderDto`
**Often changes with:** `system/server/src/services/cms.service.ts` (8x), `system/core/common/src/types/entities.ts` (7x), `system/server/src/dto/order-total.dto.ts` (6x), `system/core/common/src/types/data.ts` (6x), `system/core/frontend/src/api/CGraphQLClient.ts` (5x)

### `system/server/src/dto/create-user.dto.ts`
**Imported by:** `system/server/src/dto/setup.dto.ts`
**Symbols:** class:`CreateUserDto`
**Often changes with:** `system/server/src/controllers/auth.controller.ts` (3x), `system/server/src/controllers/cms.controller.ts` (3x)

### `system/server/src/dto/currency.dto.ts`
**Imported by:** `system/server/src/dto/cms-settings.dto.ts`
**Symbols:** class:`CurrencyDto`

### `system/server/src/dto/dashboard-settings.dto.ts`
**Symbols:** class:`DashboardSettingsDto`

### `system/server/src/dto/export-options.dto.ts`
**Symbols:** class:`ExportOptionsDto`

### `system/server/src/dto/frontend-bundle.dto.ts`
**Symbols:** class:`FrontendBundleDto`
**Often changes with:** `system/server/src/controllers/auth.controller.ts` (3x)

### `system/server/src/dto/generate-thumbnail.dto.ts`
**Symbols:** class:`GenerateThumbnailDto`

### `system/server/src/dto/login.dto.ts`
**Symbols:** class:`LoginDto`

### `system/server/src/dto/module-info.dto.ts`
**Symbols:** class:`ModuleInfoDto`
**Often changes with:** `system/server/src/controllers/cms.controller.ts` (3x), `system/core/common/src/types/data.ts` (3x), `system/core/frontend/src/components/CGallery/CGallery.tsx` (3x)

### `system/server/src/dto/order-total.dto.ts`
**Symbols:** class:`PaymentOptionDto`, class:`ShippingOptionDto`, class:`OrderTotalDto`
**Often changes with:** `system/server/src/dto/create-order.dto.ts` (6x), `system/core/common/src/types/entities.ts` (5x), `system/server/src/services/cms.service.ts` (5x), `themes/store/src/pages/checkout.tsx` (5x), `system/core/common/src/types/data.ts` (4x)

### `system/server/src/dto/page-config.dto.ts`
**Imported by:** `system/server/src/dto/theme-config.dto.ts`
**Symbols:** class:`PageConfigDto`
**Often changes with:** `system/server/src/controllers/theme.controller.ts` (4x), `system/server/src/dto/page-info.dto.ts` (4x), `system/server/src/controllers/cms.controller.ts` (3x), `system/core/common/src/types/data.ts` (3x)

### `system/server/src/dto/page-info.dto.ts`
**Symbols:** class:`PageInfoDto`
**Often changes with:** `system/server/src/controllers/theme.controller.ts` (4x), `system/server/src/dto/page-config.dto.ts` (4x), `system/core/common/src/types/data.ts` (3x)

### `system/server/src/dto/page-stats.dto.ts`
**Imported by:** `system/server/src/dto/cms-stats.dto.ts`
**Symbols:** class:`PageStatsDto`
**Often changes with:** `system/core/common/src/types/data.ts` (3x), `system/server/src/services/cms.service.ts` (3x)

### `system/server/src/dto/permission.dto.ts`
**Symbols:** class:`PermissionDto`
**Often changes with:** `system/server/src/helpers/connect-database.ts` (4x), `system/core/backend/src/repositories/role.repository.ts` (3x), `system/core/common/src/types/entities.ts` (3x), `system/server/src/controllers/cms.controller.ts` (3x), `system/server/src/services/cms.service.ts` (3x)

### `system/server/src/dto/plugin-entity.dto.ts`
**Symbols:** class:`PluginEntityDto`

### `system/server/src/dto/plugin-info.dto.ts`
**Symbols:** class:`PluginInfoDto`

### `system/server/src/dto/reset-password.dto.ts`
**Symbols:** class:`ResetPasswordDto`

### `system/server/src/dto/server-action.dto.ts`
**Symbols:** class:`ServerActionDto`

### `system/server/src/dto/setup.dto.ts`
**Imports:** `toolkits/commerce/src/_index.ts`, `system/server/src/dto/create-user.dto.ts`
**Symbols:** class:`SetupFirstStepDto`, class:`SetupSecondStepDto`
**Often changes with:** `system/server/src/helpers/get-resolvers.ts` (3x), `system/core/common/src/types/entities.ts` (3x), `system/server/src/controllers/cms.controller.ts` (3x), `system/server/src/services/cms.service.ts` (3x)

### `system/server/src/dto/system-usage.dto.ts`
**Symbols:** class:`SystemUsageDto`
**Often changes with:** `system/server/src/main.ts` (3x)

### `system/server/src/dto/theme-config.dto.ts`
**Imports:** `system/server/src/dto/page-config.dto.ts`
**Symbols:** class:`ThemeConfigDto`

### `system/server/src/dto/theme-palette.dto.ts`
**Symbols:** class:`ThemePaletteDto`

### `system/server/src/dto/update-info.dto.ts`
**Imported by:** `system/server/src/dto/cms-status.dto.ts`
**Symbols:** class:`UpdateInfoDto`
**Often changes with:** `system/server/src/main.ts` (3x), `system/manager/src/managers/adminPanelManager.ts` (3x), `system/manager/src/managers/baseManager.ts` (3x), `system/manager/src/managers/serverManager.ts` (3x)

### `system/server/src/dto/user.dto.ts`
**Imported by:** `system/server/src/dto/access-tokens.dto.ts`
**Symbols:** class:`UserDto`
**Often changes with:** `system/server/src/services/auth.service.ts` (7x), `system/core/common/src/types/entities.ts` (6x), `system/server/src/resolvers/post.resolver.ts` (6x), `system/server/src/services/mock.service.ts` (6x), `system/core/frontend/src/api/CGraphQLClient.ts` (5x)

### `system/server/src/filters/apollo-exception.filter.ts`
**Imports:** `system/server/src/helpers/settings.ts`
**Imported by:** `system/server/src/main.ts`
**Symbols:** const_fn:`getErrorFormatter`
**Often changes with:** `system/server/src/filters/rest-exception.filter.ts` (4x), `system/server/src/main.ts` (4x)

### `system/server/src/filters/auth.interceptor.ts`
**Imports:** `system/core/backend/src/helpers/auth-roles-permissions.ts`
**Symbols:** class:`AuthInterceptor`, const_fn:`activate`

### `system/server/src/filters/rest-exception.filter.ts`
**Imports:** `system/server/src/helpers/settings.ts`
**Imported by:** `system/server/src/main.ts`
**Symbols:** class:`RestExceptionFilter`
**Often changes with:** `system/server/src/filters/apollo-exception.filter.ts` (4x), `system/server/src/main.ts` (4x)

### `system/server/src/helpers/connect-database.ts`
**Feature:** Utilities
**Imports:** `system/server/src/helpers/constants.ts`, `system/server/src/helpers/settings.ts`
**Imported by:** `system/renderer/src/server.ts`, `system/server/src/main.ts`, `system/server/tests/controller.helpers.ts`, `system/server/tests/helpers.ts`, `system/server/tests/setup.ts`
**Symbols:** const_fn:`connectDatabase`, const_fn:`checkData`, const_fn:`closeConnection`
**Often changes with:** `system/server/src/main.ts` (5x), `system/core/common/src/types/entities.ts` (5x), `system/core/frontend/src/api/CRestApiClient.ts` (4x), `system/server/src/services/auth.service.ts` (4x), `system/server/src/services/theme.service.ts` (4x)

### `system/server/src/helpers/constants.ts`
**Feature:** Utilities
**Imported by:** `system/server/src/helpers/connect-database.ts`, `system/server/src/helpers/server-manager.ts`, `system/server/src/helpers/settings.ts`
**Symbols:** const_fn:`restartServer`
**Often changes with:** `system/server/src/controllers/cms.controller.ts` (7x), `system/server/src/services/cms.service.ts` (6x), `system/server/src/main.ts` (5x), `system/server/src/proxy.ts` (4x), `system/core/common/src/types/data.ts` (4x)

### `system/server/src/helpers/cors-handler.ts`
**Feature:** Utilities
**Imported by:** `system/server/src/main.ts`

### `system/server/src/helpers/data-filters.ts`
**Feature:** Utilities
**Imports:** `system/server/src/helpers/reset-page.ts`
**Imported by:** `system/server/src/controllers/plugin.controller.ts`
**Symbols:** const_fn:`data`, const_fn:`data`
**Often changes with:** `system/core/common/src/types/entities.ts` (4x), `system/core/common/src/types/data.ts` (3x), `system/server/src/resolvers/attribute.resolver.ts` (3x), `system/server/src/resolvers/coupon.resolver.ts` (3x), `system/server/src/resolvers/custom-entity.resolver.ts` (3x)

### `system/server/src/helpers/get-controllers.ts`
**Feature:** Utilities
**Imported by:** `system/server/src/modules/restapi.module.ts`
**Symbols:** const_fn:`getControllers`, const_fn:`getServices`, const_fn:`getExports`
**Often changes with:** `system/server/src/main.ts` (4x), `system/server/src/helpers/connect-database.ts` (3x), `system/server/src/helpers/get-resolvers.ts` (3x), `system/server/src/helpers/server-manager.ts` (3x), `system/server/src/proxy.ts` (3x)

### `system/server/src/helpers/get-resolvers.ts`
**Feature:** Utilities
**Imported by:** `system/server/src/main.ts`, `system/server/tests/resolver.helpers.ts`
**Symbols:** const_fn:`getResolvers`
**Often changes with:** `system/core/common/src/types/data.ts` (5x), `system/server/src/helpers/connect-database.ts` (4x), `system/server/src/resolvers/order.resolver.ts` (4x), `system/server/src/resolvers/product.resolver.ts` (4x), `system/core/common/src/types/entities.ts` (4x)

### `system/server/src/helpers/monitor-client.ts`
**Feature:** Utilities
**Imported by:** `system/server/src/services/stats.service.ts`
**Symbols:** const_fn:`getSysInfo`, const_fn:`getSysUsageInfo`
**Often changes with:** `system/server/src/main.ts` (3x), `system/server/src/proxy.ts` (3x), `system/server/src/resolvers/order.resolver.ts` (3x)

### `system/server/src/helpers/patches.js`
**Feature:** Utilities
**Imported by:** `system/server/src/main.ts`
**Symbols:** function:`newHTTPGraphQLHead`, const_fn:`httpFromErrors`

### `system/server/src/helpers/reset-page.ts`
**Feature:** Utilities
**Imported by:** `system/server/src/controllers/cms.controller.ts`, `system/server/src/helpers/data-filters.ts`, `system/server/src/services/cms.service.ts`, `system/server/src/services/mock.service.ts`, `system/server/src/services/theme.service.ts`
**Symbols:** const_fn:`resetPageCache`, const_fn:`defaultPages`, const_fn:`resetAllPagesCache`
**Often changes with:** `system/server/src/resolvers/post.resolver.ts` (3x)

### `system/server/src/helpers/resize-image-client.ts`
**Feature:** Utilities
**Imports:** `system/server/src/resize-image.ts`
**Imported by:** `system/server/src/services/cms.service.ts`
**Symbols:** function:`createWorker`, function:`resizeImage`

### `system/server/src/helpers/server-fire-action.ts`
**Feature:** Utilities
**Imported by:** `system/server/src/services/cms.service.ts`, `system/server/src/services/plugin.service.ts`, `system/server/src/services/store.service.ts`, `system/server/src/services/theme.service.ts`

### `system/server/src/helpers/server-manager.ts`
**Feature:** Utilities
**Imports:** `themes/store/src/constants.js`, `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/helpers/paths.ts`, `system/server/src/helpers/constants.ts`, `system/server/src/helpers/settings.ts`
**Imported by:** `system/server/src/main.ts`, `system/server/src/proxy.ts`, `system/server/src/helpers/state-manager.ts`, `system/server/src/services/cms.service.ts`, `system/server/src/services/plugin.service.ts`, `system/server/src/services/theme.service.ts`
**Symbols:** const_fn:`getServerPort`, const_fn:`launchServerManager`, const_fn:`makeServer`, const_fn:`closeServer`, const_fn:`restartServer`, const_fn:`updateActiveServer`, const_fn:`serverAliveWatcher`, const_fn:`checkServerAlive`, const_fn:`childRegister`, const_fn:`childSendMessage`, const_fn:`cb`, const_fn:`parentRegisterChild`
**Often changes with:** `system/server/src/proxy.ts` (6x), `system/server/src/main.ts` (5x), `system/core/frontend/src/api/CRestApiClient.ts` (4x), `system/server/src/resolvers/post.resolver.ts` (4x), `system/server/src/resolvers/product-category.resolver.ts` (4x)

### `system/server/src/helpers/settings.ts`
**Feature:** Utilities
**Imports:** `system/core/backend/src/helpers/cms-settings.ts`, `themes/store/src/constants.js`, `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/helpers/paths.ts`, `system/server/src/helpers/constants.ts`
**Imported by:** `system/server/src/main.ts`, `system/server/src/proxy.ts`, `system/server/src/filters/apollo-exception.filter.ts`, `system/server/src/filters/rest-exception.filter.ts`, `system/server/src/helpers/connect-database.ts`, `system/server/src/helpers/server-manager.ts`, `system/server/src/modules/restapi.module.ts`
**Symbols:** const_fn:`loadEnv`, const_fn:`envMode`, const_fn:`checkConfigs`, const_fn:`checkCmsVersion`, const_fn:`getMigrationsDirName`
**Often changes with:** `system/server/src/main.ts` (6x), `system/server/src/proxy.ts` (5x), `system/server/src/services/plugin.service.ts` (5x), `system/server/src/services/theme.service.ts` (5x), `system/core/common/src/types/data.ts` (5x)

### `system/server/src/helpers/state-manager.ts`
**Feature:** Utilities
**Imports:** `system/server/src/helpers/server-manager.ts`
**Imported by:** `system/server/src/services/theme.service.ts`
**Symbols:** const_fn:`getManagerState`, const_fn:`restartService`, const_fn:`setPendingKill`, const_fn:`setPendingRestart`, const_fn:`setPendingServiceRestart`, const_fn:`startTransaction`, const_fn:`endTransaction`
**Often changes with:** `system/server/src/proxy.ts` (3x), `system/server/src/resolvers/attribute.resolver.ts` (3x), `system/server/src/resolvers/order.resolver.ts` (3x), `system/server/src/resolvers/post.resolver.ts` (3x), `system/server/src/resolvers/product-category.resolver.ts` (3x)

### `system/server/src/helpers/utils.ts`
**Feature:** Utilities
**Imported by:** `plugins/marqo/src/frontend/components/SimilarProducts.tsx`, `system/admin/src/components/entity/entityEdit/EntityEdit.tsx`, `system/admin/src/components/entity/entityTable/EntityTable.tsx`, `system/admin/src/components/inputs/TextInput/RegisteredTextInput.tsx`, `system/manager/src/tasks/buildTask.ts`, `system/manager/src/tasks/checkModules.ts`, `system/server/src/controllers/auth.controller.ts`, `system/server/src/controllers/cms.controller.ts`, `system/server/src/controllers/mock.controller.ts`, `system/server/src/controllers/plugin.controller.ts`

### `system/server/src/main.ts`
**Imports:** `system/server/src/helpers/patches.js`, `system/renderer/src/server.ts`, `system/core/backend/src/helpers/auth-roles-permissions.ts`, `system/core/backend/src/helpers/shell.ts`, `system/server/src/filters/apollo-exception.filter.ts`, `system/server/src/filters/rest-exception.filter.ts`, `system/server/src/helpers/connect-database.ts`, `system/server/src/helpers/cors-handler.ts`, `system/server/src/helpers/get-resolvers.ts`, `system/server/src/helpers/server-manager.ts`
**Symbols:** function:`bootstrap`
**Often changes with:** `system/server/src/controllers/cms.controller.ts` (28x), `system/server/src/services/cms.service.ts` (28x), `system/server/src/services/theme.service.ts` (22x), `system/server/src/services/plugin.service.ts` (21x), `system/core/frontend/src/api/CGraphQLClient.ts` (18x)

### `system/server/src/modules/app.module.ts`
**Imports:** `system/server/src/modules/restapi.module.ts`
**Imported by:** `system/server/src/main.ts`
**Symbols:** class:`AppModule`
**Often changes with:** `system/server/src/main.ts` (7x), `system/server/src/controllers/cms.controller.ts` (6x), `system/server/src/services/auth.service.ts` (6x), `system/server/src/controllers/plugin.controller.ts` (5x), `system/server/src/controllers/theme.controller.ts` (5x)

### `system/server/src/modules/restapi.module.ts`
**Imports:** `system/server/src/helpers/get-controllers.ts`, `system/server/src/helpers/settings.ts`
**Imported by:** `system/server/src/modules/app.module.ts`
**Symbols:** class:`RestApiModule`
**Often changes with:** `system/server/src/main.ts` (10x), `system/server/src/controllers/cms.controller.ts` (8x), `system/server/src/resolvers/post.resolver.ts` (8x), `system/server/src/services/auth.service.ts` (7x), `system/server/src/services/cms.service.ts` (7x)

### `system/server/src/monitor.ts`
**Imports:** `system/core/backend/src/helpers/shell.ts`
**Symbols:** const_fn:`getSysInfo`, const_fn:`getMemUsageByProcesses`, const_fn:`stats`, const_fn:`getUsageInfo`, const_fn:`getMem`, const_fn:`getLoad`, const_fn:`getFsSize`, const_fn:`getProcessesStats`
**Often changes with:** `system/server/src/main.ts` (3x), `system/server/src/proxy.ts` (3x)

### `system/server/src/proxy.ts`
**Imports:** `system/core/backend/src/helpers/cms-settings.ts`, `system/core/backend/src/helpers/logger.ts`, `system/core/backend/src/helpers/shell.ts`, `system/server/src/helpers/server-manager.ts`, `system/server/src/helpers/settings.ts`
**Symbols:** function:`main`, const_fn:`getErrorCallback`, const_fn:`proxyApiServer`
**Often changes with:** `system/server/src/main.ts` (14x), `system/server/src/services/cms.service.ts` (13x), `system/server/src/services/plugin.service.ts` (13x), `system/core/common/src/types/data.ts` (9x), `system/server/src/controllers/cms.controller.ts` (9x)

### `system/server/src/resize-image.ts`
**Imports:** `system/core/backend/src/helpers/shell.ts`
**Imported by:** `system/server/src/helpers/resize-image-client.ts`
**Symbols:** const_fn:`resize`
**Often changes with:** `system/core/common/src/types/data.ts` (3x), `system/core/common/src/types/entities.ts` (3x), `system/renderer/src/server.ts` (3x)

### `system/server/src/resolvers/attribute.resolver.ts`
**Feature:** GraphQL Resolvers
**Symbols:** class:`AttributeResolver`
**Often changes with:** `system/server/src/resolvers/post.resolver.ts` (15x), `system/server/src/resolvers/product-category.resolver.ts` (15x), `system/server/src/resolvers/product.resolver.ts` (15x), `system/server/src/resolvers/tag.resolver.ts` (14x), `system/server/src/resolvers/user.resolver.ts` (14x)

### `system/server/src/resolvers/coupon.resolver.ts`
**Feature:** GraphQL Resolvers
**Symbols:** class:`CouponResolver`
**Often changes with:** `system/server/src/resolvers/order.resolver.ts` (6x), `system/server/src/resolvers/attribute.resolver.ts` (5x), `system/server/src/resolvers/custom-entity.resolver.ts` (5x), `system/server/src/resolvers/post.resolver.ts` (5x), `system/server/src/resolvers/product-category.resolver.ts` (5x)

### `system/server/src/resolvers/custom-entity.resolver.ts`
**Feature:** GraphQL Resolvers
**Imports:** `system/server/src/helpers/utils.ts`
**Symbols:** class:`CustomEntityResolver`
**Often changes with:** `system/server/src/services/migration.service.ts` (8x), `system/server/src/resolvers/product.resolver.ts` (8x), `system/server/src/resolvers/attribute.resolver.ts` (7x), `system/server/src/resolvers/order.resolver.ts` (7x), `system/server/src/resolvers/post.resolver.ts` (7x)

### `system/server/src/resolvers/order.resolver.ts`
**Feature:** GraphQL Resolvers
**Symbols:** class:`OrderResolver`
**Often changes with:** `system/server/src/resolvers/post.resolver.ts` (19x), `system/server/src/resolvers/product.resolver.ts` (17x), `system/server/src/resolvers/product-category.resolver.ts` (16x), `system/server/src/resolvers/user.resolver.ts` (15x), `system/server/src/resolvers/tag.resolver.ts` (14x)

### `system/server/src/resolvers/post.resolver.ts`
**Feature:** GraphQL Resolvers
**Symbols:** class:`PostResolver`
**Often changes with:** `system/server/src/resolvers/product.resolver.ts` (21x), `system/server/src/resolvers/product-category.resolver.ts` (20x), `system/server/src/resolvers/order.resolver.ts` (19x), `system/server/src/resolvers/tag.resolver.ts` (18x), `system/server/src/resolvers/user.resolver.ts` (17x)

### `system/server/src/resolvers/product-category.resolver.ts`
**Feature:** GraphQL Resolvers
**Symbols:** class:`ProductCategoryResolver`, const_fn:`categories`
**Often changes with:** `system/server/src/resolvers/post.resolver.ts` (20x), `system/server/src/resolvers/product.resolver.ts` (19x), `system/server/src/resolvers/tag.resolver.ts` (17x), `system/server/src/resolvers/order.resolver.ts` (16x), `system/server/src/resolvers/attribute.resolver.ts` (15x)

### `system/server/src/resolvers/product-review.resolver.ts`
**Feature:** GraphQL Resolvers
**Symbols:** class:`ProductReviewResolver`
**Often changes with:** `system/server/src/resolvers/post.resolver.ts` (15x), `system/server/src/resolvers/product-category.resolver.ts` (15x), `system/server/src/resolvers/product.resolver.ts` (15x), `system/server/src/resolvers/attribute.resolver.ts` (13x), `system/server/src/resolvers/order.resolver.ts` (13x)

### `system/server/src/resolvers/product-variant.resolver.ts`
**Feature:** GraphQL Resolvers
**Symbols:** class:`ProductVariantResolver`

### `system/server/src/resolvers/product.resolver.ts`
**Feature:** GraphQL Resolvers
**Symbols:** class:`ProductResolver`
**Often changes with:** `system/server/src/resolvers/post.resolver.ts` (21x), `system/server/src/resolvers/product-category.resolver.ts` (19x), `system/server/src/resolvers/order.resolver.ts` (17x), `system/server/src/resolvers/tag.resolver.ts` (16x), `system/server/src/resolvers/user.resolver.ts` (16x)

### `system/server/src/resolvers/role.resolver.ts`
**Feature:** GraphQL Resolvers
**Symbols:** class:`RoleResolver`
**Often changes with:** `system/server/src/resolvers/custom-entity.resolver.ts` (6x), `system/server/src/resolvers/attribute.resolver.ts` (5x), `system/server/src/resolvers/coupon.resolver.ts` (5x), `system/server/src/resolvers/order.resolver.ts` (5x), `system/server/src/resolvers/post.resolver.ts` (5x)

### `system/server/src/resolvers/tag.resolver.ts`
**Feature:** GraphQL Resolvers
**Symbols:** class:`TagResolver`
**Often changes with:** `system/server/src/resolvers/post.resolver.ts` (18x), `system/server/src/resolvers/product-category.resolver.ts` (17x), `system/server/src/resolvers/product.resolver.ts` (16x), `system/server/src/resolvers/user.resolver.ts` (15x), `system/server/src/resolvers/attribute.resolver.ts` (14x)

### `system/server/src/resolvers/user.resolver.ts`
**Feature:** GraphQL Resolvers
**Symbols:** class:`UserResolver`
**Often changes with:** `system/server/src/resolvers/post.resolver.ts` (17x), `system/server/src/resolvers/product.resolver.ts` (16x), `system/server/src/resolvers/order.resolver.ts` (15x), `system/server/src/resolvers/product-category.resolver.ts` (15x), `system/server/src/resolvers/tag.resolver.ts` (15x)

### `system/server/src/services/auth.service.ts`
**Feature:** Service Layer
**Imports:** `themes/store/src/constants.js`
**Imported by:** `system/server/src/main.ts`, `system/server/src/services/cms.service.ts`
**Symbols:** class:`AuthService`, const_fn:`accessToken`, const_fn:`resetUserCode`, const_fn:`dbType`
**Often changes with:** `system/server/src/services/cms.service.ts` (16x), `system/server/src/controllers/cms.controller.ts` (15x), `system/server/src/main.ts` (15x), `system/server/src/controllers/auth.controller.ts` (15x), `system/server/src/services/theme.service.ts` (13x)

### `system/server/src/services/cms.service.ts`
**Feature:** Service Layer
**Imports:** `themes/store/src/constants.js`, `system/server/src/helpers/reset-page.ts`, `system/server/src/helpers/server-fire-action.ts`, `system/server/src/helpers/server-manager.ts`, `system/server/src/helpers/utils.ts`, `system/server/src/services/auth.service.ts`, `system/server/src/services/mock.service.ts`, `system/server/src/services/plugin.service.ts`, `system/server/src/services/theme.service.ts`, `system/server/src/helpers/resize-image-client.ts`
**Imported by:** `system/server/src/services/migration.service.ts`, `system/server/src/services/plugin.service.ts`, `system/server/src/services/theme.service.ts`
**Symbols:** class:`CmsService`, const_fn:`uploadHandler`, const_fn:`data`, const_fn:`data`, const_fn:`adminRole`
**Often changes with:** `system/server/src/controllers/cms.controller.ts` (38x), `system/core/common/src/types/entities.ts` (33x), `system/server/src/services/theme.service.ts` (32x), `system/server/src/main.ts` (28x), `system/server/src/services/plugin.service.ts` (26x)

### `system/server/src/services/migration.service.ts`
**Feature:** Service Layer
**Imports:** `system/server/src/helpers/utils.ts`, `system/server/src/services/cms.service.ts`
**Symbols:** class:`MigrationService`, const_fn:`metaKeys`, const_fn:`metaKeys`
**Often changes with:** `system/server/src/services/cms.service.ts` (24x), `system/core/common/src/types/entities.ts` (19x), `system/core/backend/src/repositories/product.repository.ts` (15x), `system/server/src/services/mock.service.ts` (14x), `system/server/src/resolvers/product.resolver.ts` (13x)

### `system/server/src/services/mock.service.ts`
**Feature:** Service Layer
**Imports:** `system/server/src/helpers/reset-page.ts`
**Imported by:** `system/server/src/services/cms.service.ts`
**Symbols:** class:`MockService`, const_fn:`getRandImg`, const_fn:`getRandImg`
**Often changes with:** `system/core/common/src/types/entities.ts` (30x), `system/core/frontend/src/api/CGraphQLClient.ts` (21x), `system/server/src/services/cms.service.ts` (21x), `system/server/src/controllers/cms.controller.ts` (20x), `system/server/src/resolvers/post.resolver.ts` (16x)

### `system/server/src/services/plugin.service.ts`
**Feature:** Service Layer
**Imports:** `system/server/src/helpers/server-fire-action.ts`, `system/server/src/helpers/server-manager.ts`, `system/server/src/helpers/utils.ts`, `system/server/src/services/cms.service.ts`
**Imported by:** `system/server/src/services/cms.service.ts`, `system/server/src/services/theme.service.ts`
**Symbols:** class:`PluginService`, const_fn:`source`
**Often changes with:** `system/server/src/services/theme.service.ts` (35x), `system/server/src/services/cms.service.ts` (26x), `system/server/src/controllers/cms.controller.ts` (22x), `system/server/src/main.ts` (21x), `system/server/src/controllers/theme.controller.ts` (18x)

### `system/server/src/services/renderer.service.ts`
**Feature:** Service Layer
**Imports:** `system/server/src/helpers/utils.ts`, `system/server/src/services/theme.service.ts`
**Symbols:** class:`RendererService`
**Often changes with:** `system/server/src/services/theme.service.ts` (8x), `system/server/src/services/cms.service.ts` (7x), `system/core/common/src/types/data.ts` (4x), `system/server/src/controllers/renderer.controller.ts` (4x), `system/server/src/controllers/theme.controller.ts` (4x)

### `system/server/src/services/stats.service.ts`
**Feature:** Service Layer
**Imports:** `system/server/src/helpers/monitor-client.ts`
**Symbols:** class:`StatsService`, const_fn:`getReviews`, const_fn:`getOrders`, const_fn:`getSalesPerDay`, const_fn:`getPageViews`, const_fn:`getTopPageViews`, const_fn:`getCustomers`
**Often changes with:** `system/server/src/services/cms.service.ts` (5x), `system/server/src/services/migration.service.ts` (4x), `system/server/src/services/mock.service.ts` (4x), `system/server/src/resolvers/attribute.resolver.ts` (3x), `system/server/src/resolvers/coupon.resolver.ts` (3x)

### `system/server/src/services/store.service.ts`
**Feature:** Service Layer
**Imports:** `system/server/src/helpers/server-fire-action.ts`
**Symbols:** class:`StoreService`, const_fn:`decreaseStock`
**Often changes with:** `system/server/src/controllers/cms.controller.ts` (4x), `system/server/src/resolvers/order.resolver.ts` (4x), `system/server/src/services/cms.service.ts` (4x), `system/server/src/services/mock.service.ts` (4x), `system/core/common/src/types/entities.ts` (3x)

### `system/server/src/services/theme.service.ts`
**Feature:** Service Layer
**Imports:** `system/server/src/helpers/reset-page.ts`, `system/server/src/helpers/server-fire-action.ts`, `system/server/src/helpers/server-manager.ts`, `system/server/src/helpers/state-manager.ts`, `system/server/src/helpers/utils.ts`, `system/server/src/services/cms.service.ts`, `system/server/src/services/plugin.service.ts`
**Imported by:** `system/server/src/services/cms.service.ts`, `system/server/src/services/renderer.service.ts`
**Symbols:** class:`ThemeService`
**Often changes with:** `system/server/src/services/plugin.service.ts` (35x), `system/server/src/services/cms.service.ts` (32x), `system/server/src/controllers/cms.controller.ts` (25x), `system/server/src/controllers/theme.controller.ts` (24x), `system/server/src/main.ts` (22x)

### `system/server/startup.js`
**Imports:** `system/core/backend/src/helpers/paths.ts`, `themes/store/src/constants.js`, `system/core/backend/src/helpers/shell.ts`
**Symbols:** const_fn:`buildServer`, const_fn:`isServiceBuild`, const_fn:`runDevScript`, const_fn:`buffToText`, const_fn:`main`
**Often changes with:** `system/renderer/src/generator.ts` (12x), `system/server/src/main.ts` (11x), `system/server/src/services/plugin.service.ts` (9x), `system/server/src/services/theme.service.ts` (9x), `system/server/src/services/cms.service.ts` (9x)

### `system/server/tests/controller.helpers.ts`
**Feature:** Testing
**Imports:** `system/server/src/helpers/connect-database.ts`, `system/server/tests/helpers.ts`
**Symbols:** const_fn:`setupController`, const_fn:`tearDownController`
**Often changes with:** `system/server/tests/resolver.helpers.ts` (13x), `system/server/src/main.ts` (11x), `system/server/src/services/cms.service.ts` (10x), `system/server/src/resolvers/post.resolver.ts` (8x), `system/server/src/services/auth.service.ts` (8x)

### `system/server/tests/controllers/auth.controller.spec.ts`
**Feature:** Controllers
**Imports:** `toolkits/commerce/tests/helpers.ts`
**Often changes with:** `system/server/src/services/auth.service.ts` (4x), `system/server/src/resolvers/role.resolver.ts` (3x), `system/server/src/services/cms.service.ts` (3x), `system/server/src/services/theme.service.ts` (3x), `system/server/tests/resolver.helpers.ts` (3x)

### `system/server/tests/controllers/cms.controller.spec.ts`
**Feature:** Controllers
**Imports:** `toolkits/commerce/tests/helpers.ts`
**Often changes with:** `system/server/tests/controllers/theme.controller.spec.ts` (7x), `system/server/src/main.ts` (7x), `system/server/src/services/cms.service.ts` (6x), `system/server/tests/controller.helpers.ts` (6x), `system/server/tests/controllers/plugin.controller.spec.ts` (6x)

### `system/server/tests/controllers/plugin.controller.spec.ts`
**Feature:** Controllers
**Imports:** `toolkits/commerce/tests/helpers.ts`
**Often changes with:** `system/server/tests/controllers/cms.controller.spec.ts` (6x), `system/server/tests/controllers/theme.controller.spec.ts` (6x), `system/server/tests/controller.helpers.ts` (4x), `system/server/src/main.ts` (4x), `system/server/src/services/auth.service.ts` (3x)

### `system/server/tests/controllers/theme.controller.spec.ts`
**Feature:** Controllers
**Imports:** `toolkits/commerce/tests/helpers.ts`
**Often changes with:** `system/server/tests/controllers/cms.controller.spec.ts` (7x), `system/server/tests/controllers/plugin.controller.spec.ts` (6x), `system/server/src/services/cms.service.ts` (5x), `system/server/src/controllers/theme.controller.ts` (5x), `system/server/src/services/theme.service.ts` (4x)

### `system/server/tests/helpers.ts`
**Feature:** Testing
**Imports:** `system/server/src/helpers/connect-database.ts`
**Imported by:** `system/server/tests/controller.helpers.ts`, `system/server/tests/resolver.helpers.ts`
**Symbols:** const_fn:`mockWorkingDirectory`, const_fn:`setupConnection`
**Often changes with:** `system/server/tests/resolver.helpers.ts` (7x), `system/server/src/services/cms.service.ts` (6x), `system/server/tests/controller.helpers.ts` (6x), `system/server/src/services/theme.service.ts` (3x), `system/server/tests/controllers/cms.controller.spec.ts` (3x)

### `system/server/tests/jest.config.ts`
**Feature:** Testing
**Imports:** `themes/store/src/types.ts`
**Often changes with:** `system/server/tests/controller.helpers.ts` (3x)

### `system/server/tests/resolver.helpers.ts`
**Feature:** Testing
**Imports:** `system/server/src/helpers/get-resolvers.ts`, `system/server/tests/helpers.ts`
**Symbols:** const_fn:`setupResolver`, const_fn:`tearDownResolver`
**Often changes with:** `system/server/src/services/cms.service.ts` (15x), `system/server/tests/controller.helpers.ts` (13x), `system/server/src/main.ts` (11x), `system/server/src/services/auth.service.ts` (9x), `system/server/src/services/theme.service.ts` (9x)

### `system/server/tests/resolvers/attribute.resolver.spec.ts`
**Feature:** GraphQL Resolvers
**Imports:** `toolkits/commerce/tests/helpers.ts`
**Symbols:** const_fn:`getAttributeById`
**Often changes with:** `system/server/tests/resolvers/post.resolver.spec.ts` (7x), `system/server/tests/resolvers/product.resolver.spec.ts` (7x), `system/server/tests/resolver.helpers.ts` (6x), `system/server/tests/resolvers/generic.resolver.spec.ts` (6x), `system/server/tests/resolvers/order.resolver.spec.ts` (6x)

### `system/server/tests/resolvers/coupon.resolver.spec.ts`
**Feature:** GraphQL Resolvers
**Imports:** `toolkits/commerce/tests/helpers.ts`
**Symbols:** const_fn:`getCoupon`
**Often changes with:** `system/server/src/services/cms.service.ts` (3x)

### `system/server/tests/resolvers/custom-entity.resolver.spec.ts`
**Feature:** GraphQL Resolvers
**Imports:** `toolkits/commerce/tests/helpers.ts`
**Symbols:** const_fn:`getCustomEntity`, const_fn:`updateEntity`, const_fn:`deleteEntity`, const_fn:`getFilteredCustomEntities`
**Often changes with:** `system/server/tests/resolvers/attribute.resolver.spec.ts` (4x), `system/server/tests/resolver.helpers.ts` (3x), `system/server/tests/resolvers/generic.resolver.spec.ts` (3x), `system/server/tests/resolvers/order.resolver.spec.ts` (3x), `system/server/tests/resolvers/post.resolver.spec.ts` (3x)

### `system/server/tests/resolvers/generic.resolver.spec.ts`
**Feature:** GraphQL Resolvers
**Imports:** `toolkits/commerce/tests/helpers.ts`
**Symbols:** const_fn:`getGenericById`, const_fn:`getDefaultId`, const_fn:`getDefaultSlug`, const_fn:`getGenericBySlug`
**Often changes with:** `system/server/tests/resolvers/order.resolver.spec.ts` (7x), `system/server/tests/resolvers/post.resolver.spec.ts` (7x), `system/server/tests/resolvers/product-category.resolver.spec.ts` (7x), `system/server/tests/resolvers/attribute.resolver.spec.ts` (6x), `system/server/tests/resolvers/product.resolver.spec.ts` (6x)

### `system/server/tests/resolvers/order.resolver.spec.ts`
**Feature:** GraphQL Resolvers
**Imports:** `toolkits/commerce/tests/helpers.ts`
**Symbols:** const_fn:`getOrder`
**Often changes with:** `system/server/tests/resolvers/generic.resolver.spec.ts` (7x), `system/server/tests/resolvers/attribute.resolver.spec.ts` (6x), `system/server/tests/resolvers/post.resolver.spec.ts` (6x), `system/server/tests/resolvers/product-category.resolver.spec.ts` (6x), `system/server/tests/resolvers/product.resolver.spec.ts` (6x)

### `system/server/tests/resolvers/post.resolver.spec.ts`
**Feature:** GraphQL Resolvers
**Imports:** `toolkits/commerce/tests/helpers.ts`
**Symbols:** const_fn:`getPostById`, const_fn:`getPostBySlug`
**Often changes with:** `system/server/tests/resolvers/attribute.resolver.spec.ts` (7x), `system/server/tests/resolvers/generic.resolver.spec.ts` (7x), `system/server/tests/resolvers/product.resolver.spec.ts` (7x), `system/server/tests/resolvers/order.resolver.spec.ts` (6x), `system/server/tests/resolvers/product-category.resolver.spec.ts` (6x)

### `system/server/tests/resolvers/product-category.resolver.spec.ts`
**Feature:** GraphQL Resolvers
**Imports:** `toolkits/commerce/tests/helpers.ts`
**Symbols:** const_fn:`getProductCategoryById`, const_fn:`getProductCategoryBySlug`
**Often changes with:** `system/server/tests/resolvers/generic.resolver.spec.ts` (7x), `system/server/tests/resolvers/attribute.resolver.spec.ts` (6x), `system/server/tests/resolvers/order.resolver.spec.ts` (6x), `system/server/tests/resolvers/post.resolver.spec.ts` (6x), `system/server/tests/resolvers/product.resolver.spec.ts` (6x)

### `system/server/tests/resolvers/product-review.resolver.spec.ts`
**Feature:** GraphQL Resolvers
**Imports:** `toolkits/commerce/tests/helpers.ts`
**Symbols:** const_fn:`getProductReview`
**Often changes with:** `system/server/tests/resolvers/attribute.resolver.spec.ts` (6x), `system/server/tests/resolvers/post.resolver.spec.ts` (6x), `system/server/tests/resolvers/product.resolver.spec.ts` (6x), `system/server/tests/resolver.helpers.ts` (5x), `system/server/tests/resolvers/generic.resolver.spec.ts` (5x)

### `system/server/tests/resolvers/product.resolver.spec.ts`
**Feature:** GraphQL Resolvers
**Imports:** `toolkits/commerce/tests/helpers.ts`
**Symbols:** const_fn:`getProductById`, const_fn:`getProductBySlug`
**Often changes with:** `system/server/tests/resolvers/attribute.resolver.spec.ts` (7x), `system/server/tests/resolvers/post.resolver.spec.ts` (7x), `system/server/tests/resolvers/generic.resolver.spec.ts` (6x), `system/server/tests/resolvers/order.resolver.spec.ts` (6x), `system/server/tests/resolvers/product-category.resolver.spec.ts` (6x)

### `system/server/tests/resolvers/role.resolver.spec.ts`
**Feature:** GraphQL Resolvers
**Imports:** `toolkits/commerce/tests/helpers.ts`
**Symbols:** const_fn:`getRole`

### `system/server/tests/resolvers/tag.resolver.spec.ts`
**Feature:** GraphQL Resolvers
**Imports:** `toolkits/commerce/tests/helpers.ts`
**Symbols:** const_fn:`getTag`
**Often changes with:** `system/server/tests/resolver.helpers.ts` (5x), `system/server/tests/resolvers/attribute.resolver.spec.ts` (5x), `system/server/tests/resolvers/generic.resolver.spec.ts` (5x), `system/server/tests/resolvers/order.resolver.spec.ts` (5x), `system/server/tests/resolvers/post.resolver.spec.ts` (5x)

### `system/server/tests/resolvers/user.resolver.spec.ts`
**Feature:** GraphQL Resolvers
**Imports:** `toolkits/commerce/tests/helpers.ts`
**Symbols:** const_fn:`getUser`
**Often changes with:** `system/server/tests/resolvers/attribute.resolver.spec.ts` (4x), `system/server/tests/resolvers/generic.resolver.spec.ts` (4x), `system/server/tests/resolvers/order.resolver.spec.ts` (4x), `system/server/tests/resolvers/post.resolver.spec.ts` (4x), `system/server/tests/resolvers/product-category.resolver.spec.ts` (4x)

### `system/server/tests/setup-files.ts`
**Feature:** Testing
**Symbols:** class:`Console`, class:`File`
**Often changes with:** `system/server/tests/helpers.ts` (3x), `system/server/tests/resolver.helpers.ts` (3x), `system/server/tests/setup.ts` (3x)

### `system/server/tests/setup.ts`
**Feature:** Testing
**Imports:** `system/server/src/helpers/connect-database.ts`
**Often changes with:** `system/server/tests/resolver.helpers.ts` (6x), `system/server/src/services/cms.service.ts` (5x), `system/server/src/resolvers/post.resolver.ts` (4x), `system/server/tests/controller.helpers.ts` (4x), `system/server/tests/controllers/cms.controller.spec.ts` (3x)

### `system/server/tests/teardown.ts`
**Feature:** Testing
**Often changes with:** `system/server/tests/helpers.ts` (3x)

### `system/utils/.eslintrc.js`
**Feature:** Utilities
**Often changes with:** `system/utils/src/plugins/rollup.ts` (3x), `themes/blog/.eslintrc.js` (3x), `system/server/src/services/plugin.service.ts` (3x)

### `system/utils/jest.config.ts`
**Feature:** Utilities
**Imports:** `themes/store/src/types.ts`
**Often changes with:** `system/utils/src/plugins/rollup.ts` (3x)

### `system/utils/rollup.config.js`
**Feature:** Utilities
**Often changes with:** `system/utils/src/exports.ts` (5x), `system/utils/src/plugins/rollup.ts` (5x), `system/utils/src/downloader.ts` (4x), `system/renderer/rollup.config.js` (4x), `system/server/tests/resolvers/tag.resolver.spec.ts` (3x)

### `system/utils/src/downloader.ts`
**Imports:** `system/utils/src/shared.ts`, `system/utils/src/types.ts`
**Imported by:** `system/cli/src/cli.ts`, `system/manager/src/tasks/checkModules.ts`, `system/utils/src/installer.ts`, `system/utils/tests/downloader.spec.ts`
**Symbols:** const_fn:`downloader`, const_fn:`downloadDepsRecursively`, const_fn:`downloadBundle`, const_fn:`downloadBundleZipped`
**Often changes with:** `system/utils/src/plugins/rollup.ts` (8x), `system/renderer/src/generator.ts` (7x), `system/manager/src/managers/baseManager.ts` (5x), `system/server/src/services/plugin.service.ts` (5x), `system/server/src/services/theme.service.ts` (5x)

### `system/utils/src/exports.ts`
**Purpose:** Main cjs exports to be used as "require('@cromwell/utils');"
**Imported by:** `system/admin/src/helpers/importDependencies.tsx`, `system/admin/src/router-pages/settings/pages/seo.tsx`, `system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx`
**Often changes with:** `system/utils/src/plugins/rollup.ts` (6x), `system/utils/rollup.config.js` (5x), `system/utils/src/shared.ts` (5x), `system/utils/src/downloader.ts` (4x), `system/server/src/services/cms.service.ts` (3x)

### `system/utils/src/installer.ts`
**Imports:** `system/utils/src/downloader.ts`, `system/utils/src/shared.ts`, `system/utils/src/types.ts`
**Symbols:** const_fn:`installer`, const_fn:`makeSymlink`, const_fn:`createInstallPackage`, const_fn:`removeInstallPackage`, const_fn:`main`, const_fn:`onInstallationDone`

### `system/utils/src/plugins/rollup-globals.ts`
**Feature:** Plugins
**Imports:** `system/utils/src/plugins/rollup.ts`
**Imported by:** `system/utils/src/plugins/rollup.ts`
**Symbols:** const_fn:`defaultDynamicWrapper`, function:`analyzeImport`, function:`makeGlobalName`, function:`writeSpecLocal`, function:`writeIdentifier`, function:`analyzeExportNamed`, function:`writeDynamicImport`, function:`getDynamicImportSource`, function:`importToGlobals`, function:`createPlugin`
**Often changes with:** `system/utils/src/plugins/rollup.ts` (6x), `system/utils/src/downloader.ts` (3x)

### `system/utils/src/plugins/rollup.ts`
**Feature:** Plugins
**Imports:** `system/utils/src/plugins/rollup-globals.ts`
**Imported by:** `system/manager/src/tasks/buildTask.ts`, `system/manager/src/tasks/buildTask.ts`, `system/utils/src/plugins/rollup-globals.ts`, `system/utils/tests/rollup.spec.ts`
**Symbols:** const_fn:`resolveExternal`, const_fn:`rollupConfigWrapper`, const_fn:`resolveFileExtension`
**Often changes with:** `system/renderer/src/generator.ts` (13x), `system/server/src/services/theme.service.ts` (9x), `system/server/src/services/plugin.service.ts` (9x), `system/core/common/src/types/data.ts` (8x), `system/utils/src/downloader.ts` (8x)

### `system/utils/src/shared.ts`
**Imports:** `system/utils/src/types.ts`
**Imported by:** `system/manager/src/tasks/checkModules.ts`, `system/renderer/src/generator.ts`, `system/utils/src/downloader.ts`, `system/utils/src/installer.ts`
**Symbols:** const_fn:`getNodeModuleVersion`, const_fn:`getNodeModuleNameWithVersion`, const_fn:`getDepVersion`, const_fn:`getDepNameWithVersion`, const_fn:`getModuleInfo`, const_fn:`collectDeps`, const_fn:`hoistDeps`, const_fn:`getCromwellaConfigSync`, const_fn:`globPackages`, const_fn:`addDir`, const_fn:`collectPackagesInfo`
**Often changes with:** `system/utils/src/plugins/rollup.ts` (6x), `system/renderer/src/generator.ts` (6x), `system/utils/src/exports.ts` (5x), `system/utils/src/downloader.ts` (4x), `system/utils/tests/downloader.spec.ts` (4x)

### `system/utils/src/static.ts`
**Imports:** `system/core/backend/src/helpers/paths.ts`, `system/core/frontend/src/api/CRestApiClient.ts`
**Imported by:** `system/admin/src/startup/server.ts`, `system/renderer/src/server.ts`
**Symbols:** function:`resolvePublicFilePathToServe`, function:`fastifySendFile`, function:`vanillaSendFile`

### `system/utils/src/types.ts`
**Imported by:** `system/utils/src/downloader.ts`, `system/utils/src/installer.ts`, `system/utils/src/shared.ts`

### `system/utils/tests/downloader.spec.ts`
**Feature:** Testing
**Imports:** `system/utils/src/downloader.ts`, `system/utils/tests/helpers.ts`
**Often changes with:** `system/utils/src/downloader.ts` (5x), `system/utils/src/plugins/rollup.ts` (5x), `system/utils/src/shared.ts` (4x), `system/utils/rollup.config.js` (3x), `system/utils/src/exports.ts` (3x)

### `system/utils/tests/helpers.ts`
**Feature:** Testing
**Imported by:** `system/utils/tests/downloader.spec.ts`, `system/utils/tests/rollup.spec.ts`
**Symbols:** const_fn:`mockWorkingDirectory`, const_fn:`tearDown`

### `system/utils/tests/rollup.spec.ts`
**Feature:** Testing
**Imports:** `system/utils/src/plugins/rollup.ts`, `system/utils/tests/helpers.ts`
**Often changes with:** `system/utils/src/plugins/rollup.ts` (6x), `system/utils/src/exports.ts` (3x)

### `themes/blog/.eslintrc.js`
**Often changes with:** `system/utils/.eslintrc.js` (3x)

### `themes/blog/cromwell.config.js`
**Often changes with:** `themes/store/cromwell.config.js` (9x), `themes/blog/src/pages/_app.tsx` (4x), `system/utils/src/plugins/rollup.ts` (3x), `themes/blog/src/components/footer/Footer.tsx` (3x), `themes/blog/src/pages/index.tsx` (3x)

### `themes/blog/next-env.d.ts`
**Purpose:** / <reference types="next" />
/ <reference types="next/types/global" />
/ <reference types="next/image-types/global" />

### `themes/blog/src/components/footer/Footer.tsx`
**Symbols:** function:`Footer`
**Often changes with:** `system/core/common/src/types/blocks.ts` (6x), `themes/blog/src/components/header/Header.tsx` (5x), `themes/blog/src/components/postCard/PostCard.tsx` (5x), `themes/blog/src/pages/index.tsx` (5x), `themes/blog/src/pages/tag/[slug].tsx` (5x)

### `themes/blog/src/components/header/Header.tsx`
**Imports:** `toolkits/commerce/src/base/icons.tsx`, `themes/blog/src/components/header/HeaderSearch.tsx`
**Symbols:** const_fn:`Header`, const_fn:`handleCloseMenu`, const_fn:`handleOpenMenu`, function:`HideOnScroll`
**Often changes with:** `themes/blog/src/components/postCard/PostCard.tsx` (8x), `themes/blog/src/pages/tag/[slug].tsx` (7x), `themes/store/src/components/header/Header.tsx` (7x), `themes/blog/src/pages/index.tsx` (6x), `themes/store/src/components/header/MobileHeader.tsx` (6x)

### `themes/blog/src/components/header/HeaderSearch.tsx`
**Imports:** `system/admin/src/components/inputs/DateInput/styles.ts`
**Imported by:** `themes/blog/src/components/header/Header.tsx`
**Symbols:** class:`HeaderSearch`
**Often changes with:** `themes/blog/src/pages/search.tsx` (5x), `themes/blog/src/pages/tag/[slug].tsx` (5x), `themes/store/src/components/modals/productQuickView/ProductQuickView.tsx` (5x), `themes/blog/src/components/header/Header.tsx` (4x), `themes/blog/src/pages/index.tsx` (4x)

### `themes/blog/src/components/icons.tsx`
**Feature:** UI Components

### `themes/blog/src/components/layout/Layout.tsx`
**Imports:** `themes/store/src/components/footer/Footer.tsx`, `themes/store/src/components/header/Header.tsx`
**Symbols:** function:`Layout`
**Often changes with:** `system/utils/src/plugins/rollup.ts` (4x), `themes/blog/src/components/header/Header.tsx` (4x), `themes/blog/src/pages/index.tsx` (4x), `themes/blog/src/pages/search.tsx` (4x), `themes/blog/src/pages/tag/[slug].tsx` (4x)

### `themes/blog/src/components/loadbox/Loadbox.tsx`
**Feature:** Database
**Imports:** `system/admin/src/components/inputs/DateInput/styles.ts`
**Symbols:** const_fn:`LoadBox`
**Often changes with:** `themes/blog/src/components/header/Header.tsx` (3x), `themes/blog/src/components/layout/Layout.tsx` (3x), `themes/blog/src/components/pagination/Pagination.tsx` (3x)

### `themes/blog/src/components/pagination/Pagination.tsx`
**Symbols:** const_fn:`Pagination`
**Often changes with:** `themes/blog/src/components/header/Header.tsx` (3x), `themes/blog/src/components/layout/Layout.tsx` (3x), `themes/blog/src/components/loadbox/Loadbox.tsx` (3x)

### `themes/blog/src/components/postCard/PostCard.tsx`
**Imports:** `toolkits/commerce/src/base/icons.tsx`
**Symbols:** const_fn:`PostCard`, const_fn:`imageLoader`, const_fn:`PostInfo`
**Often changes with:** `themes/blog/src/pages/tag/[slug].tsx` (11x), `themes/store/src/components/postCard/PostCard.tsx` (11x), `themes/blog/src/components/header/Header.tsx` (8x), `themes/blog/src/pages/search.tsx` (7x), `themes/blog/src/pages/post/[slug].tsx` (7x)

### `themes/blog/src/declarations.d.ts`

### `themes/blog/src/helpers/createEmotionCache.ts`
**Feature:** Utilities
**Symbols:** function:`createEmotionCache`

### `themes/blog/src/helpers/getPosts.ts`
**Feature:** Utilities
**Symbols:** const_fn:`handleGetFilteredPosts`
**Often changes with:** `themes/blog/src/pages/search.tsx` (5x), `themes/blog/src/pages/tag/[slug].tsx` (5x), `themes/blog/src/components/header/Header.tsx` (4x), `themes/blog/src/components/postCard/PostCard.tsx` (4x), `themes/blog/src/pages/index.tsx` (4x)

### `themes/blog/src/helpers/theme.ts`
**Feature:** Utilities
**Imports:** `system/admin/src/components/inputs/DateInput/styles.ts`
**Symbols:** const_fn:`getTheme`

### `themes/blog/src/pages/404.tsx`
**Feature:** Pages
**Imports:** `themes/store/src/components/layout/Layout.tsx`, `themes/blog/src/pages/_app.tsx`
**Often changes with:** `themes/blog/src/pages/index.tsx` (3x), `themes/blog/src/pages/pages/[slug].tsx` (3x), `themes/blog/src/pages/post/[slug].tsx` (3x), `themes/blog/src/pages/search.tsx` (3x), `themes/blog/src/pages/tag/[slug].tsx` (3x)

### `themes/blog/src/pages/_app.tsx`
**Feature:** Pages
**Imports:** `themes/store/src/helpers/createEmotionCache.ts`, `themes/store/src/helpers/theme.ts`
**Imported by:** `themes/blog/src/pages/404.tsx`, `themes/blog/src/pages/index.tsx`, `themes/blog/src/pages/search.tsx`
**Symbols:** function:`App`
**Often changes with:** `themes/store/src/pages/_app.tsx` (6x), `themes/blog/src/pages/index.tsx` (5x), `themes/blog/src/pages/pages/[slug].tsx` (5x), `themes/blog/src/pages/tag/[slug].tsx` (5x), `themes/store/src/pages/category/[slug].tsx` (5x)

### `themes/blog/src/pages/_document.tsx`
**Feature:** Pages
**Imports:** `system/renderer/src/helpers/document.tsx`, `themes/store/src/helpers/createEmotionCache.ts`, `themes/store/src/helpers/theme.ts`
**Symbols:** class:`BlogDocument`
**Often changes with:** `themes/blog/src/pages/tag/[slug].tsx` (7x), `themes/blog/src/pages/post/[slug].tsx` (5x), `themes/blog/src/components/header/Header.tsx` (4x), `themes/blog/src/pages/pages/[slug].tsx` (4x), `themes/blog/src/pages/search.tsx` (4x)

### `themes/blog/src/pages/index.tsx`
**Feature:** Pages
**Imports:** `themes/store/src/components/layout/Layout.tsx`, `themes/store/src/components/postCard/PostCard.tsx`, `themes/store/src/helpers/getPosts.ts`, `themes/blog/src/pages/_app.tsx`
**Symbols:** const_fn:`otherPosts`
**Often changes with:** `themes/blog/src/pages/tag/[slug].tsx` (11x), `themes/blog/src/pages/post/[slug].tsx` (9x), `themes/blog/src/pages/search.tsx` (8x), `themes/store/src/pages/blog/[slug].tsx` (7x), `themes/blog/src/components/header/Header.tsx` (6x)

### `themes/blog/src/pages/pages/[slug].tsx`
**Feature:** Pages
**Imports:** `themes/store/src/components/layout/Layout.tsx`, `themes/store/src/pages/_app.tsx`
**Symbols:** const_fn:`getStaticPaths`
**Often changes with:** `themes/blog/src/pages/tag/[slug].tsx` (7x), `themes/blog/src/pages/post/[slug].tsx` (6x), `themes/blog/src/pages/_app.tsx` (5x), `themes/blog/src/pages/index.tsx` (5x), `themes/store/src/pages/blog/[slug].tsx` (5x)

### `themes/blog/src/pages/post/[slug].tsx`
**Imports:** `themes/store/src/components/layout/Layout.tsx`, `themes/store/src/components/postCard/PostCard.tsx`, `themes/store/src/pages/_app.tsx`
**Symbols:** const_fn:`getStaticPaths`
**Often changes with:** `themes/store/src/pages/blog/[slug].tsx` (17x), `themes/blog/src/pages/tag/[slug].tsx` (15x), `themes/store/src/pages/tag/[slug].tsx` (13x), `themes/store/src/pages/product/[slug].tsx` (12x), `themes/blog/src/pages/index.tsx` (9x)

### `themes/blog/src/pages/search.tsx`
**Feature:** Pages
**Imports:** `themes/store/src/components/layout/Layout.tsx`, `toolkits/commerce/src/mui/Pagination/Pagination.tsx`, `themes/store/src/components/postCard/PostCard.tsx`, `themes/store/src/helpers/getPosts.ts`, `themes/blog/src/pages/_app.tsx`
**Imported by:** `themes/blog/tests/pages/search.test.tsx`
**Symbols:** const_fn:`updateList`, const_fn:`handleChangeTags`, const_fn:`handleGetPosts`, const_fn:`handleChangeSort`, const_fn:`handleTagClick`, function:`useForceUpdate`
**Often changes with:** `themes/blog/src/pages/tag/[slug].tsx` (14x), `themes/store/src/pages/blog.tsx` (11x), `themes/store/src/pages/tag/[slug].tsx` (9x), `themes/blog/src/pages/index.tsx` (8x), `themes/blog/src/pages/post/[slug].tsx` (8x)

### `themes/blog/src/pages/tag/[slug].tsx`
**Imports:** `themes/store/src/components/layout/Layout.tsx`, `toolkits/commerce/src/mui/Pagination/Pagination.tsx`, `themes/store/src/components/postCard/PostCard.tsx`, `themes/store/src/helpers/getPosts.ts`, `themes/store/src/pages/_app.tsx`
**Symbols:** const_fn:`resetList`, const_fn:`handleGetPosts`, const_fn:`handleChangeSort`, const_fn:`getStaticPaths`
**Often changes with:** `themes/store/src/pages/tag/[slug].tsx` (16x), `themes/blog/src/pages/post/[slug].tsx` (15x), `themes/blog/src/pages/search.tsx` (14x), `themes/store/src/pages/blog/[slug].tsx` (14x), `themes/store/src/pages/blog.tsx` (12x)

### `themes/blog/src/types.ts`

### `themes/blog/tests/jest.config.ts`
**Feature:** Testing
**Imports:** `themes/store/src/types.ts`

### `themes/blog/tests/pages/index.test.tsx`
**Feature:** Pages
**Imports:** `website/src/theme/Footer/index.tsx`

### `themes/blog/tests/pages/pages-slug.test.tsx`
**Feature:** Pages

### `themes/blog/tests/pages/post-slug.test.tsx`
**Feature:** Pages

### `themes/blog/tests/pages/search.test.tsx`
**Feature:** Pages
**Imports:** `themes/blog/src/pages/search.tsx`

### `themes/blog/tests/pages/tag-slug.test.tsx`
**Feature:** Pages

### `themes/blog/tests/setup.ts`
**Feature:** Testing

### `themes/store/.eslintrc.js`
**Feature:** State Management

### `themes/store/cromwell.config.js`
**Feature:** State Management
**Often changes with:** `themes/blog/cromwell.config.js` (9x), `themes/store/src/components/productCard/ProductCard.tsx` (8x), `themes/store/src/pages/product/[slug].tsx` (8x), `system/server/src/controllers/cms.controller.ts` (7x), `system/server/src/services/cms.service.ts` (7x)

### `themes/store/next-env.d.ts`
**Purpose:** / <reference types="next" />
/ <reference types="next/types/global" />
/ <reference types="next/image-types/global" />
**Feature:** State Management

### `themes/store/next.config.js`
**Feature:** State Management

### `themes/store/src/admin-panel/index.tsx`
**Feature:** Administration
**Symbols:** const_fn:`AdminPanel`

### `themes/store/src/components/footer/Footer.tsx`
**Imported by:** `themes/blog/src/components/layout/Layout.tsx`, `themes/store/src/components/layout/Layout.tsx`
**Symbols:** const_fn:`Footer`
**Often changes with:** `themes/store/src/components/header/Header.tsx` (6x), `themes/store/src/components/header/MobileHeader.tsx` (6x), `themes/store/src/components/layout/Layout.tsx` (6x), `themes/store/src/components/postCard/PostCard.tsx` (5x), `system/core/common/src/types/blocks.ts` (5x)

### `themes/store/src/components/header/Header.tsx`
**Imports:** `themes/store/src/helpers/AppState.ts`, `themes/store/src/components/header/MobileHeader.tsx`
**Imported by:** `themes/blog/src/components/layout/Layout.tsx`, `themes/store/src/components/layout/Layout.tsx`
**Symbols:** const_fn:`Header`, const_fn:`handleCartClick`, const_fn:`handleLogout`, const_fn:`handleOpenWishlist`, const_fn:`handleOpenWatched`, const_fn:`handleOpenSignIn`
**Often changes with:** `themes/store/src/components/header/MobileHeader.tsx` (11x), `themes/store/src/components/postCard/PostCard.tsx` (11x), `themes/store/src/components/layout/Layout.tsx` (10x), `themes/store/src/components/modals/cart/CartModal.tsx` (10x), `themes/store/src/components/modals/wishlist/WishlistModal.tsx` (9x)

### `themes/store/src/components/header/MobileHeader.tsx`
**Imports:** `themes/store/src/helpers/AppState.ts`, `toolkits/commerce/src/base/icons.tsx`
**Imported by:** `themes/store/src/components/header/Header.tsx`
**Symbols:** const_fn:`MobileHeader`, const_fn:`handleCloseMenu`, const_fn:`handleOpenMenu`, const_fn:`handleOpenCart`, const_fn:`handleOpenWishlist`, const_fn:`handleOpenWatched`, function:`HideOnScroll`
**Often changes with:** `themes/store/src/components/header/Header.tsx` (11x), `themes/store/src/components/modals/wishlist/WishlistModal.tsx` (9x), `themes/store/src/components/postCard/PostCard.tsx` (9x), `themes/store/src/components/productCard/ProductCard.tsx` (9x), `themes/store/src/components/modals/cart/CartModal.tsx` (8x)

### `themes/store/src/components/icons.tsx`
**Feature:** UI Components
**Often changes with:** `themes/store/src/components/modals/signIn/SignIn.tsx` (3x)

### `themes/store/src/components/layout/Layout.tsx`
**Imports:** `themes/store/src/helpers/AppState.ts`, `themes/store/src/components/footer/Footer.tsx`, `themes/store/src/components/header/Header.tsx`, `themes/store/src/components/modals/cart/CartModal.tsx`, `themes/store/src/components/modals/productQuickView/ProductQuickView.tsx`, `themes/store/src/components/modals/viewed/ViewedModal.tsx`, `themes/store/src/components/modals/wishlist/WishlistModal.tsx`, `themes/store/src/components/modals/signIn/SignIn.tsx`
**Imported by:** `themes/blog/src/pages/404.tsx`, `themes/blog/src/pages/index.tsx`, `themes/blog/src/pages/search.tsx`, `themes/blog/src/pages/pages/[slug].tsx`, `themes/blog/src/pages/post/[slug].tsx`, `themes/blog/src/pages/tag/[slug].tsx`, `themes/store/src/pages/404.tsx`, `themes/store/src/pages/account.tsx`, `themes/store/src/pages/blog.tsx`, `themes/store/src/pages/checkout.tsx`
**Symbols:** function:`Layout`
**Often changes with:** `themes/store/src/components/productDetails/ProductDetails.tsx` (12x), `themes/store/src/components/header/Header.tsx` (10x), `themes/store/src/components/productCard/ProductCard.tsx` (10x), `themes/store/src/components/header/MobileHeader.tsx` (7x), `themes/store/src/components/modals/wishlist/WishlistModal.tsx` (7x)

### `themes/store/src/components/loadbox/Loadbox.tsx`
**Feature:** Database
**Imports:** `system/admin/src/components/inputs/DateInput/styles.ts`
**Symbols:** const_fn:`LoadBox`
**Often changes with:** `themes/store/src/components/layout/Layout.tsx` (5x), `themes/store/src/components/header/Header.tsx` (4x), `themes/store/src/components/header/MobileHeader.tsx` (4x), `themes/store/src/components/modals/cart/CartModal.tsx` (4x), `themes/store/src/components/postCard/PostCard.tsx` (4x)

### `themes/store/src/components/modals/baseModal/Modal.tsx`
**Imported by:** `system/admin/src/components/cmsInfo/CmsInfo.tsx`, `system/admin/src/components/fileManager/FileManager.tsx`, `system/admin/src/components/pluginSettingsLayout/PluginSettingsLayout.tsx`, `system/admin/src/components/systemMonitor/SystemMonitor.tsx`, `system/admin/src/router-pages/pluginMarket/PluginMarket.tsx`, `system/admin/src/router-pages/reviewList/ReviewList.tsx`, `system/admin/src/router-pages/themeMarket/ThemeMarket.tsx`, `themes/store/src/components/modals/cart/CartModal.tsx`, `themes/store/src/components/modals/productQuickView/ProductQuickView.tsx`, `themes/store/src/components/modals/signIn/SignIn.tsx`
**Symbols:** const_fn:`Modal`, const_fn:`setBlur`
**Often changes with:** `themes/store/src/components/header/Header.tsx` (5x), `themes/store/src/components/layout/Layout.tsx` (5x), `themes/store/src/components/modals/cart/CartModal.tsx` (5x), `themes/store/src/components/productDetails/ProductDetails.tsx` (5x), `themes/store/src/components/header/MobileHeader.tsx` (4x)

### `themes/store/src/components/modals/cart/CartModal.tsx`
**Feature:** Shopping Cart
**Imports:** `themes/store/src/helpers/AppState.ts`, `toolkits/commerce/src/base/icons.tsx`, `themes/store/src/components/modals/baseModal/Modal.tsx`
**Imported by:** `themes/store/src/components/layout/Layout.tsx`
**Symbols:** const_fn:`handleCartClose`
**Often changes with:** `themes/store/src/components/header/Header.tsx` (10x), `themes/store/src/components/postCard/PostCard.tsx` (10x), `themes/store/src/components/header/MobileHeader.tsx` (8x), `themes/store/src/components/modals/wishlist/WishlistModal.tsx` (8x), `themes/store/src/components/productCard/ProductCard.tsx` (8x)

### `themes/store/src/components/modals/productQuickView/ProductQuickView.tsx`
**Imports:** `themes/store/src/helpers/AppState.ts`, `toolkits/commerce/src/base/icons.tsx`, `toolkits/commerce/src/mui/Loadbox/Loadbox.tsx`, `themes/store/src/components/productDetails/ProductDetails.tsx`, `themes/store/src/components/modals/baseModal/Modal.tsx`
**Imported by:** `themes/store/src/components/layout/Layout.tsx`
**Symbols:** const_fn:`handleClose`, const_fn:`getData`
**Often changes with:** `themes/store/src/components/header/Header.tsx` (7x), `themes/store/src/components/modals/cart/CartModal.tsx` (7x), `themes/store/src/components/productCard/ProductCard.tsx` (7x), `themes/store/src/components/header/MobileHeader.tsx` (6x), `themes/store/src/components/layout/Layout.tsx` (6x)

### `themes/store/src/components/modals/signIn/PasswordField.tsx`
**Imports:** `toolkits/commerce/src/base/icons.tsx`
**Imported by:** `themes/store/src/components/modals/signIn/SignIn.tsx`
**Symbols:** const_fn:`PasswordField`, const_fn:`handleClickShowPassword`

### `themes/store/src/components/modals/signIn/SignIn.tsx`
**Imports:** `themes/store/src/helpers/AppState.ts`, `themes/store/src/components/toast/toast.tsx`, `themes/store/src/components/modals/baseModal/Modal.tsx`, `themes/store/src/components/modals/signIn/PasswordField.tsx`
**Imported by:** `themes/store/src/components/layout/Layout.tsx`
**Symbols:** const_fn:`handleTabChange`, const_fn:`onSignUpSuccess`, const_fn:`handleClose`
**Often changes with:** `themes/store/src/components/header/Header.tsx` (7x), `themes/store/src/components/postCard/PostCard.tsx` (6x), `system/server/src/services/auth.service.ts` (6x), `themes/store/src/components/modals/cart/CartModal.tsx` (5x), `themes/store/src/components/modals/productQuickView/ProductQuickView.tsx` (5x)

### `themes/store/src/components/modals/viewed/ViewedModal.tsx`
**Imports:** `themes/store/src/helpers/AppState.ts`, `toolkits/commerce/src/base/ProductCard/ProductCard.tsx`, `toolkits/commerce/src/base/icons.tsx`, `themes/store/src/components/modals/baseModal/Modal.tsx`
**Imported by:** `themes/store/src/components/layout/Layout.tsx`
**Symbols:** const_fn:`handleClose`
**Often changes with:** `themes/store/src/components/modals/wishlist/WishlistModal.tsx` (3x), `themes/store/src/components/productCard/ProductCard.tsx` (3x), `themes/store/src/components/productDetails/ProductDetails.tsx` (3x)

### `themes/store/src/components/modals/wishlist/WishlistModal.tsx`
**Imports:** `themes/store/src/helpers/AppState.ts`, `toolkits/commerce/src/base/icons.tsx`, `toolkits/commerce/src/base/ProductCard/ProductCard.tsx`, `themes/store/src/components/modals/baseModal/Modal.tsx`
**Imported by:** `themes/store/src/components/layout/Layout.tsx`
**Symbols:** const_fn:`handleClose`
**Often changes with:** `themes/store/src/components/productCard/ProductCard.tsx` (10x), `themes/store/src/components/header/Header.tsx` (9x), `themes/store/src/components/header/MobileHeader.tsx` (9x), `themes/store/src/components/modals/cart/CartModal.tsx` (8x), `themes/store/src/components/postCard/PostCard.tsx` (8x)

### `themes/store/src/components/postCard/PostCard.tsx`
**Imports:** `toolkits/commerce/src/base/icons.tsx`
**Imported by:** `themes/blog/src/pages/index.tsx`, `themes/blog/src/pages/search.tsx`, `themes/blog/src/pages/post/[slug].tsx`, `themes/blog/src/pages/tag/[slug].tsx`, `themes/store/src/pages/_app.tsx`, `themes/store/src/pages/blog.tsx`, `themes/store/src/pages/blog/[slug].tsx`, `themes/store/src/pages/tag/[slug].tsx`
**Symbols:** const_fn:`PostCard`, const_fn:`imageLoader`, const_fn:`PostInfo`
**Often changes with:** `themes/blog/src/components/postCard/PostCard.tsx` (11x), `themes/store/src/components/header/Header.tsx` (11x), `themes/store/src/pages/blog.tsx` (10x), `themes/store/src/components/modals/cart/CartModal.tsx` (10x), `themes/store/src/components/productCard/ProductCard.tsx` (10x)

### `themes/store/src/components/productCard/ProductCard.tsx`
**Imports:** `themes/store/src/helpers/AppState.ts`
**Symbols:** const_fn:`ProductCard`, const_fn:`handleOpenQuickView`
**Often changes with:** `themes/store/src/components/productDetails/ProductDetails.tsx` (12x), `themes/store/src/pages/checkout.tsx` (11x), `themes/store/src/pages/product/[slug].tsx` (11x), `themes/store/src/components/layout/Layout.tsx` (10x), `themes/store/src/components/modals/wishlist/WishlistModal.tsx` (10x)

### `themes/store/src/components/productDetails/ProductDetails.tsx`
**Imports:** `themes/store/src/helpers/AppState.ts`
**Imported by:** `themes/store/src/components/modals/productQuickView/ProductQuickView.tsx`, `themes/store/src/pages/product/[slug].tsx`
**Symbols:** function:`ProductDetails`, const_fn:`scrollToReviews`, const_fn:`onTitleClick`
**Often changes with:** `themes/store/src/components/layout/Layout.tsx` (12x), `themes/store/src/components/productCard/ProductCard.tsx` (12x), `themes/store/src/pages/product/[slug].tsx` (12x), `themes/store/src/pages/checkout.tsx` (10x), `themes/store/src/pages/account.tsx` (9x)

### `themes/store/src/components/toast/toast.tsx`
**Imported by:** `system/admin/src/components/entity/entityEdit/EntityEdit.tsx`, `system/admin/src/components/entity/entityTable/EntityTable.tsx`, `system/admin/src/components/fileManager/FileManager.tsx`, `system/admin/src/components/layout/hooks/useAppState.ts`, `system/admin/src/components/notificationCenter/NotificationCenter.tsx`, `system/admin/src/components/pluginSettingsLayout/PluginSettingsLayout.tsx`, `system/admin/src/components/topbar/Topbar.tsx`, `system/admin/src/helpers/editor/editor.ts`, `system/admin/src/router-pages/login/LoginPage.tsx`, `system/admin/src/router-pages/login/components/ForgotPassForm.tsx`
**Symbols:** class:`Toast`
**Often changes with:** `themes/store/src/pages/checkout.tsx` (3x)

### `themes/store/src/constants.js`
**Imported by:** `plugins/marqo/src/admin/index.tsx`, `plugins/marqo/src/frontend/utils.ts`, `plugins/paypal/src/admin/index.tsx`, `plugins/paypal/src/backend/index.ts`, `plugins/paypal/src/backend/actions/create-payment.action.ts`, `plugins/product-filter/src/admin/widgets/SettingsPage.tsx`, `plugins/product-filter/src/frontend/components/Filter.tsx`, `plugins/stripe/src/admin/index.tsx`, `plugins/stripe/src/backend/index.ts`, `plugins/stripe/src/backend/actions/create-payment.action.ts`
**Often changes with:** `themes/store/src/components/layout/Layout.tsx` (3x), `themes/store/src/pages/_app.tsx` (3x), `themes/store/src/pages/blog.tsx` (3x), `themes/store/src/pages/blog/[slug].tsx` (3x), `themes/store/src/pages/category/[slug].tsx` (3x)

### `themes/store/src/declarations.d.ts`

### `themes/store/src/helpers/AppState.ts`
**Feature:** Utilities
**Imported by:** `themes/store/src/components/header/Header.tsx`, `themes/store/src/components/header/MobileHeader.tsx`, `themes/store/src/components/layout/Layout.tsx`, `themes/store/src/components/modals/cart/CartModal.tsx`, `themes/store/src/components/modals/productQuickView/ProductQuickView.tsx`, `themes/store/src/components/modals/signIn/SignIn.tsx`, `themes/store/src/components/modals/viewed/ViewedModal.tsx`, `themes/store/src/components/modals/wishlist/WishlistModal.tsx`, `themes/store/src/components/productCard/ProductCard.tsx`, `themes/store/src/components/productDetails/ProductDetails.tsx`
**Symbols:** class:`State`
**Often changes with:** `themes/store/src/components/layout/Layout.tsx` (6x), `themes/store/src/components/productDetails/ProductDetails.tsx` (5x), `themes/store/src/components/header/Header.tsx` (4x), `themes/store/src/components/header/MobileHeader.tsx` (4x), `themes/store/src/pages/_app.tsx` (4x)

### `themes/store/src/helpers/createEmotionCache.ts`
**Feature:** Utilities
**Imported by:** `themes/blog/src/pages/_app.tsx`, `themes/blog/src/pages/_document.tsx`, `themes/store/src/pages/_app.tsx`, `themes/store/src/pages/_document.tsx`
**Symbols:** function:`createEmotionCache`

### `themes/store/src/helpers/forceUpdate.ts`
**Feature:** Utilities
**Imported by:** `system/admin/src/components/entity/entityEdit/components/InputField.tsx`, `system/admin/src/components/entity/entityTable/components/TableHeader.tsx`, `system/admin/src/components/inputs/ColorInput.tsx`, `system/admin/src/components/inputs/Search/ListItem.tsx`, `system/admin/src/components/layout/hooks/useAppState.ts`, `system/admin/src/components/sideNav/SideNav.tsx`, `system/admin/src/components/topbar/Topbar.tsx`, `system/admin/src/helpers/customFields/RenderCustomFields.tsx`, `system/admin/src/router-pages/categoryList/CategoryList.tsx`, `system/admin/src/router-pages/categoryList/components/CategoryItem.tsx`
**Symbols:** function:`useForceUpdate`

### `themes/store/src/helpers/getPosts.ts`
**Feature:** Utilities
**Imported by:** `themes/blog/src/pages/index.tsx`, `themes/blog/src/pages/search.tsx`, `themes/blog/src/pages/tag/[slug].tsx`, `themes/store/src/pages/blog.tsx`, `themes/store/src/pages/tag/[slug].tsx`
**Symbols:** const_fn:`handleGetFilteredPosts`
**Often changes with:** `themes/store/src/pages/blog.tsx` (6x), `themes/store/src/pages/blog/[slug].tsx` (6x), `themes/store/src/pages/tag/[slug].tsx` (6x), `themes/store/src/components/modals/productQuickView/ProductQuickView.tsx` (4x), `themes/store/src/components/modals/wishlist/WishlistModal.tsx` (4x)

### `themes/store/src/helpers/theme.ts`
**Feature:** Utilities
**Imports:** `system/admin/src/components/inputs/DateInput/styles.ts`
**Imported by:** `themes/blog/src/pages/_app.tsx`, `themes/blog/src/pages/_document.tsx`, `themes/store/src/pages/_app.tsx`, `themes/store/src/pages/_document.tsx`
**Symbols:** const_fn:`getTheme`
**Often changes with:** `themes/store/src/pages/checkout.tsx` (3x)

### `themes/store/src/pages/404.tsx`
**Feature:** Pages
**Imports:** `themes/store/src/components/layout/Layout.tsx`, `themes/store/src/pages/_app.tsx`
**Often changes with:** `themes/store/src/pages/account.tsx` (4x), `themes/store/src/pages/blog.tsx` (4x), `themes/store/src/pages/blog/[slug].tsx` (4x), `themes/store/src/pages/category/[slug].tsx` (4x), `themes/store/src/pages/checkout.tsx` (4x)

### `themes/store/src/pages/_app.tsx`
**Feature:** Pages
**Imports:** `system/admin/src/components/inputs/DateInput/styles.ts`, `themes/store/src/components/postCard/PostCard.tsx`, `toolkits/commerce/src/base/ProductCard/ProductCard.tsx`, `themes/store/src/components/toast/toast.tsx`, `themes/store/src/helpers/createEmotionCache.ts`, `themes/store/src/helpers/theme.ts`
**Imported by:** `themes/blog/src/pages/pages/[slug].tsx`, `themes/blog/src/pages/post/[slug].tsx`, `themes/blog/src/pages/tag/[slug].tsx`, `themes/store/src/pages/404.tsx`, `themes/store/src/pages/account.tsx`, `themes/store/src/pages/blog.tsx`, `themes/store/src/pages/checkout.tsx`, `themes/store/src/pages/index.tsx`, `themes/store/src/pages/blog/[slug].tsx`, `themes/store/src/pages/category/[slug].tsx`
**Symbols:** function:`App`
**Often changes with:** `themes/store/src/pages/category/[slug].tsx` (11x), `themes/store/src/pages/checkout.tsx` (10x), `themes/store/src/pages/product/[slug].tsx` (10x), `themes/store/src/components/header/Header.tsx` (9x), `themes/store/src/pages/blog.tsx` (8x)

### `themes/store/src/pages/_document.tsx`
**Feature:** Pages
**Imports:** `system/renderer/src/helpers/document.tsx`, `themes/store/src/helpers/createEmotionCache.ts`, `themes/store/src/helpers/theme.ts`
**Symbols:** class:`MyDocument`
**Often changes with:** `themes/store/src/pages/tag/[slug].tsx` (7x), `themes/store/src/components/productCard/ProductCard.tsx` (6x), `themes/store/src/pages/blog.tsx` (6x), `themes/store/src/pages/blog/[slug].tsx` (6x), `themes/store/src/pages/product/[slug].tsx` (6x)

### `themes/store/src/pages/account.tsx`
**Feature:** Pages
**Imports:** `themes/store/src/components/layout/Layout.tsx`, `themes/store/src/helpers/AppState.ts`, `themes/store/src/pages/_app.tsx`
**Imported by:** `themes/store/tests/pages/account.test.tsx`
**Symbols:** const_fn:`handleSignInOpen`, const_fn:`handleSignUpOpen`
**Often changes with:** `themes/store/src/pages/checkout.tsx` (11x), `themes/store/src/pages/product/[slug].tsx` (11x), `themes/store/src/pages/tag/[slug].tsx` (10x), `themes/store/src/components/productDetails/ProductDetails.tsx` (9x), `themes/store/src/pages/blog.tsx` (9x)

### `themes/store/src/pages/blog.tsx`
**Feature:** Pages
**Imports:** `themes/store/src/components/layout/Layout.tsx`, `themes/store/src/components/postCard/PostCard.tsx`, `themes/store/src/helpers/getPosts.ts`, `themes/store/src/pages/_app.tsx`
**Imported by:** `themes/store/tests/pages/blog.test.tsx`
**Symbols:** const_fn:`resetList`, const_fn:`handleChangeTags`, const_fn:`handleGetPosts`, const_fn:`handleChangeSort`, const_fn:`handleTagClick`, function:`useForceUpdate`
**Often changes with:** `themes/store/src/pages/tag/[slug].tsx` (18x), `themes/store/src/pages/product/[slug].tsx` (13x), `themes/blog/src/pages/tag/[slug].tsx` (12x), `themes/store/src/pages/blog/[slug].tsx` (12x), `themes/store/src/pages/category/[slug].tsx` (12x)

### `themes/store/src/pages/blog/[slug].tsx`
**Imports:** `themes/store/src/components/layout/Layout.tsx`, `themes/store/src/components/postCard/PostCard.tsx`, `themes/store/src/pages/_app.tsx`
**Symbols:** const_fn:`getStaticPaths`
**Often changes with:** `themes/blog/src/pages/post/[slug].tsx` (17x), `themes/store/src/pages/tag/[slug].tsx` (16x), `themes/store/src/pages/product/[slug].tsx` (15x), `themes/blog/src/pages/tag/[slug].tsx` (14x), `themes/store/src/pages/blog.tsx` (12x)

### `themes/store/src/pages/category/[slug].tsx`
**Imports:** `themes/store/src/components/layout/Layout.tsx`, `toolkits/commerce/src/base/ProductCard/ProductCard.tsx`, `themes/store/src/pages/_app.tsx`
**Symbols:** const_fn:`getStaticPaths`
**Often changes with:** `themes/store/src/pages/product/[slug].tsx` (17x), `themes/store/src/pages/tag/[slug].tsx` (14x), `themes/store/src/pages/blog.tsx` (12x), `themes/store/src/pages/blog/[slug].tsx` (12x), `themes/store/src/pages/_app.tsx` (11x)

### `themes/store/src/pages/checkout.tsx`
**Feature:** Pages
**Imports:** `themes/store/src/components/layout/Layout.tsx`, `themes/store/src/helpers/AppState.ts`, `themes/store/src/pages/_app.tsx`
**Imported by:** `themes/store/tests/pages/checkout.test.tsx`
**Symbols:** const_fn:`handleSignInOpen`, const_fn:`handleSignUpOpen`
**Often changes with:** `themes/store/src/components/productCard/ProductCard.tsx` (11x), `themes/store/src/pages/account.tsx` (11x), `themes/store/src/pages/blog.tsx` (11x), `themes/store/src/pages/product/[slug].tsx` (11x), `themes/store/src/components/productDetails/ProductDetails.tsx` (10x)

### `themes/store/src/pages/index.tsx`
**Feature:** Pages
**Imports:** `themes/store/src/components/layout/Layout.tsx`, `themes/store/src/pages/_app.tsx`
**Often changes with:** `themes/store/src/pages/_app.tsx` (7x), `themes/store/src/pages/blog.tsx` (7x), `themes/store/src/pages/blog/[slug].tsx` (6x), `themes/store/src/pages/category/[slug].tsx` (6x), `themes/store/src/pages/product/[slug].tsx` (6x)

### `themes/store/src/pages/pages/[slug].tsx`
**Feature:** Pages
**Imports:** `themes/store/src/components/layout/Layout.tsx`, `themes/store/src/pages/_app.tsx`
**Symbols:** const_fn:`getStaticPaths`
**Often changes with:** `themes/store/src/pages/_app.tsx` (6x), `themes/store/src/pages/blog/[slug].tsx` (6x), `themes/store/src/pages/category/[slug].tsx` (6x), `themes/store/src/pages/product/[slug].tsx` (6x), `themes/store/src/pages/tag/[slug].tsx` (6x)

### `themes/store/src/pages/product/[slug].tsx`
**Imports:** `themes/store/src/components/layout/Layout.tsx`, `themes/store/src/components/productDetails/ProductDetails.tsx`, `themes/store/src/pages/_app.tsx`
**Symbols:** const_fn:`getStaticPaths`
**Often changes with:** `themes/store/src/pages/category/[slug].tsx` (17x), `themes/store/src/pages/blog/[slug].tsx` (15x), `themes/store/src/pages/tag/[slug].tsx` (15x), `themes/store/src/pages/blog.tsx` (13x), `themes/store/src/components/productDetails/ProductDetails.tsx` (12x)

### `themes/store/src/pages/tag/[slug].tsx`
**Imports:** `themes/store/src/components/layout/Layout.tsx`, `themes/store/src/components/postCard/PostCard.tsx`, `themes/store/src/helpers/getPosts.ts`, `themes/store/src/pages/_app.tsx`
**Symbols:** const_fn:`resetList`, const_fn:`handleGetPosts`, const_fn:`handleChangeSort`, const_fn:`getStaticPaths`
**Often changes with:** `themes/store/src/pages/blog.tsx` (18x), `themes/blog/src/pages/tag/[slug].tsx` (16x), `themes/store/src/pages/blog/[slug].tsx` (16x), `themes/store/src/pages/product/[slug].tsx` (15x), `themes/store/src/pages/category/[slug].tsx` (14x)

### `themes/store/src/types.ts`
**Imported by:** `plugins/main-menu/src/admin/widgets/SettingsPage.tsx`, `plugins/main-menu/src/admin/widgets/components/MenuItem.tsx`, `plugins/main-menu/src/frontend/DefaultElements.tsx`, `plugins/main-menu/src/frontend/index.tsx`, `plugins/main-menu/tests/jest.config.ts`, `plugins/marqo/src/admin/widgets/SettingsPage.tsx`, `plugins/marqo/src/backend/index.ts`, `plugins/marqo/src/backend/marqo-client.ts`, `plugins/marqo/src/frontend/index.tsx`, `plugins/newsletter/src/admin/widgets/SettingsPage.tsx`

### `themes/store/suppress-hydration-loader.js`
**Feature:** State Management

### `themes/store/tests/jest.config.ts`
**Feature:** Testing
**Imports:** `themes/store/src/types.ts`

### `themes/store/tests/pages/account.test.tsx`
**Feature:** Pages
**Imports:** `themes/store/src/pages/account.tsx`
**Often changes with:** `themes/store/src/pages/checkout.tsx` (4x), `themes/store/tests/pages/category-slug.test.tsx` (4x), `themes/store/tests/pages/checkout.test.tsx` (4x), `themes/store/src/pages/_app.tsx` (3x), `themes/store/src/pages/account.tsx` (3x)

### `themes/store/tests/pages/blog-slug.test.tsx`
**Feature:** Pages
**Often changes with:** `themes/store/src/pages/blog.tsx` (3x), `themes/store/src/pages/category/[slug].tsx` (3x), `themes/store/src/pages/checkout.tsx` (3x), `themes/store/src/pages/tag/[slug].tsx` (3x), `themes/store/tests/pages/account.test.tsx` (3x)

### `themes/store/tests/pages/blog.test.tsx`
**Feature:** Pages
**Imports:** `themes/store/src/pages/blog.tsx`
**Often changes with:** `themes/store/src/pages/blog.tsx` (3x), `themes/store/src/pages/category/[slug].tsx` (3x), `themes/store/src/pages/checkout.tsx` (3x), `themes/store/src/pages/tag/[slug].tsx` (3x), `themes/store/tests/pages/account.test.tsx` (3x)

### `themes/store/tests/pages/category-slug.test.tsx`
**Feature:** Pages
**Often changes with:** `themes/store/src/pages/checkout.tsx` (4x), `themes/store/tests/pages/account.test.tsx` (4x), `themes/store/tests/pages/checkout.test.tsx` (4x), `themes/store/src/pages/_app.tsx` (3x), `themes/store/src/pages/account.tsx` (3x)

### `themes/store/tests/pages/checkout.test.tsx`
**Feature:** Pages
**Imports:** `themes/store/src/pages/checkout.tsx`
**Often changes with:** `themes/store/src/pages/checkout.tsx` (5x), `themes/store/src/pages/account.tsx` (4x), `themes/store/src/pages/blog.tsx` (4x), `themes/store/src/pages/tag/[slug].tsx` (4x), `themes/store/tests/pages/account.test.tsx` (4x)

### `themes/store/tests/pages/index.test.tsx`
**Feature:** Pages

### `themes/store/tests/pages/pages-slug.test.tsx`
**Feature:** Pages

### `themes/store/tests/pages/product-slug.test.tsx`
**Feature:** Pages
**Often changes with:** `themes/store/src/pages/blog.tsx` (3x), `themes/store/src/pages/category/[slug].tsx` (3x), `themes/store/src/pages/checkout.tsx` (3x), `themes/store/src/pages/tag/[slug].tsx` (3x), `themes/store/tests/pages/account.test.tsx` (3x)

### `themes/store/tests/pages/tag-slug.test.tsx`
**Feature:** Pages
**Often changes with:** `themes/store/src/pages/blog.tsx` (3x), `themes/store/src/pages/category/[slug].tsx` (3x), `themes/store/src/pages/checkout.tsx` (3x), `themes/store/src/pages/tag/[slug].tsx` (3x), `themes/store/tests/pages/account.test.tsx` (3x)

### `themes/store/tests/setup.ts`
**Feature:** Testing

### `toolkits/commerce/.eslintrc.js`
**Often changes with:** `toolkits/commerce/rollup.config.js` (4x), `themes/store/src/pages/product/[slug].tsx` (3x), `toolkits/commerce/src/base/Breadcrumbs/Breadcrumbs.tsx` (3x), `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx` (3x), `toolkits/commerce/src/base/ProductReviews/ProductReviews.tsx` (3x)

### `toolkits/commerce/jest.config.ts`
**Imports:** `themes/store/src/types.ts`

### `toolkits/commerce/rollup.config.js`
**Symbols:** const_fn:`external`, const_fn:`getOutput`, const_fn:`getPlugins`
**Often changes with:** `toolkits/commerce/src/base/Breadcrumbs/Breadcrumbs.tsx` (6x), `themes/store/src/pages/product/[slug].tsx` (6x), `toolkits/commerce/src/base/CategoryList/CategoryList.tsx` (5x), `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx` (5x), `toolkits/commerce/.eslintrc.js` (4x)

### `toolkits/commerce/src/_index.ts`
**Imported by:** `system/server/src/dto/setup.dto.ts`
**Often changes with:** `toolkits/commerce/src/base/Checkout/actions.ts` (4x), `toolkits/commerce/src/base/AccountInfo/actions.ts` (3x), `toolkits/commerce/src/base/ProductActions/ProductActions.tsx` (3x), `toolkits/commerce/src/base/ProductCard/ProductCard.tsx` (3x), `toolkits/commerce/src/base/CategoryList/CategoryList.tsx` (3x)

### `toolkits/commerce/src/base/AccountInfo/AccountInfo.test.tsx`
**Feature:** Account Management
**Imports:** `toolkits/commerce/src/base/AccountInfo/AccountInfo.tsx`
**Often changes with:** `toolkits/commerce/src/base/AccountInfo/actions.ts` (3x), `toolkits/commerce/src/base/AccountOrders/AccountOrders.test.tsx` (3x)

### `toolkits/commerce/src/base/AccountInfo/AccountInfo.tsx`
**Feature:** Account Management
**Imports:** `toolkits/commerce/src/helpers/notifier.tsx`, `toolkits/commerce/src/base/shared/Button.tsx`, `toolkits/commerce/src/base/shared/TextField.tsx`, `toolkits/commerce/src/base/AccountInfo/actions.ts`, `toolkits/commerce/src/base/AccountInfo/DefaultElements.tsx`
**Imported by:** `toolkits/commerce/src/base/AccountInfo/AccountInfo.test.tsx`, `toolkits/commerce/src/base/AccountInfo/DefaultElements.tsx`, `toolkits/commerce/src/base/AccountInfo/actions.ts`, `toolkits/commerce/src/mui/index.ts`
**Symbols:** function:`AccountInfo`

### `toolkits/commerce/src/base/AccountInfo/DefaultElements.tsx`
**Feature:** Account Management
**Imports:** `toolkits/commerce/src/base/shared/TextField.tsx`, `toolkits/commerce/src/base/AccountInfo/AccountInfo.tsx`
**Imported by:** `toolkits/commerce/src/base/AccountInfo/AccountInfo.tsx`, `toolkits/commerce/src/base/AccountInfo/actions.ts`
**Symbols:** const_fn:`getDefaultAccountFields`

### `toolkits/commerce/src/base/AccountInfo/actions.ts`
**Feature:** Account Management
**Imports:** `toolkits/commerce/src/helpers/notifier.tsx`, `toolkits/commerce/src/base/AccountInfo/AccountInfo.tsx`, `toolkits/commerce/src/base/AccountInfo/DefaultElements.tsx`
**Imported by:** `toolkits/commerce/src/base/AccountInfo/AccountInfo.tsx`
**Symbols:** const_fn:`useAccountActions`, const_fn:`onChange`
**Often changes with:** `toolkits/commerce/src/_index.ts` (3x), `toolkits/commerce/src/base/AccountInfo/AccountInfo.test.tsx` (3x), `toolkits/commerce/src/base/AccountOrders/AccountOrders.test.tsx` (3x)

### `toolkits/commerce/src/base/AccountOrders/AccountOrders.test.tsx`
**Feature:** Account Management
**Imports:** `toolkits/commerce/src/base/AccountOrders/AccountOrders.tsx`
**Often changes with:** `toolkits/commerce/src/base/AccountInfo/AccountInfo.test.tsx` (3x), `toolkits/commerce/src/base/AccountInfo/actions.ts` (3x)

### `toolkits/commerce/src/base/AccountOrders/AccountOrders.tsx`
**Feature:** Account Management
**Imports:** `toolkits/commerce/src/base/CartList/CartList.tsx`
**Imported by:** `toolkits/commerce/src/base/AccountOrders/AccountOrders.test.tsx`, `toolkits/commerce/src/mui/index.ts`
**Symbols:** function:`AccountOrders`, const_fn:`getOrders`, const_fn:`onChange`
**Often changes with:** `toolkits/commerce/src/base/Checkout/actions.ts` (3x)

### `toolkits/commerce/src/base/Breadcrumbs/Breadcrumbs.test.tsx`
**Imports:** `toolkits/commerce/src/base/Breadcrumbs/Breadcrumbs.tsx`

### `toolkits/commerce/src/base/Breadcrumbs/Breadcrumbs.tsx`
**Imports:** `toolkits/commerce/src/base/Breadcrumbs/Crumb.tsx`, `toolkits/commerce/src/base/Breadcrumbs/DefaultElements.tsx`, `toolkits/commerce/src/base/Breadcrumbs/getData.ts`
**Imported by:** `toolkits/commerce/src/base/Breadcrumbs/Breadcrumbs.test.tsx`, `toolkits/commerce/src/base/Breadcrumbs/Crumb.tsx`, `toolkits/commerce/src/base/Breadcrumbs/getData.ts`
**Symbols:** function:`Breadcrumbs`, const_fn:`originProps`, const_fn:`slug`
**Often changes with:** `themes/store/src/pages/product/[slug].tsx` (7x), `toolkits/commerce/rollup.config.js` (6x), `toolkits/commerce/src/base/Breadcrumbs/getData.ts` (6x), `toolkits/commerce/src/base/CategoryList/CategoryList.tsx` (6x), `toolkits/commerce/src/base/CategoryFilter/CategoryFilter.tsx` (5x)

### `toolkits/commerce/src/base/Breadcrumbs/Crumb.tsx`
**Imports:** `toolkits/commerce/src/helpers/useLinks.ts`, `toolkits/commerce/src/base/Breadcrumbs/Breadcrumbs.tsx`, `toolkits/commerce/src/base/Breadcrumbs/DefaultElements.tsx`
**Imported by:** `toolkits/commerce/src/base/Breadcrumbs/Breadcrumbs.tsx`
**Symbols:** const_fn:`Crumb`
**Often changes with:** `toolkits/commerce/rollup.config.js` (3x), `toolkits/commerce/src/base/Breadcrumbs/Breadcrumbs.tsx` (3x), `toolkits/commerce/src/base/Breadcrumbs/DefaultElements.tsx` (3x), `toolkits/commerce/src/base/CartList/CartList.tsx` (3x), `toolkits/commerce/src/base/CartList/CartListItem.tsx` (3x)

### `toolkits/commerce/src/base/Breadcrumbs/DefaultElements.tsx`
**Imports:** `toolkits/commerce/src/base/icons.tsx`
**Imported by:** `toolkits/commerce/src/base/Breadcrumbs/Breadcrumbs.tsx`, `toolkits/commerce/src/base/Breadcrumbs/Crumb.tsx`
**Symbols:** const_fn:`DefaultBreadcrumb`, const_fn:`DefaultWrapper`, const_fn:`DefaultHomeIcon`
**Often changes with:** `toolkits/commerce/rollup.config.js` (3x), `toolkits/commerce/src/base/Breadcrumbs/Breadcrumbs.tsx` (3x), `toolkits/commerce/src/base/Breadcrumbs/Crumb.tsx` (3x), `toolkits/commerce/src/base/CartList/CartList.tsx` (3x), `toolkits/commerce/src/base/CartList/CartListItem.tsx` (3x)

### `toolkits/commerce/src/base/Breadcrumbs/getData.ts`
**Imports:** `toolkits/commerce/src/base/Breadcrumbs/Breadcrumbs.tsx`
**Imported by:** `toolkits/commerce/src/base/Breadcrumbs/Breadcrumbs.tsx`
**Symbols:** const_fn:`breadcrumbsGetData`, const_fn:`getBreadCrumb`
**Often changes with:** `toolkits/commerce/src/base/Breadcrumbs/Breadcrumbs.tsx` (6x), `toolkits/commerce/src/base/CategoryList/CategoryList.tsx` (5x), `themes/store/src/pages/product/[slug].tsx` (5x), `toolkits/commerce/rollup.config.js` (4x), `toolkits/commerce/src/base/CategoryFilter/CategoryFilter.tsx` (4x)

### `toolkits/commerce/src/base/CartList/CartList.test.tsx`
**Feature:** Shopping Cart
**Imports:** `toolkits/commerce/src/base/CartList/CartList.tsx`
**Often changes with:** `toolkits/commerce/src/base/CategoryList/CategoryList.test.tsx` (3x), `toolkits/commerce/src/base/CategoryList/CategoryList.tsx` (3x), `toolkits/commerce/src/base/Checkout/Checkout.test.tsx` (3x), `toolkits/commerce/src/base/CurrencySwitch/CurrencySwitch.test.tsx` (3x), `toolkits/commerce/src/base/ProductActions/ProductActions.test.tsx` (3x)

### `toolkits/commerce/src/base/CartList/CartList.tsx`
**Feature:** Shopping Cart
**Imports:** `toolkits/commerce/src/base/shared/Button.tsx`, `toolkits/commerce/src/base/CartList/CartListItem.tsx`, `toolkits/commerce/src/helpers/state.ts`, `toolkits/commerce/src/helpers/useStoreAttributes.ts`
**Imported by:** `toolkits/commerce/src/base/AccountOrders/AccountOrders.tsx`, `toolkits/commerce/src/base/CartList/CartList.test.tsx`, `toolkits/commerce/src/base/CartList/CartListItem.tsx`, `toolkits/commerce/src/mui/index.ts`
**Symbols:** function:`CartList`, const_fn:`viewCart`, const_fn:`listJsx`, const_fn:`headerJsx`
**Often changes with:** `toolkits/commerce/src/base/Checkout/Checkout.tsx` (5x), `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx` (5x), `toolkits/commerce/src/base/CartList/CartListItem.tsx` (5x), `toolkits/commerce/src/base/CategoryList/CategoryList.tsx` (5x), `toolkits/commerce/rollup.config.js` (4x)

### `toolkits/commerce/src/base/CartList/CartListItem.tsx`
**Feature:** Shopping Cart
**Imports:** `toolkits/commerce/src/helpers/useLinks.ts`, `toolkits/commerce/src/base/icons.tsx`, `toolkits/commerce/src/base/shared/Button.tsx`, `toolkits/commerce/src/base/CartList/CartList.tsx`
**Imported by:** `toolkits/commerce/src/base/CartList/CartList.tsx`
**Symbols:** function:`CartListItem`, const_fn:`handleDeleteItem`
**Often changes with:** `toolkits/commerce/src/base/CartList/CartList.tsx` (5x), `toolkits/commerce/src/base/CategoryList/CategoryList.tsx` (5x), `toolkits/commerce/src/base/ProductCard/ProductCard.tsx` (5x), `toolkits/commerce/rollup.config.js` (4x), `toolkits/commerce/src/base/Checkout/Checkout.tsx` (4x)

### `toolkits/commerce/src/base/CategoryFilter/CategoryFilter.test.tsx`
**Imports:** `toolkits/commerce/src/base/CategoryFilter/CategoryFilter.tsx`

### `toolkits/commerce/src/base/CategoryFilter/CategoryFilter.tsx`
**Imports:** `toolkits/commerce/src/helpers/state.ts`
**Imported by:** `toolkits/commerce/src/base/CategoryFilter/CategoryFilter.test.tsx`
**Symbols:** function:`CategoryFilter`
**Often changes with:** `toolkits/commerce/src/base/Breadcrumbs/Breadcrumbs.tsx` (5x), `toolkits/commerce/src/base/CategoryList/CategoryList.tsx` (5x), `toolkits/commerce/src/base/CategorySort/CategorySort.tsx` (5x), `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx` (5x), `toolkits/commerce/src/base/ProductCard/ProductCard.tsx` (5x)

### `toolkits/commerce/src/base/CategoryList/CategoryList.test.tsx`
**Imports:** `toolkits/commerce/src/base/CategoryList/CategoryList.tsx`
**Often changes with:** `toolkits/commerce/src/base/CartList/CartList.test.tsx` (3x), `toolkits/commerce/src/base/CategoryList/CategoryList.tsx` (3x), `toolkits/commerce/src/base/Checkout/Checkout.test.tsx` (3x), `toolkits/commerce/src/base/CurrencySwitch/CurrencySwitch.test.tsx` (3x), `toolkits/commerce/src/base/ProductActions/ProductActions.test.tsx` (3x)

### `toolkits/commerce/src/base/CategoryList/CategoryList.tsx`
**Imports:** `toolkits/commerce/src/helpers/state.ts`, `toolkits/commerce/src/helpers/useStoreAttributes.ts`, `toolkits/commerce/src/base/ProductCard/ProductCard.tsx`
**Imported by:** `system/admin/src/router-pages/categoryList/components/CategoryItem.tsx`, `system/admin/src/router-pages/categoryList/components/HeaderActions.tsx`, `toolkits/commerce/src/base/CategoryList/CategoryList.test.tsx`, `toolkits/commerce/src/mui/index.ts`
**Symbols:** function:`CategoryList`
**Often changes with:** `toolkits/commerce/src/base/ProductCard/ProductCard.tsx` (9x), `toolkits/commerce/src/base/Breadcrumbs/Breadcrumbs.tsx` (6x), `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx` (6x), `themes/store/src/pages/product/[slug].tsx` (6x), `themes/store/src/pages/blog.tsx` (5x)

### `toolkits/commerce/src/base/CategorySort/CategorySort.test.tsx`
**Imports:** `toolkits/commerce/src/base/CategorySort/CategorySort.tsx`

### `toolkits/commerce/src/base/CategorySort/CategorySort.tsx`
**Imports:** `toolkits/commerce/src/helpers/state.ts`, `toolkits/commerce/src/mui/Select/Select.tsx`
**Imported by:** `toolkits/commerce/src/base/CategorySort/CategorySort.test.tsx`, `toolkits/commerce/src/mui/index.ts`
**Symbols:** function:`CategorySort`, const_fn:`handleValueChange`
**Often changes with:** `toolkits/commerce/src/base/Breadcrumbs/Breadcrumbs.tsx` (5x), `toolkits/commerce/src/base/CategoryFilter/CategoryFilter.tsx` (5x), `toolkits/commerce/src/base/CategoryList/CategoryList.tsx` (5x), `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx` (5x), `toolkits/commerce/src/base/ProductCard/ProductCard.tsx` (5x)

### `toolkits/commerce/src/base/Checkout/Checkout.test.tsx`
**Feature:** Checkout
**Imports:** `toolkits/commerce/src/base/Checkout/Checkout.tsx`
**Often changes with:** `toolkits/commerce/src/base/CartList/CartList.test.tsx` (3x), `toolkits/commerce/src/base/CategoryList/CategoryList.test.tsx` (3x), `toolkits/commerce/src/base/CategoryList/CategoryList.tsx` (3x), `toolkits/commerce/src/base/CurrencySwitch/CurrencySwitch.test.tsx` (3x), `toolkits/commerce/src/base/ProductActions/ProductActions.test.tsx` (3x)

### `toolkits/commerce/src/base/Checkout/Checkout.tsx`
**Feature:** Checkout
**Imports:** `toolkits/commerce/src/helpers/notifier.tsx`, `toolkits/commerce/src/base/shared/Button.tsx`, `toolkits/commerce/src/base/shared/Radio.tsx`, `toolkits/commerce/src/base/shared/TextField.tsx`, `toolkits/commerce/src/base/Checkout/actions.ts`, `toolkits/commerce/src/base/Checkout/Coupons.tsx`
**Imported by:** `toolkits/commerce/src/base/Checkout/Checkout.test.tsx`, `toolkits/commerce/src/base/Checkout/Coupons.tsx`, `toolkits/commerce/src/base/Checkout/DefaultElements.tsx`, `toolkits/commerce/src/base/Checkout/actions.ts`, `toolkits/commerce/src/mui/index.ts`
**Symbols:** function:`Checkout`, const_fn:`wrapContent`
**Often changes with:** `toolkits/commerce/src/base/Checkout/actions.ts` (7x), `toolkits/commerce/src/base/CartList/CartList.tsx` (5x), `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx` (5x), `toolkits/commerce/src/base/Checkout/DefaultElements.tsx` (5x), `toolkits/commerce/src/base/ProductCard/ProductCard.tsx` (5x)

### `toolkits/commerce/src/base/Checkout/Coupons.tsx`
**Feature:** Checkout
**Imports:** `toolkits/commerce/src/base/shared/Button.tsx`, `toolkits/commerce/src/base/shared/TextField.tsx`, `toolkits/commerce/src/base/Checkout/actions.ts`, `toolkits/commerce/src/base/Checkout/DefaultElements.tsx`, `toolkits/commerce/src/base/Checkout/Checkout.tsx`
**Imported by:** `toolkits/commerce/src/base/Checkout/Checkout.tsx`
**Symbols:** function:`Coupons`
**Often changes with:** `toolkits/commerce/src/base/CartList/CartList.tsx` (4x), `toolkits/commerce/src/base/Checkout/Checkout.tsx` (4x), `toolkits/commerce/src/base/Checkout/actions.ts` (4x), `toolkits/commerce/src/base/Breadcrumbs/Breadcrumbs.tsx` (3x), `toolkits/commerce/src/base/Breadcrumbs/Crumb.tsx` (3x)

### `toolkits/commerce/src/base/Checkout/DefaultElements.tsx`
**Feature:** Checkout
**Imports:** `toolkits/commerce/src/base/shared/TextField.tsx`, `toolkits/commerce/src/base/Checkout/actions.ts`, `toolkits/commerce/src/base/Checkout/Checkout.tsx`
**Imported by:** `toolkits/commerce/src/base/Checkout/Coupons.tsx`, `toolkits/commerce/src/base/Checkout/actions.ts`
**Symbols:** const_fn:`DefaultPlacedOrder`, const_fn:`DefaultEmptyCartAlert`, const_fn:`DefaultField`, const_fn:`DefaultCouponProblemIcon`, const_fn:`DefaultCouponAppliedIcon`, const_fn:`DefaultRemoveCouponIcon`, const_fn:`getDefaultCheckoutFields`
**Often changes with:** `toolkits/commerce/src/base/Checkout/Checkout.tsx` (5x), `toolkits/commerce/src/base/Breadcrumbs/Breadcrumbs.tsx` (4x), `toolkits/commerce/src/base/ProductCard/ProductCard.tsx` (4x), `toolkits/commerce/src/base/ProductGallery/ProductGallery.tsx` (4x), `toolkits/commerce/src/base/Checkout/actions.ts` (4x)

### `toolkits/commerce/src/base/Checkout/actions.ts`
**Feature:** Checkout
**Imports:** `toolkits/commerce/src/helpers/notifier.tsx`, `toolkits/commerce/src/helpers/state.ts`, `toolkits/commerce/src/base/Checkout/Checkout.tsx`, `toolkits/commerce/src/base/Checkout/DefaultElements.tsx`
**Imported by:** `system/core/backend/tests/helpers/actions.test.ts`, `toolkits/commerce/src/base/Checkout/Checkout.tsx`, `toolkits/commerce/src/base/Checkout/Coupons.tsx`, `toolkits/commerce/src/base/Checkout/DefaultElements.tsx`
**Symbols:** const_fn:`usuCheckoutActions`, const_fn:`onUserChange`
**Often changes with:** `toolkits/commerce/src/base/Checkout/Checkout.tsx` (7x), `toolkits/commerce/src/base/ProductCard/ProductCard.tsx` (6x), `toolkits/commerce/src/base/ProductActions/ProductActions.tsx` (6x), `toolkits/commerce/src/base/ProductReviews/ProductReviews.tsx` (5x), `toolkits/commerce/src/base/ProductReviews/ReviewForm.tsx` (5x)

### `toolkits/commerce/src/base/CurrencySwitch/CurrencySwitch.test.tsx`
**Imports:** `toolkits/commerce/src/base/CurrencySwitch/CurrencySwitch.tsx`
**Often changes with:** `toolkits/commerce/src/base/CategoryList/CategoryList.tsx` (4x), `toolkits/commerce/src/base/ProductActions/ProductActions.test.tsx` (4x), `toolkits/commerce/src/base/ProductSearch/ProductSearch.test.tsx` (4x), `toolkits/commerce/src/base/ProductSearch/ProductSearch.tsx` (4x), `toolkits/commerce/src/base/Breadcrumbs/Breadcrumbs.tsx` (3x)

### `toolkits/commerce/src/base/CurrencySwitch/CurrencySwitch.tsx`
**Imports:** `toolkits/commerce/src/mui/Select/Select.tsx`
**Imported by:** `toolkits/commerce/src/base/CurrencySwitch/CurrencySwitch.test.tsx`, `toolkits/commerce/src/mui/index.ts`
**Symbols:** function:`CurrencySwitch`, const_fn:`handleCurrencyChange`
**Often changes with:** `toolkits/commerce/src/base/Breadcrumbs/Breadcrumbs.tsx` (4x), `toolkits/commerce/src/base/CategoryFilter/CategoryFilter.tsx` (4x), `toolkits/commerce/src/base/CategoryList/CategoryList.tsx` (4x), `toolkits/commerce/src/base/CategorySort/CategorySort.tsx` (4x), `toolkits/commerce/src/base/ProductActions/ProductActions.tsx` (4x)

### `toolkits/commerce/src/base/ProductActions/ProductActions.test.tsx`
**Imports:** `toolkits/commerce/src/base/ProductActions/ProductActions.tsx`
**Often changes with:** `toolkits/commerce/src/base/CategoryList/CategoryList.tsx` (4x), `toolkits/commerce/src/base/CurrencySwitch/CurrencySwitch.test.tsx` (4x), `toolkits/commerce/src/base/ProductSearch/ProductSearch.test.tsx` (4x), `toolkits/commerce/src/base/ProductSearch/ProductSearch.tsx` (4x), `toolkits/commerce/src/base/CartList/CartList.test.tsx` (3x)

### `toolkits/commerce/src/base/ProductActions/ProductActions.tsx`
**Imports:** `toolkits/commerce/src/helpers/notifier.tsx`, `toolkits/commerce/src/helpers/state.ts`, `toolkits/commerce/src/helpers/useStoreAttributes.ts`, `toolkits/commerce/src/base/shared/Alert.tsx`, `toolkits/commerce/src/base/shared/Button.tsx`
**Imported by:** `toolkits/commerce/src/base/ProductActions/ProductActions.test.tsx`
**Symbols:** function:`ProductActions`, const_fn:`handleAddToCart`, const_fn:`handleAddToWishlist`
**Often changes with:** `toolkits/commerce/src/base/ProductCard/ProductCard.tsx` (7x), `toolkits/commerce/src/base/Checkout/actions.ts` (6x), `toolkits/commerce/src/base/ProductReviews/ProductReviews.tsx` (6x), `toolkits/commerce/src/base/ProductReviews/ReviewForm.tsx` (6x), `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx` (6x)

### `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.test.tsx`
**Imports:** `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx`
**Often changes with:** `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx` (4x), `toolkits/commerce/src/base/ProductActions/ProductActions.tsx` (3x), `toolkits/commerce/src/base/ProductCard/ProductCard.tsx` (3x), `toolkits/commerce/src/base/ProductReviews/ProductReviews.tsx` (3x), `toolkits/commerce/src/base/ProductReviews/ReviewForm.tsx` (3x)

### `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx`
**Imports:** `toolkits/commerce/src/helpers/state.ts`, `toolkits/commerce/src/helpers/useStoreAttributes.ts`
**Imported by:** `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.test.tsx`, `toolkits/commerce/src/mui/ProductAttributes/AttributeTitle.tsx`, `toolkits/commerce/src/mui/ProductAttributes/AttributeValue.tsx`
**Symbols:** function:`ProductAttributes`, const_fn:`handleSetAttribute`, const_fn:`handleClick`
**Often changes with:** `toolkits/commerce/src/base/ProductCard/ProductCard.tsx` (8x), `toolkits/commerce/src/base/ProductReviews/ProductReviews.tsx` (7x), `toolkits/commerce/src/base/ProductSearch/ProductSearch.tsx` (6x), `toolkits/commerce/src/base/CategoryList/CategoryList.tsx` (6x), `toolkits/commerce/src/base/ProductActions/ProductActions.tsx` (6x)

### `toolkits/commerce/src/base/ProductCard/ProductCard.test.tsx`
**Imports:** `toolkits/commerce/src/base/ProductCard/ProductCard.tsx`
**Often changes with:** `toolkits/commerce/src/base/CategoryList/CategoryList.test.tsx` (3x), `toolkits/commerce/src/base/CategoryList/CategoryList.tsx` (3x), `toolkits/commerce/src/base/Checkout/Checkout.test.tsx` (3x), `toolkits/commerce/src/base/CurrencySwitch/CurrencySwitch.test.tsx` (3x), `toolkits/commerce/src/base/ProductActions/ProductActions.test.tsx` (3x)

### `toolkits/commerce/src/base/ProductCard/ProductCard.tsx`
**Imports:** `toolkits/commerce/src/helpers/notifier.tsx`, `toolkits/commerce/src/helpers/useLinks.ts`, `toolkits/commerce/src/helpers/useStoreAttributes.ts`, `toolkits/commerce/src/base/icons.tsx`, `toolkits/commerce/src/base/shared/Button.tsx`, `toolkits/commerce/src/base/shared/Rating.tsx`, `toolkits/commerce/src/base/shared/Tooltip.tsx`
**Imported by:** `themes/store/src/components/modals/viewed/ViewedModal.tsx`, `themes/store/src/components/modals/wishlist/WishlistModal.tsx`, `themes/store/src/pages/_app.tsx`, `themes/store/src/pages/category/[slug].tsx`, `toolkits/commerce/src/base/CategoryList/CategoryList.tsx`, `toolkits/commerce/src/base/ProductCard/ProductCard.test.tsx`, `toolkits/commerce/src/base/ViewedItems/ViewedItems.tsx`, `toolkits/commerce/src/base/Wishlist/Wishlist.tsx`, `toolkits/commerce/src/mui/index.ts`
**Symbols:** const_fn:`Empty`, function:`ProductCard`, const_fn:`handleAddToCart`, const_fn:`handleAddToWishlist`
**Often changes with:** `toolkits/commerce/src/base/CategoryList/CategoryList.tsx` (9x), `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx` (8x), `toolkits/commerce/src/base/ProductActions/ProductActions.tsx` (7x), `toolkits/commerce/src/base/Checkout/actions.ts` (6x), `toolkits/commerce/src/base/ProductReviews/ReviewForm.tsx` (6x)

### `toolkits/commerce/src/base/ProductGallery/ProductGallery.test.tsx`
**Imports:** `toolkits/commerce/src/base/ProductGallery/ProductGallery.tsx`

### `toolkits/commerce/src/base/ProductGallery/ProductGallery.tsx`
**Imported by:** `toolkits/commerce/src/base/ProductGallery/ProductGallery.test.tsx`
**Symbols:** function:`ProductGallery`
**Often changes with:** `toolkits/commerce/src/base/ProductCard/ProductCard.tsx` (5x), `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx` (5x), `toolkits/commerce/src/base/Checkout/Checkout.tsx` (4x), `toolkits/commerce/src/base/Checkout/DefaultElements.tsx` (4x), `toolkits/commerce/src/base/shared/Alert.tsx` (4x)

### `toolkits/commerce/src/base/ProductReviews/ProductReviews.test.tsx`
**Feature:** Views/Pages
**Imports:** `toolkits/commerce/src/base/ProductReviews/ProductReviews.tsx`
**Often changes with:** `toolkits/commerce/src/base/CategoryList/CategoryList.tsx` (3x), `toolkits/commerce/src/base/Checkout/Checkout.test.tsx` (3x), `toolkits/commerce/src/base/CurrencySwitch/CurrencySwitch.test.tsx` (3x), `toolkits/commerce/src/base/ProductActions/ProductActions.test.tsx` (3x), `toolkits/commerce/src/base/ProductCard/ProductCard.test.tsx` (3x)

### `toolkits/commerce/src/base/ProductReviews/ProductReviews.tsx`
**Feature:** Views/Pages
**Imports:** `toolkits/commerce/src/helpers/notifier.tsx`, `toolkits/commerce/src/base/shared/Alert.tsx`, `toolkits/commerce/src/base/shared/Button.tsx`, `toolkits/commerce/src/base/shared/Rating.tsx`, `toolkits/commerce/src/base/shared/TextField.tsx`, `toolkits/commerce/src/base/shared/Tooltip.tsx`, `toolkits/commerce/src/base/ProductReviews/ReviewForm.tsx`, `toolkits/commerce/src/base/ProductReviews/ReviewItem.tsx`
**Imported by:** `toolkits/commerce/src/base/ProductReviews/ProductReviews.test.tsx`, `toolkits/commerce/src/base/ProductReviews/ReviewForm.tsx`, `toolkits/commerce/src/base/ProductReviews/ReviewItem.tsx`, `toolkits/commerce/src/mui/index.ts`
**Symbols:** const_fn:`ListItem`, function:`ProductReviews`
**Often changes with:** `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx` (7x), `toolkits/commerce/src/base/ProductReviews/ReviewForm.tsx` (7x), `toolkits/commerce/src/base/ProductActions/ProductActions.tsx` (6x), `toolkits/commerce/src/base/ProductReviews/ReviewItem.tsx` (6x), `toolkits/commerce/src/base/ProductCard/ProductCard.tsx` (5x)

### `toolkits/commerce/src/base/ProductReviews/ReviewForm.tsx`
**Feature:** Views/Pages
**Imports:** `toolkits/commerce/src/helpers/notifier.tsx`, `toolkits/commerce/src/base/shared/Alert.tsx`, `toolkits/commerce/src/base/shared/Button.tsx`, `toolkits/commerce/src/base/shared/Rating.tsx`, `toolkits/commerce/src/base/shared/TextField.tsx`, `toolkits/commerce/src/base/shared/Tooltip.tsx`, `toolkits/commerce/src/base/ProductReviews/ProductReviews.tsx`
**Imported by:** `toolkits/commerce/src/base/ProductReviews/ProductReviews.tsx`
**Symbols:** const_fn:`ReviewForm`, const_fn:`userInfoChange`, const_fn:`handleSubmit`
**Often changes with:** `toolkits/commerce/src/base/ProductReviews/ProductReviews.tsx` (7x), `toolkits/commerce/src/base/ProductActions/ProductActions.tsx` (6x), `toolkits/commerce/src/base/ProductCard/ProductCard.tsx` (6x), `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx` (6x), `toolkits/commerce/src/base/ProductReviews/ReviewItem.tsx` (6x)

### `toolkits/commerce/src/base/ProductReviews/ReviewItem.tsx`
**Feature:** Views/Pages
**Imports:** `toolkits/commerce/src/base/shared/Rating.tsx`, `toolkits/commerce/src/base/ProductReviews/ProductReviews.tsx`
**Imported by:** `toolkits/commerce/src/base/ProductReviews/ProductReviews.tsx`
**Symbols:** const_fn:`ReviewItem`
**Often changes with:** `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx` (6x), `toolkits/commerce/src/base/ProductReviews/ProductReviews.tsx` (6x), `toolkits/commerce/src/base/ProductReviews/ReviewForm.tsx` (6x), `toolkits/commerce/src/base/ProductActions/ProductActions.tsx` (4x), `toolkits/commerce/src/base/ProductGallery/ProductGallery.tsx` (4x)

### `toolkits/commerce/src/base/ProductSearch/ListItem.tsx`
**Feature:** Product Catalog
**Imports:** `toolkits/commerce/src/base/ProductSearch/ProductSearch.tsx`
**Imported by:** `toolkits/commerce/src/base/ProductSearch/ProductSearch.tsx`
**Symbols:** const_fn:`DefaultListItem`
**Often changes with:** `toolkits/commerce/src/base/CurrencySwitch/CurrencySwitch.tsx` (3x), `toolkits/commerce/src/base/ProductActions/ProductActions.tsx` (3x), `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx` (3x), `toolkits/commerce/src/base/ProductCard/ProductCard.tsx` (3x), `toolkits/commerce/src/base/ProductSearch/ProductSearch.tsx` (3x)

### `toolkits/commerce/src/base/ProductSearch/ProductSearch.test.tsx`
**Feature:** Product Catalog
**Imports:** `toolkits/commerce/src/base/ProductSearch/ProductSearch.tsx`
**Often changes with:** `toolkits/commerce/src/base/CurrencySwitch/CurrencySwitch.test.tsx` (4x), `toolkits/commerce/src/base/ProductActions/ProductActions.test.tsx` (4x), `toolkits/commerce/src/base/ProductSearch/ProductSearch.tsx` (4x), `toolkits/commerce/src/base/ProductCard/ProductCard.test.tsx` (3x), `toolkits/commerce/src/base/ProductReviews/ProductReviews.test.tsx` (3x)

### `toolkits/commerce/src/base/ProductSearch/ProductSearch.tsx`
**Feature:** Product Catalog
**Imports:** `toolkits/commerce/src/mui/Popper/Popper.tsx`, `toolkits/commerce/src/base/shared/TextField.tsx`, `toolkits/commerce/src/base/ProductSearch/ListItem.tsx`
**Imported by:** `toolkits/commerce/src/base/ProductSearch/ListItem.tsx`, `toolkits/commerce/src/base/ProductSearch/ProductSearch.test.tsx`, `toolkits/commerce/src/mui/index.ts`
**Symbols:** function:`ProductSearch`, const_fn:`handleSearchInput`, const_fn:`handleSearchClose`
**Often changes with:** `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx` (6x), `toolkits/commerce/src/base/ProductReviews/ProductReviews.tsx` (5x), `toolkits/commerce/src/base/ProductCard/ProductCard.tsx` (5x), `toolkits/commerce/src/base/CategoryList/CategoryList.tsx` (5x), `toolkits/commerce/src/helpers/useStoreAttributes.ts` (5x)

### `toolkits/commerce/src/base/ViewedItems/ViewedItems.test.tsx`
**Imports:** `toolkits/commerce/src/base/ViewedItems/ViewedItems.tsx`
**Often changes with:** `toolkits/commerce/src/base/CurrencySwitch/CurrencySwitch.test.tsx` (3x), `toolkits/commerce/src/base/ProductActions/ProductActions.test.tsx` (3x), `toolkits/commerce/src/base/ProductCard/ProductCard.test.tsx` (3x), `toolkits/commerce/src/base/ProductReviews/ProductReviews.test.tsx` (3x), `toolkits/commerce/src/base/ProductReviews/ProductReviews.tsx` (3x)

### `toolkits/commerce/src/base/ViewedItems/ViewedItems.tsx`
**Imports:** `toolkits/commerce/src/helpers/useStoreAttributes.ts`, `toolkits/commerce/src/base/ProductCard/ProductCard.tsx`
**Imported by:** `toolkits/commerce/src/base/ViewedItems/ViewedItems.test.tsx`, `toolkits/commerce/src/mui/index.ts`
**Symbols:** function:`ViewedItems`
**Often changes with:** `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx` (5x), `toolkits/commerce/src/base/Wishlist/Wishlist.tsx` (5x), `toolkits/commerce/src/base/CurrencySwitch/CurrencySwitch.tsx` (4x), `toolkits/commerce/src/base/ProductActions/ProductActions.tsx` (4x), `toolkits/commerce/src/base/ProductCard/ProductCard.tsx` (4x)

### `toolkits/commerce/src/base/Wishlist/Wishlist.test.tsx`
**Imports:** `toolkits/commerce/src/base/Wishlist/Wishlist.tsx`
**Often changes with:** `toolkits/commerce/src/base/ProductActions/ProductActions.test.tsx` (3x), `toolkits/commerce/src/base/ProductCard/ProductCard.test.tsx` (3x), `toolkits/commerce/src/base/ProductReviews/ProductReviews.test.tsx` (3x), `toolkits/commerce/src/base/ProductReviews/ProductReviews.tsx` (3x), `toolkits/commerce/src/base/ProductSearch/ProductSearch.test.tsx` (3x)

### `toolkits/commerce/src/base/Wishlist/Wishlist.tsx`
**Imports:** `toolkits/commerce/src/helpers/useStoreAttributes.ts`, `toolkits/commerce/src/base/ProductCard/ProductCard.tsx`
**Imported by:** `toolkits/commerce/src/base/Wishlist/Wishlist.test.tsx`, `toolkits/commerce/src/mui/index.ts`
**Symbols:** function:`Wishlist`
**Often changes with:** `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx` (5x), `toolkits/commerce/src/base/ViewedItems/ViewedItems.tsx` (5x), `toolkits/commerce/src/base/ProductActions/ProductActions.tsx` (4x), `toolkits/commerce/src/base/ProductCard/ProductCard.tsx` (4x), `toolkits/commerce/src/base/ProductSearch/ProductSearch.tsx` (4x)

### `toolkits/commerce/src/base/icons.tsx`
**Imported by:** `plugins/main-menu/src/admin/widgets/SettingsPage.tsx`, `plugins/main-menu/src/admin/widgets/components/MenuItem.tsx`, `themes/blog/src/components/header/Header.tsx`, `themes/blog/src/components/postCard/PostCard.tsx`, `themes/store/src/components/header/MobileHeader.tsx`, `themes/store/src/components/modals/cart/CartModal.tsx`, `themes/store/src/components/modals/productQuickView/ProductQuickView.tsx`, `themes/store/src/components/modals/signIn/PasswordField.tsx`, `themes/store/src/components/modals/viewed/ViewedModal.tsx`, `themes/store/src/components/modals/wishlist/WishlistModal.tsx`
**Often changes with:** `toolkits/commerce/src/base/ProductReviews/ReviewForm.tsx` (6x), `toolkits/commerce/src/base/ProductActions/ProductActions.tsx` (5x), `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx` (5x), `toolkits/commerce/src/base/ProductCard/ProductCard.tsx` (5x), `toolkits/commerce/src/mui/index.ts` (5x)

### `toolkits/commerce/src/base/shared/Alert.tsx`
**Imported by:** `toolkits/commerce/src/base/ProductActions/ProductActions.tsx`, `toolkits/commerce/src/base/ProductReviews/ProductReviews.tsx`, `toolkits/commerce/src/base/ProductReviews/ReviewForm.tsx`
**Often changes with:** `toolkits/commerce/src/base/shared/Button.tsx` (5x), `toolkits/commerce/src/base/shared/Rating.tsx` (5x), `toolkits/commerce/src/base/shared/TextField.tsx` (5x), `toolkits/commerce/src/base/shared/Tooltip.tsx` (5x), `toolkits/commerce/src/base/ProductCard/ProductCard.tsx` (4x)

### `toolkits/commerce/src/base/shared/Button.tsx`
**Imported by:** `toolkits/commerce/src/base/AccountInfo/AccountInfo.tsx`, `toolkits/commerce/src/base/CartList/CartList.tsx`, `toolkits/commerce/src/base/CartList/CartListItem.tsx`, `toolkits/commerce/src/base/Checkout/Checkout.tsx`, `toolkits/commerce/src/base/Checkout/Coupons.tsx`, `toolkits/commerce/src/base/ProductActions/ProductActions.tsx`, `toolkits/commerce/src/base/ProductCard/ProductCard.tsx`, `toolkits/commerce/src/base/ProductReviews/ProductReviews.tsx`, `toolkits/commerce/src/base/ProductReviews/ReviewForm.tsx`
**Often changes with:** `toolkits/commerce/src/base/shared/Alert.tsx` (5x), `toolkits/commerce/src/base/shared/Rating.tsx` (5x), `toolkits/commerce/src/base/shared/TextField.tsx` (5x), `toolkits/commerce/src/base/shared/Tooltip.tsx` (5x), `toolkits/commerce/src/base/ProductCard/ProductCard.tsx` (4x)

### `toolkits/commerce/src/base/shared/Popper.tsx`
**Symbols:** function:`BasePopper`
**Often changes with:** `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx` (4x), `toolkits/commerce/src/base/ProductCard/ProductCard.tsx` (4x), `toolkits/commerce/src/base/ProductSearch/ProductSearch.tsx` (4x), `toolkits/commerce/src/base/ViewedItems/ViewedItems.tsx` (4x), `toolkits/commerce/src/base/Wishlist/Wishlist.tsx` (4x)

### `toolkits/commerce/src/base/shared/Radio.tsx`
**Imported by:** `toolkits/commerce/src/base/Checkout/Checkout.tsx`, `toolkits/commerce/src/mui/RadioGroup/RadioGroup.tsx`
**Symbols:** const_fn:`BaseRadio`
**Often changes with:** `toolkits/commerce/src/base/ProductCard/ProductCard.tsx` (4x), `toolkits/commerce/src/base/ProductGallery/ProductGallery.tsx` (4x), `toolkits/commerce/src/helpers/state.ts` (4x), `toolkits/commerce/src/base/shared/Alert.tsx` (3x), `toolkits/commerce/src/base/shared/Button.tsx` (3x)

### `toolkits/commerce/src/base/shared/Rating.tsx`
**Imported by:** `toolkits/commerce/src/base/ProductCard/ProductCard.tsx`, `toolkits/commerce/src/base/ProductReviews/ProductReviews.tsx`, `toolkits/commerce/src/base/ProductReviews/ReviewForm.tsx`, `toolkits/commerce/src/base/ProductReviews/ReviewItem.tsx`
**Often changes with:** `toolkits/commerce/src/base/shared/Alert.tsx` (5x), `toolkits/commerce/src/base/shared/Button.tsx` (5x), `toolkits/commerce/src/base/shared/TextField.tsx` (5x), `toolkits/commerce/src/base/shared/Tooltip.tsx` (5x), `toolkits/commerce/src/base/ProductCard/ProductCard.tsx` (4x)

### `toolkits/commerce/src/base/shared/Select.tsx`
**Symbols:** const_fn:`BaseSelect`
**Often changes with:** `toolkits/commerce/src/base/ProductCard/ProductCard.tsx` (4x), `toolkits/commerce/src/base/shared/Tooltip.tsx` (4x), `toolkits/commerce/src/helpers/state.ts` (4x), `toolkits/commerce/src/helpers/useStoreAttributes.ts` (4x), `toolkits/commerce/src/base/ProductGallery/ProductGallery.tsx` (3x)

### `toolkits/commerce/src/base/shared/TextField.tsx`
**Imported by:** `toolkits/commerce/src/base/AccountInfo/AccountInfo.tsx`, `toolkits/commerce/src/base/AccountInfo/DefaultElements.tsx`, `toolkits/commerce/src/base/Checkout/Checkout.tsx`, `toolkits/commerce/src/base/Checkout/Coupons.tsx`, `toolkits/commerce/src/base/Checkout/DefaultElements.tsx`, `toolkits/commerce/src/base/ProductReviews/ProductReviews.tsx`, `toolkits/commerce/src/base/ProductReviews/ReviewForm.tsx`, `toolkits/commerce/src/base/ProductSearch/ProductSearch.tsx`
**Often changes with:** `toolkits/commerce/src/base/shared/Alert.tsx` (5x), `toolkits/commerce/src/base/shared/Button.tsx` (5x), `toolkits/commerce/src/base/shared/Rating.tsx` (5x), `toolkits/commerce/src/base/shared/Tooltip.tsx` (5x), `toolkits/commerce/src/base/ProductGallery/ProductGallery.tsx` (4x)

### `toolkits/commerce/src/base/shared/Tooltip.tsx`
**Imported by:** `toolkits/commerce/src/base/ProductCard/ProductCard.tsx`, `toolkits/commerce/src/base/ProductReviews/ProductReviews.tsx`, `toolkits/commerce/src/base/ProductReviews/ReviewForm.tsx`
**Often changes with:** `toolkits/commerce/src/base/shared/Alert.tsx` (5x), `toolkits/commerce/src/base/shared/Button.tsx` (5x), `toolkits/commerce/src/base/shared/Rating.tsx` (5x), `toolkits/commerce/src/base/shared/TextField.tsx` (5x), `toolkits/commerce/src/base/ProductCard/ProductCard.tsx` (4x)

### `toolkits/commerce/src/declarations.d.ts`

### `toolkits/commerce/src/helpers/notifier.tsx`
**Feature:** Utilities
**Imported by:** `toolkits/commerce/src/base/AccountInfo/AccountInfo.tsx`, `toolkits/commerce/src/base/AccountInfo/actions.ts`, `toolkits/commerce/src/base/Checkout/Checkout.tsx`, `toolkits/commerce/src/base/Checkout/actions.ts`, `toolkits/commerce/src/base/ProductActions/ProductActions.tsx`, `toolkits/commerce/src/base/ProductCard/ProductCard.tsx`, `toolkits/commerce/src/base/ProductReviews/ProductReviews.tsx`, `toolkits/commerce/src/base/ProductReviews/ReviewForm.tsx`, `toolkits/commerce/src/mui/Notifier/Notifier.tsx`
**Symbols:** const_fn:`DefaultWrapper`, class:`Notifier`, function:`getNotifier`, function:`setNotifier`
**Often changes with:** `toolkits/commerce/src/base/ProductReviews/ReviewForm.tsx` (5x), `toolkits/commerce/src/base/ProductCard/ProductCard.tsx` (4x), `toolkits/commerce/src/base/shared/Alert.tsx` (4x), `toolkits/commerce/src/base/shared/Button.tsx` (4x), `toolkits/commerce/src/base/shared/Rating.tsx` (4x)

### `toolkits/commerce/src/helpers/state.ts`
**Feature:** Utilities
**Imported by:** `toolkits/commerce/src/base/CartList/CartList.tsx`, `toolkits/commerce/src/base/CategoryFilter/CategoryFilter.tsx`, `toolkits/commerce/src/base/CategoryList/CategoryList.tsx`, `toolkits/commerce/src/base/CategorySort/CategorySort.tsx`, `toolkits/commerce/src/base/Checkout/actions.ts`, `toolkits/commerce/src/base/ProductActions/ProductActions.tsx`, `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx`, `toolkits/commerce/src/helpers/useProductVariants.ts`, `toolkits/commerce/src/helpers/useStoreAttributes.ts`
**Symbols:** class:`ModuleState`, const_fn:`useModuleState`
**Often changes with:** `toolkits/commerce/src/mui/index.ts` (6x), `toolkits/commerce/src/helpers/useStoreAttributes.ts` (5x), `toolkits/commerce/src/base/ProductReviews/ReviewItem.tsx` (4x), `toolkits/commerce/src/base/ProductSearch/ProductSearch.tsx` (4x), `toolkits/commerce/src/base/ViewedItems/ViewedItems.tsx` (4x)

### `toolkits/commerce/src/helpers/useImageLoader.ts`
**Feature:** Utilities
**Symbols:** const_fn:`useImageLoader`, const_fn:`imageLoader`
**Often changes with:** `toolkits/commerce/src/base/ProductSearch/ProductSearch.tsx` (3x), `toolkits/commerce/src/base/ViewedItems/ViewedItems.tsx` (3x), `toolkits/commerce/src/base/Wishlist/Wishlist.tsx` (3x), `toolkits/commerce/src/base/icons.tsx` (3x), `toolkits/commerce/src/base/shared/Popper.tsx` (3x)

### `toolkits/commerce/src/helpers/useLinks.ts`
**Feature:** Utilities
**Imported by:** `toolkits/commerce/src/base/Breadcrumbs/Crumb.tsx`, `toolkits/commerce/src/base/CartList/CartListItem.tsx`, `toolkits/commerce/src/base/ProductCard/ProductCard.tsx`
**Symbols:** const_fn:`useProductLink`, const_fn:`useCategoryLink`
**Often changes with:** `toolkits/commerce/src/base/ProductSearch/ProductSearch.tsx` (3x), `toolkits/commerce/src/base/ViewedItems/ViewedItems.tsx` (3x), `toolkits/commerce/src/base/Wishlist/Wishlist.tsx` (3x), `toolkits/commerce/src/base/shared/Popper.tsx` (3x), `toolkits/commerce/src/base/shared/Radio.tsx` (3x)

### `toolkits/commerce/src/helpers/useProductVariants.ts`
**Feature:** Utilities
**Imports:** `toolkits/commerce/src/helpers/state.ts`
**Symbols:** const_fn:`useProductVariants`
**Often changes with:** `toolkits/commerce/src/base/shared/Tooltip.tsx` (4x), `toolkits/commerce/src/mui/index.ts` (4x), `toolkits/commerce/src/base/icons.tsx` (3x), `toolkits/commerce/src/base/shared/Alert.tsx` (3x), `toolkits/commerce/src/base/shared/Button.tsx` (3x)

### `toolkits/commerce/src/helpers/useStoreAttributes.ts`
**Feature:** Utilities
**Imports:** `toolkits/commerce/src/helpers/state.ts`
**Imported by:** `toolkits/commerce/src/base/CartList/CartList.tsx`, `toolkits/commerce/src/base/CategoryList/CategoryList.tsx`, `toolkits/commerce/src/base/ProductActions/ProductActions.tsx`, `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx`, `toolkits/commerce/src/base/ProductCard/ProductCard.tsx`, `toolkits/commerce/src/base/ViewedItems/ViewedItems.tsx`, `toolkits/commerce/src/base/Wishlist/Wishlist.tsx`
**Symbols:** const_fn:`useStoreAttributes`, const_fn:`checkAttributesData`
**Often changes with:** `toolkits/commerce/src/helpers/state.ts` (5x), `toolkits/commerce/src/base/ProductSearch/ProductSearch.tsx` (5x), `toolkits/commerce/src/base/ViewedItems/ViewedItems.tsx` (4x), `toolkits/commerce/src/base/Wishlist/Wishlist.tsx` (4x), `toolkits/commerce/src/base/shared/Popper.tsx` (4x)

### `toolkits/commerce/src/helpers/withElements.ts`
**Feature:** Utilities
**Imported by:** `toolkits/commerce/src/mui/index.ts`
**Symbols:** const_fn:`hoc`
**Often changes with:** `toolkits/commerce/src/mui/index.ts` (5x), `toolkits/commerce/src/base/icons.tsx` (4x), `toolkits/commerce/src/base/shared/Alert.tsx` (4x), `toolkits/commerce/src/base/shared/Button.tsx` (4x), `toolkits/commerce/src/base/shared/Rating.tsx` (4x)

### `toolkits/commerce/src/mui/Breadcrumbs/Breadcrumbs.tsx`
**Imports:** `system/admin/src/components/inputs/DateInput/styles.ts`
**Imported by:** `toolkits/commerce/src/mui/index.ts`, `toolkits/commerce/src/mui/index.ts`
**Often changes with:** `toolkits/commerce/src/base/icons.tsx` (3x), `toolkits/commerce/src/base/shared/Alert.tsx` (3x), `toolkits/commerce/src/base/shared/Button.tsx` (3x), `toolkits/commerce/src/base/shared/Rating.tsx` (3x), `toolkits/commerce/src/base/shared/TextField.tsx` (3x)

### `toolkits/commerce/src/mui/Loadbox/Loadbox.tsx`
**Feature:** Database
**Imports:** `system/admin/src/components/inputs/DateInput/styles.ts`
**Imported by:** `system/core/frontend/src/components/CList/CList.tsx`, `themes/store/src/components/modals/productQuickView/ProductQuickView.tsx`, `toolkits/commerce/src/mui/index.ts`
**Symbols:** const_fn:`Loadbox`
**Often changes with:** `toolkits/commerce/src/base/Wishlist/Wishlist.tsx` (3x), `toolkits/commerce/src/base/shared/Popper.tsx` (3x), `toolkits/commerce/src/base/shared/Select.tsx` (3x), `toolkits/commerce/src/base/shared/Tooltip.tsx` (3x), `toolkits/commerce/src/helpers/state.ts` (3x)

### `toolkits/commerce/src/mui/Notifier/Notifier.tsx`
**Imports:** `toolkits/commerce/src/helpers/notifier.tsx`
**Imported by:** `toolkits/commerce/src/mui/index.ts`
**Symbols:** const_fn:`NotifierWrapper`
**Often changes with:** `toolkits/commerce/src/base/icons.tsx` (4x), `toolkits/commerce/src/helpers/notifier.tsx` (4x), `toolkits/commerce/src/mui/index.ts` (4x), `toolkits/commerce/src/base/shared/Alert.tsx` (3x), `toolkits/commerce/src/base/shared/Button.tsx` (3x)

### `toolkits/commerce/src/mui/Pagination/Pagination.tsx`
**Imported by:** `system/admin/src/components/entity/entityTable/EntityTable.tsx`, `system/admin/src/components/fileManager/FileManager.tsx`, `system/admin/src/router-pages/pluginMarket/PluginMarket.tsx`, `system/admin/src/router-pages/themeMarket/ThemeMarket.tsx`, `themes/blog/src/pages/search.tsx`, `themes/blog/src/pages/tag/[slug].tsx`, `toolkits/commerce/src/mui/index.ts`
**Symbols:** const_fn:`Pagination`
**Often changes with:** `toolkits/commerce/src/mui/index.ts` (3x)

### `toolkits/commerce/src/mui/Popper/Popper.tsx`
**Imported by:** `system/admin/src/components/inputs/AutocompleteInput.tsx`, `toolkits/commerce/src/base/ProductSearch/ProductSearch.tsx`, `toolkits/commerce/src/mui/index.ts`
**Symbols:** function:`Popper`, const_fn:`onClose`
**Often changes with:** `toolkits/commerce/src/base/shared/Popper.tsx` (3x), `toolkits/commerce/src/base/shared/Select.tsx` (3x), `toolkits/commerce/src/base/shared/Tooltip.tsx` (3x), `toolkits/commerce/src/helpers/state.ts` (3x), `toolkits/commerce/src/helpers/useStoreAttributes.ts` (3x)

### `toolkits/commerce/src/mui/ProductActions/ProductActions.tsx`
**Imported by:** `toolkits/commerce/src/mui/index.ts`, `toolkits/commerce/src/mui/index.ts`
**Symbols:** const_fn:`ActionButton`
**Often changes with:** `toolkits/commerce/src/base/shared/Rating.tsx` (3x), `toolkits/commerce/src/base/shared/TextField.tsx` (3x), `toolkits/commerce/src/base/shared/Tooltip.tsx` (3x), `toolkits/commerce/src/helpers/withElements.ts` (3x), `toolkits/commerce/src/mui/ProductAttributes/AttributeTitle.tsx` (3x)

### `toolkits/commerce/src/mui/ProductAttributes/AttributeTitle.tsx`
**Imports:** `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx`
**Imported by:** `toolkits/commerce/src/mui/index.ts`
**Often changes with:** `toolkits/commerce/src/mui/ProductAttributes/AttributeValue.tsx` (6x), `toolkits/commerce/src/mui/index.ts` (6x), `toolkits/commerce/src/base/shared/Tooltip.tsx` (4x), `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx` (4x), `toolkits/commerce/src/base/shared/Rating.tsx` (3x)

### `toolkits/commerce/src/mui/ProductAttributes/AttributeValue.tsx`
**Imports:** `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx`
**Imported by:** `toolkits/commerce/src/mui/index.ts`
**Often changes with:** `toolkits/commerce/src/mui/ProductAttributes/AttributeTitle.tsx` (6x), `toolkits/commerce/src/mui/index.ts` (6x), `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx` (5x), `toolkits/commerce/src/base/shared/Tooltip.tsx` (4x), `toolkits/commerce/src/base/shared/Rating.tsx` (3x)

### `toolkits/commerce/src/mui/QuantityField/QuantityField.tsx`
**Imports:** `toolkits/commerce/src/base/icons.tsx`
**Imported by:** `toolkits/commerce/src/mui/index.ts`
**Symbols:** function:`QuantityField`
**Often changes with:** `toolkits/commerce/src/base/shared/TextField.tsx` (4x), `toolkits/commerce/src/base/shared/Tooltip.tsx` (4x), `toolkits/commerce/src/helpers/withElements.ts` (4x), `toolkits/commerce/src/mui/index.ts` (4x), `toolkits/commerce/src/helpers/notifier.tsx` (3x)

### `toolkits/commerce/src/mui/RadioGroup/RadioGroup.tsx`
**Imports:** `toolkits/commerce/src/base/shared/Radio.tsx`
**Imported by:** `toolkits/commerce/src/mui/index.ts`
**Symbols:** function:`RadioGroup`, const_fn:`label`
**Often changes with:** `toolkits/commerce/src/helpers/state.ts` (4x), `toolkits/commerce/src/helpers/useImageLoader.ts` (3x), `toolkits/commerce/src/helpers/useLinks.ts` (3x), `toolkits/commerce/src/helpers/useStoreAttributes.ts` (3x), `toolkits/commerce/src/mui/index.ts` (3x)

### `toolkits/commerce/src/mui/Select/Select.tsx`
**Imported by:** `toolkits/commerce/src/base/CategorySort/CategorySort.tsx`, `toolkits/commerce/src/base/CurrencySwitch/CurrencySwitch.tsx`, `toolkits/commerce/src/mui/index.ts`
**Symbols:** function:`Select`
**Often changes with:** `toolkits/commerce/src/mui/index.ts` (4x), `toolkits/commerce/src/base/shared/Tooltip.tsx` (3x), `toolkits/commerce/src/helpers/state.ts` (3x), `toolkits/commerce/src/helpers/useStoreAttributes.ts` (3x), `toolkits/commerce/src/mui/Loadbox/Loadbox.tsx` (3x)

### `toolkits/commerce/src/mui/index.ts`
**Imports:** `toolkits/commerce/src/base/AccountInfo/AccountInfo.tsx`, `toolkits/commerce/src/base/AccountOrders/AccountOrders.tsx`, `toolkits/commerce/src/mui/Breadcrumbs/Breadcrumbs.tsx`, `toolkits/commerce/src/base/CartList/CartList.tsx`, `toolkits/commerce/src/base/CategoryList/CategoryList.tsx`, `toolkits/commerce/src/base/CategorySort/CategorySort.tsx`, `toolkits/commerce/src/base/Checkout/Checkout.tsx`, `toolkits/commerce/src/base/CurrencySwitch/CurrencySwitch.tsx`, `toolkits/commerce/src/mui/ProductActions/ProductActions.tsx`, `toolkits/commerce/src/base/ProductCard/ProductCard.tsx`
**Often changes with:** `toolkits/commerce/src/helpers/state.ts` (6x), `toolkits/commerce/src/mui/ProductAttributes/AttributeTitle.tsx` (6x), `toolkits/commerce/src/mui/ProductAttributes/AttributeValue.tsx` (6x), `toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx` (6x), `toolkits/commerce/src/helpers/withElements.ts` (5x)

### `toolkits/commerce/tests/helpers.ts`
**Feature:** Testing
**Imported by:** `system/admin/src/components/entity/entityEdit/components/EntityCustomFields.tsx`, `system/admin/src/components/entity/entityEdit/components/EntityFields.tsx`, `system/admin/src/components/entity/entityEdit/components/EntityHeader.tsx`, `system/admin/src/components/entity/entityEdit/components/EntityMetaFields.tsx`, `system/admin/src/components/entity/entityTable/EntityTable.tsx`, `system/admin/src/components/entity/entityTable/components/DeleteSelectedButton.tsx`, `system/admin/src/components/entity/entityTable/components/TableHeader.tsx`, `system/admin/src/components/inputs/Image/ImageInput.tsx`, `system/admin/src/components/notificationCenter/NotificationCenter.tsx`, `system/admin/src/components/topbar/Topbar.tsx`
**Symbols:** const_fn:`mockWorkingDirectory`, const_fn:`tearDown`

### `toolkits/commerce/tests/setup.ts`
**Feature:** Testing

### `website/.eslintrc.js`

### `website/api-generator/generate.js`
**Feature:** API Layer
**Symbols:** const_fn:`generate`, const_fn:`processFiles`
**Often changes with:** `system/manager/src/managers/baseManager.ts` (3x)

### `website/babel.config.js`

### `website/docusaurus.config.js`
**Purpose:** @type {import('@docusaurus/types').DocusaurusConfig}
**Often changes with:** `website/src/pages/index.tsx` (10x), `website/src/components/CoverFlowImages.tsx` (4x), `website/src/pages/latest-frontend-dependencies.tsx` (4x), `website/src/theme/Footer/index.tsx` (4x), `system/utils/src/plugins/rollup.ts` (3x)

### `website/sidebarItemsGenerator.js`
**Symbols:** function:`sidebarItemsGenerator`, const_fn:`parseItems`

### `website/sidebars.js`
**Purpose:** Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesy
**Often changes with:** `website/docusaurus.config.js` (3x)

### `website/src/components/CoverFlowImages.tsx`
**Feature:** UI Components
**Imports:** `website/src/components/Lightbox.tsx`
**Imported by:** `website/src/pages/index.tsx`
**Symbols:** const_fn:`CoverFlowImages`, const_fn:`openLightBox`, const_fn:`onScroll`, function:`isElementInViewport`
**Often changes with:** `website/docusaurus.config.js` (4x), `website/src/pages/index.tsx` (4x)

### `website/src/components/Lightbox.tsx`
**Feature:** UI Components
**Imported by:** `website/src/components/CoverFlowImages.tsx`
**Symbols:** class:`Lightbox`

### `website/src/declarations.d.ts`

### `website/src/helpers/api-client.ts`
**Feature:** Utilities
**Imported by:** `website/src/pages/latest-frontend-dependencies.tsx`
**Symbols:** class:`ApiClient`

### `website/src/pages/index.tsx`
**Feature:** Pages
**Imports:** `system/core/frontend/src/components/Link/Link.tsx`, `themes/store/src/components/layout/Layout.tsx`, `website/src/components/CoverFlowImages.tsx`
**Symbols:** function:`Home`
**Often changes with:** `website/docusaurus.config.js` (10x), `website/src/pages/latest-frontend-dependencies.tsx` (5x), `website/src/components/CoverFlowImages.tsx` (4x), `themes/store/src/pages/checkout.tsx` (4x), `website/src/theme/Footer/index.tsx` (3x)

### `website/src/pages/latest-frontend-dependencies.tsx`
**Feature:** Pages
**Imports:** `system/core/frontend/src/components/Link/Link.tsx`, `themes/store/src/components/layout/Layout.tsx`, `website/src/helpers/api-client.ts`
**Symbols:** function:`FrontendDependencies`, const_fn:`handleExpandClick`, const_fn:`versions`, const_fn:`getDependencies`, const_fn:`getDepName`, const_fn:`changeCmsVersion`
**Often changes with:** `website/src/pages/index.tsx` (5x), `website/docusaurus.config.js` (4x)

### `website/src/theme/Footer/index.tsx`
**Purpose:** Copyright (c) Facebook, Inc. and its affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
**Imports:** `system/core/frontend/src/components/Link/Link.tsx`
**Imported by:** `plugins/main-menu/tests/frontend/index.test.tsx`, `plugins/newsletter/tests/frontend/index.test.tsx`, `plugins/product-filter/tests/frontend/index.test.tsx`, `plugins/product-showcase/tests/frontend/index.test.tsx`, `system/manager/startup.js`, `themes/blog/tests/pages/index.test.tsx`
**Symbols:** function:`FooterLink`, const_fn:`FooterLogo`, function:`Footer`, function:`gtag`
**Often changes with:** `website/docusaurus.config.js` (4x), `website/src/pages/index.tsx` (3x)

### `website/src/theme/prism-include-languages.js`
**Purpose:** Copyright (c) Facebook, Inc. and its affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
**Imports:** `system/manager/src/config.ts`
**Symbols:** const_fn:`prismIncludeLanguages`, function:`withId`
**Often changes with:** `website/docusaurus.config.js` (3x)

## Import Graph (Adjacency List)

```
plugins/main-menu/src/admin/index.tsx → plugins/main-menu/src/admin/widgets/SettingsPage.tsx
plugins/main-menu/src/admin/styles.ts → system/admin/src/components/inputs/DateInput/styles.ts
plugins/main-menu/src/admin/widgets/SettingsPage.tsx → themes/store/src/types.ts, toolkits/commerce/src/base/icons.tsx, system/admin/src/components/inputs/DateInput/styles.ts, plugins/main-menu/src/admin/widgets/components/MenuItem.tsx
plugins/main-menu/src/admin/widgets/components/MenuItem.tsx → themes/store/src/types.ts, toolkits/commerce/src/base/icons.tsx, system/admin/src/components/inputs/DateInput/styles.ts
plugins/main-menu/src/frontend/DefaultElements.tsx → themes/store/src/types.ts
plugins/main-menu/src/frontend/index.tsx → themes/store/src/types.ts, plugins/main-menu/src/frontend/DefaultElements.tsx
plugins/main-menu/tests/admin/SettingsPage.test.tsx → plugins/stripe/src/admin/widgets/SettingsPage.tsx
plugins/main-menu/tests/frontend/index.test.tsx → website/src/theme/Footer/index.tsx
plugins/main-menu/tests/jest.config.ts → themes/store/src/types.ts
plugins/marqo/src/admin/index.tsx → themes/store/src/constants.js, plugins/marqo/src/admin/widgets/SettingsPage.tsx
plugins/marqo/src/admin/widgets/SettingsPage.tsx → themes/store/src/types.ts
plugins/marqo/src/backend/controllers/plugin-marqo.controller.ts → plugins/marqo/src/backend/marqo-client.ts
plugins/marqo/src/backend/index.ts → themes/store/src/types.ts, plugins/marqo/src/backend/controllers/plugin-marqo.controller.ts, plugins/marqo/src/backend/marqo-client.ts, plugins/marqo/src/backend/resolvers/plugin-marqo.resolver.ts
plugins/marqo/src/backend/marqo-client.ts → themes/store/src/types.ts
plugins/marqo/src/backend/resolvers/plugin-marqo.resolver.ts → plugins/marqo/src/backend/marqo-client.ts
plugins/marqo/src/frontend/components/SimilarProducts.tsx → plugins/marqo/src/frontend/components/ProductCard.tsx, system/server/src/helpers/utils.ts
plugins/marqo/src/frontend/index.tsx → themes/store/src/types.ts, plugins/marqo/src/frontend/components/SimilarProducts.tsx
plugins/marqo/src/frontend/utils.ts → themes/store/src/constants.js
plugins/newsletter/src/admin/index.tsx → plugins/newsletter/src/admin/widgets/Dashboard.tsx, plugins/newsletter/src/admin/widgets/SettingsPage.tsx
plugins/newsletter/src/admin/styles.ts → system/admin/src/components/inputs/DateInput/styles.ts
plugins/newsletter/src/admin/widgets/Dashboard.tsx → system/admin/src/components/inputs/DateInput/styles.ts
plugins/newsletter/src/admin/widgets/SettingsPage.tsx → themes/store/src/types.ts, system/admin/src/components/inputs/DateInput/styles.ts
plugins/newsletter/src/backend/controllers/plugin-newsletter.controller.ts → system/core/common/src/auth.ts
plugins/newsletter/src/backend/entities/newsletter-form.entity.ts → themes/store/src/types.ts
plugins/newsletter/src/backend/index.ts → plugins/newsletter/src/backend/controllers/plugin-newsletter.controller.ts, plugins/newsletter/src/backend/entities/newsletter-form.entity.ts, plugins/newsletter/src/backend/resolvers/plugin-newsletter.resolver.ts
plugins/newsletter/src/backend/resolvers/plugin-newsletter.resolver.ts → system/core/common/src/auth.ts
plugins/newsletter/src/frontend/index.tsx → plugins/newsletter/src/frontend/styles.ts
plugins/newsletter/src/frontend/styles.ts → system/admin/src/components/inputs/DateInput/styles.ts
plugins/newsletter/tests/admin/Dashboard.test.tsx → system/admin/src/router-pages/dashboard/Dashboard.tsx
plugins/newsletter/tests/admin/SettingsPage.test.tsx → plugins/stripe/src/admin/widgets/SettingsPage.tsx
plugins/newsletter/tests/frontend/index.test.tsx → website/src/theme/Footer/index.tsx
plugins/newsletter/tests/jest.config.ts → themes/store/src/types.ts
plugins/paypal/src/admin/index.tsx → themes/store/src/constants.js, plugins/paypal/src/admin/widgets/SettingsPage.tsx
plugins/paypal/src/admin/widgets/SettingsPage.tsx → themes/store/src/types.ts
plugins/paypal/src/backend/actions/create-payment.action.ts → themes/store/src/constants.js, themes/store/src/types.ts
plugins/paypal/src/backend/index.ts → themes/store/src/constants.js, plugins/paypal/src/backend/actions/create-payment.action.ts
plugins/paypal/tests/admin/SettingsPage.test.tsx → plugins/stripe/src/admin/widgets/SettingsPage.tsx
plugins/paypal/tests/backend/create-payment.action.test.ts → themes/store/src/types.ts
plugins/paypal/tests/jest.config.ts → themes/store/src/types.ts
plugins/product-filter/src/admin/index.tsx → plugins/product-filter/src/admin/widgets/SettingsPage.tsx, plugins/product-filter/src/admin/widgets/ThemeEditor.tsx
plugins/product-filter/src/admin/widgets/SettingsPage.tsx → themes/store/src/constants.js, themes/store/src/types.ts
plugins/product-filter/src/constants.ts → plugins/product-filter/src/types.ts
plugins/product-filter/src/frontend/components/Filter.tsx → system/admin/src/components/inputs/DateInput/styles.ts, themes/store/src/constants.js, themes/store/src/types.ts, system/admin/src/components/inputs/DateInput/styles.ts, plugins/product-filter/src/frontend/utils/queries.ts, plugins/product-filter/src/frontend/components/Slider.tsx
plugins/product-filter/src/frontend/components/Slider.tsx → system/admin/src/components/inputs/DateInput/styles.ts
plugins/product-filter/src/frontend/index.tsx → plugins/product-filter/src/frontend/components/Filter.tsx, themes/store/src/types.ts
plugins/product-filter/src/frontend/styles.ts → system/admin/src/components/inputs/DateInput/styles.ts
plugins/product-filter/tests/admin/SettingsPage.test.tsx → plugins/stripe/src/admin/widgets/SettingsPage.tsx
plugins/product-filter/tests/frontend/index.test.tsx → website/src/theme/Footer/index.tsx
plugins/product-filter/tests/jest.config.ts → themes/store/src/types.ts
plugins/product-showcase/src/admin/index.tsx → plugins/product-showcase/src/admin/widgets/SettingsPage.tsx
plugins/product-showcase/src/admin/widgets/SettingsPage.tsx → system/admin/src/components/inputs/DateInput/styles.ts, themes/store/src/types.ts
plugins/product-showcase/src/backend/index.ts → plugins/product-showcase/src/backend/resolvers/product-showcase.resolver.ts
plugins/product-showcase/src/backend/resolvers/product-showcase.resolver.ts → themes/store/src/types.ts
plugins/product-showcase/src/frontend/index.tsx → plugins/product-showcase/src/frontend/ProductCard.tsx
plugins/product-showcase/tests/admin/SettingsPage.test.tsx → plugins/stripe/src/admin/widgets/SettingsPage.tsx
plugins/product-showcase/tests/frontend/index.test.tsx → website/src/theme/Footer/index.tsx
plugins/product-showcase/tests/jest.config.ts → themes/store/src/types.ts
plugins/stripe/src/admin/index.tsx → themes/store/src/constants.js, plugins/stripe/src/admin/widgets/SettingsPage.tsx
plugins/stripe/src/admin/widgets/SettingsPage.tsx → themes/store/src/types.ts
plugins/stripe/src/backend/actions/create-payment.action.ts → themes/store/src/constants.js, themes/store/src/types.ts
plugins/stripe/src/backend/index.ts → themes/store/src/constants.js, plugins/stripe/src/backend/actions/create-payment.action.ts
plugins/stripe/tests/admin/SettingsPage.test.tsx → plugins/stripe/src/admin/widgets/SettingsPage.tsx
plugins/stripe/tests/jest.config.ts → themes/store/src/types.ts
system/admin/jest.config.ts → themes/store/src/types.ts
system/admin/postcss.config.js → system/core/backend/src/helpers/paths.ts
system/admin/src/components/cmsInfo/CmsInfo.tsx → themes/store/src/components/modals/baseModal/Modal.tsx
system/admin/src/components/draggableList/DraggableList.tsx → system/admin/src/components/buttons/IconButton.tsx
system/admin/src/components/entity/entityEdit/EntityEdit.test.tsx → system/admin/src/components/entity/entityEdit/EntityEdit.tsx
system/admin/src/components/entity/entityEdit/EntityEdit.tsx → themes/store/src/components/toast/toast.tsx, themes/store/src/types.ts, system/server/src/helpers/utils.ts, system/admin/src/components/entity/entityEdit/components/EntityFields.tsx, system/admin/src/components/entity/entityEdit/components/EntityHeader.tsx, system/admin/src/components/entity/entityEdit/helpers.tsx, system/admin/src/components/entity/entityEdit/type.ts
system/admin/src/components/entity/entityEdit/components/EntityCustomFields.tsx → toolkits/commerce/tests/helpers.ts
system/admin/src/components/entity/entityEdit/components/EntityFields.tsx → toolkits/commerce/tests/helpers.ts, system/admin/src/components/entity/entityEdit/components/EntityCustomFields.tsx, system/admin/src/components/entity/entityEdit/components/EntityMetaFields.tsx, system/admin/src/components/entity/entityEdit/components/InputField.tsx
system/admin/src/components/entity/entityEdit/components/EntityHeader.tsx → system/admin/src/components/buttons/IconButton.tsx, system/admin/src/components/buttons/TextButton.tsx, toolkits/commerce/tests/helpers.ts, system/admin/src/components/entity/entityEdit/components/ElevationScroll.tsx
system/admin/src/components/entity/entityEdit/components/EntityMetaFields.tsx → system/admin/src/components/inputs/AutocompleteInput.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx, toolkits/commerce/tests/helpers.ts
system/admin/src/components/entity/entityEdit/components/InputField.tsx → themes/store/src/helpers/forceUpdate.ts, themes/store/src/types.ts
system/admin/src/components/entity/entityEdit/helpers.tsx → themes/store/src/types.ts, system/admin/src/components/entity/entityEdit/type.ts
system/admin/src/components/entity/entityEdit/type.ts → themes/store/src/types.ts
system/admin/src/components/entity/entityTable/EntityTable.test.tsx → system/admin/src/router-pages/settings/pages/store.tsx, themes/store/src/types.ts, system/admin/src/components/entity/entityTable/EntityTable.tsx
system/admin/src/components/entity/entityTable/EntityTable.tsx → toolkits/commerce/tests/helpers.ts, system/admin/src/components/modal/Confirmation.tsx, toolkits/commerce/src/mui/Pagination/Pagination.tsx, system/admin/src/components/skeleton/SkeletonPreloader.tsx, themes/store/src/components/toast/toast.tsx, themes/store/src/types.ts, system/server/src/helpers/utils.ts, system/admin/src/components/entity/entityTable/components/EntityTableItem.tsx, system/admin/src/components/entity/entityTable/components/PageHeader.tsx, system/admin/src/components/entity/entityTable/components/TableHeader.tsx
system/admin/src/components/entity/entityTable/components/ColumnConfigureItem.tsx → system/admin/src/components/inputs/SwitchInput/SwitchInput.tsx, themes/store/src/types.ts
system/admin/src/components/entity/entityTable/components/DeleteSelectedButton.tsx → toolkits/commerce/tests/helpers.ts, system/admin/src/router-pages/settings/pages/store.tsx, system/admin/src/components/buttons/IconButton.tsx
system/admin/src/components/entity/entityTable/components/EntityTableItem.tsx → system/admin/src/helpers/time.ts, system/admin/src/router-pages/settings/pages/store.tsx, system/admin/src/components/buttons/IconButton.tsx, system/admin/src/components/inputs/CheckboxInput.tsx, themes/store/src/types.ts
system/admin/src/components/entity/entityTable/components/PageHeader.tsx → system/admin/src/components/sideNav/ResponsiveSideNav.tsx, system/admin/src/components/buttons/IconButton.tsx, system/admin/src/components/buttons/TextButton.tsx, system/admin/src/components/icons/clearFilter.tsx, themes/store/src/types.ts, system/admin/src/components/entity/entityTable/components/DeleteSelectedButton.tsx
system/admin/src/components/entity/entityTable/components/SearchContent.tsx → system/admin/src/components/inputs/AutocompleteInput.tsx, system/admin/src/components/inputs/DateInput/DateInput.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx, system/admin/src/components/entity/entityTable/components/TableHeader.tsx
system/admin/src/components/entity/entityTable/components/TableHeader.tsx → system/admin/src/components/inputs/DateInput/styles.ts, themes/store/src/helpers/forceUpdate.ts, toolkits/commerce/tests/helpers.ts, system/admin/src/router-pages/settings/pages/store.tsx, system/admin/src/components/buttons/TextButton.tsx, system/admin/src/components/draggableList/DraggableList.tsx, system/admin/src/components/inputs/CheckboxInput.tsx, themes/store/src/types.ts, system/admin/src/components/entity/entityTable/EntityTable.tsx, system/admin/src/components/entity/entityTable/components/ColumnConfigureItem.tsx, system/admin/src/components/entity/entityTable/components/SearchContent.tsx
system/admin/src/components/fileManager/FileItem.tsx → system/admin/src/components/buttons/IconButton.tsx, system/admin/src/components/fileManager/types.ts
system/admin/src/components/fileManager/FileManager.test.tsx → system/admin/src/components/fileManager/FileManager.tsx, system/admin/src/components/fileManager/helpers.ts
system/admin/src/components/fileManager/FileManager.tsx → system/admin/src/components/buttons/IconButton.tsx, system/admin/src/components/buttons/TextButton.tsx, system/admin/src/components/loadBox/LoadingStatus.tsx, system/admin/src/components/modal/Confirmation.tsx, themes/store/src/components/modals/baseModal/Modal.tsx, toolkits/commerce/src/mui/Pagination/Pagination.tsx, themes/store/src/components/toast/toast.tsx, system/admin/src/components/fileManager/FileItem.tsx, system/admin/src/components/fileManager/types.ts
system/admin/src/components/inputs/AutocompleteInput.tsx → toolkits/commerce/src/mui/Popper/Popper.tsx, system/admin/src/components/inputs/DateInput/styles.ts, system/admin/src/components/inputs/TextInput/TextInput.tsx
system/admin/src/components/inputs/ColorInput.tsx → themes/store/src/helpers/forceUpdate.ts, system/admin/src/components/inputs/TextInput/TextInput.tsx
system/admin/src/components/inputs/DateInput/DateInput.tsx → system/admin/src/components/inputs/DateInput/styles.ts
system/admin/src/components/inputs/DateInput/styles.ts → system/admin/src/helpers/getPalette.ts
system/admin/src/components/inputs/GalleryInput/GalleryInput.tsx → system/admin/src/components/icons/grabIcon.tsx, system/admin/src/components/inputs/Image/ImageInput.tsx, system/admin/src/components/inputs/GalleryInput/ImageItem.tsx
system/admin/src/components/inputs/GalleryInput/ImageItem.tsx → system/admin/src/components/inputs/Image/ImageInput.tsx
system/admin/src/components/inputs/Image/ImageInput.tsx → toolkits/commerce/tests/helpers.ts, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx
system/admin/src/components/inputs/Image/RegisteredImageInput.tsx → system/admin/src/components/inputs/Image/ImageInput.tsx
system/admin/src/components/inputs/Search/ListItem.tsx → system/admin/src/components/inputs/CheckboxInput.tsx, themes/store/src/helpers/forceUpdate.ts
system/admin/src/components/inputs/Search/SearchInput.test.tsx → system/admin/src/components/inputs/Search/SearchInput.tsx
system/admin/src/components/inputs/Search/SearchInput.tsx → system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx, system/admin/src/components/inputs/Search/ListItem.tsx
system/admin/src/components/inputs/SelectInput/RegisteredSelectInput.tsx → system/admin/src/components/inputs/SelectInput/SelectInput.tsx
system/admin/src/components/inputs/SwitchInput/RegisteredSwitchInput.tsx → system/admin/src/components/inputs/SwitchInput/SwitchInput.tsx
system/admin/src/components/inputs/TextEditor/TextEditor.tsx → system/admin/src/helpers/editor/editor.ts
system/admin/src/components/inputs/TextInput/RegisteredTextInput.tsx → system/server/src/helpers/utils.ts, system/admin/src/components/inputs/TextInput/TextInput.tsx
system/admin/src/components/inputs/TextInput/TextInput.tsx → system/admin/src/helpers/NumberFormatCustom.tsx
system/admin/src/components/layout/Layout.tsx → system/admin/src/components/sideNav/ResponsiveSideNav.tsx, system/admin/src/helpers/LayoutPortal.tsx, system/admin/src/helpers/navigation.tsx, system/admin/src/router-pages/settings/pages/store.tsx, system/admin/src/router-pages/404/404page.tsx, system/admin/src/components/errorBoundaries/PageErrorBoundary.tsx, system/admin/src/components/fileManager/FileManager.tsx, system/admin/src/components/modal/Confirmation.tsx, system/admin/src/components/layout/components/BrowserRouter.tsx, system/admin/src/components/layout/hooks/useAppState.ts, system/admin/src/components/layout/hooks/useTheme.ts
system/admin/src/components/layout/hooks/useAppState.ts → themes/store/src/components/toast/toast.tsx, system/admin/src/constants/PageInfos.ts, system/admin/src/helpers/customEntities.tsx, themes/store/src/helpers/forceUpdate.ts, system/admin/src/helpers/loadPlugins.ts, system/admin/src/router-pages/settings/pages/store.tsx
system/admin/src/components/layout/hooks/useTheme.ts → system/admin/src/helpers/getPalette.ts, system/admin/src/components/inputs/DateInput/styles.ts
system/admin/src/components/loadBox/Loadbox.test.tsx → system/admin/src/components/loadBox/LoadBox.tsx
system/admin/src/components/loadBox/LoadingStatus.tsx → system/admin/src/components/loadBox/LoadBox.tsx
system/admin/src/components/modal/Confirmation.test.tsx → system/admin/src/components/modal/Confirmation.tsx
system/admin/src/components/modal/Confirmation.tsx → system/admin/src/components/buttons/TextButton.tsx, system/admin/src/components/modal/Modal.tsx
system/admin/src/components/modeSwitch/ModeSwitch.tsx → system/admin/src/components/inputs/DateInput/styles.ts
system/admin/src/components/notificationCenter/NotificationCenter.tsx → toolkits/commerce/tests/helpers.ts, system/admin/src/router-pages/settings/pages/store.tsx, system/admin/src/components/modal/Confirmation.tsx, themes/store/src/components/toast/toast.tsx, system/admin/src/components/notificationCenter/UpdateInfoCard.tsx
system/admin/src/components/pluginSettingsLayout/PluginSettingsLayout.tsx → themes/store/src/components/toast/toast.tsx, system/admin/src/constants/PageInfos.ts, system/admin/src/components/loadBox/LoadBox.tsx, system/admin/src/components/market/MarketModal.tsx, themes/store/src/components/modals/baseModal/Modal.tsx, system/admin/src/components/buttons/TextButton.tsx, system/admin/src/components/buttons/IconButton.tsx
system/admin/src/components/sideNav/ResponsiveSideNav.tsx → system/admin/src/components/buttons/IconButton.tsx, system/admin/src/helpers/navigation.tsx, system/admin/src/components/sideNav/SideNav.tsx, system/admin/src/components/sideNav/SwipeableTemporaryDrawer.tsx
system/admin/src/components/sideNav/SideNav.tsx → themes/store/src/helpers/forceUpdate.ts, system/admin/src/helpers/navigation.tsx, system/admin/src/router-pages/settings/pages/store.tsx, system/admin/src/components/topbar/Topbar.tsx, system/admin/src/components/sideNav/SideNavLink.tsx
system/admin/src/components/sideNav/SideNavLink.tsx → system/admin/src/constants/PageInfos.ts, system/admin/src/components/sideNav/ResponsiveSideNav.tsx
system/admin/src/components/systemMonitor/SystemMonitor.tsx → system/admin/src/components/loadBox/LoadBox.tsx, themes/store/src/components/modals/baseModal/Modal.tsx, system/admin/src/components/systemMonitor/chartOptions.ts
system/admin/src/components/textFieldWithTooltip/TextFieldWithTooltip.tsx → system/admin/src/components/buttons/IconButton.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx
system/admin/src/components/topbar/Topbar.tsx → system/admin/src/constants/PageInfos.ts, themes/store/src/helpers/forceUpdate.ts, toolkits/commerce/tests/helpers.ts, system/admin/src/router-pages/settings/pages/store.tsx, system/admin/src/components/cmsInfo/CmsInfo.tsx, toolkits/commerce/tests/helpers.ts, system/admin/src/components/modal/Confirmation.tsx, system/admin/src/components/systemMonitor/SystemMonitor.tsx, themes/store/src/components/toast/toast.tsx
system/admin/src/components/transferList/CheckList.tsx → system/admin/src/components/inputs/CheckboxInput.tsx, system/admin/src/components/transferList/helpers.ts
system/admin/src/components/transferList/TransferList.tsx → system/admin/src/components/buttons/TextButton.tsx, system/admin/src/components/transferList/CheckList.tsx, system/admin/src/components/transferList/helpers.ts
system/admin/src/components/virtualList/infiniteLoader.ts → system/admin/src/components/virtualList/isRangeVisible.ts, system/admin/src/components/virtualList/scanForUnloadedRanges.ts, system/admin/src/components/virtualList/types.ts
system/admin/src/components/virtualList/scanForUnloadedRanges.ts → system/admin/src/components/virtualList/types.ts
system/admin/src/exports.ts → system/admin/src/redux/store.ts
system/admin/src/helpers/LayoutPortal.tsx → system/admin/src/helpers/forceUpdate.ts
system/admin/src/helpers/customEntities.tsx → system/admin/src/components/entity/entityEdit/EntityEdit.tsx, system/admin/src/components/entity/entityTable/EntityTable.tsx, themes/store/src/types.ts, system/admin/src/constants/PageInfos.ts, system/admin/src/router-pages/settings/pages/store.tsx, system/admin/src/helpers/time.ts
system/admin/src/helpers/customFields/RenderCustomFields.tsx → themes/store/src/helpers/forceUpdate.ts, system/admin/src/helpers/customFields/helpers.ts, system/admin/src/helpers/customFields/state.ts, system/admin/src/helpers/customFields/types.ts
system/admin/src/helpers/customFields/fields.tsx → system/admin/src/components/inputs/CheckboxInput.tsx, system/admin/src/components/inputs/ColorInput.tsx, system/admin/src/components/inputs/DateInput/DateInput.tsx, system/admin/src/components/inputs/GalleryInput/GalleryInput.tsx, system/admin/src/components/inputs/Image/ImageInput.tsx, system/admin/src/components/inputs/SelectInput/SelectInput.tsx, system/admin/src/components/inputs/TextEditor/TextEditor.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx, system/admin/src/helpers/editor/editor.ts, system/admin/src/helpers/NumberFormatCustom.tsx, system/admin/src/helpers/customFields/helpers.ts, system/admin/src/helpers/customFields/hooks.ts, system/admin/src/helpers/customFields/state.ts
system/admin/src/helpers/customFields/helpers.ts → system/admin/src/helpers/customFields/state.ts, system/admin/src/helpers/customFields/types.ts
system/admin/src/helpers/customFields/state.ts → system/admin/src/helpers/customFields/types.ts
system/admin/src/helpers/editor/editor.ts → toolkits/commerce/tests/helpers.ts, themes/store/src/components/toast/toast.tsx, system/admin/src/helpers/editor/customHtml/CustomHtml.ts, system/admin/src/helpers/editor/fontSize/FontSize.tsx
system/admin/src/helpers/editor/fontSize/FontSize.tsx → system/admin/src/helpers/LayoutPortal.tsx, system/admin/src/helpers/editor/fontSize/InputSlider.tsx
system/admin/src/helpers/editor/fontSize/InputSlider.tsx → plugins/product-filter/src/frontend/components/Slider.tsx
system/admin/src/helpers/importDependencies.tsx → system/utils/src/exports.ts, system/admin/src/components/inputs/DateInput/styles.ts
system/admin/src/helpers/navigation.tsx → system/admin/src/helpers/customEntities.tsx, system/admin/src/router-pages/settings/pages/store.tsx
system/admin/src/hooks/useDashboard.tsx → system/core/frontend/src/components/AdminPanelWidget/WidgetErrorBoundary.tsx
system/admin/src/pages/_app.tsx → system/admin/src/helpers/importDependencies.tsx
system/admin/src/pages/_document.tsx → system/renderer/src/helpers/document.tsx
system/admin/src/redux/helpers.ts → system/admin/src/redux/store.ts
system/admin/src/redux/store.ts → system/admin/src/helpers/Draggable/Draggable.ts, system/admin/src/redux/helpers.ts
system/admin/src/router-pages/attribute/AttributePage.tsx → system/admin/src/components/entity/entityEdit/EntityEdit.tsx, system/admin/src/constants/PageInfos.ts, system/admin/src/router-pages/attribute/components/AttributeValues.tsx
system/admin/src/router-pages/attribute/components/AttributeValues.tsx → system/admin/src/components/buttons/IconButton.tsx, system/admin/src/components/transferList/CheckList.tsx, system/admin/src/router-pages/attribute/components/ValueItem.tsx
system/admin/src/router-pages/attribute/components/ValueItem.tsx → system/admin/src/components/buttons/IconButton.tsx, toolkits/commerce/tests/helpers.ts, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx
system/admin/src/router-pages/attributeList/AttributesList.tsx → system/admin/src/components/entity/entityTable/EntityTable.tsx, system/admin/src/constants/PageInfos.ts, system/admin/src/helpers/customEntities.tsx
system/admin/src/router-pages/attributeList/AttributesPage.test.tsx → system/admin/src/router-pages/attributeList/AttributesList.tsx
system/admin/src/router-pages/category/CategoryPage.test.tsx → system/admin/src/router-pages/category/CategoryPage.tsx
system/admin/src/router-pages/category/CategoryPage.tsx → system/admin/src/components/inputs/Search/SearchInput.tsx, system/admin/src/components/entity/entityEdit/EntityEdit.tsx, system/admin/src/constants/PageInfos.ts
system/admin/src/router-pages/categoryList/CategoryList.test.tsx → system/admin/src/router-pages/categoryList/CategoryList.tsx, system/admin/src/router-pages/settings/pages/store.tsx
system/admin/src/router-pages/categoryList/CategoryList.tsx → system/admin/src/components/entity/entityTable/EntityTable.tsx, themes/store/src/types.ts, system/admin/src/constants/PageInfos.ts, system/admin/src/helpers/customEntities.tsx, themes/store/src/helpers/forceUpdate.ts, system/admin/src/router-pages/categoryList/components/HeaderActions.tsx, system/admin/src/router-pages/categoryList/components/TreeView.tsx
system/admin/src/router-pages/categoryList/components/CategoryItem.tsx → system/admin/src/components/buttons/IconButton.tsx, system/admin/src/components/inputs/CheckboxInput.tsx, system/admin/src/constants/PageInfos.ts, themes/store/src/helpers/forceUpdate.ts, system/admin/src/router-pages/settings/pages/store.tsx, toolkits/commerce/src/base/CategoryList/CategoryList.tsx
system/admin/src/router-pages/categoryList/components/HeaderActions.tsx → system/admin/src/components/buttons/IconButton.tsx, toolkits/commerce/src/base/CategoryList/CategoryList.tsx
system/admin/src/router-pages/categoryList/components/TreeView.tsx → themes/store/src/types.ts, toolkits/commerce/tests/helpers.ts, system/admin/src/router-pages/categoryList/components/CategoryItem.tsx
system/admin/src/router-pages/coupon/Coupon.test.tsx → system/admin/src/router-pages/coupon/Coupon.tsx
system/admin/src/router-pages/coupon/Coupon.tsx → system/admin/src/components/buttons/IconButton.tsx, system/admin/src/components/entity/entityEdit/EntityEdit.tsx, system/admin/src/components/inputs/Search/SearchInput.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx, system/admin/src/components/loadBox/LoadBox.tsx, system/admin/src/constants/PageInfos.ts
system/admin/src/router-pages/couponList/CouponList.test.tsx → system/admin/src/router-pages/couponList/CouponList.tsx, system/admin/src/router-pages/settings/pages/store.tsx
system/admin/src/router-pages/couponList/CouponList.tsx → system/admin/src/components/entity/entityTable/EntityTable.tsx, system/admin/src/constants/PageInfos.ts, system/admin/src/helpers/customEntities.tsx
system/admin/src/router-pages/dashboard/Dashboard.test.tsx → system/admin/src/router-pages/dashboard/Dashboard.tsx
system/admin/src/router-pages/dashboard/Dashboard.tsx → system/admin/src/components/buttons/TextButton.tsx, system/admin/src/components/sideNav/ResponsiveSideNav.tsx, system/admin/src/hooks/useDashboard.tsx, system/admin/src/hooks/useLongPress.tsx, system/admin/src/router-pages/dashboard/components/addWidgetMenu.tsx, system/admin/src/router-pages/dashboard/widgets/ordersLastWeek.tsx, system/admin/src/router-pages/dashboard/widgets/pageViews.tsx, system/admin/src/router-pages/dashboard/widgets/pageViewsList.tsx, system/admin/src/router-pages/dashboard/widgets/productRating.tsx, system/admin/src/router-pages/dashboard/widgets/productReviews.tsx, system/admin/src/router-pages/dashboard/widgets/salesLastWeek.tsx, system/admin/src/router-pages/dashboard/widgets/salesValue.tsx, system/admin/src/router-pages/dashboard/widgets/widgetPanel.tsx
system/admin/src/router-pages/dashboard/components/addWidgetMenu.tsx → system/admin/src/hooks/useDashboard.tsx
system/admin/src/router-pages/dashboard/widgets/ordersLastWeek.tsx → system/admin/src/hooks/useDashboard.tsx, system/admin/src/router-pages/dashboard/widgets/widgetPanel.tsx
system/admin/src/router-pages/dashboard/widgets/pageViews.tsx → system/admin/src/hooks/useDashboard.tsx, system/admin/src/router-pages/dashboard/widgets/widgetPanel.tsx
system/admin/src/router-pages/dashboard/widgets/pageViewsList.tsx → system/admin/src/hooks/useDashboard.tsx, system/admin/src/router-pages/dashboard/widgets/widgetPanel.tsx
system/admin/src/router-pages/dashboard/widgets/productRating.tsx → system/admin/src/hooks/useDashboard.tsx, system/admin/src/router-pages/dashboard/components/StarRating.tsx, system/admin/src/router-pages/dashboard/widgets/widgetPanel.tsx
system/admin/src/router-pages/dashboard/widgets/productReviews.tsx → system/admin/src/hooks/useDashboard.tsx, system/admin/src/router-pages/dashboard/components/StarRating.tsx, system/admin/src/router-pages/dashboard/widgets/widgetPanel.tsx
system/admin/src/router-pages/dashboard/widgets/salesLastWeek.tsx → system/admin/src/hooks/useDashboard.tsx, system/admin/src/router-pages/dashboard/widgets/widgetPanel.tsx
system/admin/src/router-pages/dashboard/widgets/salesValue.tsx → system/admin/src/hooks/useDashboard.tsx, system/admin/src/router-pages/dashboard/widgets/widgetPanel.tsx
system/admin/src/router-pages/dashboard/widgets/widgetPanel.tsx → system/admin/src/hooks/useDashboard.tsx
system/admin/src/router-pages/login/LoginPage.test.tsx → system/admin/src/router-pages/login/LoginPage.tsx
system/admin/src/router-pages/login/LoginPage.tsx → system/admin/src/components/loadBox/LoadingStatus.tsx, themes/store/src/components/toast/toast.tsx, system/admin/src/helpers/navigation.tsx, system/admin/src/router-pages/login/components/ForgotPassForm.tsx, system/admin/src/router-pages/login/components/ResetPassForm.tsx, system/admin/src/router-pages/login/components/SignInForm.tsx
system/admin/src/router-pages/login/components/ForgotPassForm.tsx → themes/store/src/components/toast/toast.tsx
system/admin/src/router-pages/login/components/ResetPassForm.tsx → themes/store/src/components/toast/toast.tsx
system/admin/src/router-pages/login/components/SignInForm.tsx → themes/store/src/components/toast/toast.tsx
system/admin/src/router-pages/order/Order.test.tsx → system/admin/src/router-pages/order/Order.tsx
system/admin/src/router-pages/order/Order.tsx → system/admin/src/components/entity/entityEdit/EntityEdit.tsx, system/admin/src/constants/PageInfos.ts, system/admin/src/router-pages/order/components/PageContent.tsx
system/admin/src/router-pages/order/components/PageContent.tsx → system/admin/src/components/entity/entityEdit/components/EntityCustomFields.tsx, themes/store/src/types.ts, system/admin/src/components/inputs/AutocompleteInput.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx, system/admin/src/constants/order.ts, system/admin/src/constants/PageInfos.ts, system/admin/src/helpers/addressParser.tsx, themes/store/src/helpers/forceUpdate.ts, system/admin/src/helpers/time.ts
system/admin/src/router-pages/orderList/OrderList.test.tsx → system/admin/src/router-pages/orderList/OrderList.tsx, system/admin/src/router-pages/settings/pages/store.tsx
system/admin/src/router-pages/orderList/OrderList.tsx → system/admin/src/components/entity/entityTable/EntityTable.tsx, system/admin/src/constants/order.ts, system/admin/src/constants/PageInfos.ts, system/admin/src/helpers/addressParser.tsx, system/admin/src/helpers/time.ts
system/admin/src/router-pages/plugin/PluginPage.test.tsx → system/admin/src/router-pages/plugin/PluginPage.tsx
system/admin/src/router-pages/pluginList/PluginList.test.tsx → system/admin/src/router-pages/pluginList/PluginList.tsx
system/admin/src/router-pages/pluginList/PluginList.tsx → system/admin/src/components/buttons/IconButton.tsx, system/admin/src/components/entity/entityTable/EntityTable.tsx, themes/store/src/types.ts, themes/store/src/components/toast/toast.tsx, system/admin/src/constants/PageInfos.ts
system/admin/src/router-pages/pluginMarket/PluginMarket.test.tsx → system/admin/src/router-pages/pluginMarket/PluginMarket.tsx
system/admin/src/router-pages/pluginMarket/PluginMarket.tsx → system/admin/src/components/market/MarketItem.tsx, system/admin/src/components/market/MarketModal.tsx, themes/store/src/components/modals/baseModal/Modal.tsx, toolkits/commerce/src/mui/Pagination/Pagination.tsx, themes/store/src/components/toast/toast.tsx
system/admin/src/router-pages/post/Post.test.tsx → system/admin/src/router-pages/post/Post.tsx
system/admin/src/router-pages/post/Post.tsx → system/admin/src/components/entity/entityEdit/EntityEdit.tsx, system/admin/src/constants/PageInfos.ts, system/admin/src/router-pages/post/components/HeaderActions.tsx, system/admin/src/router-pages/post/components/PageContent.tsx, system/admin/src/router-pages/post/contexts/PostContext.tsx
system/admin/src/router-pages/post/components/HeaderActions.tsx → system/admin/src/components/buttons/IconButton.tsx, system/admin/src/components/buttons/TextButton.tsx, themes/store/src/helpers/forceUpdate.ts, themes/store/src/types.ts, system/admin/src/router-pages/post/contexts/PostContext.tsx, system/admin/src/router-pages/post/components/PostSettings.tsx
system/admin/src/router-pages/post/components/PageContent.tsx → themes/store/src/types.ts, system/admin/src/helpers/editor/editor.ts, themes/store/src/helpers/forceUpdate.ts, system/admin/src/router-pages/post/contexts/PostContext.tsx
system/admin/src/router-pages/post/components/PostSettings.tsx → system/admin/src/components/buttons/IconButton.tsx, system/admin/src/components/buttons/TextButton.tsx, system/admin/src/components/inputs/AutocompleteInput.tsx, system/admin/src/components/inputs/DateInput/DateInput.tsx, system/admin/src/components/inputs/SwitchInput/SwitchInput.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx, system/admin/src/components/inputs/Image/ImageInput.tsx, themes/store/src/helpers/forceUpdate.ts, system/admin/src/router-pages/post/contexts/PostContext.tsx
system/admin/src/router-pages/post/contexts/PostContext.tsx → system/admin/src/hooks/useBlocker.ts
system/admin/src/router-pages/postList/PostList.test.tsx → system/admin/src/router-pages/settings/pages/store.tsx, system/admin/src/router-pages/postList/PostList.tsx
system/admin/src/router-pages/postList/PostList.tsx → system/admin/src/components/entity/entityTable/EntityTable.tsx, system/admin/src/constants/PageInfos.ts, system/admin/src/helpers/customEntities.tsx, system/admin/src/helpers/time.ts
system/admin/src/router-pages/product/Product.test.tsx → system/admin/src/router-pages/product/Product.tsx
system/admin/src/router-pages/product/Product.tsx → system/admin/src/components/entity/entityEdit/EntityEdit.tsx, system/admin/src/constants/PageInfos.ts, system/admin/src/router-pages/product/components/Header.tsx, system/admin/src/router-pages/product/components/PageContent.tsx, system/admin/src/router-pages/product/contexts/Product.ts, system/admin/src/router-pages/product/hooks/useTabs.ts
system/admin/src/router-pages/product/components/AttributesTab.tsx → system/admin/src/components/buttons/IconButton.tsx, system/admin/src/components/buttons/TextButton.tsx, system/admin/src/components/transferList/TransferList.tsx
system/admin/src/router-pages/product/components/Header.tsx → system/admin/src/router-pages/product/hooks/useTabs.ts
system/admin/src/router-pages/product/components/MainInfoCard.tsx → system/admin/src/components/inputs/GalleryInput/GalleryInput.tsx, system/admin/src/components/inputs/SelectInput/SelectInput.tsx, system/admin/src/components/inputs/SwitchInput/SwitchInput.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx, system/admin/src/helpers/editor/editor.ts, themes/store/src/helpers/forceUpdate.ts
system/admin/src/router-pages/product/components/PageContent.tsx → system/admin/src/components/entity/entityEdit/components/EntityCustomFields.tsx, system/admin/src/components/entity/entityEdit/components/EntityMetaFields.tsx, themes/store/src/types.ts, system/admin/src/components/inputs/Search/SearchInput.tsx, themes/store/src/helpers/forceUpdate.ts, system/admin/src/constants/PageInfos.ts, system/admin/src/router-pages/product/contexts/Product.ts, system/admin/src/router-pages/product/hooks/useTabs.ts, system/admin/src/router-pages/product/components/AttributesTab.tsx, system/admin/src/router-pages/product/components/MainInfoCard.tsx, system/admin/src/router-pages/product/components/VariantsTab.tsx
system/admin/src/router-pages/product/components/VariantsTab.tsx → system/admin/src/components/buttons/IconButton.tsx, system/admin/src/components/buttons/TextButton.tsx, system/admin/src/components/inputs/SelectInput/SelectInput.tsx, system/admin/src/components/inputs/SwitchInput/SwitchInput.tsx, system/admin/src/components/modal/Confirmation.tsx, system/admin/src/router-pages/product/components/MainInfoCard.tsx
system/admin/src/router-pages/product/hooks/useTabs.ts → system/admin/src/router-pages/product/contexts/Product.ts
system/admin/src/router-pages/productList/ProductList.test.tsx → system/admin/src/router-pages/settings/pages/store.tsx, system/admin/src/router-pages/productList/ProductList.tsx
system/admin/src/router-pages/productList/ProductList.tsx → plugins/product-filter/src/frontend/components/Filter.tsx, themes/store/src/types.ts, system/admin/src/components/entity/entityTable/EntityTable.tsx, themes/store/src/types.ts, system/admin/src/constants/PageInfos.ts, system/admin/src/helpers/customEntities.tsx, themes/store/src/helpers/forceUpdate.ts
system/admin/src/router-pages/reviewList/ProductListItem.tsx → system/admin/src/constants/PageInfos.ts, system/admin/src/router-pages/settings/pages/store.tsx
system/admin/src/router-pages/reviewList/ReviewList.test.tsx → system/admin/src/router-pages/reviewList/ReviewList.tsx, system/admin/src/router-pages/settings/pages/store.tsx
system/admin/src/router-pages/reviewList/ReviewList.tsx → system/admin/src/components/buttons/IconButton.tsx, system/admin/src/components/entity/entityTable/EntityTable.tsx, themes/store/src/types.ts, themes/store/src/components/modals/baseModal/Modal.tsx, themes/store/src/components/toast/toast.tsx, system/admin/src/constants/PageInfos.ts, system/admin/src/helpers/time.ts, system/admin/src/router-pages/reviewList/ProductListItem.tsx
system/admin/src/router-pages/settings/Settings.test.tsx → system/admin/src/constants/languages.ts, system/admin/src/router-pages/settings/Settings.tsx
system/admin/src/router-pages/settings/Settings.tsx → system/admin/src/components/entity/entityEdit/components/EntityHeader.tsx, system/admin/src/components/loadBox/LoadingStatus.tsx, system/admin/src/components/sideNav/ResponsiveSideNav.tsx, system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx, system/admin/src/router-pages/settings/pages/index.tsx, system/admin/src/router-pages/settings/pages/acl.tsx, system/admin/src/router-pages/settings/pages/code.tsx, system/admin/src/router-pages/settings/pages/custom/CustomEntity/index.tsx, system/admin/src/router-pages/settings/pages/custom/CustomRole/index.tsx, system/admin/src/router-pages/settings/pages/custom/DefaultEntity/index.tsx, system/admin/src/router-pages/settings/pages/customData.tsx, system/admin/src/router-pages/settings/pages/general.tsx, system/admin/src/router-pages/settings/pages/migration.tsx, system/admin/src/router-pages/settings/pages/seo.tsx, system/admin/src/router-pages/settings/pages/store.tsx, system/admin/src/router-pages/settings/pages/Themes/index.tsx
system/admin/src/router-pages/settings/components/customTextEditorInputField.tsx → system/admin/src/helpers/editor/editor.ts
system/admin/src/router-pages/settings/components/draggableCurrencies.tsx → system/admin/src/components/icons/grabIcon.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx, themes/store/src/types.ts
system/admin/src/router-pages/settings/components/draggableEntityFields.tsx → system/admin/src/components/icons/grabIcon.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx, system/admin/src/helpers/slugify.ts, themes/store/src/types.ts, system/admin/src/components/inputs/SelectInput/SelectInput.tsx
system/admin/src/router-pages/settings/components/newEntityForm.tsx → system/admin/src/components/buttons/TextButton.tsx, system/admin/src/components/inputs/Image/ImageInput.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx, system/admin/src/helpers/customEntities.tsx, system/admin/src/helpers/slugify.ts, system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx
system/admin/src/router-pages/settings/components/newRoleForm.tsx → system/admin/src/components/buttons/TextButton.tsx, system/admin/src/components/inputs/SwitchInput/SwitchInput.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx, themes/store/src/components/toast/toast.tsx, system/admin/src/helpers/slugify.ts, system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx
system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx → themes/store/src/components/toast/toast.tsx, themes/store/src/types.ts
system/admin/src/router-pages/settings/pages/Themes/components/ThemePackage.tsx → system/admin/src/components/buttons/TextButton.tsx, system/admin/src/constants/PageInfos.ts
system/admin/src/router-pages/settings/pages/Themes/index.tsx → themes/store/src/components/toast/toast.tsx, system/admin/src/constants/PageInfos.ts, system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx, system/admin/src/router-pages/settings/pages/Themes/components/ThemePackage.tsx
system/admin/src/router-pages/settings/pages/acl.tsx → system/admin/src/components/icons/spyIcon.tsx, system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx, system/admin/src/router-pages/settings/components/newRoleForm.tsx, system/admin/src/router-pages/settings/components/settingItem.tsx, system/admin/src/router-pages/settings/components/SettingCategory.tsx
system/admin/src/router-pages/settings/pages/code.tsx → system/admin/src/components/inputs/CodeEditor.tsx, system/admin/src/router-pages/settings/components/SettingCategory.tsx, system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx, themes/store/src/types.ts
system/admin/src/router-pages/settings/pages/custom/CustomEntity/index.tsx → system/admin/src/components/inputs/Image/ImageInput.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx, system/admin/src/constants/PageInfos.ts, system/admin/src/helpers/slugify.ts, system/admin/src/router-pages/settings/components/SettingCategory.tsx, themes/store/src/types.ts, system/admin/src/router-pages/settings/components/draggableEntityFields.tsx, system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx
system/admin/src/router-pages/settings/pages/custom/CustomRole/index.tsx → system/admin/src/components/inputs/SwitchInput/SwitchInput.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx, themes/store/src/components/toast/toast.tsx, system/admin/src/helpers/slugify.ts, system/admin/src/router-pages/settings/components/SettingCategory.tsx, system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx, system/admin/src/router-pages/settings/pages/custom/CustomRole/PermissionCategory.tsx, system/admin/src/router-pages/settings/pages/custom/CustomRole/PermissionOption.tsx
system/admin/src/router-pages/settings/pages/custom/DefaultEntity/index.tsx → system/admin/src/router-pages/settings/components/SettingCategory.tsx, themes/store/src/types.ts, system/admin/src/router-pages/settings/components/draggableEntityFields.tsx, system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx, system/admin/src/router-pages/settings/pages/custom/DefaultEntity/constants.ts
system/admin/src/router-pages/settings/pages/customData.tsx → system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx, system/admin/src/router-pages/settings/components/newEntityForm.tsx, system/admin/src/router-pages/settings/components/settingItem.tsx, system/admin/src/router-pages/settings/components/SettingCategory.tsx
system/admin/src/router-pages/settings/pages/general.tsx → system/admin/src/components/inputs/SelectInput/SelectInput.tsx, system/admin/src/components/inputs/SwitchInput/SwitchInput.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx, system/admin/src/constants/languages.ts, system/admin/src/constants/timezones.ts, system/admin/src/router-pages/settings/components/SettingCategory.tsx, system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx, themes/store/src/types.ts
system/admin/src/router-pages/settings/pages/index.tsx → toolkits/commerce/tests/helpers.ts, system/admin/src/components/icons/marketicon.tsx, system/admin/src/components/icons/stackIcon.tsx, system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx, system/admin/src/router-pages/settings/components/settingItem.tsx
system/admin/src/router-pages/settings/pages/migration.tsx → system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx, system/admin/src/components/loadBox/LoadingStatus.tsx, themes/store/src/components/toast/toast.tsx, system/admin/src/router-pages/settings/components/SettingCategory.tsx
system/admin/src/router-pages/settings/pages/seo.tsx → system/admin/src/components/inputs/CodeEditor.tsx, system/utils/src/exports.ts, system/admin/src/components/loadBox/LoadingStatus.tsx, themes/store/src/components/toast/toast.tsx, system/admin/src/router-pages/settings/components/SettingCategory.tsx, system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx, themes/store/src/types.ts
system/admin/src/router-pages/settings/pages/store.tsx → system/admin/src/components/inputs/SwitchInput/SwitchInput.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx, system/admin/src/components/icons/grabIcon.tsx, system/admin/src/router-pages/settings/components/draggableCurrencies.tsx, system/admin/src/router-pages/settings/components/SettingCategory.tsx, system/admin/src/router-pages/settings/hooks/useAdminSettings.tsx, themes/store/src/types.ts
system/admin/src/router-pages/tag/Tag.test.tsx → system/admin/src/router-pages/tag/Tag.tsx
system/admin/src/router-pages/tag/Tag.tsx → system/admin/src/components/entity/entityEdit/EntityEdit.tsx, system/admin/src/constants/PageInfos.ts
system/admin/src/router-pages/tagList/TagList.test.tsx → system/admin/src/router-pages/tagList/TagList.tsx, system/admin/src/router-pages/settings/pages/store.tsx
system/admin/src/router-pages/tagList/TagList.tsx → system/admin/src/components/entity/entityTable/EntityTable.tsx, system/admin/src/constants/PageInfos.ts, system/admin/src/helpers/customEntities.tsx
system/admin/src/router-pages/themeEdit/ThemeEdit.tsx → system/admin/src/components/sideNav/ResponsiveSideNav.tsx, system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx, system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx, system/admin/src/router-pages/themeEdit/pageEditor/PageEditor.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PageActions.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/PageEditorSidebar.tsx, system/admin/src/router-pages/themeEdit/pageList/PageList.tsx
system/admin/src/router-pages/themeEdit/hooks/useBlockEvents.tsx → system/admin/src/helpers/Draggable/Draggable.ts
system/admin/src/router-pages/themeEdit/hooks/useHoveredFrames.tsx → system/admin/src/helpers/Draggable/Draggable.ts
system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx → system/admin/src/components/modal/Confirmation.tsx, system/utils/src/exports.ts, system/admin/src/helpers/Draggable/Draggable.ts, system/admin/src/router-pages/themeEdit/pageEditor/components/BlockMenu.tsx, system/admin/src/router-pages/themeEdit/ThemeEdit.tsx, system/admin/src/router-pages/themeEdit/hooks/useBlockEvents.tsx, system/admin/src/router-pages/themeEdit/hooks/useBlockFns.tsx, system/admin/src/router-pages/themeEdit/hooks/useEditorUtils.tsx, system/admin/src/router-pages/themeEdit/hooks/useHoveredFrames.tsx, system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx
system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx → system/admin/src/router-pages/themeEdit/ThemeEdit.tsx
system/admin/src/router-pages/themeEdit/pageEditor/PageEditor.tsx → system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx, system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx, system/admin/src/router-pages/themeEdit/pageEditor/components/BlockMenu.tsx
system/admin/src/router-pages/themeEdit/pageEditor/components/BlockMenu.tsx → system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx, system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx, system/admin/src/router-pages/themeEdit/pageEditor/components/NewBlockMenu.tsx
system/admin/src/router-pages/themeEdit/pageEditor/components/NewBlockMenu.tsx → system/admin/src/router-pages/themeEdit/hooks/useDebounce.ts, system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx, system/admin/src/router-pages/themeEdit/pageEditor/components/BlockMenu.tsx
system/admin/src/router-pages/themeEdit/pageEditorSidebar/PageEditorSidebar.tsx → themes/store/src/helpers/forceUpdate.ts, system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx, system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PageDesignEditor.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PageSettings.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PluginEditor.tsx
system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/BackgroundEditor.tsx → system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/ColorPickerField.tsx
system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/ColorPickerField.tsx → system/admin/src/router-pages/themeEdit/hooks/useDocumentEvents.tsx, system/admin/src/router-pages/themeEdit/hooks/useDebounce.ts
system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/DimensionsEditor.tsx → system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/MarginEditor.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PaddingEditor.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/StyleNumberField.tsx
system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/EditorBlockEditor.tsx → system/admin/src/helpers/editor/editor.ts, system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx
system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/FontEditor.tsx → system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/ColorPickerField.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/SelectableField.tsx
system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/HTMLBlockEditor.tsx → system/admin/src/components/inputs/CodeEditor.tsx, system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx, system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx
system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/ImageBlockEditor.tsx → system/admin/src/components/inputs/Image/ImageInput.tsx, system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx, system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/SelectableField.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/StyleNumberField.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx
system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/MarginEditor.tsx → system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/StyleNumberField.tsx
system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PaddingEditor.tsx → system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/StyleNumberField.tsx
system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PageActions.tsx → system/admin/src/components/sideNav/ResponsiveSideNav.tsx, system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx, system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx
system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PageDesignEditor.tsx → system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx, system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/BackgroundEditor.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/DimensionsEditor.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/FontEditor.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/ShadowEditor.tsx
system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PageSettings.tsx → system/admin/src/components/inputs/CodeEditor.tsx, system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx, system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx, system/admin/src/router-pages/themeEdit/ThemeEdit.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextInput.tsx
system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/PluginEditor.tsx → system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/EditorBlockEditor.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/HTMLBlockEditor.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/ImageBlockEditor.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextBlockEditor.tsx
system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/ShadowEditor.tsx → system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/ColorPickerField.tsx, system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/SelectableField.tsx
system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/StyleNumberField.tsx → system/admin/src/router-pages/themeEdit/pageEditorSidebar/SlideableNumberInput.tsx
system/admin/src/router-pages/themeEdit/pageEditorSidebar/components/TextBlockEditor.tsx → system/admin/src/router-pages/themeEdit/hooks/usePageBuilder.tsx, system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx
system/admin/src/router-pages/themeEdit/pageList/PageItem.tsx → system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx, system/admin/src/router-pages/themeEdit/ThemeEdit.tsx
system/admin/src/router-pages/themeEdit/pageList/PageList.tsx → system/admin/src/router-pages/themeEdit/hooks/useThemeEditor.tsx, system/admin/src/router-pages/themeEdit/pageList/PageItem.tsx
system/admin/src/router-pages/themeMarket/ThemeMarket.test.tsx → system/admin/src/router-pages/themeMarket/ThemeMarket.tsx
system/admin/src/router-pages/themeMarket/ThemeMarket.tsx → system/admin/src/components/market/MarketItem.tsx, system/admin/src/components/market/MarketModal.tsx, themes/store/src/components/modals/baseModal/Modal.tsx, toolkits/commerce/src/mui/Pagination/Pagination.tsx, themes/store/src/components/toast/toast.tsx
system/admin/src/router-pages/user/User.test.tsx → system/admin/src/router-pages/user/User.tsx
system/admin/src/router-pages/user/User.tsx → system/admin/src/components/entity/entityEdit/EntityEdit.tsx, system/admin/src/constants/PageInfos.ts, system/admin/src/helpers/addressParser.tsx
system/admin/src/router-pages/userList/UserList.test.tsx → system/admin/src/router-pages/userList/UserList.tsx, system/admin/src/router-pages/settings/pages/store.tsx
system/admin/src/router-pages/userList/UserList.tsx → system/admin/src/components/entity/entityTable/EntityTable.tsx, system/admin/src/constants/PageInfos.ts, system/admin/src/helpers/addressParser.tsx, system/admin/src/helpers/customEntities.tsx
system/admin/src/router-pages/welcome/Welcome.test.tsx → system/admin/src/router-pages/welcome/Welcome.tsx
system/admin/src/router-pages/welcome/Welcome.tsx → system/admin/src/router-pages/welcome/components/CmsSettingsForm.tsx, system/admin/src/router-pages/welcome/components/UserForm.tsx
system/admin/src/router-pages/welcome/components/CmsSettingsForm.tsx → system/admin/src/components/inputs/SwitchInput/SwitchInput.tsx, system/admin/src/components/loadBox/LoadingStatus.tsx
system/admin/src/router-pages/welcome/components/UserForm.tsx → system/admin/src/components/inputs/Image/ImageInput.tsx
system/admin/src/startup/server.ts → system/core/backend/src/helpers/cms-settings.ts, system/core/backend/src/helpers/logger.ts, system/core/backend/src/helpers/shell.ts, system/core/frontend/src/api/CRestApiClient.ts, system/utils/src/static.ts
system/admin/startup.js → system/core/backend/src/helpers/paths.ts, themes/store/src/constants.js, system/core/backend/src/helpers/logger.ts, system/core/backend/src/helpers/shell.ts
system/admin/tailwind.config.js → system/core/backend/src/helpers/paths.ts
system/cli/jest.config.ts → themes/store/src/types.ts
system/cli/src/cli.ts → system/core/backend/src/helpers/shell.ts, system/cli/src/tasks/create.ts, system/utils/src/downloader.ts
system/cli/startup.js → system/core/backend/src/helpers/shell.ts
system/core/backend/jest.config.ts → themes/store/src/types.ts
system/core/backend/src/helpers/actions.ts → system/core/backend/src/helpers/logger.ts, system/core/backend/src/helpers/types.ts
system/core/backend/src/helpers/auth-guards.ts → system/core/backend/src/helpers/auth-roles-permissions.ts, system/core/backend/src/helpers/types.ts
system/core/backend/src/helpers/auth-settings.ts → system/core/backend/src/helpers/cms-settings.ts, system/core/backend/src/helpers/paths.ts
system/core/backend/src/helpers/base-queries.ts → system/core/backend/src/helpers/entity-meta.ts
system/core/backend/src/helpers/cms-modules.ts → system/core/backend/src/helpers/constants.ts, system/core/backend/src/helpers/paths.ts
system/core/backend/src/helpers/cms-settings.ts → system/core/backend/src/helpers/constants.ts, system/core/backend/src/helpers/logger.ts, system/core/backend/src/helpers/paths.ts
system/core/backend/src/helpers/connect-database.ts → system/core/backend/src/helpers/cms-settings.ts, system/core/backend/src/helpers/constants.ts, system/core/backend/src/helpers/logger.ts, system/core/backend/src/helpers/paths.ts, system/core/backend/src/helpers/plugin-exports.ts
system/core/backend/src/helpers/constants.ts → system/core/backend/src/helpers/logger.ts
system/core/backend/src/helpers/data-filters.ts → system/core/backend/src/helpers/types.ts
system/core/backend/src/helpers/emailing.ts → system/core/backend/src/helpers/cms-settings.ts, system/core/backend/src/helpers/logger.ts, system/core/backend/src/helpers/paths.ts
system/core/backend/src/helpers/generic-entities.ts → system/core/backend/src/helpers/create-generic-entity.ts
system/core/backend/src/helpers/logger.ts → system/core/backend/src/helpers/paths.ts
system/core/backend/src/helpers/paths.ts → system/core/backend/src/helpers/logger.ts
system/core/backend/src/helpers/plugin-exports.ts → system/core/backend/src/helpers/cms-modules.ts, system/core/backend/src/helpers/constants.ts, system/core/backend/src/helpers/logger.ts, system/core/backend/src/helpers/types.ts
system/core/backend/src/helpers/plugin-settings.ts → system/core/backend/src/helpers/generic-entities.ts, system/core/backend/src/helpers/logger.ts
system/core/backend/src/helpers/service-versions.ts → system/core/backend/src/helpers/cms-settings.ts, system/core/backend/src/helpers/logger.ts
system/core/backend/src/helpers/shell.ts → system/core/backend/src/helpers/logger.ts, system/core/backend/src/helpers/paths.ts
system/core/backend/src/helpers/theme-config.ts → system/core/backend/src/helpers/generic-entities.ts, system/core/backend/src/helpers/logger.ts
system/core/backend/src/models/entities/attribute-product.entity.ts → system/core/backend/src/models/entities/attribute-value.entity.ts, system/core/backend/src/models/entities/product.entity.ts
system/core/backend/src/models/entities/attribute-value.entity.ts → system/core/backend/src/models/entities/attribute.entity.ts, system/core/backend/src/models/entities/base-page.entity.ts, system/core/backend/src/models/entities/attribute-product.entity.ts
system/core/backend/src/models/entities/attribute.entity.ts → system/core/backend/src/models/entities/attribute-value.entity.ts, system/core/backend/src/models/entities/base-page.entity.ts, system/core/backend/src/models/entities/meta/attribute-meta.entity.ts
system/core/backend/src/models/entities/coupon.entity.ts → system/core/backend/src/models/entities/base-page.entity.ts, system/core/backend/src/models/entities/meta/coupon-meta.entity.ts
system/core/backend/src/models/entities/custom-entity.entity.ts → system/core/backend/src/models/entities/base-page.entity.ts, system/core/backend/src/models/entities/meta/custom-entity-meta.entity.ts
system/core/backend/src/models/entities/dashboard-entity.entity.ts → system/core/backend/src/models/entities/user.entity.ts
system/core/backend/src/models/entities/meta/attribute-meta.entity.ts → system/core/backend/src/models/entities/meta/base-meta.entity.ts
system/core/backend/src/models/entities/meta/coupon-meta.entity.ts → system/core/backend/src/models/entities/meta/base-meta.entity.ts
system/core/backend/src/models/entities/meta/custom-entity-meta.entity.ts → system/core/backend/src/models/entities/meta/base-meta.entity.ts
system/core/backend/src/models/entities/meta/order-meta.entity.ts → system/core/backend/src/models/entities/meta/base-meta.entity.ts
system/core/backend/src/models/entities/meta/post-meta.entity.ts → system/core/backend/src/models/entities/meta/base-meta.entity.ts
system/core/backend/src/models/entities/meta/product-category-meta.entity.ts → system/core/backend/src/models/entities/meta/base-meta.entity.ts
system/core/backend/src/models/entities/meta/product-meta.entity.ts → system/core/backend/src/models/entities/meta/base-meta.entity.ts
system/core/backend/src/models/entities/meta/product-variant-meta.entity.ts → system/core/backend/src/models/entities/meta/base-meta.entity.ts
system/core/backend/src/models/entities/meta/role-meta.entity.ts → system/core/backend/src/models/entities/meta/base-meta.entity.ts
system/core/backend/src/models/entities/meta/tag-meta.entity.ts → system/core/backend/src/models/entities/meta/base-meta.entity.ts
system/core/backend/src/models/entities/meta/user-meta.entity.ts → system/core/backend/src/models/entities/meta/base-meta.entity.ts
system/core/backend/src/models/entities/order.entity.ts → system/core/backend/src/models/entities/meta/order-meta.entity.ts, system/core/backend/src/models/entities/coupon.entity.ts
system/core/backend/src/models/entities/plugin.entity.ts → system/core/backend/src/models/entities/base-page.entity.ts
system/core/backend/src/models/entities/post-comment.entity.ts → system/core/backend/src/models/entities/base-page.entity.ts, system/core/backend/src/models/entities/post.entity.ts
system/core/backend/src/models/entities/post.entity.ts → system/core/backend/src/models/entities/base-page.entity.ts, system/core/backend/src/models/entities/meta/post-meta.entity.ts, system/core/backend/src/models/entities/post-comment.entity.ts, system/core/backend/src/models/entities/tag.entity.ts, system/core/backend/src/models/entities/user.entity.ts
system/core/backend/src/models/entities/product-category.entity.ts → system/core/backend/src/models/entities/base-page.entity.ts, system/core/backend/src/models/entities/meta/product-category-meta.entity.ts, system/core/backend/src/models/entities/product.entity.ts
system/core/backend/src/models/entities/product-review.entity.ts → system/core/backend/src/models/entities/base-page.entity.ts, system/core/backend/src/models/entities/product.entity.ts
system/core/backend/src/models/entities/product-variant.entity.ts → system/core/backend/src/models/entities/base-page.entity.ts, system/core/backend/src/models/entities/meta/product-variant-meta.entity.ts, system/core/backend/src/models/entities/product.entity.ts
system/core/backend/src/models/entities/product.entity.ts → system/core/backend/src/models/entities/attribute-product.entity.ts, system/core/backend/src/models/entities/base-page.entity.ts, system/core/backend/src/models/entities/meta/product-meta.entity.ts, system/core/backend/src/models/entities/product-category.entity.ts, system/core/backend/src/models/entities/product-review.entity.ts, system/core/backend/src/models/entities/product-variant.entity.ts
system/core/backend/src/models/entities/role.entity.ts → system/core/backend/src/models/entities/base-page.entity.ts, system/core/backend/src/models/entities/user.entity.ts, system/core/backend/src/models/entities/meta/role-meta.entity.ts
system/core/backend/src/models/entities/tag.entity.ts → system/core/backend/src/models/entities/base-page.entity.ts, system/core/backend/src/models/entities/meta/tag-meta.entity.ts
system/core/backend/src/models/entities/theme.entity.ts → system/core/backend/src/models/entities/base-page.entity.ts
system/core/backend/src/models/entities/user.entity.ts → system/core/backend/src/models/entities/base-page.entity.ts, system/core/backend/src/models/entities/dashboard-entity.entity.ts, system/core/backend/src/models/entities/meta/user-meta.entity.ts, system/core/backend/src/models/entities/post.entity.ts, system/core/backend/src/models/entities/role.entity.ts
system/core/backend/src/models/filters/custom-entity.filter.ts → system/core/backend/src/models/filters/base-filter.filter.ts
system/core/backend/src/models/filters/order.filter.ts → system/core/backend/src/models/filters/base-filter.filter.ts
system/core/backend/src/models/filters/post.filter.ts → system/core/backend/src/models/filters/base-filter.filter.ts
system/core/backend/src/models/filters/product-category.filter.ts → system/core/backend/src/models/filters/base-filter.filter.ts
system/core/backend/src/models/filters/product-review.filter.ts → system/core/backend/src/models/filters/base-filter.filter.ts
system/core/backend/src/models/filters/product.filter.ts → system/core/backend/src/models/filters/base-filter.filter.ts
system/core/backend/src/models/filters/user.filter.ts → system/core/backend/src/models/filters/base-filter.filter.ts
system/core/backend/src/models/inputs/attribute.input.ts → system/core/backend/src/models/inputs/base-page.input.ts
system/core/backend/src/models/inputs/coupon.input.ts → system/core/backend/src/models/inputs/base-page.input.ts
system/core/backend/src/models/inputs/custom-entity.input.ts → system/core/backend/src/models/inputs/base-page.input.ts
system/core/backend/src/models/inputs/order.input.ts → system/core/backend/src/models/inputs/base-page.input.ts
system/core/backend/src/models/inputs/plugin.input.ts → system/core/backend/src/models/inputs/base-page.input.ts
system/core/backend/src/models/inputs/post.create.ts → system/core/backend/src/models/inputs/base-page.input.ts
system/core/backend/src/models/inputs/post.update.ts → system/core/backend/src/models/inputs/base-page.input.ts
system/core/backend/src/models/inputs/product-category.create.ts → system/core/backend/src/models/inputs/base-page.input.ts
system/core/backend/src/models/inputs/product-category.update.ts → system/core/backend/src/models/inputs/base-page.input.ts
system/core/backend/src/models/inputs/product-variant.input.ts → system/core/backend/src/models/inputs/base-page.input.ts
system/core/backend/src/models/inputs/product.create.ts → system/core/backend/src/models/inputs/base-page.input.ts, system/core/backend/src/models/inputs/product-variant.input.ts
system/core/backend/src/models/inputs/product.update.ts → system/core/backend/src/models/inputs/base-page.input.ts, system/core/backend/src/models/inputs/product-variant.input.ts
system/core/backend/src/models/inputs/role.input.ts → system/core/backend/src/models/inputs/base-page.input.ts
system/core/backend/src/models/inputs/tag.input.ts → system/core/backend/src/models/inputs/base-page.input.ts
system/core/backend/src/models/inputs/user.create.ts → system/core/backend/src/models/inputs/base-page.input.ts
system/core/backend/src/models/inputs/user.update.ts → system/core/backend/src/models/inputs/base-page.input.ts
system/core/backend/src/models/paged/attribute.paged.ts → system/core/backend/src/models/paged/meta.paged.ts
system/core/backend/src/models/paged/coupon.paged.ts → system/core/backend/src/models/paged/meta.paged.ts
system/core/backend/src/models/paged/custom-entity.paged.ts → system/core/backend/src/models/paged/meta.paged.ts
system/core/backend/src/models/paged/order.paged.ts → system/core/backend/src/models/paged/meta.paged.ts
system/core/backend/src/models/paged/post.paged.ts → system/core/backend/src/models/paged/meta.paged.ts
system/core/backend/src/models/paged/product-category.paged.ts → system/core/backend/src/models/paged/meta.paged.ts
system/core/backend/src/models/paged/product-review.paged.ts → system/core/backend/src/models/paged/meta.paged.ts
system/core/backend/src/models/paged/product.paged.ts → system/core/backend/src/models/paged/meta.paged.ts
system/core/backend/src/models/paged/role.paged.ts → system/core/backend/src/models/paged/meta.paged.ts
system/core/backend/src/models/paged/tag.paged.ts → system/core/backend/src/models/paged/meta.paged.ts
system/core/backend/src/models/paged/user.paged.ts → system/core/backend/src/models/paged/meta.paged.ts
system/core/backend/src/repositories/attribute.repository.ts → system/core/backend/src/helpers/base-queries.ts, system/core/backend/src/helpers/logger.ts, system/core/backend/src/repositories/base.repository.ts
system/core/backend/src/repositories/base.repository.ts → system/core/backend/src/helpers/base-queries.ts, system/core/backend/src/helpers/entity-meta.ts, system/core/backend/src/helpers/logger.ts
system/core/backend/src/repositories/coupon.repository.ts → system/core/backend/src/helpers/base-queries.ts, system/core/backend/src/helpers/logger.ts, system/core/backend/src/repositories/base.repository.ts
system/core/backend/src/repositories/custom-entity.repository.ts → system/core/backend/src/helpers/base-queries.ts, system/core/backend/src/helpers/logger.ts, system/core/backend/src/repositories/base.repository.ts
system/core/backend/src/repositories/order.repository.ts → system/core/backend/src/helpers/base-queries.ts, system/core/backend/src/helpers/logger.ts, system/core/backend/src/helpers/validation.ts, system/core/backend/src/repositories/base.repository.ts, system/core/backend/src/repositories/coupon.repository.ts
system/core/backend/src/repositories/page-stats.repository.ts → system/core/backend/src/repositories/base.repository.ts
system/core/backend/src/repositories/plugin.repository.ts → system/core/backend/src/helpers/base-queries.ts, system/core/backend/src/helpers/logger.ts, system/core/backend/src/repositories/base.repository.ts
system/core/backend/src/repositories/post.repository.ts → system/core/backend/src/helpers/base-queries.ts, system/core/backend/src/helpers/logger.ts, system/core/backend/src/repositories/base.repository.ts, system/core/backend/src/repositories/tag.repository.ts, system/core/backend/src/repositories/user.repository.ts
system/core/backend/src/repositories/product-category.repository.ts → system/core/backend/src/helpers/entity-meta.ts, system/core/backend/src/helpers/logger.ts, system/cli/src/tasks/create.ts, system/core/backend/src/repositories/product.repository.ts
system/core/backend/src/repositories/product-review.repository.ts → system/core/backend/src/helpers/base-queries.ts, system/core/backend/src/helpers/logger.ts, system/core/backend/src/repositories/base.repository.ts, system/core/backend/src/repositories/product.repository.ts
system/core/backend/src/repositories/product-variant.repository.ts → system/core/backend/src/helpers/base-queries.ts, system/core/backend/src/helpers/logger.ts, system/core/backend/src/repositories/base.repository.ts, system/core/backend/src/repositories/product.repository.ts
system/core/backend/src/repositories/product.repository.ts → system/core/backend/src/helpers/logger.ts, system/core/backend/src/repositories/attribute.repository.ts, system/core/backend/src/repositories/base.repository.ts, system/core/backend/src/repositories/product-category.repository.ts, system/core/backend/src/repositories/product-review.repository.ts, system/core/backend/src/repositories/product-variant.repository.ts
system/core/backend/src/repositories/role.repository.ts → system/core/backend/src/helpers/auth-roles-permissions.ts, system/core/backend/src/helpers/base-queries.ts, system/core/backend/src/helpers/logger.ts, system/core/backend/src/repositories/base.repository.ts
system/core/backend/src/repositories/tag.repository.ts → system/core/backend/src/helpers/base-queries.ts, system/core/backend/src/helpers/logger.ts, system/core/backend/src/repositories/base.repository.ts
system/core/backend/src/repositories/user.repository.ts → system/core/backend/src/helpers/auth-settings.ts, themes/store/src/constants.js, system/core/backend/src/helpers/base-queries.ts, system/core/backend/src/helpers/logger.ts, system/core/backend/src/helpers/validation.ts, system/core/backend/src/repositories/base.repository.ts, system/core/backend/src/repositories/role.repository.ts
system/core/backend/tests/helpers.ts → themes/store/src/constants.js
system/core/backend/tests/helpers/actions.test.ts → toolkits/commerce/src/base/Checkout/actions.ts
system/core/backend/tests/helpers/auth-guards.test.ts → themes/store/src/types.ts, system/core/backend/src/helpers/auth-guards.ts
system/core/backend/tests/helpers/base-queries.test.ts → system/core/backend/src/helpers/base-queries.ts
system/core/backend/tests/helpers/cms-modules.test.ts → system/core/backend/src/helpers/cms-modules.ts, toolkits/commerce/tests/helpers.ts
system/core/backend/tests/helpers/cms-settings.test.ts → system/core/backend/src/helpers/cms-settings.ts, themes/store/src/constants.js, toolkits/commerce/tests/helpers.ts
system/core/backend/tests/helpers/create-generic-entity.test.ts → system/core/backend/src/helpers/create-generic-entity.ts
system/core/backend/tests/helpers/emailing.test.ts → system/core/backend/src/helpers/emailing.ts, system/core/backend/src/helpers/paths.ts, toolkits/commerce/tests/helpers.ts
system/core/backend/tests/helpers/logger.test.ts → system/core/backend/src/helpers/logger.ts, system/core/backend/src/helpers/paths.ts, toolkits/commerce/tests/helpers.ts
system/core/backend/tests/helpers/paths.test.ts → toolkits/commerce/tests/helpers.ts
system/core/backend/tests/helpers/plugin-exports.test.ts → system/core/backend/src/helpers/plugin-exports.ts, toolkits/commerce/tests/helpers.ts
system/core/backend/tests/helpers/plugin-settings.test.ts → system/core/backend/src/helpers/plugin-settings.ts, toolkits/commerce/tests/helpers.ts
system/core/backend/tests/helpers/service-versions.test.ts → system/core/backend/src/helpers/service-versions.ts, toolkits/commerce/tests/helpers.ts
system/core/backend/tests/helpers/theme-config.test.ts → system/core/backend/src/helpers/theme-config.ts, system/core/backend/src/helpers/cms-settings.ts, toolkits/commerce/tests/helpers.ts
system/core/backend/tests/helpers/validation.test.ts → system/core/backend/src/helpers/validation.ts
system/core/backend/tests/teardown.ts → system/core/backend/tests/helpers.ts
system/core/common/src/auth.ts → system/core/common/src/types/data.ts, system/core/common/src/types/entities.ts
system/core/common/src/constants.ts → system/core/common/src/types/data.ts, system/core/common/src/types/entities.ts
system/core/common/src/global-store.ts → system/core/common/src/helpers.ts, system/core/common/src/types/blocks.ts, system/core/common/src/types/data.ts, system/core/common/src/types/entities.ts
system/core/common/src/helpers.ts → system/core/common/src/global-store.ts, system/core/common/src/types/data.ts
system/core/common/src/redirects.ts → system/core/common/src/global-store.ts, system/core/common/src/types/entities.ts
system/core/common/src/service-locator.ts → system/core/common/src/global-store.ts, system/core/common/src/helpers.ts, system/core/common/src/types/data.ts
system/core/common/src/types/blocks.ts → system/core/common/src/types/data.ts, system/renderer/src/helpers/document.tsx
system/core/common/src/types/data.ts → themes/store/src/constants.js, system/core/common/src/types/blocks.ts
system/core/common/src/types/entities.ts → system/core/common/src/types/data.ts
system/core/frontend/jest.config.ts → themes/store/src/types.ts
system/core/frontend/src/api/CGraphQLClient.ts → system/core/frontend/src/helpers/getServiceSecret.ts, system/core/frontend/src/helpers/isomorphicFetch.ts
system/core/frontend/src/api/CRestApiClient.ts → system/core/frontend/src/helpers/getServiceSecret.ts, system/core/frontend/src/helpers/isomorphicFetch.ts
system/core/frontend/src/api/CentralServerClient.ts → system/core/frontend/src/helpers/isomorphicFetch.ts, system/core/frontend/src/api/CRestApiClient.ts
system/core/frontend/src/components/AdminPanelWidget/AdminPanelWidgetPlace.test.tsx → system/core/frontend/src/components/AdminPanelWidget/AdminPanelWidgetPlace.tsx, system/core/frontend/src/helpers/registerWidget.ts
system/core/frontend/src/components/AdminPanelWidget/AdminPanelWidgetPlace.tsx → system/core/frontend/src/widget-types.ts, system/core/frontend/src/helpers/registerWidget.ts, system/core/frontend/src/components/AdminPanelWidget/WidgetErrorBoundary.tsx, themes/store/src/helpers/forceUpdate.ts
system/core/frontend/src/components/CBlock/CBlock.test.tsx → system/core/frontend/src/components/CBlock/CBlock.tsx
system/core/frontend/src/components/CBlock/CBlock.tsx → system/core/frontend/src/components/CContainer/CContainer.tsx, system/core/frontend/src/components/CEditor/CEditor.tsx, system/core/frontend/src/components/CGallery/CGallery.tsx, system/core/frontend/src/components/CHTML/CHTML.tsx, system/core/frontend/src/components/CImage/CImage.tsx, system/core/frontend/src/components/CPlugin/CPlugin.tsx, system/core/frontend/src/components/CText/CText.tsx
system/core/frontend/src/components/CContainer/CContainer.test.tsx → system/core/frontend/src/components/CContainer/CContainer.tsx
system/core/frontend/src/components/CContainer/CContainer.tsx → system/core/frontend/src/components/CBlock/CBlock.tsx
system/core/frontend/src/components/CEditor/CEditor.test.tsx → system/core/frontend/src/components/CEditor/CEditor.tsx
system/core/frontend/src/components/CEditor/CEditor.tsx → system/core/frontend/src/helpers/parserTransform.tsx, system/core/frontend/src/components/CBlock/CBlock.tsx
system/core/frontend/src/components/CGallery/CGallery.test.tsx → system/core/frontend/src/components/CGallery/CGallery.tsx
system/core/frontend/src/components/CGallery/CGallery.tsx → system/core/frontend/src/components/CBlock/CBlock.tsx, system/core/frontend/src/components/Link/Link.tsx, system/core/frontend/src/components/CGallery/Lightbox.tsx, system/core/frontend/src/components/CGallery/Thumbs.tsx
system/core/frontend/src/components/CGallery/Thumbs.tsx → system/core/frontend/src/helpers/thumbs.ts, system/core/frontend/src/components/CGallery/CGallery.tsx
system/core/frontend/src/components/CHTML/CHTML.test.tsx → system/core/frontend/src/components/CHTML/CHTML.tsx
system/core/frontend/src/components/CHTML/CHTML.tsx → system/core/frontend/src/helpers/parserTransform.tsx, system/core/frontend/src/components/CBlock/CBlock.tsx
system/core/frontend/src/components/CImage/CImage.test.tsx → system/core/frontend/src/components/CImage/CImage.tsx
system/core/frontend/src/components/CImage/CImage.tsx → system/core/frontend/src/components/CBlock/CBlock.tsx, system/core/frontend/src/components/Link/Link.tsx
system/core/frontend/src/components/CList/CList.test.tsx → system/core/frontend/src/components/CList/CList.tsx
system/core/frontend/src/components/CList/CList.tsx → system/core/frontend/src/components/CBlock/CBlock.tsx, toolkits/commerce/src/mui/Loadbox/Loadbox.tsx, system/core/frontend/src/components/throbber.ts, system/core/frontend/src/components/CList/CListPagination.tsx, system/core/frontend/src/components/CList/helpers.ts, system/core/frontend/src/components/CList/types.ts
system/core/frontend/src/components/CList/CListPagination.tsx → system/core/frontend/src/components/CList/helpers.ts, system/core/frontend/src/components/CList/types.ts
system/core/frontend/src/components/CPlugin/CPlugin.test.tsx → system/core/frontend/src/components/CPlugin/CPlugin.tsx
system/core/frontend/src/components/CPlugin/CPlugin.tsx → system/core/frontend/src/api/CRestApiClient.ts, themes/store/src/constants.js, system/core/frontend/src/helpers/loadFrontendBundle.ts, system/core/frontend/src/components/CBlock/CBlock.tsx
system/core/frontend/src/components/CText/CText.test.tsx → system/core/frontend/src/components/CText/CText.tsx
system/core/frontend/src/components/CText/CText.tsx → system/core/frontend/src/components/CBlock/CBlock.tsx, system/core/frontend/src/components/Link/Link.tsx
system/core/frontend/src/components/EntityHead/EntityHead.tsx → themes/store/src/constants.js
system/core/frontend/src/components/Link/Link.test.tsx → system/core/frontend/src/components/Link/Link.tsx
system/core/frontend/src/components/SignIn/SignIn.test.tsx → system/core/frontend/src/components/SignIn/SignIn.tsx
system/core/frontend/src/components/SignIn/SignIn.tsx → system/core/frontend/src/helpers/AuthClient.ts, system/core/frontend/src/components/BaseElements/BaseButton.tsx, system/core/frontend/src/components/BaseElements/BaseTextField.tsx
system/core/frontend/src/components/SignUp/SignUp.test.tsx → system/core/frontend/src/components/SignUp/SignUp.tsx
system/core/frontend/src/components/SignUp/SignUp.tsx → system/core/frontend/src/helpers/AuthClient.ts, system/core/frontend/src/components/BaseElements/BaseButton.tsx, system/core/frontend/src/components/BaseElements/BaseTextField.tsx
system/core/frontend/src/components/loadBox/Loadbox.tsx → system/core/frontend/src/components/throbber.ts
system/core/frontend/src/helpers/AuthClient.ts → system/core/frontend/src/api/CRestApiClient.ts, system/core/frontend/src/helpers/forceUpdate.ts
system/core/frontend/src/helpers/CStore.ts → system/core/frontend/src/api/CGraphQLClient.ts
system/core/frontend/src/helpers/hooks.ts → system/core/frontend/src/helpers/CStore.ts
system/core/frontend/src/helpers/importer.ts → system/core/frontend/src/helpers/isomorphicFetch.ts
system/core/frontend/src/helpers/loadFrontendBundle.ts → themes/store/src/constants.js, system/core/frontend/src/helpers/importer.ts
system/core/frontend/src/helpers/registerWidget.ts → system/core/frontend/src/widget-types.ts
system/core/frontend/tests/helpers/CStore.spec.ts → system/core/frontend/src/helpers/CStore.ts, toolkits/commerce/tests/helpers.ts
system/core/frontend/tests/helpers/importer.spec.ts → system/core/frontend/src/helpers/importer.ts, toolkits/commerce/tests/helpers.ts
system/manager/src/config.ts → system/core/backend/src/helpers/paths.ts
system/manager/src/index.ts → system/core/backend/src/helpers/cms-settings.ts, system/core/backend/src/helpers/shell.ts
system/manager/src/managers/adminPanelManager.ts → system/core/backend/src/helpers/cms-settings.ts, system/core/backend/src/helpers/logger.ts, system/core/backend/src/helpers/paths.ts, system/manager/src/config.ts, themes/store/src/constants.js, system/manager/src/managers/baseManager.ts
system/manager/src/managers/baseManager.ts → system/core/backend/src/helpers/cms-settings.ts, themes/store/src/constants.js, system/core/backend/src/helpers/logger.ts, system/core/backend/src/helpers/service-versions.ts, system/core/frontend/src/api/CRestApiClient.ts, system/manager/src/config.ts, themes/store/src/constants.js, system/manager/src/tasks/checkModules.ts, system/renderer/src/helpers/cacheManager.ts, system/manager/src/managers/adminPanelManager.ts, system/manager/src/managers/dockerManager.ts, system/manager/src/managers/rendererManager.ts, system/manager/src/managers/serverManager.ts
system/manager/src/managers/dockerManager.ts → system/core/backend/src/helpers/logger.ts, system/core/backend/src/helpers/paths.ts
system/manager/src/managers/rendererManager.ts → system/core/backend/src/helpers/cms-settings.ts, themes/store/src/constants.js, system/core/backend/src/helpers/logger.ts, system/core/frontend/src/api/CRestApiClient.ts, system/manager/src/config.ts, themes/store/src/constants.js, system/manager/src/managers/baseManager.ts
system/manager/src/managers/serverManager.ts → system/core/backend/src/helpers/cms-settings.ts, themes/store/src/constants.js, system/core/backend/src/helpers/logger.ts, system/core/backend/src/helpers/paths.ts, system/manager/src/config.ts, themes/store/src/constants.js, system/manager/src/managers/baseManager.ts
system/manager/src/tasks/buildTask.ts → system/core/backend/src/helpers/logger.ts, system/renderer/src/server.ts, system/utils/src/plugins/rollup.ts, system/manager/src/managers/rendererManager.ts, system/manager/src/tasks/checkModules.ts, system/manager/src/utils/buildUtils.ts, system/utils/src/plugins/rollup.ts, system/server/src/helpers/utils.ts
system/manager/src/tasks/checkModules.ts → system/core/backend/src/helpers/logger.ts, system/server/src/helpers/utils.ts, system/utils/src/downloader.ts, system/utils/src/shared.ts
system/manager/src/utils/cacheManager.js → system/manager/src/config.ts
system/manager/startup.js → system/core/backend/src/helpers/shell.ts, website/src/theme/Footer/index.tsx
system/renderer/src/generator.ts → system/core/backend/src/helpers/cms-settings.ts, system/core/backend/src/helpers/logger.ts, system/core/backend/src/helpers/shell.ts, system/core/frontend/src/api/CRestApiClient.ts, system/utils/src/shared.ts, system/renderer/src/helpers/defaultContents.tsx, system/renderer/src/helpers/helpers.ts
system/renderer/src/helpers/cacheManager.ts → system/core/backend/src/helpers/auth-settings.ts, system/core/backend/src/helpers/logger.ts, system/core/backend/src/helpers/paths.ts
system/renderer/src/helpers/pluginsDataFetcher.ts → system/renderer/src/helpers/initRenderer.ts
system/renderer/src/server.ts → system/core/backend/src/helpers/auth-settings.ts, system/core/backend/src/helpers/cms-settings.ts, system/core/backend/src/helpers/logger.ts, system/core/backend/src/helpers/shell.ts, system/utils/src/static.ts, system/renderer/src/helpers/cacheManager.ts, system/server/src/helpers/connect-database.ts
system/renderer/src/wrappers/appWrapper.tsx → system/renderer/src/helpers/document.tsx, toolkits/commerce/tests/helpers.ts, system/renderer/src/helpers/initRenderer.ts, system/renderer/src/helpers/redirects.ts
system/renderer/src/wrappers/getPropsWrapper.ts → system/renderer/src/helpers/getThemeStaticProps.ts, system/renderer/src/helpers/pluginsDataFetcher.ts
system/renderer/startup.js → system/core/backend/src/helpers/cms-settings.ts, themes/store/src/constants.js, system/core/backend/src/helpers/logger.ts, system/core/backend/src/helpers/shell.ts
system/server/migrations/mysql/1651054391643-permissions.js → system/server/migrations/sqlite/1651054396603-permissions.js
system/server/migrations/postgres/1651054394231-permissions.js → system/server/migrations/sqlite/1651054396603-permissions.js
system/server/src/controllers/auth.controller.ts → themes/store/src/constants.js, system/server/src/helpers/utils.ts
system/server/src/controllers/cms.controller.ts → themes/store/src/constants.js, system/server/src/helpers/reset-page.ts, system/server/src/helpers/utils.ts
system/server/src/controllers/mock.controller.ts → system/server/src/helpers/utils.ts
system/server/src/controllers/plugin.controller.ts → system/server/src/helpers/data-filters.ts, system/server/src/helpers/utils.ts
system/server/src/controllers/renderer.controller.ts → system/server/src/helpers/utils.ts
system/server/src/controllers/theme.controller.ts → system/server/src/helpers/utils.ts
system/server/src/dto/access-tokens.dto.ts → system/server/src/dto/user.dto.ts
system/server/src/dto/admin-cms-settings.dto.ts → system/server/src/dto/cms-settings.dto.ts
system/server/src/dto/cms-settings.dto.ts → system/server/src/dto/currency.dto.ts
system/server/src/dto/cms-stats.dto.ts → system/server/src/dto/page-stats.dto.ts
system/server/src/dto/cms-status.dto.ts → system/server/src/dto/update-info.dto.ts
system/server/src/dto/setup.dto.ts → toolkits/commerce/src/_index.ts, system/server/src/dto/create-user.dto.ts
system/server/src/dto/theme-config.dto.ts → system/server/src/dto/page-config.dto.ts
system/server/src/filters/apollo-exception.filter.ts → system/server/src/helpers/settings.ts
system/server/src/filters/auth.interceptor.ts → system/core/backend/src/helpers/auth-roles-permissions.ts
system/server/src/filters/rest-exception.filter.ts → system/server/src/helpers/settings.ts
system/server/src/helpers/connect-database.ts → system/server/src/helpers/constants.ts, system/server/src/helpers/settings.ts
system/server/src/helpers/data-filters.ts → system/server/src/helpers/reset-page.ts
system/server/src/helpers/resize-image-client.ts → system/server/src/resize-image.ts
system/server/src/helpers/server-manager.ts → themes/store/src/constants.js, system/core/backend/src/helpers/logger.ts, system/core/backend/src/helpers/paths.ts, system/server/src/helpers/constants.ts, system/server/src/helpers/settings.ts
system/server/src/helpers/settings.ts → system/core/backend/src/helpers/cms-settings.ts, themes/store/src/constants.js, system/core/backend/src/helpers/logger.ts, system/core/backend/src/helpers/paths.ts, system/server/src/helpers/constants.ts
system/server/src/helpers/state-manager.ts → system/server/src/helpers/server-manager.ts
system/server/src/main.ts → system/server/src/helpers/patches.js, system/renderer/src/server.ts, system/core/backend/src/helpers/auth-roles-permissions.ts, system/core/backend/src/helpers/shell.ts, system/server/src/filters/apollo-exception.filter.ts, system/server/src/filters/rest-exception.filter.ts, system/server/src/helpers/connect-database.ts, system/server/src/helpers/cors-handler.ts, system/server/src/helpers/get-resolvers.ts, system/server/src/helpers/server-manager.ts, system/server/src/helpers/settings.ts, system/server/src/modules/app.module.ts, system/server/src/services/auth.service.ts
system/server/src/modules/app.module.ts → system/server/src/modules/restapi.module.ts
system/server/src/modules/restapi.module.ts → system/server/src/helpers/get-controllers.ts, system/server/src/helpers/settings.ts
system/server/src/monitor.ts → system/core/backend/src/helpers/shell.ts
system/server/src/proxy.ts → system/core/backend/src/helpers/cms-settings.ts, system/core/backend/src/helpers/logger.ts, system/core/backend/src/helpers/shell.ts, system/server/src/helpers/server-manager.ts, system/server/src/helpers/settings.ts
system/server/src/resize-image.ts → system/core/backend/src/helpers/shell.ts
system/server/src/resolvers/custom-entity.resolver.ts → system/server/src/helpers/utils.ts
system/server/src/services/auth.service.ts → themes/store/src/constants.js
system/server/src/services/cms.service.ts → themes/store/src/constants.js, system/server/src/helpers/reset-page.ts, system/server/src/helpers/server-fire-action.ts, system/server/src/helpers/server-manager.ts, system/server/src/helpers/utils.ts, system/server/src/services/auth.service.ts, system/server/src/services/mock.service.ts, system/server/src/services/plugin.service.ts, system/server/src/services/theme.service.ts, system/server/src/helpers/resize-image-client.ts
system/server/src/services/migration.service.ts → system/server/src/helpers/utils.ts, system/server/src/services/cms.service.ts
system/server/src/services/mock.service.ts → system/server/src/helpers/reset-page.ts
system/server/src/services/plugin.service.ts → system/server/src/helpers/server-fire-action.ts, system/server/src/helpers/server-manager.ts, system/server/src/helpers/utils.ts, system/server/src/services/cms.service.ts
system/server/src/services/renderer.service.ts → system/server/src/helpers/utils.ts, system/server/src/services/theme.service.ts
system/server/src/services/stats.service.ts → system/server/src/helpers/monitor-client.ts
system/server/src/services/store.service.ts → system/server/src/helpers/server-fire-action.ts
system/server/src/services/theme.service.ts → system/server/src/helpers/reset-page.ts, system/server/src/helpers/server-fire-action.ts, system/server/src/helpers/server-manager.ts, system/server/src/helpers/state-manager.ts, system/server/src/helpers/utils.ts, system/server/src/services/cms.service.ts, system/server/src/services/plugin.service.ts
system/server/startup.js → system/core/backend/src/helpers/paths.ts, themes/store/src/constants.js, system/core/backend/src/helpers/shell.ts
system/server/tests/controller.helpers.ts → system/server/src/helpers/connect-database.ts, system/server/tests/helpers.ts
system/server/tests/controllers/auth.controller.spec.ts → toolkits/commerce/tests/helpers.ts
system/server/tests/controllers/cms.controller.spec.ts → toolkits/commerce/tests/helpers.ts
system/server/tests/controllers/plugin.controller.spec.ts → toolkits/commerce/tests/helpers.ts
system/server/tests/controllers/theme.controller.spec.ts → toolkits/commerce/tests/helpers.ts
system/server/tests/helpers.ts → system/server/src/helpers/connect-database.ts
system/server/tests/jest.config.ts → themes/store/src/types.ts
system/server/tests/resolver.helpers.ts → system/server/src/helpers/get-resolvers.ts, system/server/tests/helpers.ts
system/server/tests/resolvers/attribute.resolver.spec.ts → toolkits/commerce/tests/helpers.ts
system/server/tests/resolvers/coupon.resolver.spec.ts → toolkits/commerce/tests/helpers.ts
system/server/tests/resolvers/custom-entity.resolver.spec.ts → toolkits/commerce/tests/helpers.ts
system/server/tests/resolvers/generic.resolver.spec.ts → toolkits/commerce/tests/helpers.ts
system/server/tests/resolvers/order.resolver.spec.ts → toolkits/commerce/tests/helpers.ts
system/server/tests/resolvers/post.resolver.spec.ts → toolkits/commerce/tests/helpers.ts
system/server/tests/resolvers/product-category.resolver.spec.ts → toolkits/commerce/tests/helpers.ts
system/server/tests/resolvers/product-review.resolver.spec.ts → toolkits/commerce/tests/helpers.ts
system/server/tests/resolvers/product.resolver.spec.ts → toolkits/commerce/tests/helpers.ts
system/server/tests/resolvers/role.resolver.spec.ts → toolkits/commerce/tests/helpers.ts
system/server/tests/resolvers/tag.resolver.spec.ts → toolkits/commerce/tests/helpers.ts
system/server/tests/resolvers/user.resolver.spec.ts → toolkits/commerce/tests/helpers.ts
system/server/tests/setup.ts → system/server/src/helpers/connect-database.ts
system/utils/jest.config.ts → themes/store/src/types.ts
system/utils/src/downloader.ts → system/utils/src/shared.ts, system/utils/src/types.ts
system/utils/src/installer.ts → system/utils/src/downloader.ts, system/utils/src/shared.ts, system/utils/src/types.ts
system/utils/src/plugins/rollup-globals.ts → system/utils/src/plugins/rollup.ts
system/utils/src/plugins/rollup.ts → system/utils/src/plugins/rollup-globals.ts
system/utils/src/shared.ts → system/utils/src/types.ts
system/utils/src/static.ts → system/core/backend/src/helpers/paths.ts, system/core/frontend/src/api/CRestApiClient.ts
system/utils/tests/downloader.spec.ts → system/utils/src/downloader.ts, system/utils/tests/helpers.ts
system/utils/tests/rollup.spec.ts → system/utils/src/plugins/rollup.ts, system/utils/tests/helpers.ts
themes/blog/src/components/header/Header.tsx → toolkits/commerce/src/base/icons.tsx, themes/blog/src/components/header/HeaderSearch.tsx
themes/blog/src/components/header/HeaderSearch.tsx → system/admin/src/components/inputs/DateInput/styles.ts
themes/blog/src/components/layout/Layout.tsx → themes/store/src/components/footer/Footer.tsx, themes/store/src/components/header/Header.tsx
themes/blog/src/components/loadbox/Loadbox.tsx → system/admin/src/components/inputs/DateInput/styles.ts
themes/blog/src/components/postCard/PostCard.tsx → toolkits/commerce/src/base/icons.tsx
themes/blog/src/helpers/theme.ts → system/admin/src/components/inputs/DateInput/styles.ts
themes/blog/src/pages/404.tsx → themes/store/src/components/layout/Layout.tsx, themes/blog/src/pages/_app.tsx
themes/blog/src/pages/_app.tsx → themes/store/src/helpers/createEmotionCache.ts, themes/store/src/helpers/theme.ts
themes/blog/src/pages/_document.tsx → system/renderer/src/helpers/document.tsx, themes/store/src/helpers/createEmotionCache.ts, themes/store/src/helpers/theme.ts
themes/blog/src/pages/index.tsx → themes/store/src/components/layout/Layout.tsx, themes/store/src/components/postCard/PostCard.tsx, themes/store/src/helpers/getPosts.ts, themes/blog/src/pages/_app.tsx
themes/blog/src/pages/pages/[slug].tsx → themes/store/src/components/layout/Layout.tsx, themes/store/src/pages/_app.tsx
themes/blog/src/pages/post/[slug].tsx → themes/store/src/components/layout/Layout.tsx, themes/store/src/components/postCard/PostCard.tsx, themes/store/src/pages/_app.tsx
themes/blog/src/pages/search.tsx → themes/store/src/components/layout/Layout.tsx, toolkits/commerce/src/mui/Pagination/Pagination.tsx, themes/store/src/components/postCard/PostCard.tsx, themes/store/src/helpers/getPosts.ts, themes/blog/src/pages/_app.tsx
themes/blog/src/pages/tag/[slug].tsx → themes/store/src/components/layout/Layout.tsx, toolkits/commerce/src/mui/Pagination/Pagination.tsx, themes/store/src/components/postCard/PostCard.tsx, themes/store/src/helpers/getPosts.ts, themes/store/src/pages/_app.tsx
themes/blog/tests/jest.config.ts → themes/store/src/types.ts
themes/blog/tests/pages/index.test.tsx → website/src/theme/Footer/index.tsx
themes/blog/tests/pages/search.test.tsx → themes/blog/src/pages/search.tsx
themes/store/src/components/header/Header.tsx → themes/store/src/helpers/AppState.ts, themes/store/src/components/header/MobileHeader.tsx
themes/store/src/components/header/MobileHeader.tsx → themes/store/src/helpers/AppState.ts, toolkits/commerce/src/base/icons.tsx
themes/store/src/components/layout/Layout.tsx → themes/store/src/helpers/AppState.ts, themes/store/src/components/footer/Footer.tsx, themes/store/src/components/header/Header.tsx, themes/store/src/components/modals/cart/CartModal.tsx, themes/store/src/components/modals/productQuickView/ProductQuickView.tsx, themes/store/src/components/modals/viewed/ViewedModal.tsx, themes/store/src/components/modals/wishlist/WishlistModal.tsx, themes/store/src/components/modals/signIn/SignIn.tsx
themes/store/src/components/loadbox/Loadbox.tsx → system/admin/src/components/inputs/DateInput/styles.ts
themes/store/src/components/modals/cart/CartModal.tsx → themes/store/src/helpers/AppState.ts, toolkits/commerce/src/base/icons.tsx, themes/store/src/components/modals/baseModal/Modal.tsx
themes/store/src/components/modals/productQuickView/ProductQuickView.tsx → themes/store/src/helpers/AppState.ts, toolkits/commerce/src/base/icons.tsx, toolkits/commerce/src/mui/Loadbox/Loadbox.tsx, themes/store/src/components/productDetails/ProductDetails.tsx, themes/store/src/components/modals/baseModal/Modal.tsx
themes/store/src/components/modals/signIn/PasswordField.tsx → toolkits/commerce/src/base/icons.tsx
themes/store/src/components/modals/signIn/SignIn.tsx → themes/store/src/helpers/AppState.ts, themes/store/src/components/toast/toast.tsx, themes/store/src/components/modals/baseModal/Modal.tsx, themes/store/src/components/modals/signIn/PasswordField.tsx
themes/store/src/components/modals/viewed/ViewedModal.tsx → themes/store/src/helpers/AppState.ts, toolkits/commerce/src/base/ProductCard/ProductCard.tsx, toolkits/commerce/src/base/icons.tsx, themes/store/src/components/modals/baseModal/Modal.tsx
themes/store/src/components/modals/wishlist/WishlistModal.tsx → themes/store/src/helpers/AppState.ts, toolkits/commerce/src/base/icons.tsx, toolkits/commerce/src/base/ProductCard/ProductCard.tsx, themes/store/src/components/modals/baseModal/Modal.tsx
themes/store/src/components/postCard/PostCard.tsx → toolkits/commerce/src/base/icons.tsx
themes/store/src/components/productCard/ProductCard.tsx → themes/store/src/helpers/AppState.ts
themes/store/src/components/productDetails/ProductDetails.tsx → themes/store/src/helpers/AppState.ts
themes/store/src/helpers/theme.ts → system/admin/src/components/inputs/DateInput/styles.ts
themes/store/src/pages/404.tsx → themes/store/src/components/layout/Layout.tsx, themes/store/src/pages/_app.tsx
themes/store/src/pages/_app.tsx → system/admin/src/components/inputs/DateInput/styles.ts, themes/store/src/components/postCard/PostCard.tsx, toolkits/commerce/src/base/ProductCard/ProductCard.tsx, themes/store/src/components/toast/toast.tsx, themes/store/src/helpers/createEmotionCache.ts, themes/store/src/helpers/theme.ts
themes/store/src/pages/_document.tsx → system/renderer/src/helpers/document.tsx, themes/store/src/helpers/createEmotionCache.ts, themes/store/src/helpers/theme.ts
themes/store/src/pages/account.tsx → themes/store/src/components/layout/Layout.tsx, themes/store/src/helpers/AppState.ts, themes/store/src/pages/_app.tsx
themes/store/src/pages/blog.tsx → themes/store/src/components/layout/Layout.tsx, themes/store/src/components/postCard/PostCard.tsx, themes/store/src/helpers/getPosts.ts, themes/store/src/pages/_app.tsx
themes/store/src/pages/blog/[slug].tsx → themes/store/src/components/layout/Layout.tsx, themes/store/src/components/postCard/PostCard.tsx, themes/store/src/pages/_app.tsx
themes/store/src/pages/category/[slug].tsx → themes/store/src/components/layout/Layout.tsx, toolkits/commerce/src/base/ProductCard/ProductCard.tsx, themes/store/src/pages/_app.tsx
themes/store/src/pages/checkout.tsx → themes/store/src/components/layout/Layout.tsx, themes/store/src/helpers/AppState.ts, themes/store/src/pages/_app.tsx
themes/store/src/pages/index.tsx → themes/store/src/components/layout/Layout.tsx, themes/store/src/pages/_app.tsx
themes/store/src/pages/pages/[slug].tsx → themes/store/src/components/layout/Layout.tsx, themes/store/src/pages/_app.tsx
themes/store/src/pages/product/[slug].tsx → themes/store/src/components/layout/Layout.tsx, themes/store/src/components/productDetails/ProductDetails.tsx, themes/store/src/pages/_app.tsx
themes/store/src/pages/tag/[slug].tsx → themes/store/src/components/layout/Layout.tsx, themes/store/src/components/postCard/PostCard.tsx, themes/store/src/helpers/getPosts.ts, themes/store/src/pages/_app.tsx
themes/store/tests/jest.config.ts → themes/store/src/types.ts
themes/store/tests/pages/account.test.tsx → themes/store/src/pages/account.tsx
themes/store/tests/pages/blog.test.tsx → themes/store/src/pages/blog.tsx
themes/store/tests/pages/checkout.test.tsx → themes/store/src/pages/checkout.tsx
toolkits/commerce/jest.config.ts → themes/store/src/types.ts
toolkits/commerce/src/base/AccountInfo/AccountInfo.test.tsx → toolkits/commerce/src/base/AccountInfo/AccountInfo.tsx
toolkits/commerce/src/base/AccountInfo/AccountInfo.tsx → toolkits/commerce/src/helpers/notifier.tsx, toolkits/commerce/src/base/shared/Button.tsx, toolkits/commerce/src/base/shared/TextField.tsx, toolkits/commerce/src/base/AccountInfo/actions.ts, toolkits/commerce/src/base/AccountInfo/DefaultElements.tsx
toolkits/commerce/src/base/AccountInfo/DefaultElements.tsx → toolkits/commerce/src/base/shared/TextField.tsx, toolkits/commerce/src/base/AccountInfo/AccountInfo.tsx
toolkits/commerce/src/base/AccountInfo/actions.ts → toolkits/commerce/src/helpers/notifier.tsx, toolkits/commerce/src/base/AccountInfo/AccountInfo.tsx, toolkits/commerce/src/base/AccountInfo/DefaultElements.tsx
toolkits/commerce/src/base/AccountOrders/AccountOrders.test.tsx → toolkits/commerce/src/base/AccountOrders/AccountOrders.tsx
toolkits/commerce/src/base/AccountOrders/AccountOrders.tsx → toolkits/commerce/src/base/CartList/CartList.tsx
toolkits/commerce/src/base/Breadcrumbs/Breadcrumbs.test.tsx → toolkits/commerce/src/base/Breadcrumbs/Breadcrumbs.tsx
toolkits/commerce/src/base/Breadcrumbs/Breadcrumbs.tsx → toolkits/commerce/src/base/Breadcrumbs/Crumb.tsx, toolkits/commerce/src/base/Breadcrumbs/DefaultElements.tsx, toolkits/commerce/src/base/Breadcrumbs/getData.ts
toolkits/commerce/src/base/Breadcrumbs/Crumb.tsx → toolkits/commerce/src/helpers/useLinks.ts, toolkits/commerce/src/base/Breadcrumbs/Breadcrumbs.tsx, toolkits/commerce/src/base/Breadcrumbs/DefaultElements.tsx
toolkits/commerce/src/base/Breadcrumbs/DefaultElements.tsx → toolkits/commerce/src/base/icons.tsx
toolkits/commerce/src/base/Breadcrumbs/getData.ts → toolkits/commerce/src/base/Breadcrumbs/Breadcrumbs.tsx
toolkits/commerce/src/base/CartList/CartList.test.tsx → toolkits/commerce/src/base/CartList/CartList.tsx
toolkits/commerce/src/base/CartList/CartList.tsx → toolkits/commerce/src/base/shared/Button.tsx, toolkits/commerce/src/base/CartList/CartListItem.tsx, toolkits/commerce/src/helpers/state.ts, toolkits/commerce/src/helpers/useStoreAttributes.ts
toolkits/commerce/src/base/CartList/CartListItem.tsx → toolkits/commerce/src/helpers/useLinks.ts, toolkits/commerce/src/base/icons.tsx, toolkits/commerce/src/base/shared/Button.tsx, toolkits/commerce/src/base/CartList/CartList.tsx
toolkits/commerce/src/base/CategoryFilter/CategoryFilter.test.tsx → toolkits/commerce/src/base/CategoryFilter/CategoryFilter.tsx
toolkits/commerce/src/base/CategoryFilter/CategoryFilter.tsx → toolkits/commerce/src/helpers/state.ts
toolkits/commerce/src/base/CategoryList/CategoryList.test.tsx → toolkits/commerce/src/base/CategoryList/CategoryList.tsx
toolkits/commerce/src/base/CategoryList/CategoryList.tsx → toolkits/commerce/src/helpers/state.ts, toolkits/commerce/src/helpers/useStoreAttributes.ts, toolkits/commerce/src/base/ProductCard/ProductCard.tsx
toolkits/commerce/src/base/CategorySort/CategorySort.test.tsx → toolkits/commerce/src/base/CategorySort/CategorySort.tsx
toolkits/commerce/src/base/CategorySort/CategorySort.tsx → toolkits/commerce/src/helpers/state.ts, toolkits/commerce/src/mui/Select/Select.tsx
toolkits/commerce/src/base/Checkout/Checkout.test.tsx → toolkits/commerce/src/base/Checkout/Checkout.tsx
toolkits/commerce/src/base/Checkout/Checkout.tsx → toolkits/commerce/src/helpers/notifier.tsx, toolkits/commerce/src/base/shared/Button.tsx, toolkits/commerce/src/base/shared/Radio.tsx, toolkits/commerce/src/base/shared/TextField.tsx, toolkits/commerce/src/base/Checkout/actions.ts, toolkits/commerce/src/base/Checkout/Coupons.tsx
toolkits/commerce/src/base/Checkout/Coupons.tsx → toolkits/commerce/src/base/shared/Button.tsx, toolkits/commerce/src/base/shared/TextField.tsx, toolkits/commerce/src/base/Checkout/actions.ts, toolkits/commerce/src/base/Checkout/DefaultElements.tsx, toolkits/commerce/src/base/Checkout/Checkout.tsx
toolkits/commerce/src/base/Checkout/DefaultElements.tsx → toolkits/commerce/src/base/shared/TextField.tsx, toolkits/commerce/src/base/Checkout/actions.ts, toolkits/commerce/src/base/Checkout/Checkout.tsx
toolkits/commerce/src/base/Checkout/actions.ts → toolkits/commerce/src/helpers/notifier.tsx, toolkits/commerce/src/helpers/state.ts, toolkits/commerce/src/base/Checkout/Checkout.tsx, toolkits/commerce/src/base/Checkout/DefaultElements.tsx
toolkits/commerce/src/base/CurrencySwitch/CurrencySwitch.test.tsx → toolkits/commerce/src/base/CurrencySwitch/CurrencySwitch.tsx
toolkits/commerce/src/base/CurrencySwitch/CurrencySwitch.tsx → toolkits/commerce/src/mui/Select/Select.tsx
toolkits/commerce/src/base/ProductActions/ProductActions.test.tsx → toolkits/commerce/src/base/ProductActions/ProductActions.tsx
toolkits/commerce/src/base/ProductActions/ProductActions.tsx → toolkits/commerce/src/helpers/notifier.tsx, toolkits/commerce/src/helpers/state.ts, toolkits/commerce/src/helpers/useStoreAttributes.ts, toolkits/commerce/src/base/shared/Alert.tsx, toolkits/commerce/src/base/shared/Button.tsx
toolkits/commerce/src/base/ProductAttributes/ProductAttributes.test.tsx → toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx
toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx → toolkits/commerce/src/helpers/state.ts, toolkits/commerce/src/helpers/useStoreAttributes.ts
toolkits/commerce/src/base/ProductCard/ProductCard.test.tsx → toolkits/commerce/src/base/ProductCard/ProductCard.tsx
toolkits/commerce/src/base/ProductCard/ProductCard.tsx → toolkits/commerce/src/helpers/notifier.tsx, toolkits/commerce/src/helpers/useLinks.ts, toolkits/commerce/src/helpers/useStoreAttributes.ts, toolkits/commerce/src/base/icons.tsx, toolkits/commerce/src/base/shared/Button.tsx, toolkits/commerce/src/base/shared/Rating.tsx, toolkits/commerce/src/base/shared/Tooltip.tsx
toolkits/commerce/src/base/ProductGallery/ProductGallery.test.tsx → toolkits/commerce/src/base/ProductGallery/ProductGallery.tsx
toolkits/commerce/src/base/ProductReviews/ProductReviews.test.tsx → toolkits/commerce/src/base/ProductReviews/ProductReviews.tsx
toolkits/commerce/src/base/ProductReviews/ProductReviews.tsx → toolkits/commerce/src/helpers/notifier.tsx, toolkits/commerce/src/base/shared/Alert.tsx, toolkits/commerce/src/base/shared/Button.tsx, toolkits/commerce/src/base/shared/Rating.tsx, toolkits/commerce/src/base/shared/TextField.tsx, toolkits/commerce/src/base/shared/Tooltip.tsx, toolkits/commerce/src/base/ProductReviews/ReviewForm.tsx, toolkits/commerce/src/base/ProductReviews/ReviewItem.tsx
toolkits/commerce/src/base/ProductReviews/ReviewForm.tsx → toolkits/commerce/src/helpers/notifier.tsx, toolkits/commerce/src/base/shared/Alert.tsx, toolkits/commerce/src/base/shared/Button.tsx, toolkits/commerce/src/base/shared/Rating.tsx, toolkits/commerce/src/base/shared/TextField.tsx, toolkits/commerce/src/base/shared/Tooltip.tsx, toolkits/commerce/src/base/ProductReviews/ProductReviews.tsx
toolkits/commerce/src/base/ProductReviews/ReviewItem.tsx → toolkits/commerce/src/base/shared/Rating.tsx, toolkits/commerce/src/base/ProductReviews/ProductReviews.tsx
toolkits/commerce/src/base/ProductSearch/ListItem.tsx → toolkits/commerce/src/base/ProductSearch/ProductSearch.tsx
toolkits/commerce/src/base/ProductSearch/ProductSearch.test.tsx → toolkits/commerce/src/base/ProductSearch/ProductSearch.tsx
toolkits/commerce/src/base/ProductSearch/ProductSearch.tsx → toolkits/commerce/src/mui/Popper/Popper.tsx, toolkits/commerce/src/base/shared/TextField.tsx, toolkits/commerce/src/base/ProductSearch/ListItem.tsx
toolkits/commerce/src/base/ViewedItems/ViewedItems.test.tsx → toolkits/commerce/src/base/ViewedItems/ViewedItems.tsx
toolkits/commerce/src/base/ViewedItems/ViewedItems.tsx → toolkits/commerce/src/helpers/useStoreAttributes.ts, toolkits/commerce/src/base/ProductCard/ProductCard.tsx
toolkits/commerce/src/base/Wishlist/Wishlist.test.tsx → toolkits/commerce/src/base/Wishlist/Wishlist.tsx
toolkits/commerce/src/base/Wishlist/Wishlist.tsx → toolkits/commerce/src/helpers/useStoreAttributes.ts, toolkits/commerce/src/base/ProductCard/ProductCard.tsx
toolkits/commerce/src/helpers/useProductVariants.ts → toolkits/commerce/src/helpers/state.ts
toolkits/commerce/src/helpers/useStoreAttributes.ts → toolkits/commerce/src/helpers/state.ts
toolkits/commerce/src/mui/Breadcrumbs/Breadcrumbs.tsx → system/admin/src/components/inputs/DateInput/styles.ts
toolkits/commerce/src/mui/Loadbox/Loadbox.tsx → system/admin/src/components/inputs/DateInput/styles.ts
toolkits/commerce/src/mui/Notifier/Notifier.tsx → toolkits/commerce/src/helpers/notifier.tsx
toolkits/commerce/src/mui/ProductAttributes/AttributeTitle.tsx → toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx
toolkits/commerce/src/mui/ProductAttributes/AttributeValue.tsx → toolkits/commerce/src/base/ProductAttributes/ProductAttributes.tsx
toolkits/commerce/src/mui/QuantityField/QuantityField.tsx → toolkits/commerce/src/base/icons.tsx
toolkits/commerce/src/mui/RadioGroup/RadioGroup.tsx → toolkits/commerce/src/base/shared/Radio.tsx
toolkits/commerce/src/mui/index.ts → toolkits/commerce/src/base/AccountInfo/AccountInfo.tsx, toolkits/commerce/src/base/AccountOrders/AccountOrders.tsx, toolkits/commerce/src/mui/Breadcrumbs/Breadcrumbs.tsx, toolkits/commerce/src/base/CartList/CartList.tsx, toolkits/commerce/src/base/CategoryList/CategoryList.tsx, toolkits/commerce/src/base/CategorySort/CategorySort.tsx, toolkits/commerce/src/base/Checkout/Checkout.tsx, toolkits/commerce/src/base/CurrencySwitch/CurrencySwitch.tsx, toolkits/commerce/src/mui/ProductActions/ProductActions.tsx, toolkits/commerce/src/base/ProductCard/ProductCard.tsx, toolkits/commerce/src/base/ProductReviews/ProductReviews.tsx, toolkits/commerce/src/base/ProductSearch/ProductSearch.tsx, toolkits/commerce/src/base/ViewedItems/ViewedItems.tsx, toolkits/commerce/src/base/Wishlist/Wishlist.tsx, toolkits/commerce/src/helpers/withElements.ts, toolkits/commerce/src/mui/Breadcrumbs/Breadcrumbs.tsx, toolkits/commerce/src/mui/Loadbox/Loadbox.tsx, toolkits/commerce/src/mui/Notifier/Notifier.tsx, toolkits/commerce/src/mui/Pagination/Pagination.tsx, toolkits/commerce/src/mui/Popper/Popper.tsx, toolkits/commerce/src/mui/ProductActions/ProductActions.tsx, toolkits/commerce/src/mui/ProductAttributes/AttributeTitle.tsx, toolkits/commerce/src/mui/ProductAttributes/AttributeValue.tsx, toolkits/commerce/src/mui/QuantityField/QuantityField.tsx, toolkits/commerce/src/mui/RadioGroup/RadioGroup.tsx, toolkits/commerce/src/mui/Select/Select.tsx
website/src/components/CoverFlowImages.tsx → website/src/components/Lightbox.tsx
website/src/pages/index.tsx → system/core/frontend/src/components/Link/Link.tsx, themes/store/src/components/layout/Layout.tsx, website/src/components/CoverFlowImages.tsx
website/src/pages/latest-frontend-dependencies.tsx → system/core/frontend/src/components/Link/Link.tsx, themes/store/src/components/layout/Layout.tsx, website/src/helpers/api-client.ts
website/src/theme/Footer/index.tsx → system/core/frontend/src/components/Link/Link.tsx
website/src/theme/prism-include-languages.js → system/manager/src/config.ts
```

## Documentation

### CONTRIBUTING.md

# Contributing

Every contribution is pretty much appreciated and welcomed!

### Have a question?

Ask in [Discord server](https://discord.com/invite/mxmJNSZ2gn)

### Have a problem or found a bug?

If you find a bug, you can help us by submitting an issue to our [GitHub Repository](https://github.com/CromwellCMS/Cromwell/issues)

### Have a feature suggestion?

You can request a new feature by submitting an issue to our GitHub Repository. If you would like to implement a new feature, please submit an issue with a proposal for your work first, to be sure that we can use it.  
Wait for team members to leave a feedback on your issue.

## Setup

Read [Core development guide](https://github.com/CromwellCMS/Cromwell/tree/master/system)

## Submitting Changes

Workflow:

- For a major fix/feature make sure your PR has an issue and if it doesn't, please create one. This would help discussion with the community, and polishing ideas in case of a new feature.
- Create a fork of our [GitHub repos

### README.md

# Cromwell CMS

Cromwell CMS is a free open source headless TypeScript CMS for creating lightning-fast websites with React and Next.js. It has a powerful plugin/theming system while providing extensive Admin panel GUI for WordPress-like user experience.
We are focused on empowering content-creators and people with no programming knowledge to conveniently use all features of the CMS in their projects.

Main features of Cromwell CMS:

- Online store and blogging platform management systems.
- Drag-and-drop theme editor.
- Simple installation of themes and plugins from the official store and their local management.
- Free full-featured online store and blog themes with multiple plugins.
- Integrated Database. SQLite, MySQL, MariaDB, PostgreSQL are supported to use.
- Developer-friendly experience. Use all power of Next.js, Nest.js, TypeORM, TypeGraphQL along with CMS API to build any type of website.

## Installation

[See our docs](https://cromwellcms.com/docs/overview/installation)

## 

### docker/cromwell-mariadb/README.md

Cromwell CMS Image with Nginx and MariaDB

```sh
docker run -d -p 80:80 --name my-website cromwell-mariadb:latest
```


### plugins/main-menu/README.md

# Menu plugin for Cromwell CMS

Add website navigation. Elements can be edited on the admin panel plugin's page.

Supports desktop (row) and mobile (column) modes. You need to use your own solution to detect mobile screen, the plugin needs `mobile` prop to display mobile mode. Otherwise will be displayed desktop mode.

Custom elements:

- MenuItem
- IconButton
- Popover

Example of usage:

```tsx
import { IconButton, MenuItem, Popover } from '@mui/material';
import { CPlugin, registerPluginSSR } from '@cromwell/core-frontend';

registerPluginSSR('@cromwell/plugin-main-menu', '*');

export default function MyPage() {
  return (
    <CPlugin
      id="menu"
      pluginName="@cromwell/plugin-main-menu"
      plugin={{
        instanceSettings: {
          mobile: true,
          elements: {
            MenuItem,
            IconButton,
            Popover,
          },
        },
      }}
    />
  );
}
```


### plugins/product-showcase/README.md

# Product showcase plugin for Cromwell CMS

Adds a carousel with products. On a product page it will fetch products from same categories, on other pages - most recent products.

Relies on shared product card component. To register, for example add this code in custom app:

```ts title="_app.tsx"
import { registerSharedComponent } from '@cromwell/core';
import { MuiProductCard } from '@cromwell/toolkit-commerce';

registerSharedComponent(ESharedComponentNames.ProductCard, MuiProductCard);

export default function App() {
  /* ... */
}
```


### system/README.md

# CMS Core Development

### Prerequisites

- Node.js v12-16
- Python
- `npm install node-gyp -g`

### Install

```sh
$ git clone https://github.com/CromwellCMS/Cromwell
$ npm run build
$ yarn cromwell start
```

**You don't need to run `npm install`**, installation/build handled by startup.js script in the root which invoked by `npm run build`. In development use yarn to install/update dependencies.

### Configure

By default the CMS will launch with SQLite database.  
But you may need to use some specific development databases. Copy config file in the root from `cmsconfig.json.example` to `cmsconfig.json`. Rename property of needed DB to `orm` for the CMS to use it. For example `orm-mariadb` to `orm`.

Launch development databases:

- `npm run docker:start-dev-mariadb` for MariaDB
- `docker:start-dev-postgres` for Postgres

## Services

In runtime Cromwell CMS is a set of services (npm packages).  
Below listed core services with default settings (ports at localhost address can be con

### system/admin/README.md

Cromwell Admin Panel


### system/core/backend/README.md

CromwellCMS Backend SDK

Exports backend helpers, ORM repositories and entities.

### Install

```
npm i @cromwell/core-backend
```

### Use

Example of usage

```ts
import { ProductRepository } from '@cromwell/core-backend';
import { getCustomRepository } from 'typeorm';

const products = await getCustomRepository(ProductRepository).getProducts();
```


### system/core/common/README.md

CromwellCMS Shared SDK

Exports common type definitions and helpers used by frontend and backend.

### Install

```
npm i @cromwell/core
```

### Use

Example of usage

```ts
import { getStoreItem, TCmsSettings } from '@cromwell/core';

const settings: TCmsSettings | undefined = getStoreItem('cmsSettings');
```


### system/core/frontend/README.md

CromwellCMS Frontend SDK

Exports Blocks, React components, API clients and frontend helpers.

### Install

```
npm i @cromwell/core-frontend
```

### Use

Example of usage

```ts
import { getGraphQLClient } from '@cromwell/core-frontend';

const products = await getGraphQLClient().getProducts();
```


### system/utils/README.md

# Cromwell CMS node modules manager

## Node modules bundler & loader

Bundles node modules into specific format for Cromwell module loader. Similar to RequireJS.

```sh
yarn cromwell bm
```

Will scan over packages for frontendDependencies array and bundle each module in ./.cromwell/bundled-modules
Cromwell bundler plugins for Rollup and Webpack after building theme or plugin emit imports map which is supposed to be used with such bundled node modules via this cli command.

### Options:

#### "--production"

```sh
yarn cromwell bm --production
```

Will enable production mode of webpack. Development by default.

### Rebundle

```sh
yarn cromwell bm -r
```

Will delete all bundled modules and bundle new.
By default "cromwella b" command bundles only newly found modules that aren't exist in ./.cromwell/bundled-modules (caching)

## Hoisting installation of node_modules in multi-package repositories.

### Deprecated. Use Yarn now.

Simplified alternative of Lerna package manager.
Overall

### themes/store/README.md

# @cromwell/theme-store

> Online store theme for Cromwell CMS. One of two default themes.

## Use as a package

This theme will be installed by your package manager during default [installation of the CMS](https://cromwellcms.com/docs/overview/installation).
It's also can be added via theme market in the admin panel.  
Or you can add it manually via command: `yarn add @cromwell/theme-store -D`.

## Clone and develop

You don't need to clone and build entire CMS repository. For making a custom app on top of this theme you can download its files:

1. `npx github-directory-downloader https://github.com/CromwellCMS/Cromwell/tree/master/themes/store --dir=project-name`
2. `cd project-name`
3. Open `package.json`, change `name` and `cromwell.title` properties, so for the CMS there won't be collisions with current `@cromwell/theme-store`.
4. `yarn install`
5. `yarn add @cromwell/theme-store -D`
6. Start the CMS in background to use API: `yarn cromwell start`
7. Start theme development server

### toolkits/commerce/README.md

# Commerce toolkit

> A toolkit for building e-commerce websites with Cromwell CMS

### Links

- Read about Cromwell CMS toolkits in general: [https://cromwellcms.com/docs/toolkits/intro](https://cromwellcms.com/docs/toolkits/intro).
- [Live demo](https://demo-store.cromwellcms.com/category/2)
- See examples of usage in [theme-store](https://github.com/CromwellCMS/Cromwell/tree/master/themes/store).

### Install

```sh
npm i @cromwell/toolkit-commerce
```

Some components of this package use `react-toastify`. If you need notifications add `ToastContainer` into your custom app:

```tsx title="_app.tsx"
import React from 'react';
import { ToastContainer } from 'react-toastify';

export default function App() {
  return (
    <div>
      /* ... */
      <ToastContainer />
    </div>
  );
}
```

Add global CSS in `cromwell.config.js`:

```js title="cromwell.config.js"
module.exports = {
  globalCss: ['@cromwell/toolkit-commerce/dist/_index.css', 'react-toastify/dist/ReactToastify.css'],
};

### website/README.md

# Website

This website is built using [Docusaurus 2](https://docusaurus.io/)

## Building website

1. Generate API docs (they are Git ignored): `npm run generate:api`
2. Build: `npm run build`
3. Host static files from `./build` directory or `npm run serve`

## Develop

Start development server: `npm run start`

