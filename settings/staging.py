from base import *
 
DEBUG = False
 
# Load the ClearDB connection details from the environment variable
DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}
 
# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_huXVMABXPzJmtBClroUo7vFA')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_qgkn8rHXvHGEtPaqreOCeXi7')
 
 
SITE_URL = 'https://motorholics-app.herokuapp.com'
ALLOWED_HOSTS.append('motorholics-app.herokuapp.com')
 
 
# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}