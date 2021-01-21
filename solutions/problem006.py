from lib.other import my_sum, my_sum_squares


def solve(n=100):
    return my_sum(1, n)**2 - my_sum_squares(1, n)
