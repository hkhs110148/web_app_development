from . import db
from datetime import datetime

class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    ingredients = db.Column(db.Text, nullable=False)  # JSON format string expected
    steps = db.Column(db.Text, nullable=False)        # JSON format string expected
    image_url = db.Column(db.String(255))
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    collections = db.relationship('Collection', backref='recipe', lazy=True)
    reviews = db.relationship('Review', backref='recipe', lazy=True)

    @classmethod
    def create(cls, **kwargs):
        """新增一筆食譜記錄"""
        try:
            new_recipe = cls(**kwargs)
            db.session.add(new_recipe)
            db.session.commit()
            return new_recipe
        except Exception as e:
            db.session.rollback()
            print(f"Error creating recipe: {e}")
            return None

    @classmethod
    def get_all(cls):
        """取得所有食譜記錄"""
        try:
            return cls.query.all()
        except Exception as e:
            print(f"Error getting all recipes: {e}")
            return []

    @classmethod
    def get_by_id(cls, recipe_id):
        """取得單筆食譜記錄"""
        try:
            return cls.query.get(recipe_id)
        except Exception as e:
            print(f"Error getting recipe by id: {e}")
            return None

    def update(self, **kwargs):
        """更新食譜記錄"""
        try:
            for key, value in kwargs.items():
                setattr(self, key, value)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error updating recipe: {e}")
            return False

    def delete(self):
        """刪除食譜記錄"""
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error deleting recipe: {e}")
            return False

class Collection(db.Model):
    __tablename__ = 'collections'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    category = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @classmethod
    def create(cls, **kwargs):
        """新增一筆收藏記錄"""
        try:
            new_collection = cls(**kwargs)
            db.session.add(new_collection)
            db.session.commit()
            return new_collection
        except Exception as e:
            db.session.rollback()
            print(f"Error creating collection: {e}")
            return None

    @classmethod
    def get_all(cls):
        """取得所有收藏記錄"""
        try:
            return cls.query.all()
        except Exception as e:
            print(f"Error getting all collections: {e}")
            return []

    @classmethod
    def get_by_id(cls, collection_id):
        """取得單筆收藏記錄"""
        try:
            return cls.query.get(collection_id)
        except Exception as e:
            print(f"Error getting collection by id: {e}")
            return None

    def update(self, **kwargs):
        """更新收藏記錄"""
        try:
            for key, value in kwargs.items():
                setattr(self, key, value)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error updating collection: {e}")
            return False

    def delete(self):
        """刪除收藏記錄"""
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error deleting collection: {e}")
            return False
