def str_value(name):
    return sum([ord(letter) - ord("A") + 1 for letter in name])


def solve():
    data = open("./data/problem022.txt").read()
    names = sorted([name for name in data.split('","')])
    res = 0
    for idx in range(len(names)):
        res += (idx + 1) * str_value(names[idx])
    return res
