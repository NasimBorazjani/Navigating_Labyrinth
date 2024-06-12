
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

coins = [9, 11, 7, 9, 12, 19, 29, 21, 11, 10, 26, 22, 18, 29, 19, 11, 18, 23, 26, 16, 18, 4, 22, 25, 17, 18, 12, 23, 3, 17, 17, 15, 22, 25, 27, 2, 26, 22, 21, 28, 10, 23, 15]
tax = {28: 16, 10: 8, 21: 8, 18: 12, 27: 6, 7: 7, 2: 2, 19: 4, 17: 13, 26: 11, 12: 1, 9: 5, 25: 15, 29: 20, 11: 2, 15: 8, 22: 1, 16: 13, 4: 4, 3: 3, 23: 18}
target = 296
print(taxed_coin_exchange(coins, tax, target))
