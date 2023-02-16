k = int(input())

coords = [(int(x), int(y))
          for x, y in [input().split() for _ in range(k)]]
min_x, min_y = coords[0]
max_x, max_y = coords[0]

for x, y in coords:
    if min_x > x:
        min_x = x
    if min_y > y:
        min_y = y
    if max_x < x:
        max_x = x
    if max_y < y:
        max_y = y
print(min_x, min_y, max_x, max_y)
