m = 10**9 + 7


def solve(k=1001):
    return ((4*k**3 + 3*k**2 + 8*k - 15)//6 + 1) % m
