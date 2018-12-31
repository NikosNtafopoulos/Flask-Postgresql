from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://test:test@localhost/test'
db = SQLAlchemy(app)
#DB_USER:PASSWORD@HOST/DATABASE

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=True)
    last_name = db.Column(db.String(100), unique=True)

    def __init__(self, first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return '{}  {}'.format(self.first_name, self.last_name)
#routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add')
def add():
    return render_template('add.html')

#post
@app.route('/post_user',methods=['POST'])
def post_user():
    user = Client(request.form['first_name'],request.form['last_name'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))

if __name__== "__main__":
    app.run(debug=True)