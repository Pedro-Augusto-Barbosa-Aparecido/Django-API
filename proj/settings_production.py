DEBUG = False

ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ('127.0.0.1', 'localhost',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'store',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'store_db',
        'PORT': '5433'
    }
}
