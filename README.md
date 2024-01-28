- Запустим сервер: `python manage.py runserver`
- Посмотрим названия столбцов: `PRAGMA table_info(home_blog);`
- Подключимся к VPS: `ssh root@194.87.235.26`, `31GBSorbB5`

## Запуск базы в докере

```bash
docker run -d   --name postgres-container   -e POSTGRES_USER=postgres   -e POSTGRES_PASSWORD=blog_app_password   -e POSTGRES_DB=railway   -p 5435:5432   postgres:latest
```

## Создание дампа продакшн базы

```bash
pg_dump -U postgres -h pghost -p pgport -d railway -f blog_app_dump.sql
```

Значения переменных `pghost` и `pgport` можно посмотреть в railway в настройках сервиса `postgres` на странице `connect`

##  Развертка дампа в тестовой БД

```bash
psql -h phhost -p pgport -U postgres -d railway -a -f blog_app_dump.sql
```


## Перенос базы с sqlite на psql

1. Установить утилиту `pgloader`
 - Debian
    ```bash
    sudo apt-get install pgloader
    ```
 - Arch
    ```bash
    packer -S pgloader
    ```
2. Отредактировать в скрипте переноса `db_tools/pg_load.script` путь к litesql базе данных (требуется полный путь), а также реквезиты доступа к базе данных postgresql

3. Запустить скрипт переноса
```bash
pgloader ./db_tools/pg_load.script
```


## Деплой на VDS
1. Процесс установки на "голой" машине описан в `deploy/install.sh`
2. Конфигурация деплоя:
   - сервер на gunicorn, конфиг-файл в `deploy/gunicorn_config.py`
   - демон (сервис) на systemd, конфигурация в `deploy/blog_app_server.service`, на сервере размещен в `/etc/systemd/system/blog_app_server.service`
   - конфиг доступа к базе должен лежать в файле `.env`. Пример содержимого можно найти в `.env_sample`
   - На сервере используется сертификат `letsencrypt`. Сертификат лежит в `/etc/letsencrypt/live/helenkapatsa.ru `(путь по умолчанию). Необходимо помнить, что при настроеном `cloudflare` пользователь видит сертификат `cloudflare`, а не `letsencrypt`
   - запуск осуществляется посредством скрипта `deploy/run.sh`, который активирует окружение из `.env` файла
3. CI настроен на основе ssh. Хост и ключи доступа заданы в github environment `ci`, в secrets

# Обновление SSL-сертификата
`certbot certonly --standalone --preferred-challenges http -d helenkapatsa.ru`