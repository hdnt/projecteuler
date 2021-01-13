import math
import itertools


def sieve(n: int) -> list:
    arr = [True for _ in range(n + 1)]
    arr[0] = arr[1] = False
    for i in range(2, math.ceil(math.sqrt(len(arr) + 1))):
        if arr[i]:
            for j in range(i * 2, len(arr), i):
                arr[j] = False
    return arr


def prime_list(upper_limit: int) -> list:
    res = []
    sieve_list = sieve(upper_limit)
    for idx in range(len(sieve_list)):
        if sieve_list[idx]:
            res.append(idx)
    return res


def prime_factors(n: int, prime_lst: list) -> dict:
    res = {}
    idx = 0
    while n > 1 and prime_lst[idx] <= n:
        while n % prime_lst[idx] == 0:
            res[prime_lst[idx]] = res[prime_lst[idx]] + 1 if prime_lst[idx] in res else 1
            n //= prime_lst[idx]
        idx += 1
    return res


def prime_factors_list(n: int, prime_lst: list) -> list:
    arr = []
    primes_dict = prime_factors(n, prime_lst)
    for key in primes_dict.keys():
        for i in range(primes_dict[key]):
            arr.append(key)
    return arr


def divisors_list(n: int, prime_lst: list) -> list:
    res = {1}
    combs = itertools.combinations
    primes = prime_factors_list(n, prime_lst)
    for size in range(1, len(primes)):
        for comb in combs(primes, size):
            res.add(math.prod(comb))
    return sorted(list(res))


def sum_of_divisors(n: int, prime_lst: list) -> int:
    arr = []
    pfs = prime_factors(n, prime_lst)
    for prime in pfs.keys():
        arr.append((prime**(pfs[prime] + 1) - 1) // (prime - 1))
    return math.prod(arr)


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


def my_comb(n, k):
    fac = math.factorial
    return fac(n) // (fac(k) * fac(n - k))
