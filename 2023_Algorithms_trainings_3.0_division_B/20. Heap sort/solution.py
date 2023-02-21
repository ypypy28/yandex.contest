def heapify(lst: list[int]) -> None:
    full_size = len(lst)
    for end in range(1, full_size):
        insert_from_end(lst, end)


def insert_from_end(lst: list[int], end: int) -> None:
    i = end
    while i != 0:
        parent = ((i+1) >> 1) - 1
        if lst[parent] >= lst[i]:
            break
        lst[i], lst[parent] = lst[parent], lst[i]
        i = parent


def put_max_at(i: int, lst: list[int]) -> None:
    if i == 0:
        return
    end = i
    max_val = lst[0]
    lst[0] = lst[i]
    i = 0
    # sift part
    while (left_child:=(i << 1)+1) < end:
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
    lst[end] = max_val
    return


def heap_sort(lst: list[int]) -> None:
    heapify(lst)
    n = len(lst)
    while n != 1:
        n -= 1
        put_max_at(n, lst)


n = int(input())
arr = [int(val) for val in input().split()]
heap_sort(arr)
print(*arr)
