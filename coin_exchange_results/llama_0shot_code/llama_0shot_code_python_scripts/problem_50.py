
def taxed_coin_exchange(coins, taxes, total_value):
    dp = [float('inf')] * (total_value + 1)
    dp[0] = 0
    prev_coin = 0
    for coin in sorted(coins):
        for i in range(total_value, coin - 1, -1):
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + taxes[coin])
            if prev_coin <= coin:
                dp[i] = min(dp[i], dp[i - 2 * coin] + 2 * taxes[coin])
        prev_coin = coin
    return dp[-1]

coins = [19, 14, 29, 19, 29, 9, 17, 16, 25, 7, 8, 2, 23, 11, 28, 6, 29, 16, 19, 31, 30, 15, 7, 16, 23, 23, 10, 32, 8, 14, 7, 9, 6, 23, 77, 24, 22, 24, 22]
taxes = {15: 6, 29: 12, 19: 3, 30: 18, 14: 2, 77: 3, 6: 5, 17: 1, 32: 16, 9: 8, 22: 15, 31: 17, 25: 10, 24: 1, 28: 11, 2: 2, 7: 4, 8: 7, 11: 7, 23: 19, 10: 2, 16: 2}
total_value = 351

print(taxed_coin_exchange(coins, taxes, total_value))
