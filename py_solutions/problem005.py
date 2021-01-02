import mymath


def solve():
    pf = {}
    for n in range(1, 21):
        nf = mymath.prime_factors(n, mymath.prime_list(n))
        for f in nf.keys():
            pf[f] = max(pf[f], nf[f]) if f in pf else nf[f]
    res = 1
    for f in pf.keys():
        res *= f**pf[f]
    return res


if __name__ == "__main__":
    print(solve())
