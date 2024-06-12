
def taxed_coin_exchange(coins, tax, total):
    n = len(coins)
    dp = [[(0, []) for _ in range(total + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, total + 1):
            if coins[i - 1] <= j:
                if (dp[i - 1][j - coins[i - 1]][0] + tax[coins[i - 1]], dp[i - 1][j - coins[i - 1]][1] + [coins[i - 1]]) < (dp[i - 1][j][0], dp[i - 1][j][1]):
                    dp[i][j] = (dp[i - 1][j - coins[i - 1]][0] + tax[coins[i - 1]], dp[i - 1][j - coins[i - 1]][1] + [coins[i - 1]])
                else:
                    dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][total][1]

coins = [3, 35, 33, 20, 31, 29, 12, 31, 8, 10, 3, 17, 2, 28, 6, 25, 10, 13, 31, 25, 37, 35, 9, 15, 113, 26, 18, 34, 30]
tax = {31: 11, 15: 6, 13: 13, 28: 1, 9: 6, 20: 1, 34: 15, 6: 5, 113: 20, 12: 6, 2: 1, 29: 10, 37: 2, 25: 11, 26: 10, 3: 3, 33: 19, 8: 7, 18: 6, 17: 7, 10: 8, 35: 11, 30: 16}
total = 384
print(taxed_coin_exchange(coins, tax, total))
