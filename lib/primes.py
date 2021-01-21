import math


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
    for prime in prime_lst:
        while n % prime == 0:
            res[prime] = res[prime] + 1 if prime in res else 1
            n //= prime
    return res


def prime_factors_list(n: int, prime_lst: list) -> list:
    arr = []
    primes_dict = prime_factors(n, prime_lst)
    for key in primes_dict.keys():
        for i in range(primes_dict[key]):
            arr.append(key)
    return arr
