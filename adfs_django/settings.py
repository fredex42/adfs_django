"""
Django settings for adfs_django project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ftd(j*7e+7g0s6gz+lu^q(9g71fw#sa6c(l+=t6-3n@rm^qd!1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["adfs-test.local.dev-gutools.co.uk"]


# Application definition

INSTALLED_APPS = [
    'django_saml2_auth',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'adfs_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["adfs_django/templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'adfs_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

SAML2_AUTH = {
    # Metadata is required, choose either remote url or local file path
    #'METADATA_AUTO_CONF_URL': '[The auto(dynamic) metadata configuration URL of SAML2]',
    'METADATA_LOCAL_FILE_PATH': './FederationMetadata.xml',

    # Optional settings below
    'DEFAULT_NEXT_URL': '/admin',  # Custom target redirect URL after the user get logged in. Default to /admin if not set.
    # This setting will be overwritten if you have parameter ?next= specificed in the login URL.
    'CREATE_USER': 'TRUE', # Create a new Django user when a new user logs in. Defaults to True.
    'NEW_USER_PROFILE': {
        'USER_GROUPS': [],  # The default group name when a new user logs in
        'ACTIVE_STATUS': True,  # The default active status for new users
        'STAFF_STATUS': True,  # The staff status for new users
        'SUPERUSER_STATUS': False,  # The superuser status for new users
    },
    'ATTRIBUTES_MAP': {  # Change Email/UserName/FirstName/LastName to corresponding SAML2 userprofile attributes.
        'email': 'email',
        'username': 'username',
        'first_name': 'first_name',
        'last_name': 'family_name',
        'job_title': 'job_title',
        'department': 'location',
    },
    # 'TRIGGER': {
    #     'CREATE_USER': 'path.to.your.new.user.hook.method',
    #     'BEFORE_LOGIN': 'path.to.your.login.hook.method',
    # },
    'ASSERTION_URL': 'https://adfs-test.local.dev-gutools.co.uk', # Custom URL to validate incoming SAML requests against
    'ENTITY_ID': 'https://adfs-test.local.dev-gutools.co.uk/saml2_auth/acs/', # Populates the Issuer element in authn request
    'NAME_ID_FORMAT': "None",  # Sets the Format property of authn NameIDPolicy element
    'USE_JWT': False, # Set this to True if you are running a Single Page Application (SPA) with Django Rest Framework (DRF), and are using JWT authentication to authorize client users
    'FRONTEND_URL': 'https://myfrontendclient.com', # Redirect URL for the client if you are using JWT auth with DRF. See explanation below
}

