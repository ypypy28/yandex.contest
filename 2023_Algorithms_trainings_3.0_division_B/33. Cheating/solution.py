n, m = [int(x) for x in input().split()]

students = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = [int(x) for x in input().split()]
    students[a].append(b)
    students[b].append(a)

groups = (set(), set())
visited = set()

stack = [1]
group = 0
bad = False
for i in range(1, n+1):
    if i in visited:
        continue
    stack.append(i)
    while stack:
        cur = stack.pop()
        if cur in visited:
            continue
        visited.add(cur)
        group = 1 - group
        groups[group].add(cur)

        bad = False
        for s in students[cur]:
            if s not in visited:
                stack.append(s)
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


# print(students)
# print(groups)
