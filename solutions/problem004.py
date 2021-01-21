def is_palindrome(n):
    return str(n) == str(n)[::-1]


def solve():
    a = 100
    b = 110
    res = 0
    while b < 1000:
        while a < 1000:
            if is_palindrome(a*b):
                res = max(res, a*b)
            a += 1
        a = 100
        b += 11
    return res
