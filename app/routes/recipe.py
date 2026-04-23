from flask import Blueprint, render_template, request, redirect, url_for

recipe_bp = Blueprint('recipe', __name__)

@recipe_bp.route('/', methods=['GET'])
def index():
    """
    系統首頁：
    顯示推薦或最新的食譜列表，渲染 templates/recipe/index.html
    """
    pass

@recipe_bp.route('/recipes/search', methods=['GET'])
def search():
    """
    搜尋食譜：
    接收 URL 參數 (如 q=關鍵字)，查詢符合條件的食譜，渲染 templates/recipe/search.html
    """
    pass

@recipe_bp.route('/recipes/<int:recipe_id>', methods=['GET'])
def detail(recipe_id):
    """
    檢視食譜詳細內容：
    根據 ID 取得食譜及其評價與留言，渲染 templates/recipe/detail.html
    """
    pass

@recipe_bp.route('/recipes/new', methods=['GET', 'POST'])
def create_recipe():
    """
    新增食譜：
    需登入驗證。
    GET: 渲染新增表單 templates/recipe/new.html
    POST: 接收表單並建立 Recipe 紀錄，成功後重導至該食譜詳情頁
    """
    pass

@recipe_bp.route('/recipes/<int:recipe_id>/edit', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    """
    編輯食譜：
    需登入且為作者本人。
    GET: 渲染編輯表單 templates/recipe/edit.html
    POST: 更新 Recipe 資料，成功後重導至該食譜詳情頁
    """
    pass

@recipe_bp.route('/recipes/<int:recipe_id>/delete', methods=['POST'])
def delete_recipe(recipe_id):
    """
    刪除食譜：
    需登入且為作者本人。刪除 Recipe 及其關聯資料，重導至首頁或個人主頁
    """
    pass
