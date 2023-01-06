import sys
import array


bad_close_idx = saving_close = left_open = None
stack_i = -1
magic = array.array('b')
with open("input.txt", mode="rb", buffering=65536) as f:
    pos = 1
    while True:
        try:
            magic.fromfile(f, 1)
        except EOFError:
            break

        if magic[0] == 123:  # ord("{") = 123
            stack_i += 1
            if stack_i == 0:
                left_open = pos
        elif magic[0] == 125:  # ord("}") = 125
            if stack_i > -1:
                stack_i -= 1
                if not saving_close:
                    saving_close = pos
            else:
                if not bad_close_idx:
                    bad_close_idx = pos
                else:
                    print(-1)
                    sys.exit(0)
        pos += 1
        magic.pop()

if stack_i == 0:
    if bad_close_idx:
        print(-1)
    else:
        print(left_open)
elif bad_close_idx and stack_i < 0:
    if saving_close:
        print(min(bad_close_idx, saving_close))
    else:
        print(bad_close_idx)
else:
    print(-1)
