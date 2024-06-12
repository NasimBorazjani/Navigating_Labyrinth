
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

coins = [31, 9, 2, 24, 32, 6, 13, 29, 33, 22, 12, 28, 10, 7, 33, 15, 28, 7, 14, 26, 1, 10, 28, 30, 7, 29, 17, 2, 28, 13, 28, 17, 3, 4, 4, 4, 13, 3, 19, 2, 4, 26, 27, 27, 11, 25, 12]
taxes = {2: 1, 33: 8, 9: 9, 31: 3, 19: 11, 17: 8, 28: 3, 24: 12, 6: 1, 22: 7, 26: 7, 27: 5, 29: 9, 4: 4, 10: 3, 3: 2, 11: 3, 15: 12, 7: 2, 1: 1, 12: 3, 30: 2, 14: 12, 32: 7, 13: 2, 25: 9}
total = 337
print(taxed_coin_exchange(coins, taxes, total))
