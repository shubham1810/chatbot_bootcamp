url: http://localhost:8000 or http://127.0.0.1:8000

url: http://localhost:8000/admin  or http://127.0.0.1:8000/admin

python manage.py startapp bot01

url: localhost:8000/bot/one
handler: (main).(bot).(one)

url: localhost:8000/bot/
	(main).(bot).($)


#username: shubham
#password: shubhamchatbot101

python manage.py showmigrations
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser


url w/ GET: localhost:8000/bot/?name=value&class=myclass&location=someloc

url: localhost:8000/bot/convert?temp=20


