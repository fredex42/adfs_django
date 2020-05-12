import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)) + "/..")

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

# checkout the documentation for more settings
AUTH_ADFS = {
    "SERVER": "adfsdev.theguardian.com",
    "CLIENT_ID": "491711a1-e46b-4e8b-86ce-b0d4b1edc36a",
    "RELYING_PARTY_ID": "https://adfs-test.local.dev-gutools.co.uk/callback",
    # Make sure to read the documentation about the AUDIENCE setting
    # when you configured the identifier as a URL!
    "AUDIENCE": "https://adfs-test.local.dev-gutools.co.uk/callback",
    #"CA_BUNDLE": "mycert_chain.pem",
    "CLAIM_MAPPING": {"first_name": "given_name",
                      "last_name": "family_name",
                      "email": "email"},
}

# Configure django to redirect users to the right URL for login
LOGIN_URL = "django_auth_adfs:login"
LOGIN_REDIRECT_URL = "/"

ALLOWED_HOSTS = ["adfs-test.local.dev-gutools.co.uk"]

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

if os.path.isdir("/data"):
    dbpath = "/data/db.sqlite3"
else:
    dbpath = os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': dbpath,
    }
}
