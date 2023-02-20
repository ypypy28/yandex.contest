expr = input().strip().split()

ops = {
    '+': lambda a,b: a + b,
    '-': lambda a,b: b - a,
    '*': lambda a,b: a * b,
}

stack = []
for val in expr:
    match val:
        case '+' | '-' | '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(ops[val](a, b))

        case _:
            stack.append(int(val))
print(stack.pop())
