from lib.db import db

class TestCategory(db.Model):

    __tablename__ = 'test_categorys'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, name):
        self.name = name
