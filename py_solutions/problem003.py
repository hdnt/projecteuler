from math import sqrt, ceil


def solve(n):
    while n % 2 == 0:
        n //= 2
    i = 3
    while i < ceil(sqrt(n)):
        if n % i == 0:
            while n % i == 0:
                n //= i
            i = 3
        else:
            i += 2
    return n


if __name__ == "__main__":
    print(solve(600851475143))
