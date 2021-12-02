# PrepliteBackend

The backend of our app runs on Django. We make use of django in combination with the sqlite3 database.

Installation steps

git clone <url>
cd PrepliteBackend
virtualenv env
. env/bin/activate
cd Preplite
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
