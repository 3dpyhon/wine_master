from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from functions import num_years, year_form
from collections import defaultdict
import pandas as pd
import pprint

# Импорт и подготовка датафрейма
wine_list = pd.read_excel(
    io='data/wine.xlsx',
    names=['category', 'label', 'grade', 'price', 'image', 'promo']
).fillna('')

wine_list['image'] = wine_list['image'].apply(func=lambda x: 'images/' + x)

# Вывод словаря списков с помощью defaultdict
wine_dict = wine_list.to_dict(orient='records')
pp = pprint.PrettyPrinter(indent=1)
grouped_wine_dict = defaultdict(list)

for entry in wine_dict:
    grouped_wine_dict[entry['category']].append(entry)

pp.pprint(grouped_wine_dict)


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')


rendered_page = template.render(
    age_title=f'Уже {num_years()} {year_form(num_years())} с вами',
    grouped_wine_dict=grouped_wine_dict
)

with open('index.html', 'w', encoding='utf8') as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
