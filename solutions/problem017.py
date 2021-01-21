def solve():
    res = 0
    sum_one_nine = sum([3,3,5,4,4,3,5,5,4])
    sum_ten_nineteen = sum([3,6,6,8,8,7,7,9,8,8])
    sum_twenty_ninety = sum([6,6,5,5,5,7,6,6])
    hundred = 7
    res += sum_one_nine * 90
    res += sum_ten_nineteen * 10
    res += sum_twenty_ninety * 100
    res += sum_one_nine * 100
    res += hundred * 900
    res += 3 * 99 * 9
    res += 11
    return res
