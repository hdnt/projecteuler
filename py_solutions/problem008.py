from math import prod


def solve():
    s = ""
    data = open("../input_data/problem008.txt", "r")
    for line in data:
        s += line.strip()

    res = 0
    for idx in range(len(s) - 12):
        res = max(res, prod([int(x) for x in s[idx:idx+13]]))

    return res


if __name__ == "__main__":
    print(solve())
