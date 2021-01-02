import mymath


def solve():
    arr = mymath.sieve(10**6)
    count = 0
    i = 2
    while count < 10001:
        count += 1 if arr[i] else 0
        if count == 10001:
            return i
        i += 1


if __name__ == "__main__":
    print(solve())
