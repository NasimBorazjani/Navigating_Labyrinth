
def taxed_coin_exchange(coins, tax, target):
    n = len(coins)
    dp = [[float('inf')] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        for j in range(target + 1):
            if j < coins[i - 1] or (i > 1 and coins[i - 1] < coins[i - 2] and coins[i - 1] % 2 == 1) or (i > 1 and coins[i - 1] >= coins[i - 2] and coins[i - 1] % 2 == 0):
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

coins = [20, 10, 16, 21, 15, 21, 13, 6, 19, 9, 7, 5, 2, 6, 9, 22, 4, 13, 3, 16, 22, 18, 6, 5, 14, 7, 7, 2, 17, 9, 8, 83, 14]
tax = {22: 18, 21: 1, 14: 12, 10: 8, 8: 6, 17: 9, 6: 4, 7: 6, 9: 3, 20: 13, 19: 12, 5: 3, 13: 8, 4: 3, 83: 14, 3: 2, 18: 1, 2: 1, 16: 2, 15: 3}
target = 239
print(taxed_coin_exchange(coins, tax, target))
