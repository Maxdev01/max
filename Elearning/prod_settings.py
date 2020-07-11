
import django_heroku
import dj_database_url

DEBUG = True

ALLOWED_HOSTS = ['*']

SECRET_KEY = 'p4z@ln+4gcf09et8ji-_9wua#xob$r2k158ckjyelhpd8b+a)n'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'idel',
        'USER': 'name',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

django_heroku.settings(locals())
