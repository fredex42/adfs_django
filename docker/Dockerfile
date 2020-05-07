FROM python:3.7-alpine

COPY requirements.txt /opt/adfs_django/requirements.txt
#mailcap is needed for mime.types used by uwsgi. libffi, openssl and xmlsec are used by django saml. dev packages are uninstalled as soon as the have been used.
RUN apk add --no-cache alpine-sdk linux-headers libffi libffi-dev openssl-dev xmlsec-dev mailcap && pip install uwsgi==2.0.18 && cd /opt/adfs_django; pip install -r requirements.txt && apk --no-cache del alpine-sdk linux-headers libffi-dev

ADD adfs_django.tar /opt/adfs_django
#annoying, but until my Mac gets upgraded to support later Docker I can't use chown :(
RUN chown -R nobody /opt/adfs_django
ENV PYTHONPATH=/opt/adfs_django
WORKDIR /opt/adfs_django
USER nobody
CMD uwsgi --http :9000 --enable-threads --static-map /static=/opt/adfs_django/static --offload-threads 1 --module adfs_django.wsgi