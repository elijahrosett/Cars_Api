# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(q-3wbyla7o&h+o%t35x#ik)r54=hjj&1tsxhsmn3ipt3-_$id'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}
