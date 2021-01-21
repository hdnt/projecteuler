from itertools import permutations as perms


def solve(n=9):
    s = "".join([str(x) for x in range(1, n + 1)])
    res = set()
    for perm in perms(s):
        perm = "".join(perm)
        for b in range(1, n//2):
            for c in range(b + 1, n):
                if int(perm[:b]) * int(perm[b:c]) == int(perm[c:]):
                    res.add(int(perm[c:]))
    return sum(res)
