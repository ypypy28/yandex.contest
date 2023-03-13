from collections import deque


n = int(input())

train = deque()
goods = {}

for _ in range(n):
    op = input().split()

    match op:
        case "add", val, name:
            val = int(val)
            train.append([name, val])
            goods[name] = goods.get(name, 0) + val

        case "delete", val:
            val = int(val)
            left = train[-1][1] - val
            while left < 0:
                name, deleted = train.pop()
                goods[name] -= deleted
                val -= deleted
                left = train[-1][1] - val
            train[-1][1] = left
            goods[train[-1][0]] -= val
            if left == 0:
                train.pop()

        case "get", name:
            print(goods.get(name, 0))

        case _:
            raise NotImplemented
