def solve():
    data = open("../input_data/problem013.txt", "r")
    res = 0
    for line in data:
        res += int(line)
    print(str(res)[:10])


solve()
