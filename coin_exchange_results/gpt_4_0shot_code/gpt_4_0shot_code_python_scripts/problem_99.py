
def min_tax(coins, taxes, total):
    n = len(coins)
    dp = [[0 if j == 0 else float('inf') for j in range(total + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, total + 1):
            if coins[i - 1] <= j:
                dp[i][j] = min(dp[i - 1][j], taxes[coins[i - 1]] + dp[i - 1][j - coins[i - 1]])
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

coins = [37, 4, 1, 15, 2, 7, 8, 33, 35, 14, 47, 36, 41, 44, 13, 31, 3, 7, 27, 25, 26, 38, 10, 19, 7, 18, 32, 45, 29, 35, 44, 17, 40, 13, 14, 40, 28, 15, 23, 11, 7, 16, 7, 35, 31, 45, 14, 22, 7, 36, 31]
taxes = {44: 2, 1: 1, 36: 14, 26: 2, 22: 10, 33: 13, 16: 12, 23: 1, 41: 6, 8: 6, 18: 3, 13: 5, 2: 2, 7: 5, 29: 13, 25: 19, 3: 1, 45: 12, 35: 13, 17: 6, 47: 13, 10: 8, 15: 14, 31: 13, 4: 2, 14: 2, 32: 11, 40: 3, 11: 4, 28: 7, 37: 12, 27: 11, 19: 17, 38: 18}
total = 465
print(min_tax(coins, taxes, total))
