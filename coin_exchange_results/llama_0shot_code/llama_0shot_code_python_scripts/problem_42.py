
def taxed_coin_exchange(coins, taxes, total_value):
    dp = [float('inf')] * (total_value + 1)
    dp[0] = 0
    prev_coin = 0
    for coin in sorted(coins):
        if coin < prev_coin:
            assert coin % 2 == 0
        else:
            assert coin % 2 == 1
        for i in range(total_value, coin - 1, -1):
            dp[i] = min(dp[i], dp[i - coin] + taxes[coin])
        prev_coin = coin
    return dp[-1]

coins = [24, 10, 24, 3, 21, 7, 21, 26, 8, 14, 24, 5, 13, 10, 25, 6, 9, 4, 18, 4, 15, 4, 10, 23, 6, 13, 26, 20, 8, 10, 29, 27, 27, 20, 2, 15, 9, 9, 25, 8, 2, 27, 5, 22, 19, 26, 2, 29, 12, 9, 6, 12, 2, 15, 5, 16, 3, 29, 19]
taxes = {5: 2, 9: 8, 12: 5, 14: 4, 22: 8, 26: 3, 8: 7, 27: 2, 20: 13, 3: 3, 13: 3, 2: 1, 19: 19, 29: 4, 10: 3, 18: 14, 21: 12, 15: 12, 4: 3, 23: 5, 16: 9, 25: 16, 7: 4, 24: 17, 6: 6}
total_value = 300

print(taxed_coin_exchange(coins, taxes, total_value))
