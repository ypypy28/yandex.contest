n, k, row, side = [int(input()) for _ in range(4)]

petya_num = (row-1)*2 + side

petya_variant = petya_num % k
vasya_num = petya_num + k
if vasya_num > n:
    vasya_num = petya_num - k
if vasya_num < 1:
    print(-1)
else:
    # print(f"{(petya_num, vasya_num)=}")
    vasya_row, vasya_side = divmod(vasya_num, 2)
    if vasya_side == 1:
        vasya_row += 1
    else:
        vasya_side = 2
    print(vasya_row, vasya_side)
