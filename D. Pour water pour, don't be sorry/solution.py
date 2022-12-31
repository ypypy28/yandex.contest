import bisect
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
    prefix_sum = COST_PREFIX_SUM if type_ == 1 else DURATION_PREFIX_SUM
    start_i = bisect.bisect_left(prefix_sum, (start, 0))
    start_val = prefix_sum[start_i-1][1]

    end_i = bisect.bisect_right(prefix_sum, (end, prefix_sum[-1][1]))
    end_val = prefix_sum[end_i-1][1]
    return end_val - start_val


q = int(input())
for _ in range(q-1):
    start, end, type_ = (int(val) for val in input().split())

    print(process_request(start, end, type_), end=' ')

start, end, type_ = (int(val) for val in input().split())
print(process_request(start, end, type_))
