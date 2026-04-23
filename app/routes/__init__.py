from .auth import auth_bp
from .recipe import recipe_bp
from .user_action import user_action_bp

def register_blueprints(app):
    """註冊所有路由 Blueprint 到 Flask 應用程式"""
    app.register_blueprint(auth_bp)
    app.register_blueprint(recipe_bp)
    app.register_blueprint(user_action_bp)
