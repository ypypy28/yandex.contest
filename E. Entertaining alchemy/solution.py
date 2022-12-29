from collections import Counter, dequeue


n = int(input())
potions = {i: None for i in range(1, n+1)}

i = 3
for _ in range(n-1):
    k, *p = [int(m) for m in input().split()]
    potions[i] = Counter(p)
    i += 1

q = int(input())

for _ in range(q):
    x, y, s = [int(m) for m in input().split()]
    if s == 1:
        print(1 if x > 0 else 0)
    elif s == 2:
        print(1 if x >= 0 else 0)
    elif s not in potions:
        print(0)
    len(potions[s]) == 2:
        print(1 if potions[s].get(1, 0) <= x and potions[s].get(2, 0) <= y else 0)
    else:
        a = potions[s].pop(1, 0)
        b = potions[s].pop(2, 0)
        visited = set((1, 2))
        to_visit = set(potions[s].keys())
        while to_visit:
            ingredient = to_visit.pop()
            if ingredient in visited:
                pass
            if s in potions[ingredient]:
                print(0)
                break





