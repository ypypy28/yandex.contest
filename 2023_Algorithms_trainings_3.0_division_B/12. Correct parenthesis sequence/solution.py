import sys

stack = []
pairs = {c: o for c, o in zip(')]}', '([{')}

while (ch:=sys.stdin.read(1)) not in ('', '\n'):
    match ch:
        case '(' | '[' | '{':
            stack.append(ch)
        case ')' | ']' | '}':
            if not stack or stack[-1] != pairs[ch]:
                print('no')
                sys.exit(0)
            else:
                stack.pop()
print("yes" if not stack else "no")
