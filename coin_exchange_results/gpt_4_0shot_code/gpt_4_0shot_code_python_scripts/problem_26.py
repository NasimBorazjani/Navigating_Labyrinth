
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

coins = [29, 29, 22, 23, 23, 3, 26, 9, 15, 8, 21, 15, 29, 25, 71, 27, 23, 6, 7, 9, 15, 21, 6, 8, 19, 17, 18, 6, 26, 24, 24, 3, 25, 2]
tax = {24: 14, 2: 1, 25: 2, 26: 14, 18: 12, 27: 15, 29: 19, 19: 3, 15: 7, 9: 1, 8: 1, 21: 18, 6: 1, 71: 3, 23: 4, 17: 7, 7: 2, 22: 11, 3: 1}
total = 307
print(taxed_coin_exchange(coins, tax, total))
