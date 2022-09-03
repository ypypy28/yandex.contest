import sys
import array


bad_close_idx = None
saving_close = None
open_stack = [0]*578576
# tmp = [0]*578576
# open_stack = array.array('L', tmp)
# del tmp
stack_i = -1
with open("input.txt", mode="rb", buffering=0) as f:
    pos = 1
    while True:
        ch = f.read(1)
        if not ch:
            break

        if ch == b"{":  # ord("{") = 123
            stack_i += 1
            open_stack[stack_i] = pos
            # print(f"{ch=} {open_stack=} {bad_close_idx=} {saving_close=}")
        elif ch == b"}":  # ord("}") = 125
            if stack_i > -1:
                stack_i -= 1
                if not saving_close:
                    try:
                        saving_close = pos
                    except ValueError:
                        pass
            else:
                if not bad_close_idx:
                    bad_close_idx = pos
                else:
                    print(-1)
                    sys.exit(0)
            # print(f"{ch=} {open_stack=} {bad_close_idx=} {saving_close=}")
        pos += 1
        del ch

if stack_i == 0:
    if bad_close_idx:
        print(-1)
    else:
        print(open_stack[0])
elif bad_close_idx and stack_i < 0:
    if saving_close:
        print(min(bad_close_idx, saving_close))
    else:
        print(bad_close_idx)
else:
    print(-1)
