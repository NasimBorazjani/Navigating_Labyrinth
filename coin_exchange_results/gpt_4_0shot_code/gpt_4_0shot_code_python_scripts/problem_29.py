
def taxed_coin_exchange(coins, tax, target):
    n = len(coins)
    dp = [[0 if j == 0 else float('inf') for j in range(target + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if coins[i - 1] <= j:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - coins[i - 1]] + tax[coins[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]
    result = []
    i, j = n, target
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            result.append(coins[i - 1])
            j -= coins[i - 1]
        i -= 1
    result.reverse()
    return result

coins = [5, 21, 4, 18, 17, 13, 27, 10, 27, 21, 25, 22, 27, 29, 28, 15, 16, 12, 7, 19, 8, 19, 9, 21, 29, 15, 15, 23, 8, 13, 20, 9, 13, 16, 3, 14, 11, 15, 2, 23, 18, 4]
tax = {14: 2, 12: 11, 20: 5, 4: 2, 23: 12, 28: 1, 25: 8, 27: 3, 19: 1, 21: 6, 16: 2, 29: 7, 13: 5, 17: 2, 22: 15, 10: 1, 15: 1, 3: 2, 8: 5, 5: 4, 9: 1, 7: 2, 2: 2, 18: 17, 11: 1}
target = 295
print(taxed_coin_exchange(coins, tax, target))
