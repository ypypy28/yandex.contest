from collections import deque, namedtuple


Coords = namedtuple("Coords", "y x")
STEPS = {letter: Coords(d[0], d[1])
         for letter, d in zip("LRUD", ((0, 1), (0, -1), (1, 0), (-1, 0)))}
N, M = (int(val) for val in input().split())
office_map = [[ch for ch in input()] for _ in range(N)]

S = None
for i, row in enumerate(office_map):
    try:
        S = Coords(i, row.index("S"))
    except ValueError:
        continue
    break

queue = deque((S,))

while queue:
    step = queue.pop()
    for letter, deltas in STEPS.items():
        y, x = step.y + deltas.y, step.x + deltas.x
        if office_map[y][x] == '.':
            office_map[y][x] = letter
            queue.append(Coords(y, x))


print(*(''.join(row) for row in office_map), sep='\n')
