def solve(n=999, a=3, b=5):
    num_a = n // a
    res_a = (num_a * (num_a + 1) * a) // 2
    num_b = n // b
    res_b = (num_b * (num_b + 1) * b) // 2
    num_ab = n // (a*b)
    res_ab = (num_ab * (num_ab + 1) * (a*b)) // 2
    return res_a + res_b - res_ab
