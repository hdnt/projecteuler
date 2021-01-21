MAX_NUMBER = 10**6 - 1
table = {1: 1}


def next_term(n):
    return n // 2 if n % 2 == 0 else 3*n + 1


def calc(n):
    global table
    if n not in table:
        table[n] = 1 + calc(next_term(n))
    return table[n]


def helper():
    global table, MAX_NUMBER
    for n in range(2, MAX_NUMBER + 1):
        if n not in table:
            calc(n)


def solve():
    helper()
    ans = 1
    for idx in range(1, MAX_NUMBER + 1):
        if table[idx] >= table[ans]:
            ans = idx
    return ans
