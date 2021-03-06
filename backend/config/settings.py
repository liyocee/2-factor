import os
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Override in production via env
DEBUG = True
SECRET_KEY = 'p!ci1&ni8u98vvd#%18yp)aqh+m_8o565g*@!8@1wb$j#pj4d8'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': 'two_factor_db',
        'PASSWORD': '2@factor@db',
        'PORT': 5432,
        'USER': 'two_factor',
    }
}  # Env should have DATABASE_URL

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = 482
EMAIL_HOST_PASSWORD = 'no-passwd'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
ALLOWED_HOSTS = ['.2-factor.co.ke', '.localhost', '.emanager.co']
INSTALLED_APPS = (

    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.postgres',

    # libs
    'django_extensions',
    'django_filters',
    'djrill',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'oauth2_provider',
    'gunicorn',
    'corsheaders',
    'reversion',
    'rest_auth',
    'rest_auth.registration',
    'allauth',
    'allauth.account',
    'django_otp',
    'two_factor',
    'huey.djhuey'

)
LOCAL_APPS = (
    'api',
    'common',
    'users',
)
INSTALLED_APPS = LOCAL_APPS + INSTALLED_APPS
SITE_ID = 1
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    '.healthix.co.ke',
    'beyonic-api.healthix.co.ke',
    'beyonic.healthix.co.ke'

)
CORS_ALLOW_CREDENTIALS = True
CORS_PREFLIGHT_MAX_AGE = 172800
CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
)
CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken',
    'cache-control'
)
API_DOMAIN = '2factor-api.emanager.co'
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
AUTH_USER_MODEL = 'users.User'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Nairobi'
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = 'http://localhost:9000/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False  # Turn on in production
SWAGGER_SETTINGS = {
    'exclude_namespaces': [],
    'api_version': '0.1',
    'api_path': '/',
    'enabled_methods': [
        'get',
        'post',
        'put',
        'patch',
        'delete'
    ],
    'api_key': '228b67fadab69d86a8d7e49dc03ac8e2206yre22',
    'is_authenticated': True,
    'is_superuser': True,
    'permission_denied_handler': 'api.views.permission_denied_handler',
    'resource_access_handler': None,
    'base_path': 'localhost:8000',
    'info': {
        'contact': 'developers@2factor.co.ke',
        'description': 'Explore the 2-Factor v0.0.1 API',
        'title': '2-Factor V0.0.1 API',
    },
    'doc_expansion': 'none',
}
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.ScopedRateThrottle',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        # 'users.permissions.TwoFactorIsVerified',
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework_xml.parsers.XMLParser',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.JSONRenderer',
        'rest_framework_xml.renderers.XMLRenderer'
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': (
        'rest_framework.pagination.PageNumberPagination'),
    'PAGE_SIZE': 2,
    'PAGINATE_BY_PARAM': 'page_size',
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'TEST_REQUEST_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DATETIME_FORMAT': 'iso-8601',
    'DATE_FORMAT': 'iso-8601',
    'TIME_FORMAT': 'iso-8601'

}
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': os.path.join(BASE_DIR, '/common/templates/'),
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_EMAIL_SUBJECT_PREFIX = '[2-Factor]'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGOUT_REDIRECT_URL = '/api/'
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'email'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/api/v1/auth/login/'
API_LOGIN_URL = '/api/v1/auth/drf/login/'

# django_rest_auth settings
OLD_PASSWORD_FIELD_ENABLED = True
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'users.serializers.UserSerializer',
    'TOKEN_SERIALIZER': 'users.serializers.UserAuthTokenSerializer',
    'PASSWORD_RESET_SERIALIZER': (
        'users.serializers.UserPasswordResetSerializer'),
}

# Client origin to be allowed access
CLIENT_ORIGIN = 'http://localhost:8012'
DEFAULT_FROM_EMAIL = '2Factor <info@2factor.co.ke>'

# Mandrill settings
# This is the current api-key
API_ROOT = 'http://localhost:8061/api/v1'
MANDRILL_API_KEY = ''
EMAIL_BACKEND = 'djrill.mail.backends.djrill.DjrillBackend'
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
TASKS_LOG_FILE = 'error_logs.logs'
HUEY = {
    'backend': 'huey.backends.redis_backend',
    'name': 'two_factors_task_queue',
    'connection': {'host': REDIS_HOST, 'port': REDIS_PORT},
    'always_eager': False,
    'consumer_options': {'workers': 4, 'logfile': TASKS_LOG_FILE},
}
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

# two_factor settings
# TWO_FACTOR_SMS_GATEWAY = 'two_factor.gateways.twilio.gateway.Twilio'
TWO_FACTOR_SMS_GATEWAY = 'two_factor.gateways.fake.Fake'
TWO_FACTOR_TOTP_DIGITS = 6

# twilio settings
TWILIO_ACCOUNT_SID = ''
TWILIO_AUTH_TOKEN = ''
TWILIO_CALLER_ID = ''
