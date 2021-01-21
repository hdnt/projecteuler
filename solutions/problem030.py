def calc(num):
    return num == sum([int(x)**5 for x in str(num)])


def solve():
    res = []
    for num in range(2, 6*9**5):
        if calc(num):
            res.append(num)
    return sum(res)
