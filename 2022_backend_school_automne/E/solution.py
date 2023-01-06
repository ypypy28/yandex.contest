import sys
import array


CHUNK_SIZE = 8192
bad_close_idx = saving_close = left_open = None
stack_i = -1
with open("input.txt", mode="rb", buffering=CHUNK_SIZE) as f:
    pos = 1
    while True:
        tmp = f.read(CHUNK_SIZE)
        if not tmp:
            break

        for i, ch in enumerate(tmp):
            if ch == 123:  # ord("{") = 123
                stack_i += 1
                if stack_i == 0:
                    left_open = i + pos
            elif ch == 125:  # ord("}") = 125
                if stack_i > -1:
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
        pos += CHUNK_SIZE
        del tmp

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
