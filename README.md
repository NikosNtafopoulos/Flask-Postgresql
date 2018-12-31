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
