"""
Production settings for heroku
"""

import environ
# If using in your own prj, update the prj namespace below 
from website.settings.base_settings import *

env = environ.Env(
    # set casting, default value
    DEBUG = (bool, False)
)

# False if not in os.environ
DEBUG = env('DEBUG')

# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY =  env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# Parse db connection url strings
DATABASES = {
    # read os.environ['DATABASE_URL'] and raisesImproperlyConfigured exception
    'default': env.db(),
}