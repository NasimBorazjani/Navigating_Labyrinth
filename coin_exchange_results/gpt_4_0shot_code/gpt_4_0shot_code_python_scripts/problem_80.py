
def taxed_coin_exchange(coins, tax, total):
    n = len(coins)
    dp = [[0 if j == 0 else float('inf') for j in range(total+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, total+1):
            if coins[i-1] <= j:
                dp[i][j] = min(dp[i-1][j], tax[coins[i-1]] + dp[i-1][j-coins[i-1]])
            else:
                dp[i][j] = dp[i-1][j]
    result = []
    i, j = n, total
    while i > 0 and j > 0:
        if dp[i][j] != dp[i-1][j]:
            result.append(coins[i-1])
            j -= coins[i-1]
        i -= 1
    return result[::-1]

coins = [8, 7, 5, 24, 3, 18, 36, 39, 36, 25, 25, 33, 16, 20, 34, 9, 1, 22, 25, 13, 8, 37, 35, 39, 11, 26, 36, 25, 25, 27, 2, 4, 35, 2, 16, 22, 12, 15, 19, 2, 17, 25, 28, 12, 26, 17, 33, 5, 30, 3, 21, 3]
tax = {13: 7, 39: 4, 20: 18, 5: 1, 12: 7, 9: 5, 28: 20, 24: 11, 3: 3, 17: 3, 21: 9, 37: 6, 16: 8, 15: 1, 26: 10, 36: 6, 22: 9, 2: 2, 8: 1, 25: 20, 4: 3, 7: 5, 19: 7, 30: 6, 27: 12, 1: 1, 34: 7, 35: 5, 11: 6, 18: 12, 33: 4}
total = 397
print(taxed_coin_exchange(coins, tax, total))
