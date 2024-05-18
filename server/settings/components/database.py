from server.settings.components import config
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(config('DATABASE_URL')).replace('sqlite://', ''),
    },
}
