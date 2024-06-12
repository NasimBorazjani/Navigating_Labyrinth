
def taxed_coin_exchange(coins, tax, target):
    n = len(coins)
    dp = [[float('inf')] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        for j in range(target + 1):
            if j < coins[i - 1] or (i > 1 and coins[i - 1] < coins[i - 2] and coins[i - 1] % 2 != 0) or (i > 1 and coins[i - 1] >= coins[i - 2] and coins[i - 1] % 2 == 0):
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

coins = [30, 24, 27, 14, 29, 17, 4, 21, 20, 14, 19, 23, 18, 4, 12, 9, 24, 26, 21, 17, 3, 13, 25, 20, 16, 12, 2, 9, 17, 5, 6, 24, 13, 11, 6, 15, 13, 5, 13, 25, 10, 15, 10, 3, 2, 18, 7, 23, 5, 18, 21, 6]
tax = {14: 11, 3: 1, 18: 5, 21: 1, 27: 2, 19: 14, 6: 6, 25: 8, 5: 3, 29: 4, 7: 6, 24: 10, 10: 2, 13: 9, 9: 1, 11: 8, 16: 10, 2: 1, 12: 12, 15: 4, 23: 17, 17: 9, 26: 13, 30: 17, 4: 3, 20: 6}
target = 300
print(taxed_coin_exchange(coins, tax, target))
