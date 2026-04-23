from . import db
from datetime import datetime

class ShoppingList(db.Model):
    __tablename__ = 'shopping_lists'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'))
    items = db.Column(db.Text, nullable=False)  # JSON format string expected
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @classmethod
    def create(cls, **kwargs):
        """新增一筆購物清單記錄"""
        try:
            new_list = cls(**kwargs)
            db.session.add(new_list)
            db.session.commit()
            return new_list
        except Exception as e:
            db.session.rollback()
            print(f"Error creating shopping list: {e}")
            return None

    @classmethod
    def get_all(cls):
        """取得所有購物清單記錄"""
        try:
            return cls.query.all()
        except Exception as e:
            print(f"Error getting all shopping lists: {e}")
            return []

    @classmethod
    def get_by_id(cls, list_id):
        """取得單筆購物清單記錄"""
        try:
            return cls.query.get(list_id)
        except Exception as e:
            print(f"Error getting shopping list by id: {e}")
            return None

    def update(self, **kwargs):
        """更新購物清單記錄"""
        try:
            for key, value in kwargs.items():
                setattr(self, key, value)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error updating shopping list: {e}")
            return False

    def delete(self):
        """刪除購物清單記錄"""
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error deleting shopping list: {e}")
            return False
