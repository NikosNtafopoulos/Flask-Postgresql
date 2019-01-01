from datetime import datetime
from app import db
#from __main__ import db for the error
# DB MODEL
# Test model table for route /post_user with html inputs
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=True)
    last_name = db.Column(db.String(100), unique=True)

    def __init__(self, first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return '{}  {}'.format(self.first_name, self.last_name)

# test table for id,firstName,lastName,image,email,password,dateCreated
class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=True)
    last_name = db.Column(db.String(100), unique=True)
    image = db.Column(db.String(20), nullable=False,default='default.jpg')
    email = db.Column(db.String(30), unique=True,nullable=False)
    password = db.Column(db.String(100), unique=True, nullable=False)
    date_created = db.Column(db.DateTime,nullable=False,default=datetime.utcnow())

    def __repr__(self):
        return f"UserInfo('User: {self.first_name} {self.last_name}')"
