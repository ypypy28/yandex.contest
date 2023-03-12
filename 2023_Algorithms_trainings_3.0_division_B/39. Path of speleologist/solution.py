from collections import deque


MOVEMENTS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
FREE_CELL = '.'


n = int(input())
cave = [None]*n
start = None

for j in range(n):
    input()
    block = [list(input()) for _ in range(n)]
    cave[j] = block
    if start is None:
        for i in range(n):
            try:
                start = (j, i, block[i].index('S'))
                block[i][start[2]] = 0
            except ValueError:
                pass

# print(f"{start=}", *cave, sep='\n')
cur = start
res = -1
q = deque((start,))
if start[0] == 0:
    res = 0
    q.clear()
while q:
    ...
    cur = q.popleft()
    next_length = cave[cur[0]][cur[1]][cur[2]] + 1

    for next_cell in [(z, y, x)
                      for dz, dy, dx in MOVEMENTS if (
                          0 <= (z:=dz+cur[0])  < n
                          and 0 <= (y:=dy+cur[1]) < n
                          and 0 <= (x:=dx+cur[2]) < n
                      )]:
        if cave[next_cell[0]][next_cell[1]][next_cell[2]] == FREE_CELL:
            if next_cell[0] == 0:
                res = next_length
                q.clear()
                break
            cave[next_cell[0]][next_cell[1]][next_cell[2]] = next_length
            q.append(next_cell)

print(res)
