def get_row_side(target_num):
    target_row, target_side = divmod(target_num, 2)
    if target_side == 1:
        target_row += 1
    else:
        target_side = 2

    return target_row, target_side


n, k, row, side = [int(input()) for _ in range(4)]

petya_num = (row-1)*2 + side

petya_variant = petya_num % k
vasya_num = petya_num + k
if vasya_num > n:
    vasya_num = petya_num - k
if vasya_num < 1:
    print(-1)
else:
    res = min([get_row_side(x) for x in (vasya_num, petya_num - k)],
              key=lambda x: abs(row -x[0]))
    print(*res)
