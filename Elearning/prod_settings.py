from Elearning.settings import *
import django_heroku
import dj_database_url as dj

DEBUG = False
TEMPLATTE_DEBUG = False
ALLOWED_HOSTS = ['.herokuapp.com']

SECRET_KEY = 'p4z@ln+4gcf09et8ji-_9wua#xob$r2k158ckjyelhpd8b+a)n'




DATABASES['default'] = dj.config(conn_max_age=600)
django_heroku.settings(locals())
