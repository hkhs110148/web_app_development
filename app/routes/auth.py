from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from app.models.user import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """處理使用者註冊"""
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        if not username or not email or not password:
            flash('請填寫所有欄位', 'danger')
            return redirect(url_for('auth.register'))

        # 檢查 email 是否已存在
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('此電子郵件已被註冊', 'danger')
            return redirect(url_for('auth.register'))

        # 建立新使用者
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User.create(username=username, email=email, password_hash=hashed_password)
        
        if new_user:
            flash('註冊成功！請登入', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash('註冊失敗，請稍後再試', 'danger')

    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """處理使用者登入"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash('登入成功！', 'success')
            return redirect(url_for('recipe.index'))
        else:
            flash('電子郵件或密碼錯誤', 'danger')

    return render_template('auth/login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    """處理使用者登出"""
    logout_user()
    flash('您已成功登出', 'success')
    return redirect(url_for('recipe.index'))
