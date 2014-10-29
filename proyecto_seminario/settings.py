"""
Django settings for proyecto_seminario project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
RUTA_PROYECTO = os.path.dirname(os.path.realpath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vv2rr*ow1_x0(y%#$z*!yi4s_79pq7+k^7*$l+u=_lnx7&@7)1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'proyecto_seminario.apps.usuarios',
    'proyecto_seminario.apps.preguntas',
    'social_auth',
    'captcha',
    'recaptcha.client',
)

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',  
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'proyecto_seminario.urls'

WSGI_APPLICATION = 'proyecto_seminario.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-la'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
TEMPLATE_DIRS = (os.path.join(RUTA_PROYECTO,"plantilla"),)
STATICFILES_DIRS = (os.path.join(RUTA_PROYECTO,"static"),)
MEDIA_ROOT = os.path.join(RUTA_PROYECTO,"media")
ADMIN_MEDIA_PREFIX='/media/'
TEMPLATE_CONTEXT_PROCESSORS = (
    #'django.core.context_processors.auth',
    #'django.core.context_procesors.media',
    'django.contrib.auth.context_processors.auth',
    )
# TEMPLATE_CONTEXT_PROCESSORS = (
#     'social.apps.django_app.context_processors.backends',
#     'social.apps.django_app.context_processors.login_redirect',
#     'social.apps.django_app.context_processors.auth',
# )

# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
#     'social.backends.google.GoogleOAuth2',
# )

# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '773108400456-hm304tnee3um42ah91nac68cj6thsvni.apps.googleusercontent.com'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'DImo3fG3qQ02Nrr41Joiy2xa'

# SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/https://www.example.com/oauth2callback/'

# WHITELISTED_DOMAINS = ['axiacore.com','gmail.com','hotmail.com']

# SOCIAL_AUTH_PIPELINE=(
#     'social.pipeline.social_auth.social_details',
#     'social.pipeline.social_auth.social_uid',
#     'social.pipeline.social_auth.auth_allowed',
#     'social.pipeline.social_auth.social_user',
#     'social.pipeline.user.get_username',
#     'social.pipeline.user.create_user',
#     'social.pipeline.social_auth.associate_user',
#     'social.pipeline.social_auth.load_extra_data',
#     'scial.pipeline.user.user_detalls',
# )

GOOGLE_OAUTH2_CLIENT_ID = ''

GOOGLE_OAUTH2_CLIENT_SECRET = ''

FACEBOOK_APP_ID = '539064209560004'

FACEBOOK_API_SECRET = '0a3b9982fc38723714affd8d62409000'

ACCOUNT_ACTIVATION_DAYS=7

FACEBOOK_EXTENDED_PERMISSIONS = ['email']

LOGIN_REDIRECT_URL = '/'

LOGIN_URL = '/account/login/'

LOGIN_REDIRECT_URL = '/account/post_login/'

#<<<<<<< HEAD
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

#=======
#>>>>>>> 0ba6c164108dc57261780eee9b573dcc26bbea9e



