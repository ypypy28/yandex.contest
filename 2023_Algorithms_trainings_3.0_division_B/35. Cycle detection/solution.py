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
cycle = []
for i in range(1, n+1):
    if vertices[i][1] != WHITE:
        continue
    stack.append((i, None))
    while stack and not bad:
        cur, prev = stack.pop()
        # print(f"{stack=} {cur=} {prev=} {vertices[cur]=} vertices[prev]={vertices[prev] if prev is not None else ''}")
        if vertices[cur][1] == WHITE:
            vertices[cur][1] = GRAY

        for v in vertices[cur][0]:
            if vertices[v][1] == GRAY and v != prev:
                bad = True
                cycle.append(str(v))
                prev = cur
                while v != cur:
                    for next_v in vertices[v][0]:
                        if vertices[next_v][1] == GRAY and next_v != prev:
                            prev = v
                            v = next_v
                            break
                    cycle.append(str(v))
                break

        if all(vertices[v] in (GRAY, BLACK) for v in vertices[cur][0]):
            if stack:
                val = stack.pop()
                if vertices[val][1] != BLACK:
                    vertices[val][1] = BLACK
        else:
            for v in vertices[cur][0]:
                if vertices[v][1] == WHITE:
                    stack.append((v, cur))
    if bad:
        break

# print(*(f"{i=} {vertices[i]}" for i in range(1, n+1)), sep='\n')
# print(cycle)
if not cycle:
    print("NO")
else:
    print("YES", len(cycle), ' '.join(cycle), sep='\n')
