import lib.primes


def solve():
    arr = lib.primes.sieve(10**6)
    count = 0
    i = 2
    while count < 10001:
        count += 1 if arr[i] else 0
        if count == 10001:
            return i
        i += 1
