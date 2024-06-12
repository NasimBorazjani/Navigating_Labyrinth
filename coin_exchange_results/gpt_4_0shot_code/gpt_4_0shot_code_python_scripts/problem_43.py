
def min_tax(coins, tax, total):
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

coins = [69, 32, 32, 6, 19, 13, 21, 68, 32, 16, 21, 29, 20, 13, 21, 24, 26, 5, 23, 18, 16, 24, 2, 17, 15, 30, 26]
tax = {30: 3, 20: 11, 24: 15, 26: 6, 68: 2, 29: 5, 13: 2, 2: 1, 17: 2, 32: 11, 18: 4, 15: 9, 5: 3, 21: 11, 69: 19, 6: 3, 16: 4, 23: 17, 19: 15}
total = 322
print(min_tax(coins, tax, total))
