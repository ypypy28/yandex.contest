from collections import deque


def travel(cur, to_, cities, max_distance):
  visited = set()
  next_variants = deque()
  next_variants.append((cities[cur], 0))
  while next_variants:
    cur, roads = next_variants.popleft()
    visited.add(cur)
    to_visit = {val
                for val in cities
                if (
                    abs(val[0] - cur[0]) + abs(val[1] - cur[1]) <= max_distance
                    and (val not in visited)
                )
             }
    if cities[to_] in to_visit:
      return roads + 1

    for next_ in to_visit:
      next_variants.append((next_, roads+1))

  return -1


n = int(input())
cities = tuple(tuple(int(val) for val in input().split()) for _ in range(n))
max_distance = int(input())
from_, to_ = (int(val)-1 for val in input().split())

print(travel(from_, to_, cities, max_distance))
