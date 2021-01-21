def solve(n=4*10**6):
    res = 0
    a = 0
    b = 2
    while b < n:
        res += b
        temp = b
        b = 4*b + a
        a = temp
    return res
