REM create tables is needed, does not sync changes in models or deletions of models, always safe to run
python manage.py syncdb

python manage.py makemigrations
python manage.py migrate

REM run the server
python manage.py runserver 9000