
def taxed_coin_exchange(coins, tax):
    total_value = 337
    dp = [float('inf')] * (total_value + 1)
    dp[0] = 0
    sorted_coins = sorted(coins)
    for coin in sorted_coins:
        for i in range(total_value, coin - 1, -1):
            dp[i] = min(dp[i], dp[i - coin] + tax[coin])
    return dp[-1]

coins = [31, 9, 2, 24, 32, 6, 13, 29, 33, 22, 12, 28, 10, 7, 33, 15, 28, 7, 14, 26, 1, 10, 28, 30, 7, 29, 17, 2, 28, 13, 28, 17, 3, 4, 4, 4, 13, 3, 19, 2, 4, 26, 27, 27, 11, 25, 12]
tax = {2: 1, 33: 8, 9: 9, 31: 3, 19: 11, 17: 8, 28: 3, 24: 12, 6: 1, 22: 7, 26: 7, 27: 5, 29: 9, 4: 4, 10: 3, 3: 2, 11: 3, 15: 12, 7: 2, 1: 1, 12: 3, 30: 2, 14: 12, 32: 7, 13: 2, 25: 9}

print(taxed_coin_exchange(coins, tax))
