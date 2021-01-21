def solve():
    data = open("./data/problem013.txt", "r")
    res = 0
    for line in data:
        res += int(line)
    return str(res)[:10]
