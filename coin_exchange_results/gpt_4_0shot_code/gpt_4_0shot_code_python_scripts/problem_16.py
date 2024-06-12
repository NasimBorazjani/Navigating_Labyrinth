
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

coins = [11, 13, 22, 11, 16, 20, 10, 10, 17, 21, 6, 6, 15, 15, 21, 6, 4, 16, 9, 11, 3, 13, 2, 9, 11, 1, 7, 2, 2, 12, 5, 2, 11, 16, 20, 9, 2, 4, 10, 17, 11, 22, 11, 2, 18, 23, 15, 22, 11, 15, 20, 9]
tax = {6: 2, 11: 9, 3: 3, 15: 2, 9: 1, 18: 13, 22: 13, 16: 5, 21: 2, 5: 2, 12: 4, 7: 5, 4: 3, 13: 2, 1: 1, 20: 14, 2: 1, 10: 4, 23: 15, 17: 9}
target = 223
print(taxed_coin_exchange(coins, tax, target))
