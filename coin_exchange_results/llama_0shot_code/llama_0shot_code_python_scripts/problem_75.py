
def taxed_coin_exchange(coins, taxes):
    n = len(coins)
    coins.sort()
    dp = [float('inf')] * (408 + 1)
    dp[0] = 0
    for i in range(n):
        for j in range(coins[i], 408 + 1):
            dp[j] = min(dp[j], dp[j - coins[i]] + taxes[coins[i]])
            if i > 0 and coins[i] < coins[i - 1]:
                dp[j] = min(dp[j], dp[j - coins[i] - 1] + taxes[coins[i]] + taxes[coins[i - 1]] // 2)
    return dp[408]

coins = [8, 31, 28, 24, 19, 18, 26, 31, 43, 32, 3, 21, 21, 10, 36, 40, 19, 38, 3, 5, 24, 12, 11, 14, 40, 7, 19, 4, 22, 5, 33, 31, 40, 7, 5, 34, 33, 22, 14, 6, 14, 29]
taxes = {31: 12, 40: 17, 32: 19, 26: 14, 12: 1, 5: 3, 36: 1, 33: 5, 3: 2, 6: 1, 34: 19, 18: 18, 8: 7, 21: 11, 43: 20, 22: 20, 4: 4, 11: 6, 28: 20, 7: 3, 38: 13, 24: 12, 19: 16, 10: 7, 14: 9, 29: 3}
print(taxed_coin_exchange(coins, taxes))
