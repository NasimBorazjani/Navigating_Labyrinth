
def taxed_coin_exchange(coins, tax, total):
    coins.sort()
    dp = [[0 for _ in range(total+1)] for _ in range(len(coins))]
    chosen = [[[] for _ in range(total+1)] for _ in range(len(coins))]

    for i in range(len(coins)):
        for j in range(total+1):
            if j < coins[i]:
                dp[i][j] = dp[i-1][j]
                chosen[i][j] = chosen[i-1][j]
            else:
                if i > 0 and dp[i-1][j] < dp[i-1][j-coins[i]] + tax[coins[i]]:
                    dp[i][j] = dp[i-1][j]
                    chosen[i][j] = chosen[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-coins[i]] + tax[coins[i]]
                    chosen[i][j] = chosen[i-1][j-coins[i]] + [coins[i]]

    return chosen[-1][-1]

coins = [5, 29, 12, 96, 4, 13, 8, 23, 14, 25, 18, 23, 36, 32, 17, 37, 34, 7, 9, 32, 29, 37, 30, 40, 99, 9, 2, 40, 35, 14]
tax = {14: 4, 4: 2, 18: 12, 23: 12, 36: 15, 5: 1, 12: 3, 13: 13, 9: 7, 32: 8, 99: 16, 8: 7, 96: 17, 35: 13, 29: 19, 30: 19, 7: 1, 34: 16, 37: 15, 2: 2, 17: 3, 40: 18, 25: 9}
total = 427

print(taxed_coin_exchange(coins, tax, total))
