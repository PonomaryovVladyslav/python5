DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'python7db',
        'USER': 'python7user',
        'PASSWORD': 'python7pass',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
