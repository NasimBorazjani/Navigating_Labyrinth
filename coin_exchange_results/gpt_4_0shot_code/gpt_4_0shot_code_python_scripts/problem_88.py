
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

coins = [21, 31, 30, 31, 10, 17, 13, 35, 12, 2, 16, 40, 23, 10, 29, 13, 23, 2, 9, 5, 107, 46, 23, 11, 42, 9, 46, 28, 44, 22, 106, 10]
taxes = {13: 9, 106: 19, 28: 20, 44: 14, 9: 6, 35: 6, 22: 19, 46: 17, 11: 7, 40: 12, 17: 15, 10: 4, 12: 6, 30: 20, 2: 2, 23: 11, 42: 10, 16: 1, 107: 11, 21: 12, 5: 3, 31: 13, 29: 20}
total = 465
print(taxed_coin_exchange(coins, taxes, total))
