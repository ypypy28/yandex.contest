def insert(lst: list, val: int) -> None:
    i = len(lst)
    lst.append(val)
    while i != 0:
        parent = (i >> 1)
        if lst[parent] >= lst[i]:
            break
        lst[i], lst[parent] = lst[parent], lst[i]
        i = parent


def pop(lst: list) -> int:
    end = len(lst)
    if end == 1:
        return lst.pop()

    res = lst[0]
    lst[0] = lst[-1]
    i = 0
    # sift part
    while (left_child:=(i << 1)) < end:
        right_child = left_child + 1
        if right_child >= end:
            if lst[left_child] > lst[i]:
                lst[i], lst[left_child] = lst[left_child], lst[i]
                i = left_child
            else:
                break
        else:
            if lst[left_child] > lst[right_child]:
                if lst[left_child] > lst[i]:
                    lst[i], lst[left_child] = lst[left_child], lst[i]
                    i = left_child
                elif lst[right_child] > lst[i]:
                    lst[i], lst[right_child] = lst[right_child], lst[i]
                    i = right_child
                else:
                    break
            else:
                if lst[right_child] <= lst[i]:
                    break
                else:
                    lst[i], lst[right_child] = lst[right_child], lst[i]
                    i = right_child

    lst.pop()
    return res


n = int(input())

heap = []
for _ in range(n):
    cmd = input().rstrip()
    if cmd.startswith("1"):
        print(pop(heap))
    else:
        insert(heap, int(cmd[2:]))
