n, m = [int(x) for x in input().split()]

WHITE, GRAY, BLACK = 0, 1, 2

vertices = [[[], WHITE] for _ in range(n+1)]

for _ in range(m):
    a, b = [int(x) for x in input().split()]
    vertices[a][0].append(b)

stack = []

res = []
bad = False
for i in range(1, n+1):
    if vertices[i][1] == BLACK:
        continue
    stack.append(i)
    while stack:
        cur = stack[-1]
        if vertices[cur][1] == WHITE:
            vertices[cur][1] = GRAY

        if any(vertices[v][1] == GRAY for v in vertices[cur][0]):
            bad = True
            break

        if all(vertices[v][1] == BLACK for v in vertices[cur][0]):
            val = stack.pop()
            if vertices[val][1] != BLACK:
                vertices[val][1] = BLACK
                res.append(val)
        else:
            for v in vertices[cur][0]:
                if vertices[v][1] == WHITE:
                    stack.append(v)
    if bad:
        res = [-1]
        break

print(*res[::-1])
