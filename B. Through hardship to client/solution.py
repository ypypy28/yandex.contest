from datetime import datetime
from collections import namedtuple


MINUTES_IN_DAY = 24*60
Record = namedtuple("Record", "id day hour minute status")
n = int(input())

log = []
for _ in range(n):
    day, hour, minute, id_, status = input().split()
    day, hour, minute, id_ = (int(val) for val in (day, hour, minute, id_))
    log.append(Record(id_, day, hour, minute, status))

log.sort()

cur = log[0]
time_on_go = 0
for rec in log:
    if rec.id != cur.id:
        cur = rec
        print(time_on_go, end=' ')
        time_on_go = 0
        start = cur
    else:
        if rec.status == "A":
            cur = rec
        elif rec.status in "CS":
            time_on_go += (rec.day*MINUTES_IN_DAY + rec.hour*60 + rec.minute
                           - cur.day*MINUTES_IN_DAY - cur.hour*60 - cur.minute)
print(time_on_go)
