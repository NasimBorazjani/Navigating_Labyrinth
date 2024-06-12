
def taxed_coin_exchange(coins, tax, target):
    n = len(coins)
    dp = [[float('inf')] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        for j in range(target + 1):
            if j < coins[i - 1] or (i > 1 and coins[i - 1] < coins[i - 2] and coins[i - 1] % 2 != 0) or (i > 1 and coins[i - 1] >= coins[i - 2] and coins[i - 1] % 2 != 1):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - coins[i - 1]] + tax[coins[i - 1]])
    result = []
    i, j = n, target
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            result.append(coins[i - 1])
            j -= coins[i - 1]
        i -= 1
    return result[::-1]

coins = [30, 28, 81, 26, 24, 20, 5, 18, 33, 19, 30, 27, 6, 10, 22, 10, 33, 10, 15, 26, 9, 6, 22, 31, 36, 16, 4, 11, 24, 7, 17, 30, 3, 7, 8, 8, 34]
tax = {24: 7, 22: 3, 11: 10, 28: 17, 7: 7, 20: 10, 5: 2, 8: 2, 9: 5, 15: 14, 81: 17, 30: 5, 31: 17, 33: 9, 18: 3, 36: 2, 16: 14, 10: 1, 19: 15, 3: 1, 34: 12, 26: 13, 6: 3, 4: 1, 27: 11, 17: 5}
target = 387
print(taxed_coin_exchange(coins, tax, target))
