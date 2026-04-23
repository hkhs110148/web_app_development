# 路由設計文件 (ROUTES) - 食譜收藏夾系統

## 1. 路由總覽表格

| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| --- | --- | --- | --- | --- |
| 首頁 (推薦與熱門清單) | GET | `/` | `templates/recipe/index.html` | 顯示首頁 |
| 使用者註冊頁面 | GET | `/auth/register` | `templates/auth/register.html` | 顯示註冊表單 |
| 處理註冊 | POST | `/auth/register` | — | 建立帳號並重導至登入頁或首頁 |
| 使用者登入頁面 | GET | `/auth/login` | `templates/auth/login.html` | 顯示登入表單 |
| 處理登入 | POST | `/auth/login` | — | 登入驗證並重導至首頁 |
| 使用者登出 | GET | `/auth/logout` | — | 登出並重導至首頁 |
| 搜尋食譜 | GET | `/recipes/search` | `templates/recipe/search.html` | 顯示搜尋結果與條件篩選 |
| 檢視食譜詳情 | GET | `/recipes/<int:recipe_id>` | `templates/recipe/detail.html` | 顯示單篇食譜內容 |
| 新增食譜頁面 | GET | `/recipes/new` | `templates/recipe/new.html` | 顯示新增表單 |
| 建立食譜 | POST | `/recipes/new` | — | 處理新增食譜並重導至詳情頁 |
| 編輯食譜頁面 | GET | `/recipes/<int:recipe_id>/edit` | `templates/recipe/edit.html` | 顯示編輯表單 |
| 更新食譜 | POST | `/recipes/<int:recipe_id>/edit` | — | 處理編輯並重導至詳情頁 |
| 刪除食譜 | POST | `/recipes/<int:recipe_id>/delete` | — | 刪除並重導至首頁或個人主頁 |
| 收藏食譜 | POST | `/recipes/<int:recipe_id>/collect` | — | 將食譜加入收藏（Ajax或重導向） |
| 提交食譜評價 | POST | `/recipes/<int:recipe_id>/review` | — | 提交評價與留言並重導向詳情頁 |
| 個人主頁 | GET | `/profile` | `templates/profile/index.html` | 查看個人資訊與收藏列表 |
| 產生購物清單 | POST | `/recipes/<int:recipe_id>/shopping-list` | — | 根據食譜食材產生購物清單 |
| 查看購物清單 | GET | `/profile/shopping-list` | `templates/profile/shopping_list.html` | 顯示已儲存的購物清單 |

## 2. 每個路由的詳細說明

### Auth 模組 (`auth.py`)
- **`/auth/register` (GET/POST)**
  - 輸入：表單包含 `username`, `email`, `password`
  - 邏輯：檢查信箱是否已存在，對密碼做 Hash，建立 `User` 紀錄並存入 DB。
  - 輸出：成功重導至 `/auth/login`，失敗返回表單與錯誤訊息。
- **`/auth/login` (GET/POST)**
  - 輸入：表單包含 `email`, `password`
  - 邏輯：查詢 `User`，核對密碼，驗證成功後將 `user_id` 存入 session。
  - 輸出：成功重導至首頁 `/`，失敗返回表單與錯誤訊息。
- **`/auth/logout` (GET)**
  - 邏輯：清空 session 中的登入資訊。
  - 輸出：重導至首頁 `/`。

### Recipe 模組 (`recipe.py`)
- **`/` (GET)**
  - 邏輯：查詢最新或隨機推薦的 `Recipe` 列表。
  - 輸出：渲染 `recipe/index.html`。
- **`/recipes/search` (GET)**
  - 輸入：URL 參數 `q` (關鍵字)
  - 邏輯：依條件模糊搜尋 `Recipe.title` 或 `ingredients`。
  - 輸出：渲染 `recipe/search.html`。
- **`/recipes/<recipe_id>` (GET)**
  - 邏輯：透過 ID 取得 `Recipe` 實例，若不存在回傳 404，同時取得關聯的 `Review`。
  - 輸出：渲染 `recipe/detail.html`。
- **`/recipes/new` (GET/POST)**
  - 輸入：表單 `title`, `description`, `ingredients`, `steps`, `image_url`
  - 邏輯：需登入驗證。建立 `Recipe` 實例，設定 `author_id`，存入 DB。
  - 輸出：成功重導至該食譜詳情頁。
- **`/recipes/<recipe_id>/edit` (GET/POST)**
  - 邏輯：需登入且為作者本人。更新 `Recipe` 資料。
  - 輸出：成功重導至詳情頁。
- **`/recipes/<recipe_id>/delete` (POST)**
  - 邏輯：需登入且為作者本人。刪除 `Recipe` 及其關聯資料。
  - 輸出：重導至首頁或 `/profile`。

### User Action 模組 (`user_action.py`)
- **`/recipes/<recipe_id>/collect` (POST)**
  - 輸入：表單 `category` (可選)
  - 邏輯：需登入。建立 `Collection` 實例。
  - 輸出：重導至該食譜詳情頁。
- **`/recipes/<recipe_id>/review` (POST)**
  - 輸入：表單 `rating`, `comment`
  - 邏輯：需登入。建立 `Review` 實例。
  - 輸出：重導至該食譜詳情頁。
- **`/recipes/<recipe_id>/shopping-list` (POST)**
  - 邏輯：需登入。讀取食譜的 `ingredients` 轉換為陣列，建立 `ShoppingList` 實例。
  - 輸出：重導至 `/profile/shopping-list`。
- **`/profile` (GET)**
  - 邏輯：需登入。查詢該使用者的 `User` 資料，包含上傳的食譜與 `Collection`。
  - 輸出：渲染 `profile/index.html`。
- **`/profile/shopping-list` (GET)**
  - 邏輯：需登入。查詢使用者的 `ShoppingList`。
  - 輸出：渲染 `profile/shopping_list.html`。

## 3. Jinja2 模板清單

- **共用**
  - `templates/base.html`: 包含導覽列與共用資源。
- **Auth 模組** (皆繼承 `base.html`)
  - `templates/auth/login.html`: 登入表單。
  - `templates/auth/register.html`: 註冊表單。
- **Recipe 模組** (皆繼承 `base.html`)
  - `templates/recipe/index.html`: 首頁，顯示熱門/推薦食譜。
  - `templates/recipe/search.html`: 搜尋結果列表。
  - `templates/recipe/detail.html`: 單篇食譜完整內容（含評價留言區、加入收藏按鈕）。
  - `templates/recipe/new.html`: 新增食譜表單。
  - `templates/recipe/edit.html`: 編輯食譜表單。
- **Profile 模組** (皆繼承 `base.html`)
  - `templates/profile/index.html`: 個人檔案與收藏清單。
  - `templates/profile/shopping_list.html`: 購物清單瀏覽。
