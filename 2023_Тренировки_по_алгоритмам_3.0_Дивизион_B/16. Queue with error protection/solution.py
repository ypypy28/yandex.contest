import sys
from collections import deque


q = deque()
while (cmd:=sys.stdin.readline().strip().split()):
    match cmd:
        case "push", n:
            q.append(n)
            print("ok")

        case "pop", :
            if q:
                print(q.popleft())
            else:
                print("error")
        case "front", :
            if q:
                print(q[0])
            else:
                print("error")

        case "size", :
            print(len(q))

        case "clear", :
            q.clear()
            print("ok")

        case "exit", :
            print("bye")
            break
