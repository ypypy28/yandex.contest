n, m = [int(x) for x in input().split()]

vertices = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = [int(x) for x in input().split()]
    vertices[a].append(b)
    vertices[b].append(a)


visited = set()

components = []
stack = []

for i in range(1, n+1):
    if i in visited:
        continue
    components.append(set())
    stack.append(i)
    while stack:
        cur = stack.pop()
        if cur in visited:
            continue
        components[-1].add(cur)
        visited.add(cur)
        for v in vertices[cur]:
            if v not in visited:
                stack.append(v)

components.sort(key=lambda x: len(x), reverse=True)

print(len(components),
      *(f"{len(c)}\n" + ' '.join(str(el) for el in c)
        for c in components),
      sep='\n')
