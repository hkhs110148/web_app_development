from . import db
from datetime import datetime
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    recipes = db.relationship('Recipe', backref='author', lazy=True)
    collections = db.relationship('Collection', backref='user', lazy=True)
    reviews = db.relationship('Review', backref='user', lazy=True)
    shopping_lists = db.relationship('ShoppingList', backref='user', lazy=True)

    @classmethod
    def create(cls, **kwargs):
        """新增一筆使用者記錄"""
        try:
            new_user = cls(**kwargs)
            db.session.add(new_user)
            db.session.commit()
            return new_user
        except Exception as e:
            db.session.rollback()
            print(f"Error creating user: {e}")
            return None

    @classmethod
    def get_all(cls):
        """取得所有使用者記錄"""
        try:
            return cls.query.all()
        except Exception as e:
            print(f"Error getting all users: {e}")
            return []

    @classmethod
    def get_by_id(cls, user_id):
        """取得單筆使用者記錄"""
        try:
            return cls.query.get(user_id)
        except Exception as e:
            print(f"Error getting user by id: {e}")
            return None

    def update(self, **kwargs):
        """更新使用者記錄"""
        try:
            for key, value in kwargs.items():
                setattr(self, key, value)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error updating user: {e}")
            return False

    def delete(self):
        """刪除使用者記錄"""
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error deleting user: {e}")
            return False
