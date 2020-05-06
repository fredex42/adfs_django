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

if os.path.isdir("/data"):
    fedpath = "/data"
else:
    fedpath = BASE_DIR

SAML2_AUTH = {
    # Metadata is required, choose either remote url or local file path
    #'METADATA_AUTO_CONF_URL': '[The auto(dynamic) metadata configuration URL of SAML2]',
    'METADATA_LOCAL_FILE_PATH': os.path.join(fedpath, "FederationMetadata.xml"),

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
    'USE_JWT': True, # Set this to True if you are running a Single Page Application (SPA) with Django Rest Framework (DRF), and are using JWT authentication to authorize client users
    'FRONTEND_URL': 'https://adfs-test.local.dev-gutools.co.uk/logged_in', # Redirect URL for the client if you are using JWT auth with DRF.
    #If USE_JWT is True then post-auth a GET request is made to FRONTEND_URL with the JWT as the token= query parameter and the SSO index as uid= parameter
}

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
