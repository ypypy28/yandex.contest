import sys
import array


CHUNK_SIZE = 8092
bad_close_idx = None
saving_close = None
open_stack = array.array('L', [0]*556000)
# open_stack = array.array('I')
stack_i = -1
with open("input.txt", mode="rb", buffering=0) as f:
    pos = 1
    while True:
        tmp = f.read(CHUNK_SIZE)
        if not tmp:
            break

        for i, ch in enumerate(tmp):
            if ch == 123:  # ord("{") = 123
                stack_i += 1
                if stack_i < len(open_stack):
                    open_stack[stack_i] = i+pos
                else:
                    open_stack.append(i+pos)
                # open_stack.append(i+pos)
                # print(f"{ch=} {open_stack=} {bad_close_idx=} {saving_close=}")
            elif ch == 125:  # ord("}") = 125
                # if open_stack:
                if stack_i > -1:
                    # open_stack.pop()
                    stack_i -= 1
                    if not saving_close:
                        try:
                            saving_close = i + pos
                        except ValueError:
                            pass
                else:
                    if not bad_close_idx:
                        bad_close_idx = i + pos
                    else:
                        print(-1)
                        sys.exit(0)
                # print(f"{ch=} {open_stack=} {bad_close_idx=} {saving_close=}")

        pos += CHUNK_SIZE
        del tmp

# if len(open_stack) == 1:
if stack_i == 0:
    if bad_close_idx:
        print(-1)
    else:
        print(open_stack[0])
# elif bad_close_idx and not open_stack:
elif bad_close_idx and stack_i < 0:
    if saving_close:
        print(min(bad_close_idx, saving_close))
    else:
        print(bad_close_idx)
else:
    print(-1)
