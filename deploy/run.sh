#!/bin/bash
ROOT_DIR=/root/django-tailwind-blog
cd $ROOT_DIR;
eval $(cat ./.env)  ./env/bin/gunicorn -c ./deploy/gunicorn_config.py blogApp.wsgi
