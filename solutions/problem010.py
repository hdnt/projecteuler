import lib.primes


def solve(n=2*10**6):
    arr = lib.primes.sieve(n)
    res = 0
    for idx in range(len(arr)):
        res += idx if arr[idx] else 0
    return res
