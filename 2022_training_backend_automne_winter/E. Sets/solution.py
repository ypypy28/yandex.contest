n = int(input())
sets = [tuple(input()) for _ in range(n)]
print(sets)

for operators in sets:
    # SET must not be set FIXME almost everything is wrong
    i = set(range(1, n+1))
    j = set(range(1, len(operators)+1))
    print(f"{i=} {j=}")
    for op in operators:
        res = []
        match op:
            case '=':
                res.append(lambda x, y: x == y)
            case '<':
                res.append(lambda x, y: x in y)
            case '>':
                res.append(lambda x, y: y in x)
            case '!':
                res.append(lambda x, y: x not in y)
            case '^':
                res.append(lambda x, y: y not in x)
            case '?':
                res.append(lambda x, y: True)

