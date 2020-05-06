# adfs-django

Proof of concept for Django authenticating against ADFS via django_saml2_auth

This is a simple project that authorizes both a django view and a REST endpoint (via a JWT auth token)

## Setting it up (local dev run)

You need to obtain the federation metadata from the ADFS server as an XML file and save it locally.
Update `config/__init__.py` to point to the location of the file.

### 1. Build the frontend
Make sure you have a recent node.js installed.

```
$ cd frontend/
$ npm i
$ npm run dev   #start up in dev mode, this monitors the files and does not optimize. run build for a "production" build
```

### 2. Standard django setup
Set up a python virtualenv:
```
$ virtualenv -p python3.7 venv/
$ source venv/bin/activate
(venv) $
```

Install requirements:
```
(venv) $ pip install -r requirements.txt
```

Run the dev server:
```
(venv) $ ./manage.py runserver 0.0.0.0:9000
```

### 3. Configure reverse proxy
Authentication requires an https url. The easiest way to provide this from a dev setup is to configure nginx to provide
a reverse proxy.

1. First, install nginx.
See `nginx-snippet.conf` for sample server blocks for the nginx configuration.  Remove any server {} blocks already there
and replace them.  The sample configures the hostname to be `myhost.local`, change this as you want.
Make sure you update ALLOWED_HOSTS in `settings.py` or `config/__init__.py` to reflect the hostname you want.

2. Next, you need an https certificate.  The easiest way to get this is to install https://github.com/FiloSottile/mkcert.
Set it up as described in the README and generate your certificate by running `mkcert myhost.local` (replace myhost.local)
with the hostname you chose above.
Put the certificate and key into the nginx config directory and check that the filenames are correctly specified
 in the configuration.

3. Start up or restart nginx. It should now be configured to https terminate and redirect traffic from https://myhost.local
to localhost:9000 (the dev server).

### 4. Configure ADFS

In your ADFS configuration, you need to configure a "Relaying Party".  Use the URL as the identifier: 
`https://myhost.local/saml2_auth/acs/`.  You want an HTTP POST binding. The URL does not have to be resolvable from
the ADFS server.

[TODO: add in other steps!]

Once that is sorted out, then you need to get hold of the federation metadata, either as a URL or as the full XML file.
Either put the URL or path to locally downloaded XML file into the configuration at `adfs_django/config/__init__.py`.

Then re-run the dev server.

You should now be able to access `https://myhost.local` (or whatever you specified instead) and get redirected out
to ADFS for authentication and then bounced back again.

## Setting it up (Docker run)
