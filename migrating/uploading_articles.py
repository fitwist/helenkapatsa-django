# -*- coding: utf-8 -*-
import json
import sqlite3

conn = sqlite3.connect("db.sqlite3")

with open('/Users/elenakapatsa/Repositories/django-tailwind-blog/articles.json', 'r') as json_file:
    data = json.load(json_file)
    for item in data:
        conn.execute("INSERT INTO home_blog (sno, title, meta, content, thumbnail_img, slug, time, category, thumbnail_url) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (item["sno"], item["title"], item["meta"], item["content"], item["thumbnail_img"], item["slug"], item["time"], item["category"], item["thumbnail_url"]))

conn.commit()
conn.close()