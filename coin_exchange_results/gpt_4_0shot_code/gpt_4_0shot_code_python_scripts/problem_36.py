
def taxed_coin_exchange(coins, tax, total):
    n = len(coins)
    dp = [[0 if j == 0 else float('inf') for j in range(total + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, total + 1):
            if coins[i - 1] <= j:
                dp[i][j] = min(dp[i - 1][j], tax[coins[i - 1]] + dp[i - 1][j - coins[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]
    result = []
    i, j = n, total
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            result.append(coins[i - 1])
            j -= coins[i - 1]
        i -= 1
    return result[::-1]

coins = [26, 7, 24, 27, 19, 15, 12, 13, 19, 5, 17, 26, 20, 7, 3, 21, 22, 7, 17, 13, 28, 11, 19, 18, 9, 10, 25, 2, 4, 18, 14, 17, 22, 27, 14, 7, 9, 2, 11, 8, 14, 10, 18, 1, 4, 24, 2, 24, 11, 14, 27]
tax = {13: 8, 27: 5, 21: 13, 25: 11, 22: 6, 20: 14, 12: 1, 14: 12, 2: 2, 8: 5, 3: 2, 18: 4, 1: 1, 9: 9, 10: 1, 19: 10, 11: 5, 28: 10, 5: 3, 26: 7, 7: 1, 24: 9, 4: 3, 15: 2, 17: 13}
total = 281
print(taxed_coin_exchange(coins, tax, total))
