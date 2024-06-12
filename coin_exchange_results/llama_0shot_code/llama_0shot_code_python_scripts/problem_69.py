
def taxed_coin_exchange(coins, tax):
    total_value = 423
    dp = [float('inf')] * (total_value + 1)
    dp[0] = 0
    sorted_coins = sorted(coins)
    for coin in sorted_coins:
        for i in range(total_value, coin - 1, -1):
            dp[i] = min(dp[i], dp[i - coin] + tax[coin])
    return dp[-1]

coins = [28, 11, 40, 15, 21, 6, 20, 6, 12, 22, 8, 18, 34, 24, 22, 30, 35, 41, 6, 39, 5, 15, 19, 8, 26, 38, 11, 29, 31, 14, 37, 28, 8, 11, 28, 27, 38]
tax = {40: 1, 41: 13, 8: 5, 28: 2, 21: 18, 15: 7, 5: 4, 14: 13, 37: 12, 22: 12, 29: 3, 30: 15, 35: 4, 26: 19, 39: 7, 31: 14, 11: 7, 20: 3, 6: 2, 12: 8, 27: 13, 19: 19, 34: 5, 18: 9, 38: 16, 24: 17}

print(taxed_coin_exchange(coins, tax))
