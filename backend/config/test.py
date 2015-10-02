from settings import *  # NOQa
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': 'two_factor_test_db',
        'PASSWORD': '2@factor@db',
        'PORT': 5432,
        'USER': 'two_factor',
    }
}
