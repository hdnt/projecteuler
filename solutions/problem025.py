def solve():
    fib_terms = [1, 1]
    while len(str(fib_terms[-1])) < 1000:
        fib_terms.append(fib_terms[-1] + fib_terms[-2])
    return len(fib_terms)
