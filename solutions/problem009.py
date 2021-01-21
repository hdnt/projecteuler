def find_triples():
    m, n = [2, 1]
    d = {}
    while n < 50:
        while m < 50:
            _a = m**2 - n**2
            _b = 2*m*n
            _c = m**2 + n**2
            for i in range(1, 1000):
                a = _a*i
                b = _b*i
                c = _c*i
                s = a+b+c
                if s in d:
                    d[s].append(a*b*c)
                else:
                    d[s] = [a*b*c]
            m += 2
        m = n + 2
        n += 1
    return d


def solve(n=1000):
    d = find_triples()
    return max(d[n])
