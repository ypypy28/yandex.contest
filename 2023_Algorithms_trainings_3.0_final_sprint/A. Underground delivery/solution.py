from collections import deque


n = int(input())

train = deque()
goods = {}

for _ in range(n):
    op = input().split()
    # print(op, train, goods, sep='\n')

    match op:
        case "add", val, name:
            val = int(val)
            train.extend([name]*val)
            goods[name] = goods.get(name, 0) + val
        case "delete", val:
            val = int(val)
            for _ in range(val):
                name = train.pop()
                goods[name] -= 1
        case "get", name:
            print(goods.get(name, 0))
        case _:
            raise NotImplemented
