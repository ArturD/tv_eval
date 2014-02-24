Evaluator tool for tv api
=========================

```bash
# clone repository
git clone https://github.com/ArturD/tv_eval
cd tv_eval

# setup virtual env and install dependencies
virtualenv ENV
source ENV/bin/activate
pip install -r REQUIREMENTS.txt

#setup database
cd app
python manage.py syncdb # you'll be prompted for admin account
python manage.py migrate # run south migrations

# import 100 queries from file
python manage.py import ~/Pobrane/series_episode_us.txt 100
# evaluate imported queries
python manage.py eval "http://www.wikia.com/api/test/Tv/Episode"
python manage.py runserver
# open http://localhost:8000/ in browser
```


