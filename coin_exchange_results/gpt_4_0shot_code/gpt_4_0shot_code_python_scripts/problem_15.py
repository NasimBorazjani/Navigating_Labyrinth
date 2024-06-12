
def taxed_coin_exchange(coins, tax, total):
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

coins = [1, 2, 17, 12, 7, 17, 2, 20, 4, 4, 17, 19, 15, 16, 18, 21, 18, 10, 3, 9, 12, 13, 8, 16, 9, 14, 13, 5, 13, 6, 20, 6, 13, 12, 8, 14, 15, 7, 10, 3, 16, 16, 9, 3, 2, 6, 9, 14, 16, 20, 11, 4, 17]
tax = {8: 5, 5: 2, 19: 2, 4: 4, 9: 2, 3: 1, 2: 2, 12: 1, 13: 6, 6: 5, 11: 1, 17: 14, 7: 4, 16: 13, 21: 10, 14: 13, 1: 1, 18: 12, 10: 10, 15: 11, 20: 20}
total = 213
print(taxed_coin_exchange(coins, tax, total))
