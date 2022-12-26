import math


n = int(input())

DIVISOR = 10**9 + 7


def combinations(n, k):
    if n < k:
        return 0

    sub = n - k
    if sub < k:
        sub, k = k, sub

    rest = 1
    for num in range(sub+1, n+1):
        rest *= num

    return rest  // math.factorial(k) % DIVISOR


    # return math.factorial(n)//(math.factorial(n-k) * math.factorial(k))


def f_inclusion_exclusion(n):
    res = 0

    for k in range(n+1):
        res += (-1)**k * combinations(n, k) * 2**combinations(n-k, 2)
        res %=DIVISOR

    return res


print(n*f_inclusion_exclusion(n-1) % DIVISOR)
