from flask import Flask
from config import Config
from flask_login import LoginManager
import os

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = "請先登入以訪問此頁面"
login_manager.login_message_category = "danger"

@login_manager.user_loader
def load_user(user_id):
    from app.models.user import User
    return User.get_by_id(int(user_id))

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 確保 instance 資料夾存在
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # 初始化擴展套件
    from app.models import db
    db.init_app(app)
    login_manager.init_app(app)

    # 註冊路由 Blueprints
    from app.routes import register_blueprints
    register_blueprints(app)

    return app

def init_db():
    """初始化資料庫與資料表"""
    app = create_app()
    with app.app_context():
        from app.models import db
        db.create_all()
        print("Database initialized successfully.")
