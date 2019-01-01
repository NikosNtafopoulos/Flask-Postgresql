``Connecting Flask with postgresql on ubuntu 18.04``  
$ sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'   
$ sudo apt install wget ca-certificates  
$ wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -  
$ sudo apt update  
$ sudo apt install postgresql-10 pgadmin4   

``Access postgresql``   
$ sudo -i -u postgres   
$ psql		#to launch the postgres shell program  
postgres=# \du 				#shows actual users   
postgres=# \d client                   #database table's name


``generate a random secret key with python``  
Open your terminal and type 
``python3``  
```
import secrets
secrets.token_hex(16) 
```  
##SQL ALCHEMY
### Create a table through terminal
open the terminal and type ``python3``   
```
>>> from flask import Flask  
>>> from app import db
>>> db.create_all()
>>> from app import UserInfo
>>> user_1 = UserInfo(first_name="nik",last_name='test',email='test@test.com',password='password')
>>> db.session.add(user_1)
>>> db.session.commit()
```
### Query the database
TableName[model name].query.all()    
```
>>> UserInfo.query.all()
[UserInfo('User: nik test')]   
```
Get first User
```
>>> UserInfo.query.first()
```
Filter by [example: first_name]
```
>>> UserInfo.query.filter_by(username='nik').all() 
[UserInfo('User: nik test')]
>>> nik = UserInfo.query.filter_by(first_name='nik').first()
>>> nik.id
1
```
### Delete/Drop Table
db.drop_all() 

### Restructured the app to package
```
app/
   static/
   templates/
   __init__.py
   forms.py
   models.py
   routes.py
app.py
```
Accessing now through command line
```
>>> from app import db
>>> from app.models import Client,UserInfo
>>> user = UserInfo.query.all()

```
Import Bcrypt for hashing the passwords of our database
```
>>> from flask_bcrypt import Bcrypt
>>> bcrypt = Bcrypt()
>>> bcrypt.generate_password_hash('test')
b'$2b$12$qMfyqcJGnZLpr6a7uOpHtu755qzC1nrK9MpnTe8MRPSYd3aFIUIJO'
# to string
>>> bcrypt.generate_password_hash('test').decode('utf-8')
'$2b$12$gfvxz7AiqWZn11LdYIOrgeSOzkLsLrQAZr3CeES4MlOpZv.7I0zfW'
verify if true
>>> hashed = bcrypt.generate_password_hash('test').decode('utf-8')
>>> bcrypt.check_password_hash(hashed,'test')
True
```