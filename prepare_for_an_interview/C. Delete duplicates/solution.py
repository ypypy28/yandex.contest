n = int(input())
prev = None
for _ in range(n):
    num = input()
    if num != prev:
        print(num)
        prev = num
