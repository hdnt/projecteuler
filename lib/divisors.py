import math
import itertools
import lib.primes


def divisors_list(n: int, prime_lst: list) -> list:
    res = {1}
    combs = itertools.combinations
    _primes = lib.primes.prime_factors_list(n, prime_lst)
    for size in range(1, len(_primes)):
        for comb in combs(_primes, size):
            res.add(math.prod(comb))
    return sorted(list(res))


def sum_of_divisors(n: int, prime_lst: list) -> int:
    arr = []
    pfs = lib.primes.prime_factors(n, prime_lst)
    for prime in pfs.keys():
        arr.append((prime**(pfs[prime] + 1) - 1) // (prime - 1))
    return math.prod(arr)
