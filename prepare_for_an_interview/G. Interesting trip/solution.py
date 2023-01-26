from collections import deque


def travel(cur, to_, cities, available_roads, stops_from_start):
    next_variants = deque()
    next_variants.append(cur)
    while next_variants:
        cur = next_variants.popleft()
        stops = stops_from_start[cur]
        if to_ in available_roads[cur]:
            stops_from_start[to_] = stops + 1
            return stops_from_start[to_]

        for next_ in available_roads[cur]:
            if stops_from_start[next_] is None:
                stops_from_start[next_] = stops + 1
                next_variants.append(next_)
    return -1


n = int(input())
cities = [[int(val) for val in input().split()] for _ in range(n)]
max_distance = int(input())
from_, to_ = (int(val)-1 for val in input().split())

stops_from_start = [None]*n
stops_from_start[from_] = 0
available_roads = [set() for _ in range(n)]
for i in range(n):
    for j in range(i):
        if abs(cities[i][0] - cities[j][0]) + abs(cities[i][1] - cities[j][1]) <= max_distance:
            available_roads[i].add(j)
            available_roads[j].add(i)

print(travel(from_, to_, cities, available_roads, stops_from_start))
