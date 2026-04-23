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
        new_recipe = cls(**kwargs)
        db.session.add(new_recipe)
        db.session.commit()
        return new_recipe

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, recipe_id):
        return cls.query.get(recipe_id)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Collection(db.Model):
    __tablename__ = 'collections'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    category = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @classmethod
    def create(cls, **kwargs):
        new_collection = cls(**kwargs)
        db.session.add(new_collection)
        db.session.commit()
        return new_collection

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, collection_id):
        return cls.query.get(collection_id)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
