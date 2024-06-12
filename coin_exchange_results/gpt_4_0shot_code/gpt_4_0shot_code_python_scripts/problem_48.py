
def taxed_coin_exchange(coins, tax, target):
    n = len(coins)
    dp = [[0 if j == 0 else float('inf') for j in range(target + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if coins[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i - 1][j], tax[coins[i - 1]] + dp[i - 1][j - coins[i - 1]])
    result = []
    i, j = n, target
    while j > 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            result.append(coins[i - 1])
            j -= coins[i - 1]
            i -= 1
    return result[::-1]

coins = [19, 21, 16, 6, 34, 23, 8, 10, 14, 10, 59, 15, 17, 32, 11, 15, 8, 29, 58, 12, 3, 5, 11, 34, 2, 12, 20, 6, 29, 23, 10, 34, 33, 18]
tax = {6: 5, 17: 7, 12: 10, 34: 9, 5: 1, 11: 7, 10: 8, 21: 19, 15: 3, 33: 6, 3: 2, 16: 12, 58: 19, 8: 7, 14: 5, 20: 8, 2: 2, 19: 19, 59: 14, 18: 15, 29: 8, 23: 6, 32: 5}
target = 355
print(taxed_coin_exchange(coins, tax, target))
