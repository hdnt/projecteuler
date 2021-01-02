from mymath import my_sum, my_sum_squares


def solve(n):
    return my_sum(1, n)**2 - my_sum_squares(1, n)


if __name__ == "__main__":
    print(solve(100))
