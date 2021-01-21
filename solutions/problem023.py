import lib.primes
import lib.divisors
from itertools import combinations as combs


def is_abundant(n: int, prime_lst: list) -> int:
    return lib.divisors.sum_of_divisors(n, prime_lst) - n > n


def solve(upper_limit: int = 28123) -> int:
    prime_lst = lib.primes.prime_list(upper_limit)
    abundants = []
    can_sum = set()
    res = 0
    for num in range(1, upper_limit + 1):
        if is_abundant(num, prime_lst):
            abundants.append(num)
            can_sum.add(num*2)
    for comb in combs(abundants, 2):
        can_sum.add(sum(comb))
    for num in range(1, upper_limit + 1):
        if num not in can_sum:
            res += num
    return res
