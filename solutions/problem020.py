from math import factorial as fac


def solve(n=100):
    return sum([int(x) for x in str(fac(n))])
