def solve(max_total=200):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    table = [[0 for _ in range(max_total + 1)] for row in range(len(coins))]
    for idx in range(max_total + 1):
        table[0][idx] = 1
    for row in range(1, len(coins)):
        for total in range(max_total + 1):
            table[row][total] = table[row - 1][total]
            if total // coins[row]:
                table[row][total] += table[row][total - coins[row]]
    return table[-1][-1]
