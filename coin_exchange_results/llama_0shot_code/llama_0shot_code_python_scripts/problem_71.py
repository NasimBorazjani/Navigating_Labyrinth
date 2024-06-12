
def taxed_coin_exchange(coins, taxes, target_sum):
    dp = [float('inf')] * (target_sum + 1)
    dp[0] = 0
    prev_coin = 0
    for coin in sorted(coins):
        for i in range(coin, target_sum + 1):
            if coin < prev_coin:
                dp[i] = min(dp[i], dp[i - coin] + taxes[coin])
            else:
                dp[i] = min(dp[i], dp[i - coin] + taxes[coin])
        prev_coin = coin
    return dp[-1]

coins = [18, 11, 14, 3, 7, 18, 40, 3, 35, 30, 24, 29, 34, 11, 17, 14, 14, 10, 5, 40, 4, 31, 25, 14, 39, 12, 26, 24, 3, 8, 34, 2, 22, 189, 4, 31, 25, 14, 39, 12, 26, 24, 3, 8, 34, 2, 22, 189, 40]
taxes = {29: 9, 40: 8, 30: 5, 17: 16, 3: 3, 5: 3, 2: 2, 22: 17, 11: 1, 14: 4, 8: 5, 18: 11, 26: 8, 39: 15, 7: 1, 31: 2, 24: 17, 189: 5, 12: 4, 25: 10, 35: 18, 10: 1, 4: 3, 34: 16}
target_sum = 400

print(taxed_coin_exchange(coins, taxes, target_sum))
