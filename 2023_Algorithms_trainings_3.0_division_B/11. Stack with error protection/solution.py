import sys


stack = []
while (line:=sys.stdin.readline()) != '':
    match line.strip().split():
        case "push", val:
            stack.append(int(val))
            print("ok")

        case "pop",:
            if len(stack) != 0:
                print(stack.pop())
            else:
                print("error")

        case "back",:
            if len(stack) != 0:
                print(stack[-1])
            else:
                print("error")

        case "size",:
            print(len(stack))

        case "clear",:
            stack.clear()
            print("ok")

        case "exit",:
            print("bye")
            break

        case _:
            print("error")
