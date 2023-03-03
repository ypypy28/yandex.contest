from collections import deque


MOVEMENTS = ((0, 1), (1, 0))

n, m = [int(val) for val in input().split()]
end = n-1, m-1

field = [None]*n

for i in range(n):
    field[i] = [int(x) for x in input().split()]

visited = [[None for _ in range(m)] for _ in range(n)]
y, x = 0, 0
cost = field[y][x]
neighbors = [(new_y, new_x) for dy, dx in MOVEMENTS
             if (new_y:=y+dy) < n and (new_x:=x+dx) < m]
visited[y][x] = None, field[y][x]

for j, i in neighbors:
    visited[j][i] = (y, x), field[y][x] + field[j][i]

next_ = deque(neighbors)

while (y, x) != end:
    if not next_:
        break
    y, x = next_.pop()
    neighbors = [(new_y, new_x) for dy, dx in MOVEMENTS
                if (new_y:=y+dy) < n and (new_x:=x+dx) < m]

    for j, i in neighbors:
        new_cost = visited[y][x][1] + field[j][i]
        if visited[j][i] is None or visited[j][i][1] > new_cost:
            visited[j][i] = (y, x), new_cost

    next_.extendleft(neighbors)

# print(*visited, sep='\n')
print(visited[end[0]][end[1]][1])
