#!/bin/bash
#install packages
apt-get update; apt-get install -y git python3 python3-pip python3-venv software-properties-common;

#getting letsencrypt sertificate
python3 -m pip install certbot
#user actions required
certbot certonly --standalone --preferred-challenges http -d helenkapatsa.ru
SLEEPTIME=$(awk 'BEGIN{srand(); print int(rand()*(3600+1))}'); echo "0 0,12 * * * root sleep $SLEEPTIME && certbot renew -q" | sudo tee -a /etc/crontab > /dev/null

#getting and setup project
git clone https://github.com/fitwist/django-tailwind-blog ;
cd django-tailwind-blog/;
python3 -m venv env;
source env/bin/activate;
python3 -m pip install -r requirements.txt;
deactivate;

#setup systemd
cp deploy/blog_app_server.service  /etc/systemd/system/;
systemctl daemon-reload;
systemctl start blog_app_server;
systemctl enable blog_app_server;



