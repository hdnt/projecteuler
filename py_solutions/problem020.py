from math import factorial as fac


def solve(n):
    return sum([int(x) for x in str(fac(100))])


if __name__ == "__main__":
    print(solve(100))
