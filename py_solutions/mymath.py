import math


def prime_factors(n: int) -> dict:
    res = {}
    while n % 2 == 0:
        res[2] = res[2] + 1 if 2 in res else 1
        n //= 2
    i = 3
    while i <= math.ceil(math.sqrt(n)):
        if n % i == 0:
            while n % i == 0:
                res[i] = res[i] + 1 if i in res else 1
                n //= i
            i = 3
        else:
            i += 2
    res[n] = res[n] + 1 if n in res else 1
    return res


def sieve(n: int) -> list:
    arr = [True for _ in range(n + 1)]
    arr[0] = arr[1] = False
    for i in range(2, math.ceil(math.sqrt(len(arr) + 1))):
        if arr[i]:
            for j in range(i * 2, len(arr), i):
                arr[j] = False
    return arr


def my_sum(a, b):
    a -= 1
    sum_1_to_b = (b*(b+1)) // 2
    sum_1_to_a = (a*(a+1)) // 2
    return sum_1_to_b - sum_1_to_a


def my_sum_squares(a, b):
    a -= 1
    sum_1_to_b = (b*(b+1)*(2*b+1)) // 6
    sum_1_to_a = (a*(a+1)*(2*a+1)) // 6
    return sum_1_to_b - sum_1_to_a
