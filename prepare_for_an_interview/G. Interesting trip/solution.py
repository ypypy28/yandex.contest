from collections import deque


def travel(cur, to_, cities, available_roads):
    visited = set()
    next_variants = deque()
    next_variants.append((cur, 0))
    while next_variants:
        cur, roads = next_variants.popleft()
        visited.add(cur)
        to_visit = available_roads[cur] - visited
        if to_ in to_visit:
            return roads + 1

        for next_ in to_visit:
            next_variants.append((next_, roads+1))
    return -1


n = int(input())
cities = [[int(val) for val in input().split()] for _ in range(n)]
max_distance = int(input())
from_, to_ = (int(val)-1 for val in input().split())

available_roads = [set() for _ in range(len(cities))]
for i in range(len(cities)):
    for j in range(i):
        if abs(cities[i][0] - cities[j][0]) + abs(cities[i][1] - cities[j][1]) <= max_distance:
            available_roads[i].add(j)
            available_roads[j].add(i)

print(travel(from_, to_, cities, available_roads))
