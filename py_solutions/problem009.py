def solve():
    m, n = 2, 1
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2
    while True:
        while a+b+c <= 1000:
            if a+b+c == 1000:
                return a*b*c
            m += 1
            a = m ** 2 - n ** 2
            b = 2 * m * n
            c = m ** 2 + n ** 2
        m = n + 2
        n += 1
        a = m ** 2 - n ** 2
        b = 2 * m * n
        c = m ** 2 + n ** 2


print(solve())
