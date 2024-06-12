
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

coins = [4, 2, 18, 5, 18, 13, 22, 15, 5, 14, 15, 21, 23, 13, 19, 22, 6, 12, 19, 8, 15, 8, 12, 15, 11, 17, 7, 19, 23, 9, 3, 4, 12, 10, 11, 2, 22, 19, 19, 11, 18, 6, 10, 23, 20, 1, 6, 23, 8, 6]
tax = {21: 18, 1: 1, 13: 3, 20: 2, 19: 7, 5: 4, 18: 4, 4: 1, 15: 5, 12: 7, 17: 5, 22: 10, 8: 3, 7: 5, 23: 11, 9: 7, 10: 8, 3: 2, 14: 4, 6: 1, 2: 2, 11: 10}
total = 233
print(taxed_coin_exchange(coins, tax, total))
