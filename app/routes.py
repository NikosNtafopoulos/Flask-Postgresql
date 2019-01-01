from flask import render_template,request,redirect,url_for,flash
from app import app,db,bcrypt
from app.models import Client,UserInfo
from app.forms import ClientForm,ClientLoginForm
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
        # hash the password of the form
        hashed = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # create a new user/client instance with the form fields and commit to our database
        user = UserInfo(first_name=form.first_name.data,
                        last_name=form.last_name.data,email=form.email.data,
                        password=hashed)
        db.session.add(user)
        db.session.commit()
        flash(f'User {form.first_name.data} {form.last_name.data}has been created!You can now login in')
        return redirect(url_for('login'))
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
