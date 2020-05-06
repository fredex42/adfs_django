FROM python:3.7-alpine

ADD adfs_django.tar /opt/adfs_django
#annoying, but until my Mac gets upgraded to support later Docker I can't use chown :(
RUN chown -R nobody /opt/adfs_django
ENV PYTHONPATH=/opt/adfs_django
RUN apk add --no-cache alpine-sdk linux-headers libffi libffi-dev openssl-dev xmlsec-dev && pip install uwsgi && cd /opt/adfs_django; pip install -r requirements.txt && apk --no-cache del alpine-sdk linux-headers libffi-dev
WORKDIR /opt/adfs_django
USER nobody
CMD uwsgi --http :9000 --enable-threads --static-map /static=/opt/adfs_django/static --module adfs_django.wsgi