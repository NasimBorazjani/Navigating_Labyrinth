
def min_tax(coins, tax, total):
    n = len(coins)
    dp = [[float('inf')] * (total + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        for j in range(total + 1):
            if coins[i - 1] <= j:
                if i > 1 and coins[i - 1] < coins[i - 2] and coins[i - 1] % 2 == 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - coins[i - 1]] + tax[coins[i - 1]])
                elif i == 1 or coins[i - 1] >= coins[i - 2] and coins[i - 1] % 2 != 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - coins[i - 1]] + tax[coins[i - 1]])
            dp[i][j] = min(dp[i][j], dp[i - 1][j])
    res = []
    i, j = n, total
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            res.append(coins[i - 1])
            j -= coins[i - 1]
        i -= 1
    return res[::-1]

coins = [18, 26, 17, 17, 16, 27, 30, 3, 4, 2, 24, 26, 29, 23, 2, 31, 25, 25, 4, 24, 14, 29, 4, 34, 34, 23, 35, 23, 28, 18, 8, 10, 17, 8, 22, 32]
tax = {27: 14, 14: 1, 18: 3, 22: 9, 10: 8, 3: 2, 32: 20, 35: 16, 8: 3, 30: 20, 25: 18, 4: 3, 28: 12, 26: 16, 29: 2, 24: 20, 16: 6, 17: 3, 31: 9, 2: 2, 23: 17, 34: 17}
total = 342
print(min_tax(coins, tax, total))
