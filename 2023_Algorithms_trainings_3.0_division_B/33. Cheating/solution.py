n, m = [int(x) for x in input().split()]

students = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = [int(x) for x in input().split()]
    students[a].append(b)
    students[b].append(a)

groups = (set(), set())
visited = set()

stack = []
group = 0
bad = False
for i in range(1, n+1):
    if i in visited:
        continue
    stack.append((i, group))
    bad = False
    while stack:
        cur, group = stack.pop()
        next_group = 1 - group
        if cur in visited:
            continue
        visited.add(cur)
        if cur in groups[next_group]:
            bad = True
            break
        groups[group].add(cur)

        for s in students[cur]:
            if s not in visited:
                stack.append((s, next_group))
            elif s in groups[group]:
                bad = True
                break

        if bad:
            break
    if bad:
        print("NO")
        break
else:
    print("YES")
