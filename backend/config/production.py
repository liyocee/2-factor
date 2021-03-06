import os
from .settings import *  # NOQA
DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        "NAME": os.getenv("DATABASE_NAME"),
        "USER": os.getenv("DATABASE_USER"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "HOST": "localhost",
        "PORT": 5432,
    }
}
STATIC_ROOT = os.getenv("STATIC_ROOT")
MEDIA_ROOT = os.getenv("MEDIA_ROOT")
MEDIA_URL = os.getenv("MEDIA_URL")
DEBUG = TEMPLATE_DEBUG = os.getenv("DEBUG", "false") == "true"
DEBUG = True
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
SWAGGER_SETTINGS = {
    'exclude_namespaces': SWAGGER_SETTINGS.get('exclude_namespaces'),
    'api_version': SWAGGER_SETTINGS.get('api_version'),
    'api_path': SWAGGER_SETTINGS.get('api_path'),
    'enabled_methods': SWAGGER_SETTINGS.get('enabled_methods'),
    'api_key': SWAGGER_SETTINGS.get('api_key'),
    'is_authenticated': True,
    'is_superuser': True,
    'permission_denied_handler': SWAGGER_SETTINGS.get(
        'permission_denied_handler'),
    'resource_access_handler': SWAGGER_SETTINGS.get('resource_access_handler'),
    'base_path': API_DOMAIN,
    'info': SWAGGER_SETTINGS.get('info'),
    'doc_expansion': SWAGGER_SETTINGS.get('doc_expansion'),
}
MANDRILL_API_KEY = os.getenv('MANDRILL_API_KEY')
TWO_FACTOR_SMS_GATEWAY = 'two_factor.gateways.twilio.gateway.Twilio'
TWO_FACTOR_SMS_GATEWAY = 'two_factor.gateways.fake.Fake'
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_CALLER_ID = os.getenv('TWILIO_CALLER_ID')
EMAIL_VERIFY_UI_LINK = os.getenv('FRONTEND_DOMAIN')+'/users/verify'
TASKS_LOG_FILE = os.getenv('TASKS_LOG_FILE')
HUEY = {
    'backend': 'huey.backends.redis_backend',
    'name': 'two_factors_task_queue',
    'connection': {
        'host': os.getenv("REDIS_HOST"), 'port': os.getenv("REDIS_PORT")
    },
    'always_eager': False,
    'consumer_options': {'workers': 4},
}
API_DOMAIN = 'beyonic-api.healthix.co.ke'
