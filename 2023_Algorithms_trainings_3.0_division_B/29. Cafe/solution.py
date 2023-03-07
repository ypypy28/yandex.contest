from math import inf
from collections import namedtuple


DP = namedtuple("DP", "money coupon_days")

n = int(input())
costs = [0] + [int(input()) for _ in range(n)]

dp = [[DP(inf, tuple()) for _ in range(n+1)] for _ in range(n+1)]
dp[0][0] = DP(0, tuple())
coupons = money = 0
for j in range(1, n+1):
    if costs[j] > 100:
        coupons += 1
    money += costs[j]
    dp[j][coupons] = DP(money, tuple())


for day in range(1, n+1):
    for coupon in range(0, n):
        if dp[day][coupon].money != inf:
            break
        cost_without_coupon = dp[day-1][coupon].money + costs[day]
        if costs[day] > 100 and day > 1:
            cost_without_coupon = dp[day-1][coupon-1].money + costs[day]
        cost_with_coupon = dp[day-1][coupon+1].money
        if cost_with_coupon < cost_without_coupon and coupon != n:
            money = cost_with_coupon
            coupon_days = (*dp[day-1][coupon+1].coupon_days, day)
        else:
            money = cost_without_coupon
            coupon_days = dp[day-1][coupon].coupon_days
            if costs[day] > 100 and day > 1:
                coupon_days = dp[day-1][coupon-1].coupon_days
        dp[day][coupon] = DP(money, coupon_days)

# print()
# print('\n'.join(' '.join(f"{x.money:>3}" for x in line) for line in dp), sep='\n')


min_sum = min(dp[n])
k1 = dp[n].index(min_sum)
for i in range(k1+1, len(dp[n])):
    if dp[n][i].money != min_sum.money:
        break
    k1 = i

k2 = len(min_sum.coupon_days)
print(min_sum.money,
      f"{k1} {k2}",
      '\n'.join(f'{x}' for x in min_sum.coupon_days),
      sep='\n')
