import math


def my_sum(a, b):
    a -= 1
    sum_1_to_b = (b*(b+1)) // 2
    sum_1_to_a = (a*(a+1)) // 2
    return sum_1_to_b - sum_1_to_a


def my_sum_squares(a, b):
    a -= 1
    sum_1_to_b = (b*(b+1)*(2*b+1)) // 6
    sum_1_to_a = (a*(a+1)*(2*a+1)) // 6
    return sum_1_to_b - sum_1_to_a


def my_comb(n, k):
    fac = math.factorial
    return fac(n) // (fac(k) * fac(n - k))
