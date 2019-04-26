
if [ ! -d "survey" ] ;then
/usr/local/bin/python /usr/local/bin/django-admin  startproject survey 
fi
cd survey 
./manage.py makemigrations --noinput
./manage.py  migrate
gunicorn --workers=2 --bind=0:8000  survey.wsgi
