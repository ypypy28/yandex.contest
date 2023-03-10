n, m = [int(val) for val in input().split()]

vertices = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = [int(val) for val in input().split()]
    vertices[a].append(b)
    vertices[b].append(a)


cur = 1
visited = set()
stack = [cur]
while stack:
    cur = stack.pop()
    if cur in visited:
        continue
    visited.add(cur)
    for v in vertices[cur]:
        if v not in visited:
            stack.append(v)

print(len(visited))
print(*sorted(visited))
