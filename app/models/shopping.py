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
        new_list = cls(**kwargs)
        db.session.add(new_list)
        db.session.commit()
        return new_list

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, list_id):
        return cls.query.get(list_id)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
