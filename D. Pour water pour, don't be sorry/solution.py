from collections import namedtuple


TimeCost = namedtuple("TimeCost", "time cost")
TimeDuration = namedtuple("TimeDuration", "time duration")
N = int(input())

ORDERS = [None]*N
COST_DELTA_TIME = dict()
DURATION_DELTA_TIME = dict()
cost = 0
for i in range(N):
    start, end, cost = (int(val) for val in input().split())

    COST_DELTA_TIME[start] = COST_DELTA_TIME.get(start, 0) + cost
    DURATION_DELTA_TIME[end] = DURATION_DELTA_TIME.get(end, 0) + end - start

COST_PREFIX_SUM = [None]*(len(COST_DELTA_TIME) + 1)
COST_PREFIX_SUM[0] = TimeCost(0, 0)
for i, (time, dcost) in enumerate(sorted(COST_DELTA_TIME.items()), start=1):
    COST_PREFIX_SUM[i] = TimeCost(time, dcost + COST_PREFIX_SUM[i-1].cost)

DURATION_PREFIX_SUM = [None]*(len(DURATION_DELTA_TIME.items()) + 1)
DURATION_PREFIX_SUM[0] = TimeDuration(0, 0)
for i, (time, ddur) in enumerate(sorted(DURATION_DELTA_TIME.items()), start=1):
    DURATION_PREFIX_SUM[i] = TimeDuration(time, DURATION_PREFIX_SUM[i-1].duration + ddur)


def process_request(start: int, end: int, type_: int) -> int:
    if type_ == 1:
        return get_total_cost(start, end)

    return get_total_duration(start, end)


def get_total_cost(start: int, end: int) -> int:
    start_cost = end_cost = prev = None
    for tc in COST_PREFIX_SUM:
        if start_cost is None and start <= tc.time <= end:
            start_cost = prev.cost
        if start_cost is not None:
            if tc.time == end:
                end_cost = tc.cost
                break
            elif tc.time > end:
                end_cost = prev.cost
                break
        prev = tc

    if start_cost is None:
        return 0
    if end_cost is None:
        end_cost = COST_PREFIX_SUM[-1].cost
    return end_cost - start_cost


def get_total_duration(start: int, end: int) -> int:
    start_dur = end_dur = prev = None
    for td in DURATION_PREFIX_SUM:
        if start_dur is None and start <= td.time <= end:
            start_dur = prev.duration
        if start_dur is not None:
            if td.time == end:
                end_dur = td.duration
                break
            elif td.time > end:
                end_dur = prev.duration
                break
        prev = td

    if start_dur is None:
        return 0
    if end_dur is None:
        end_dur = DURATION_PREFIX_SUM[-1].duration
    return end_dur - start_dur


q = int(input())
for _ in range(q-1):
    start, end, type_ = (int(val) for val in input().split())

    print(process_request(start, end, type_), end=' ')

start, end, type_ = (int(val) for val in input().split())
print(process_request(start, end, type_))
