import json
from datetime import datetime

with open('/Users/elenakapatsa/Repositories/django-tailwind-blog/modya-export-2023-09-27.json') as json_file:
    data = json.load(json_file)


i = 0
articles = []

for i in range(len(data['db'][0]['data']['posts'])):
    sno = i + 11
    title = data['db'][0]['data']['posts'][i]['title']
    meta = ''
    content = data['db'][0]['data']['posts'][i]['html']
    thumbnail_img = ''
    slug = data['db'][0]['data']['posts'][i]['slug']
    try:
        time_obj = data['db'][0]['data']['posts'][i]['published_at']
        print(time_obj)
        date_obj = datetime.strptime(time_obj, '%Y-%m-%dT%H:%M:%S.000Z')
        time = str(date_obj.date())
    except TypeError:
        time = '2023-09-27'

    category = ''
    thumbnail_url = ''

    articles.append({'sno': sno, 
                     'title': title,
                     'meta': meta,
                     'content': content,
                     'thumbnail_img': thumbnail_img,
                     'slug': slug,
                     'time': time,
                     'category': category,
                     'thumbnail_url': thumbnail_url
                     })

final = json.dumps(articles, 
                   ensure_ascii=False,
                   indent=2)

with open('articles.json', 'w') as outfile:
    outfile.write(final)