from collections import deque


def travel(cur, to_, cities, max_distance):
  visited = set()
  available_roads = [{i
            for i in range(len(cities))
            if (abs(cities[i][0] - cities[j][0]) + abs(cities[i][1] - cities[j][1])) <= max_distance
            and i != j}
           for j in range(len(cities))]
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
cities =[[int(val) for val in input().split()] for _ in range(n)]
max_distance = int(input())
from_, to_ = (int(val)-1 for val in input().split())

print(travel(from_, to_, cities, max_distance))
