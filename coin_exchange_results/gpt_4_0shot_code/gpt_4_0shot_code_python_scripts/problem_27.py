
def taxed_coin_exchange(coins, tax, target):
    n = len(coins)
    dp = [[float('inf')] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        for j in range(target + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= coins[i - 1] and ((i > 1 and coins[i - 1] >= coins[i - 2] and coins[i - 1] % 2 == 1) or (i > 1 and coins[i - 1] < coins[i - 2] and coins[i - 1] % 2 == 0) or i == 1):
                dp[i][j] = min(dp[i][j], dp[i - 1][j - coins[i - 1]] + tax[coins[i - 1]])
    if dp[n][target] == float('inf'):
        return []
    res = []
    i, j = n, target
    while j > 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            res.append(coins[i - 1])
            j -= coins[i - 1]
            i -= 1
    return res[::-1]

coins = [22, 4, 12, 26, 4, 9, 4, 28, 28, 8, 28, 19, 15, 20, 9, 161, 11, 28, 17, 10, 25, 15, 7, 28, 21, 24, 10, 13, 22, 4, 10, 14]
tax = {15: 2, 17: 10, 10: 3, 12: 10, 21: 12, 4: 2, 22: 1, 11: 6, 26: 9, 14: 7, 24: 12, 161: 16, 20: 15, 9: 8, 8: 1, 13: 10, 28: 6, 7: 6, 25: 6, 19: 15}
target = 301
print(taxed_coin_exchange(coins, tax, target))
