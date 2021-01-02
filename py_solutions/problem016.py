def solve(n):
    return sum([int(letter) for letter in str(2**n)])


if __name__ == "__main__":
    print(solve(1000))
