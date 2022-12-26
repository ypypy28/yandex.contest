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

    return rest // math.factorial(k) % DIVISOR
    # for num in range(sub+1, n+1):
    #     rest *= num
    #     rest %= DIVISOR

    # fac = math.factorial(k)

    # if math.gcd(rest, fac) != 1:
    #     return rest // fac % DIVISOR

    # return (rest % DIVISOR) // pow(fac, DIVISOR-2, DIVISOR)


def f_inclusion_exclusion(n):
    res = 0

    for k in range(n+1):
        # res += (-1)**k * combinations(n, k) * ((1 << combinations(n-k, 2)) % DIVISOR)  #2**combinations(n-k, 2)
        res += (-1)**k * combinations(n, k) * pow(2, combinations(n-k, 2), DIVISOR)
        # res += (-1)**k * combinations(n, k) * (2**combinations(n-k, 2))
        res %=DIVISOR

    return res


print(n*f_inclusion_exclusion(n-1) % DIVISOR)
