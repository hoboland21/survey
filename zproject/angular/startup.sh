if [ ! -d survey ] ; then 
ng new survey --defaults=true
fi
cd survey
npm install
ng build --prod --output-path /usr/src/app/django/survey/static/ang/main  --watch --output-hashing none
#ng serve --host 0.0.0.0
