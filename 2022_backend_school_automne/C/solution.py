import json
from datetime import datetime
from typing import Callable


DATE_FORMAT = "%d.%m.%Y"
NUMBER_OF_FILTERS = 5


def name_contains(value: str) -> Callable:
    value = value.lower()
    return lambda item: value in item["name"].lower()


def price_less_than(value: str) -> Callable:
    value = int(value)
    return lambda item: item["price"] <= value


def price_greater_than(value: str) -> Callable:
    value = int(value)
    return lambda item: item["price"] >= value


def date_before(value: str) -> Callable:
    before = datetime.strptime(value, DATE_FORMAT)
    return lambda item: datetime.strptime(item["date"], DATE_FORMAT) <= before


def date_after(value: str) -> Callable:
    after = datetime.strptime(value, DATE_FORMAT)
    return lambda item: datetime.strptime(item["date"], DATE_FORMAT) >= after


def make_filter(name: str, value: str) -> Callable:
    return {
        "PRICE_LESS_THAN": price_less_than,
        "PRICE_GREATER_THAN": price_greater_than,
        "DATE_AFTER": date_after,
        "DATE_BEFORE": date_before,
        "NAME_CONTAINS": name_contains,
    }[name](value)


goods = sorted(json.loads(input()), key=lambda item: item["id"])
# print(goods)
filters = [make_filter(name, value)
           for name, value in (input().split()
                               for _ in range(NUMBER_OF_FILTERS))]

filtered_goods = [item for item in goods if
                  all(f(item) for f in filters)]
print(json.dumps(filtered_goods))
