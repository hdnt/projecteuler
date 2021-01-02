import mymath


def solve(max_factors):
    res = {}
    prime_lst = mymath.prime_list(1000)
    tri_num = 0
    inc = 1
    factors = 1
    while factors <= max_factors:
        factors = 1
        tri_num += inc
        inc += 1
        prime_fac_of_tri = mymath.prime_factors(tri_num, prime_lst)
        for value in prime_fac_of_tri.values():
            factors *= (value + 1)
        if factors not in res:
            res[factors] = tri_num
    return res


if __name__ == "__main__":
    ans = solve(1000)
    target = 500
    num = 10**10
    for facs in ans.keys():
        if facs > target:
            num = min(num, ans[facs])
    print(num)
