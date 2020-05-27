import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)) + "/..")

ALLOWED_HOSTS = ["adfs-test.local.dev-gutools.co.uk","localhost"]

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

JWT_VALIDATION_KEY = """{put your signing certificate here}"""

JWT_EXPECTED_AUDIENCE = "{the value that the 'aud' field is set to by your token issuer. any other value is rejected}"
JWT_EXPECTED_ISSUER = "{the value that the 'iss' field is set to by your token issuer. any other value is rejected}"
