#!/usr/bin/python
import sys
import argparse
import requests
import datetime
import prettytable

API_URL='https://public-api.blablacar.com/api/v2/trips'
API_KEY='ef2b5498bee14192904c396df93ff0f2'


def valid_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        try:
            datetime.datetime.strptime(date_text, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            raise ValueError("Incorrect data format, should be 'YYYY-MM-DD' or 'DDDD-MM-YY HH:mm:ss'")


def get_url(args):
    url = "{}?fn={}&tn={}&locale={}&_format=json&cur={}&sort=trip_{}&order={}&radius={}&limit={}&hb={}&he={}\
".format(API_URL, args.out, args.to, args.locale, args.cur, args.sort, args.order, args.radius, args.max, args.hb, args.he)

    if args.db:
        valid_date(args.db)
        url+="&db={}".format(args.db)
    if args.de:
        valid_date(args.de)
        if args.de < args.db:
            sys.exit("Date before must be greater then date end")
        url+="&de={}".format(args.de)

    return url


def parser_arguments():
    default_db = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    parser = argparse.ArgumentParser(description="Search for travel on blablakar")
    parser.add_argument('-f', '--out', metavar='PLACE', required=True, help="The departure place name")
    parser.add_argument('-t', '--to', metavar='PLACE', required=True, help="The arrival place name")
    parser.add_argument('--db', metavar='DATE', default=default_db, help="Date Begin. Format: 'DDDD-MM-YY' or 'DDDD-MM-YY HH:mm:ss'")
    parser.add_argument('--de', metavar='DATE', help="Date End. Format: 'DDDD-MM-YY' or 'DDDD-MM-YY HH:mm:ss'")
    parser.add_argument('--hb', metavar='HOUR', default=0, type=int, help="Hour Begin")
    parser.add_argument('--he', metavar='HOUR', default=24, type=int, help="Hour End")
    parser.add_argument('-l', '--locale', default='ru_RU', help="Available locales. Default: ru_RU")
    parser.add_argument('-c', '--cur', default='RUB', help="Select the currency you want. Default: RUB")
    parser.add_argument('-s', '--sort', default='date', choices=['date', 'price'], help="Sorting")
    parser.add_argument('-o', '--order', default='asc', choices=['asc', 'desc'], help="Order of the sorting")
    parser.add_argument('-m', '--max', default=10, help="Maximum results")
    parser.add_argument('-r', '--radius', default=10, help="Maximum radius of the search")

    return parser.parse_args()


def main():
    args = parser_arguments()

    url = get_url(args)
    r = requests.get(url, headers = {"accept" : "application/json", "key" : API_KEY})
    results = r.json()['trips']

    if not results:
        sys.exit("Trips are not found")

    table = prettytable.PrettyTable(hrules=True)
    table.field_names = ['Date', 'From', 'To', 'Price', 'Seats left', 'Car']
    for r in results:
        address_from = r['departure_place']['address'].replace(",", "\n")
        address_to = r['arrival_place']['address'].replace(",", "\n")
        date =  r['departure_date']
        price = r['price_with_commission']['value']
        commission = r['commission']['value']
        price_sum = price + commission
        price_display = "{} {}\n({}+{})".format(price_sum, args.cur, price, commission)
        seat_left = r['seats_left']
        car_info = "-"
        if 'car' in r:
            car_model = r['car']['model'].encode('utf-8')
            car_make = r['car']['make'].encode('utf-8')
            car_info = "Model: {}/Make: {}".format(car_model, car_make)
        table.add_row([date, address_from, address_to, price_display, seat_left, car_info])

    print table


if __name__ == '__main__':
    main()

# EOF
