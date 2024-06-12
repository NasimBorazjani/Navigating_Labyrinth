
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
    result.reverse()
    return result

coins = [21, 20, 21, 11, 23, 16, 16, 16, 3, 20, 2, 19, 16, 21, 18, 7, 20, 3, 16, 18, 7, 22, 3, 22, 7, 21, 12, 22, 5, 6, 17, 16, 8, 8, 14, 4, 18, 9, 4, 20, 2]
tax = {6: 1, 7: 3, 9: 1, 18: 1, 2: 1, 11: 7, 5: 3, 12: 2, 3: 3, 22: 6, 14: 3, 20: 15, 4: 3, 17: 4, 16: 8, 23: 18, 21: 16, 19: 2, 8: 6}
total = 228
print(taxed_coin_exchange(coins, tax, total))
