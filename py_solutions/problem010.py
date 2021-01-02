import mymath


def solve(n):
    arr = mymath.sieve(n)
    res = 0
    for idx in range(len(arr)):
        res += idx if arr[idx] else 0
    return res


if __name__ == "__main__":
    print(solve(2*10**6))
