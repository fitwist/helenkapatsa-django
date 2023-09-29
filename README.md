- Запустим сервер: `python manage.py runserver`
- Посмотрим названия столбцов: `PRAGMA table_info(home_blog);`

Проект задеплоен на railway.app.

10|some text||niekontroliruiemoie-obuchieniie|2023-09-27|uncategorized|
id|html_article||slug|publication_date|category

0|sno|INTEGER|1||1
1|title|varchar(200)|1||0
2|meta|varchar(300)|1||0
3|content|TEXT|1||0
4|thumbnail_img|varchar(100)|0||0
5|slug|varchar(100)|1||0
6|time|date|1||0
7|category|varchar(255)|1||0
8|thumbnail_url|varchar(200)|0||0