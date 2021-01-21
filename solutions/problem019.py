from math import ceil, floor


def zeller(y, m, d):  # return 1 = sunday
    months = [-1, 13, 14, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    if m < 3:
        y -= 1
    k = y % 100
    j = y // 100
    return (d + floor(26*(months[m]+1)/10) + k + floor(k/4) + floor(j/4) - 2*j) % 7


def solve(sy=1901, sm=1, sd=1, ey=2000, em=12, ed=31):
    res = 0
    year, month, day = sy, sm, sd
    month += 1 if sd > 1 else 0
    while year < ey:
        while month <= 12:
            if zeller(year, month, 1) == 1:
                res += 1
            month += 1
        month = 1
        year += 1
    for month in range(1, em + 1):
        if zeller(ey, month, 1) == 1:
            res += 1
    return res
