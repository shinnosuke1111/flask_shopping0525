from lib.db import db

class TestItem(db.Model):
    
    __tablename__ = 'test_items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    def __init__(self, category_id, name, price):
        self.name = name
        self.price = price