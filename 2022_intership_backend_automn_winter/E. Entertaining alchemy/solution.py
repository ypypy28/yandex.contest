import sys
from collections import Counter


sys.setrecursionlimit(sys.getrecursionlimit()*50)
class CycleError(Exception):
    ...


n = int(input())
empty_base = {1: 0, 2: 0}
POTIONS = {1: Counter({1: 1, 2: 0}),
           2: Counter({1: 0, 2: 1})}


def normalize_potion(s: int, prev=None) -> None:
        if POTIONS[s] is None:
            raise CycleError
        if len(POTIONS[s]) == 2:
            return

        if prev is None:
            prev = {s}
        else:
            prev.add(s)

        a = POTIONS[s].pop(1)
        b = POTIONS[s].pop(2)

        for ingredient in POTIONS[s]:
            if (
                (ingredient in prev)
                or (ingredient not in POTIONS)
                or (POTIONS[ingredient] is None)
            ):
                POTIONS[s] = None
                raise CycleError
            if len(POTIONS[ingredient]) != 2:
                try:
                    normalize_potion(ingredient, prev)
                except CycleError as er:
                    POTIONS[s] = None
                    prev.remove(s)
                    raise er

            a += POTIONS[s][ingredient]*POTIONS[ingredient][1]
            b += POTIONS[s][ingredient]*POTIONS[ingredient][2]
        POTIONS[s] = Counter({1: a, 2: b})
        prev.remove(s)


for i in range(3, 3+n-2):
    _, *p = [int(m) for m in input().split()]
    POTIONS[i] = Counter(p)
    POTIONS[i].update(empty_base)
    if i in POTIONS[i]:
        POTIONS[i] = None

for i in range(3, 3+n-2):
    try:
        normalize_potion(i)
    except CycleError:
        continue

q = int(input())

for _ in range(q):
    x, y, s = [int(m) for m in input().split()]
    if s not in POTIONS or POTIONS[s] is None:
        print(0, end='')
        continue
    # elif len(POTIONS[s]) > 2:
    #     try:
    #         normalize_potion(s)
    #     except CycleError:
    #         print(0, end='')
    #         continue

    print(1 if POTIONS[s][1] <= x and POTIONS[s][2] <= y else 0, end='')
print()
