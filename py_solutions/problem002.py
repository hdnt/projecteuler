def solve(n):
    res = 0
    a = 0
    b = 2
    while b < n:
        res += b
        temp = b
        b = 4*b + a
        a = temp
    return res


print(solve(4*10**6))
