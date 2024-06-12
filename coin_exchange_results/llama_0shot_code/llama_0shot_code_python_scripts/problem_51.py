
def taxed_coin_exchange(coins, taxes, total_value):
    dp = [float('inf')] * (total_value + 1)
    dp[0] = 0
    sorted_coins = sorted(coins)
    for coin in sorted_coins:
        for i in range(total_value, coin - 1, -1):
            dp[i] = min(dp[i], dp[i - coin] + taxes[coin])
    return dp[-1]

coins = [31, 83, 19, 4, 13, 27, 13, 18, 21, 24, 9, 3, 2, 30, 16, 14, 31, 29, 27, 23, 18, 8, 32, 3, 3, 25, 17, 8, 32, 5, 2, 28, 30, 26, 25, 12, 12]
taxes = {32: 1, 19: 12, 3: 1, 27: 14, 5: 3, 9: 5, 13: 11, 14: 10, 28: 6, 31: 15, 8: 8, 18: 18, 17: 7, 2: 2, 12: 9, 24: 16, 83: 6, 23: 9, 16: 15, 29: 4, 25: 5, 26: 18, 4: 1, 21: 10, 30: 10}
total_value = 335

print(taxed_coin_exchange(coins, taxes, total_value))
