from flask import Blueprint, render_template, request, redirect, url_for

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    處理使用者註冊：
    GET: 渲染註冊表單 templates/auth/register.html
    POST: 接收表單資料，建立 User 紀錄，成功後重導至登入頁或首頁
    """
    pass

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    處理使用者登入：
    GET: 渲染登入表單 templates/auth/login.html
    POST: 驗證帳號密碼，設定 session，成功後重導至首頁
    """
    pass

@auth_bp.route('/logout')
def logout():
    """
    處理使用者登出：
    清空 session，重導至首頁
    """
    pass
