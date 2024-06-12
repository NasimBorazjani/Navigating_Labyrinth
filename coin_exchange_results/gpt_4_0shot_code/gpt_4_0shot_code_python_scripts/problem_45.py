
def taxed_coin_exchange(coins, taxes, total):
    n = len(coins)
    dp = [[0 if j == 0 else float('inf') for j in range(total + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, total + 1):
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

coins = [21, 10, 19, 6, 20, 7, 23, 18, 4, 15, 4, 13, 2, 5, 32, 28, 113, 3, 9, 9, 11, 21, 112, 6, 6, 11, 29]
taxes = {10: 7, 5: 3, 11: 3, 23: 2, 21: 13, 19: 3, 18: 18, 29: 20, 3: 2, 9: 7, 20: 18, 6: 2, 112: 20, 2: 1, 4: 4, 7: 4, 32: 1, 15: 8, 13: 10, 28: 17, 113: 18}
total = 337
print(taxed_coin_exchange(coins, taxes, total))
