from flask import Blueprint, render_template, request, redirect, url_for

user_action_bp = Blueprint('user_action', __name__)

@user_action_bp.route('/recipes/<int:recipe_id>/collect', methods=['POST'])
def collect_recipe(recipe_id):
    """
    收藏食譜：
    需登入。將指定的食譜加入使用者的 Collection 中，重導至該食譜詳情頁
    """
    pass

@user_action_bp.route('/recipes/<int:recipe_id>/review', methods=['POST'])
def add_review(recipe_id):
    """
    提交食譜評價與留言：
    需登入。接收評分與留言內容，建立 Review 紀錄，重導至該食譜詳情頁
    """
    pass

@user_action_bp.route('/recipes/<int:recipe_id>/shopping-list', methods=['POST'])
def generate_shopping_list(recipe_id):
    """
    從食譜產生購物清單：
    需登入。將該食譜的食材明細建立為 ShoppingList 紀錄，重導至 /profile/shopping-list
    """
    pass

@user_action_bp.route('/profile', methods=['GET'])
def profile_index():
    """
    個人主頁：
    需登入。顯示個人資料、自己上傳的食譜與收藏的食譜列表，渲染 templates/profile/index.html
    """
    pass

@user_action_bp.route('/profile/shopping-list', methods=['GET'])
def view_shopping_list():
    """
    檢視購物清單：
    需登入。顯示使用者所有的購物清單，渲染 templates/profile/shopping_list.html
    """
    pass
