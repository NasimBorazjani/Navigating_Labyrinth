
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
    result.reverse()
    return result

coins = [8, 31, 28, 24, 19, 18, 26, 31, 43, 32, 3, 21, 21, 10, 36, 40, 19, 38, 3, 5, 24, 12, 11, 14, 40, 7, 19, 4, 22, 5, 33, 31, 40, 7, 5, 34, 33, 22, 14, 6, 14, 29]
tax = {31: 12, 40: 17, 32: 19, 26: 14, 12: 1, 5: 3, 36: 1, 33: 5, 3: 2, 6: 1, 34: 19, 18: 18, 8: 7, 21: 11, 43: 20, 22: 20, 4: 4, 11: 6, 28: 20, 7: 3, 38: 13, 24: 12, 19: 16, 10: 7, 14: 9, 29: 3}
total = 408
print(min_tax(coins, tax, total))
