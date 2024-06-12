
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

coins = [14, 29, 39, 40, 16, 35, 17, 37, 43, 30, 28, 26, 13, 13, 42, 30, 10, 7, 44, 5, 34, 7, 32, 11, 40, 35, 12, 34, 35, 38, 29, 42, 33, 26, 4, 36, 41, 35, 26, 34, 16, 6, 38, 13, 41, 23, 20]
tax = {11: 4, 10: 3, 41: 9, 34: 4, 7: 2, 17: 16, 29: 8, 37: 1, 44: 8, 30: 13, 32: 9, 20: 18, 23: 8, 6: 4, 5: 3, 14: 3, 13: 7, 35: 4, 33: 5, 39: 9, 40: 11, 28: 3, 4: 2, 43: 14, 42: 15, 38: 14, 16: 5, 36: 5, 12: 9, 26: 1}
total = 449
print(taxed_coin_exchange(coins, tax, total))
