import dj_database_url
from ouragan_opp.settings import *

DEBUG = False
TEMPLATE_DEBUG = False

DATABASES['default'] = dj_database_url.config()

SECRET_KEY = 's0=lzz&l0xdp!8+)hf6_1me7f0mx(h42yr_tq59i=8n_4i25&h'

ALLOWED_HOSTS = ['ouragan.herokuapp.com']
