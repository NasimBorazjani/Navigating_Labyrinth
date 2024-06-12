
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

coins = [18, 20, 11, 6, 81, 3, 9, 5, 14, 19, 30, 2, 19, 3, 9, 22, 21, 29, 6, 25, 10, 18, 27, 26, 25, 13, 15, 16, 3, 5, 23, 26, 25, 31, 15, 12]
tax = {11: 6, 6: 3, 16: 11, 23: 16, 18: 3, 31: 4, 9: 2, 3: 1, 22: 10, 10: 1, 30: 4, 81: 14, 2: 1, 14: 1, 13: 11, 15: 7, 19: 16, 25: 6, 12: 12, 29: 11, 26: 9, 5: 1, 27: 15, 20: 7, 21: 14}
total = 324
print(taxed_coin_exchange(coins, tax, total))
