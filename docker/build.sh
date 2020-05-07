#!/bin/bash -e

if [ -f adfs_django.tar ]; then rm -f adfs_django.tar; fi
if [ -f requirements.txt ]; then rm -f requirements.txt; fi

if [ ! -f ../static/js/bundle.js ]; then
  echo "bundle.js not found. Please run \'npm run build\' from the frontend directory before running"
  echo "this script."
  exit 1
fi

tar cv --exclude __pycache__ ../adfs_django ../static ../requirements.txt ../manage.py > adfs_django.tar
cp ../requirements.txt .

docker build . -t andyg42/adfs_django