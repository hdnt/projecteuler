m = 10**9 + 7


def solve(k):
    return ((4*k**3 + 3*k**2 + 8*k - 15)//6 + 1) % m


if __name__ == "__main__":
    print(solve(1001))