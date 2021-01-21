import lib.primes
import lib.divisors


def solve(upper=10000):
    prime_lst = lib.primes.prime_list(upper)
    amicables = []
    table = {}
    for a in range(1, upper):
        b = lib.divisors.sum_of_divisors(a, prime_lst)
        b -= a
        table[a] = b
        if a != b and b in table and table[b] == a:
            amicables.append(a)
            amicables.append(b)
    return sum(amicables)
