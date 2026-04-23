from . import db
from datetime import datetime

class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @classmethod
    def create(cls, **kwargs):
        """新增一筆評價與留言記錄"""
        try:
            new_review = cls(**kwargs)
            db.session.add(new_review)
            db.session.commit()
            return new_review
        except Exception as e:
            db.session.rollback()
            print(f"Error creating review: {e}")
            return None

    @classmethod
    def get_all(cls):
        """取得所有評價記錄"""
        try:
            return cls.query.all()
        except Exception as e:
            print(f"Error getting all reviews: {e}")
            return []

    @classmethod
    def get_by_id(cls, review_id):
        """取得單筆評價記錄"""
        try:
            return cls.query.get(review_id)
        except Exception as e:
            print(f"Error getting review by id: {e}")
            return None

    def update(self, **kwargs):
        """更新評價記錄"""
        try:
            for key, value in kwargs.items():
                setattr(self, key, value)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error updating review: {e}")
            return False

    def delete(self):
        """刪除評價記錄"""
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error deleting review: {e}")
            return False
