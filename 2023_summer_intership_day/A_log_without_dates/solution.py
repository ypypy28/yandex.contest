n = int(input())

days = 0
last_time = 3600 * 24 + 1

for _ in range(n):
    h, m, s = [int(x) for x in input().split(':')]
    s += m * 60 + h * 3600
    if last_time >= s:
        days += 1
    last_time = s

print(days)
