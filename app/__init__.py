from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://test:test@localhost/test'
#security for modified cookies,sessions etc
app.config['SECRET_KEY']= '8810fc810e8c15c03186e3cbb695fb92'
db = SQLAlchemy(app)
#DB_USER:PASSWORD@HOST/DATABASE
bcrypt = Bcrypt(app)

#routes
from app import routes