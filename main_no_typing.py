import sys


CHUNK_SIZE = 1024

bad_close_idx = None
saving_close = None
open_stack = []
with open("input.txt") as f:
    pos = 1
    while True:
        tmp = f.read(CHUNK_SIZE)
        if not tmp:
            break

        for i, ch in enumerate(tmp):
            if ch == "{":
                open_stack.append(i+pos)
            elif ch == "}":
                if open_stack:
                    open_stack.pop()
                else:
                    if not bad_close_idx:
                        bad_close_idx = i + pos
                    else:
                        print(-1)
                        sys.exit()

        if not saving_close:
            try:
                saving_close = tmp.index("}") + pos
            except ValueError:
                pass
        pos += CHUNK_SIZE
        del tmp

if len(open_stack) == 1:
    print(open_stack[0])
elif bad_close_idx:
    print(saving_close)
else:
    print(-1)
