
def taxed_coin_exchange(coins, tax, total_value):
    dp = [float('inf')] * (total_value + 1)
    dp[0] = 0
    for coin in sorted(coins):
        for i in range(total_value, coin - 1, -1):
            dp[i] = min(dp[i], dp[i - coin] + tax[coin])
    return dp[total_value]

coins = [9, 20, 4, 23, 10, 11, 8, 6, 20, 8, 20, 12, 15, 20, 18, 16, 19, 21, 5, 6, 4, 5, 14, 5, 4, 18, 22, 7, 8, 15, 5, 15, 8, 19, 14, 12, 2, 5, 5, 15, 2, 6, 10, 18, 14, 13, 8, 10, 21, 14, 5, 18, 16, 6, 11]
tax = {20: 3, 9: 2, 23: 1, 10: 3, 5: 4, 21: 14, 22: 5, 18: 7, 16: 4, 13: 5, 2: 1, 8: 2, 19: 16, 7: 3, 6: 6, 11: 3, 14: 8, 4: 2, 12: 7, 15: 14}
total_value = 243

print(taxed_coin_exchange(coins, tax, total_value))
