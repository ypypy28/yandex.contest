WHITE, GRAY, BLACK = 0, 1, 2

n = int(input())
vertices = [[set(), WHITE] for _ in range(n+1)]

for i in range(n):
    edges = [int(x) for x in input().split()]
    a = i + 1
    for j, v in enumerate(edges):
        if v == 1:
            b = j + 1
            vertices[a][0].add(b)
            vertices[b][0].add(a)

stack = []

bad = False
cycle = None
for i in range(1, n+1):
    if vertices[i][1] != WHITE:
        continue
    stack.append((i, tuple()))
    while stack:
        cur, prev = stack.pop()
        if vertices[cur][1] == WHITE:
            vertices[cur][1] = GRAY

        for v in vertices[cur][0]:
            if vertices[v][1] == GRAY and v != prev[0]:
                bad = True
                end_indx = prev.index(v)
                cycle = [str(x) for x in (cur, *prev[:end_indx+1])]
                break
        if bad:
            break

        if all(vertices[v] in (GRAY, BLACK) for v in vertices[cur][0]):
            if stack:
                val, _ = stack.pop()
                if vertices[val][1] != BLACK:
                    vertices[val][1] = BLACK
        else:
            for v in vertices[cur][0]:
                if vertices[v][1] == WHITE:
                    stack.append((v, (cur, *prev)))
    if bad:
        break

if cycle is None:
    print("NO")
else:
    print("YES", len(cycle), ' '.join(cycle), sep='\n')
