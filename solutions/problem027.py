import lib.primes


def solve():
    longest = -1
    res = -1
    primes = lib.primes.sieve(10000000)
    for b in range(1001):
        if primes[b]:
            for a in range(-999, 1000):
                n = 0
                while primes[n**2 + a*n + b]:
                    n += 1
                if n > longest:
                    longest = n
                    res = a*b
    return res
