import mymath


def solve():
    pf = {}
    for n in range(1, 21):
        nf = mymath.prime_factors(n)
        for f in nf.keys():
            pf[f] = max(pf[f], nf[f]) if f in pf else nf[f]
    res = 1
    for f in pf.keys():
        res *= f**pf[f]
    return res


print(solve())
