if [ ! -d "survey" ] ;then
/usr/local/bin/python /usr/local/bin/django-admin  startproject survey 
fi
cd survey 
./manage.py makemigrations
./manage.py  migrate
./manage.py runserver 0:8100
