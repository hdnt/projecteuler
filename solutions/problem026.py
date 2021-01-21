def solve(max_num=1000):
    max_rems = -1
    res = -1
    for num in range(max_num, 1, -1):
        rems = set()
        rem = 1 % num
        while rem != 0 and rem not in rems:
            rems.add(rem)
            rem = (rem*10) % num
        if len(rems) > max_rems:
            max_rems = len(rems)
            res = num
    return res
