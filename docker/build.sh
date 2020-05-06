#!/bin/bash

if [ -f adfs_django.tar ]; then rm -f adfs_django.tar; fi

tar cv --exclude __pycache__ ../adfs_django ../static ../requirements.txt ../manage.py > adfs_django.tar

docker build . -t andyg42/adfs_django