def right_prod(arr, row, col):
    return arr[row][col] * arr[row][col+1] * arr[row][col+2] * arr[row][col+3]


def down_prod(arr, row, col):
    return arr[row][col] * arr[row+1][col] * arr[row+2][col] * arr[row+3][col]


def diag_right_prod(arr, row, col):
    return arr[row][col] * arr[row+1][col+1] * arr[row+2][col+2] * arr[row+3][col+3]


def diag_left_prod(arr, row, col):
    return arr[row][col] * arr[row+1][col-1] * arr[row+2][col-2] * arr[row+3][col-3]


def solve():
    arr = []

    data = open("./data/problem011.txt", "r")
    for line in data:
        arr.append([int(n) for n in line.split()])

    res = 0

    for row in range(len(arr)):
        for col in range(len(arr[0])):
            if col < len(arr[0]) - 3:
                res = max(res, right_prod(arr, row, col))
            if row < len(arr) - 3:
                res = max(res, down_prod(arr, row, col))
            if col < len(arr[0]) - 3 and row < len(arr) - 3:
                res = max(res, diag_right_prod(arr, row, col))
            if col > 2 and row < len(arr) - 3:
                res = max(res, diag_left_prod(arr, row, col))

    return res
