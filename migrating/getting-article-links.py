import json

with open('/Users/elenakapatsa/Repositories/django-tailwind-blog/migrating/modya-export-2023-09-27.json') as json_file:
    data = json.load(json_file)

links = []

for i in range(len(data['db'][0]['data']['posts'])):
    link = 'https://www.helenkapatsa.ru/' + data['db'][0]['data']['posts'][i]['slug']
    
    links.append(link)

print(links)