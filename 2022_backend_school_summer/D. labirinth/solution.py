WALL, EMPTY, START = '#', '.', 'S'
LEFT, RIGHT, UP, DOWN = 'L', 'R', 'U', 'D'

n, m = (int(x) for x in input().split())
field = [list(input()) for _ in range(n)]
start_position = max([(i, line.index(START)) for i, line in enumerate(field) if START in line])

movements = {(0, -1): LEFT,
             (0, 1): RIGHT,
             (1, 0): DOWN,
             (-1, 0): UP}

def next_steps(cur: tuple[int]) -> list[tuple[int]]:
    steps = []
    for (dy, dx), move in movements.items():
        y, x = cur[0]+dy, cur[1]+dx
        if 0 <= y < n and 0 <= x < m and field[y][x] == EMPTY:
            steps.append((y, x))
            field[y][x] = move
    return steps

steps = next_steps(start_position)
while steps:
    cur = steps.pop(0)
    steps.extend(next_steps(cur))

print(*(''.join(line) for line in field), sep='\n')
