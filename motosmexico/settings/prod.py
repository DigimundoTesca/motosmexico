from motosmexico.settings.develop import *

DEBUG = False

# ALLOWED_HOSTS = ['motosmexico.digimundo.com.mx', 'motosmexico-env-dev.us-west-2.elasticbenstalk.com']
ALLOWED_HOSTS = ['*']

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('MOTOS_MEXICO_DB_NAME'),
        'USER': os.getenv('MOTOS_MEXICO_DB_USER'),
        'PASSWORD': os.getenv('MOTOS_MEXICO_DB_PASSWORD'),
        'HOST': os.getenv('MOTOS_MEXICO_DB_HOST'),
        'PORT': os.getenv('MOTOS_MEXICO_DB_PORT'),
    }
}
