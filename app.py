from flask import Flask,render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from forms import ClientForm,ClientLoginForm
from datetime import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://test:test@localhost/test'
#security for modified cookies,sessions etc
app.config['SECRET_KEY']= '8810fc810e8c15c03186e3cbb695fb92'
db = SQLAlchemy(app)
#DB_USER:PASSWORD@HOST/DATABASE

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

#routes
@app.route('/')
def index():
    return render_template('index.html')

# Render the html form
@app.route('/add')
def add():
    return render_template('add.html')

# Post route to database from the html form
@app.route('/post_user',methods=['POST'])
def post_user():
    user = Client(request.form['first_name'],request.form['last_name'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))

'''
    ROUTES FROM forms.py
    python forms with classes and templating
'''
@app.route('/register',methods=['GET','POST'])
def register():
    form = ClientForm()
    if form.validate_on_submit():
        flash(f'User {form.first_name.data} {form.last_name.data}has been created')
        return redirect(url_for('index'))
    else:
        flash('Failed')
    return render_template('register.html',form=form)

#login route
@app.route('/login',methods=['GET','POST'])
def login():
    form = ClientLoginForm()
    if form.validate_on_submit():
        flash('Welcome')
        return redirect(url_for('index'))
    else:
        flash('Login Unsuccessful')
    return render_template('login.html',form=form)


if __name__== "__main__":
    app.run(debug=True)