import math
n = int(input())

DIVISOR = 10**9 + 7

def combinations(n, k):
    if n < k:
        return 0
    return math.factorial(n)//(math.factorial(n-k) * math.factorial(k))


def f_inclusion_exclusion(n):
    res = 0
    for k in range(n+1):
        res += (-1)**k * combinations(n, k) * 2**combinations(n-k, 2) % DIVISOR

    return res


print(n*f_inclusion_exclusion(n-1) % DIVISOR)
