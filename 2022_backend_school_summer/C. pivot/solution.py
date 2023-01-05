import json
from datetime import datetime


DATEFMT = '%d.%m.%Y'


def make_dt(date):
    return datetime.strptime(date, DATEFMT)


def name_contains_builder(val):
    val = val.lower()
    def name_contains(d):
        return val in d['name'].lower()
    return name_contains


def price_greater_than_builder(val):
    val = int(val)
    def price_greater_than(d):
        return d['price'] >= val
    return price_greater_than


def price_less_than_builder(val):
    val = int(val)
    def price_less_than(d):
        return d['price'] <= val
    return price_less_than


def date_before_builder(val):
    date = make_dt(val)
    def date_before(d):
        return make_dt(d['date']) <= date
    return date_before

def date_after_builder(val):
    date = make_dt(val)
    def date_after(d):
        return make_dt(d['date']) >= date
    return date_after


constraints = {"NAME_CONTAINS": name_contains_builder,
               "PRICE_GREATER_THAN": price_greater_than_builder,
               "PRICE_LESS_THAN": price_less_than_builder,
               "DATE_BEFORE": date_before_builder,
               "DATE_AFTER": date_after_builder,
               }

goods = json.loads(input())
filters = [constraints[name](val)
           for name, val in [input().split() for _ in range(5)]]

filtered = sorted(filter(lambda x: all(f(x) for f in filters), goods),
                  key=lambda d: d['id'])
print(json.dumps(filtered))
