
def min_tax(coins, taxes, total):
    n = len(coins)
    dp = [[float('inf')] * (total + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        for j in range(total + 1):
            if coins[i - 1] <= j:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - coins[i - 1]] + taxes[coins[i - 1]])
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

coins = [22, 14, 13, 18, 2, 5, 14, 26, 28, 9, 20, 26, 11, 29, 2, 15, 13, 11, 28, 12, 14, 6, 3, 25, 12, 24, 4, 28, 27, 10, 20, 6, 8, 7, 37, 18, 3, 10, 27, 20, 21, 8, 11, 13, 5, 19, 4, 2]
taxes = {2: 2, 14: 13, 29: 2, 13: 3, 25: 20, 28: 18, 11: 7, 9: 1, 3: 2, 15: 3, 8: 2, 7: 1, 12: 6, 26: 9, 19: 11, 24: 1, 22: 9, 27: 17, 6: 4, 18: 14, 21: 12, 4: 3, 37: 6, 20: 16, 5: 5, 10: 6}
total = 293
print(min_tax(coins, taxes, total))
