if [ ! -d survey ] ; then 
ng new survey --defaults=true
fi
cd survey
npm install
ng serve --host 0.0.0.0
#ng build --prod --output-path /usr/src/app/django/survey/static/angular --watch --output-hashing none
