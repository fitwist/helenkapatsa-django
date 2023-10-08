command = '/root/django-tailwind-blog/env/bin/gunicorn'

pythonpath = '/root/django-tailwind-blog/env/bin/python3'

bind = '0.0.0.0:80'

workers = 4

certfile='/etc/letsencrypt/live/helenkapatsa.ru/fullchain.pem'
keyfile='/etc/letsencrypt/live/helenkapatsa.ru/privkey.pem'
