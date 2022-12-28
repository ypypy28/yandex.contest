from collections import namedtuple


Order = namedtuple("Order", "start end cost")
N = int(input())

ORDERS_STARTORDER = [Order(*(int(val) for val in input().split()))
          for _ in range(N)]
ORDERS_STARTORDER.sort()
ORDERS_ENDORDER = sorted(ORDERS_STARTORDER, key=lambda o: o.end)

def process_request(start: int, end: int, type_: int) -> int:
    if type_ == 1:
        return get_total_cost(start, end)

    return get_total_duration(start, end)


def get_total_cost(start: int, end: int) -> int:
    total_cost = 0
    for order in ORDERS_STARTORDER:
        # print(f"{N=} {order=} {start=} {end=}")
        if start <= order.start <= end:
            total_cost += order.cost
        elif order.start > end:
            break
    return total_cost


def get_total_duration(start: int, end: int) -> int:
    total_duration = 0
    for order in ORDERS_ENDORDER:
        if start <= order.end <= end:
            total_duration += order.end - order.start
            # print(f"{total_duration=} {order} {start=} {end=}")
        elif order.end > end:
            # print(f"{total_duration=} {order} {start=} {end=}")
            break
    return total_duration


q = int(input())
for _ in range(q-1):
    start, end, type_ = (int(val) for val in input().split())

    print(process_request(start, end, type_), end=' ')

start, end, type_ = (int(val) for val in input().split())
print(process_request(start, end, type_))
