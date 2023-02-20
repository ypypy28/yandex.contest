n = int(input())
res = ["-1"]*n
living_costs = [int(val) for val in input().split()]

stack = []
for i, el in enumerate(living_costs):
    if not stack:
        stack.append((el, i))
    else:
        while stack[-1][0] > el:
            _, j = stack.pop()
            res[j] = str(i)
            if not stack:
                break
        stack.append((el, i))
print(' '.join(res))
