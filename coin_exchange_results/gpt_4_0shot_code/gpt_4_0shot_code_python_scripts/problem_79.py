
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
    result.reverse()
    return result

coins = [33, 4, 5, 9, 31, 26, 25, 19, 31, 33, 24, 6, 13, 17, 15, 37, 7, 21, 3, 23, 22, 7, 3, 11, 19, 28, 24, 32, 27, 31, 24, 12, 23, 22, 16, 6, 33, 8, 19, 13, 5, 11, 10, 4, 8, 16, 14, 17, 13, 9, 25, 17]
tax = {3: 3, 19: 1, 5: 2, 9: 4, 17: 4, 24: 11, 8: 5, 22: 10, 4: 2, 32: 10, 16: 1, 37: 5, 23: 12, 26: 18, 12: 1, 27: 9, 14: 5, 25: 13, 15: 8, 6: 6, 21: 13, 10: 3, 31: 17, 7: 3, 33: 10, 11: 2, 28: 10, 13: 10}
total = 389
print(taxed_coin_exchange(coins, tax, total))
