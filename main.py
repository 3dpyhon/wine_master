from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from collections import defaultdict
import argparse
import pandas as pd
import datetime as dt
from dateutil.relativedelta import relativedelta


def generate_year_form(year: int) -> str:
    f"Функция, которая генерирует правильную форму слова \'год\'"
    if year % 100 == 1:
        return 'год'
    elif (year % 100) in range(2, 5):
        return 'года'
    else:
        return 'лет'


def main():
    parser = argparse.ArgumentParser(description="Path to data")
    parser.add_argument('path', nargs='?', type=str, default='data/', help='Path to .xlsx file')
    parser.add_argument('filename', nargs='?', type=str, default='wine.xlsx', help='Name of the file')
    args = parser.parse_args()

    data = pd.read_excel(
        io=args.path + args.filename,
        names=['category', 'label', 'grade', 'price', 'image', 'promo']
    ).fillna('')

    data['image'] = data['image'].apply(func=lambda x: 'images/' + x)

    data = data.to_dict(orient='records')
    products_by_category = defaultdict(list)

    for entry in data:
        products_by_category[entry['category']].append(entry)

    foundation_date = dt.datetime(year=1920, month=1, day=1)
    years_passed = relativedelta(dt.datetime.today(), foundation_date).years

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        age_title=f'Уже {years_passed} {generate_year_form(years_passed)} с вами',
        products_by_category=products_by_category
    )

    with open('index.html', 'w', encoding='utf8') as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
