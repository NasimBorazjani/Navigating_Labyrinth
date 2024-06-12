
def min_tax(coins, tax, total):
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

coins = [4, 33, 14, 32, 9, 32, 2, 35, 25, 10, 11, 6, 8, 26, 10, 25, 34, 21, 13, 15, 3, 15, 25, 3, 16, 3, 2, 25, 15, 23, 31, 35, 13, 14, 5, 7, 2, 18, 10, 8, 25, 30, 13, 35, 3, 26, 33, 2, 5, 26, 26, 28, 6]
tax = {26: 4, 34: 4, 7: 5, 28: 11, 35: 8, 18: 13, 25: 19, 14: 10, 23: 7, 6: 1, 10: 5, 21: 8, 13: 13, 2: 1, 3: 1, 30: 5, 4: 4, 31: 18, 11: 3, 9: 1, 8: 3, 5: 3, 32: 5, 15: 15, 33: 18, 16: 4}
total = 355
print(min_tax(coins, tax, total))
