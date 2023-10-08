#!/bin/bash
apt-get update; apt-get install -y git python3 python3-pip python3-venv;
git clone https://github.com/fitwist/django-tailwind-blog ;
cd django-tailwind-blog/;
python3 -m venv env;
source env/bin/activate;
python3 -m pip install -r requirements.txt;
deactivate;
cp deploy/blog_app_server.service  /etc/systemd/system/;
systemctl daemon-reload;
systemctl start blog_app_server;
systemctl enable blog_app_server;




