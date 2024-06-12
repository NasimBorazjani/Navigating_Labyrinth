
def taxed_coin_exchange(coins, taxes, target_sum):
    dp = [float('inf')] * (target_sum + 1)
    dp[0] = 0
    prev_coin = 0
    for coin in sorted(coins):
        for i in range(coin, target_sum + 1):
            if coin < prev_coin:
                dp[i] = min(dp[i], dp[i - coin] + taxes[coin])
            else:
                if taxes[coin] % 2 == 0:
                    dp[i] = min(dp[i], dp[i - coin] + taxes[coin])
        prev_coin = coin
    return dp[-1] if dp[-1] != float('inf') else -1

coins = [22, 4, 12, 26, 4, 9, 4, 28, 28, 8, 28, 19, 15, 20, 9, 161, 11, 28, 17, 10, 25, 15, 7, 28, 21, 24, 10, 13, 22, 4, 10, 14]
taxes = {15: 2, 17: 10, 10: 3, 12: 10, 21: 12, 4: 2, 22: 1, 11: 6, 26: 9, 14: 7, 24: 12, 161: 16, 20: 15, 9: 8, 8: 1, 13: 10, 28: 6, 7: 6, 25: 6, 19: 15}
target_sum = 301

print(taxed_coin_exchange(coins, taxes, target_sum))
