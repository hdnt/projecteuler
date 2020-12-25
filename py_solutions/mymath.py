import math


def prime_factors(n: int, prime_lst: list) -> dict:
    res = {}
    for prime in prime_lst:
        while n % prime == 0:
            res[prime] = res[prime] + 1 if prime in res else 1
            n //= prime
    return res


def sieve(n: int) -> list:
    arr = [True for _ in range(n + 1)]
    arr[0] = arr[1] = False
    for i in range(2, math.ceil(math.sqrt(len(arr) + 1))):
        if arr[i]:
            for j in range(i * 2, len(arr), i):
                arr[j] = False
    return arr


def prime_list(upper_limit: int) -> list:  # used in problem 12
    res = []
    sieve_list = sieve(upper_limit)
    for idx in range(len(sieve_list)):
        if sieve_list[idx]:
            res.append(idx)
    return res


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
