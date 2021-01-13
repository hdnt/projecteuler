def calc(tri, row, col):
    if col == 0:
        tri[row][col] += tri[row - 1][col]
    elif col == len(tri[row]) - 1:
        tri[row][col] += tri[row - 1][col - 1]
    else:
        tri[row][col] += max(tri[row - 1][col - 1], tri[row - 1][col])


def solve():
    tri = []
    data = open("../input_data/problem018.txt")
    for line in data:
        tri.append([int(x) for x in line.split()])
    for row in range(1, len(tri)):
        for col in range(len(tri[row])):
            calc(tri, row, col)
    print(max(tri[-1]))


if __name__ == "__main__":
    solve()
