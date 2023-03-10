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
res = []
for i in range(1, n+1):
    if vertices[i][1] != WHITE:
        continue
    stack.append((i, None))
    while stack:
        cur, prev = stack.pop()
        # print(f"{stack=} {cur=} {prev=} {vertices[cur]=} vertices[prev]={vertices[prev] if prev is not None else ''}")
        if vertices[cur][1] == WHITE:
            vertices[cur][1] = GRAY

        for v in vertices[cur][0]:
            if vertices[v][1] == GRAY and v != prev:
                bad = True
                res = [str(cur), str(prev)]
                back, prev = stack.pop()
                res.append(str(prev))
                while prev != v:
                    back, prev = stack.pop()
                    res.append(str(prev))
                break

        if all(vertices[v] in (GRAY, BLACK) for v in vertices[cur][0]):
            val = stack.pop()
            if vertices[val][1] != BLACK:
                vertices[val][1] = BLACK
        else:
            for v in vertices[cur][0]:
                if vertices[v][1] == WHITE:
                    stack.append((v, cur))
    if bad:
        break

# print(vertices)
# print(res)
if not res:
    print("NO")
else:
    print("YES", len(res), ' '.join(res), sep='\n')
