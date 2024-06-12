
def taxed_coin_exchange(coins, tax, total):
    n = len(coins)
    dp = [[0 if j == 0 else float('inf') for j in range(total + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, total + 1):
            if coins[i - 1] <= j:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - coins[i - 1]] + tax[coins[i - 1]])
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

coins = [46, 10, 4, 8, 2, 22, 26, 49, 4, 19, 2, 9, 23, 28, 6, 21, 9, 14, 15, 21, 22, 3, 14, 2, 28, 13, 20, 2, 28, 7, 16, 27, 22, 18, 28, 10, 14, 14, 4, 20, 18]
tax = {21: 14, 19: 16, 4: 3, 23: 10, 10: 3, 18: 7, 9: 3, 27: 13, 20: 12, 13: 9, 26: 17, 3: 3, 6: 6, 49: 16, 2: 2, 15: 7, 28: 13, 46: 10, 8: 3, 7: 6, 22: 20, 14: 5, 16: 8}
total = 294
print(taxed_coin_exchange(coins, tax, total))
