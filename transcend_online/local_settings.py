# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '<your secret key>'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

#DATABASES = {
#	'default': {
#		'ENGINE': 'django.db.backends.postgresql',
#		'NAME': 'transcend_online',
#		'USER': 'postgres',
#		'PASSWORD': 'Blueprint06!',
#		'HOST': 'transcend-online.cipyjxysyrgm.eu-west-2.rds.amazonaws.com',
#	}
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST =''
EMAIL_HOST_USER =''
EMAIL_HOST_PASSWORD =''
EMAIL_PORT =''
EMAIL_USE_SSL =''
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

STRIPE_TEST_PUBLISHABLE_KEY='pk_live_51LscRDCYNl15EF6b4TGZJkLU6BizC3NgP4J5N6A0dcvep4UZ2DEdYOunW6vZnGl9v00r3T8WCEMBLXVcnyhgOebW00sn2xoY5H'
STRIPE_TEST_SECRET_KEY='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'
