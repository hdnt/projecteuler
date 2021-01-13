import mymath


def solve(upper):
    prime_lst = mymath.prime_list(upper)
    amicables = []
    table = {}
    for a in range(1, upper):
        b = mymath.sum_of_divisors(a, prime_lst)
        b -= a
        table[a] = b
        if a != b and b in table and table[b] == a:
            amicables.append(a)
            amicables.append(b)
    return sum(amicables)


if __name__ == "__main__":
    print(solve(10000))
