
def taxed_coin_exchange(coins, taxes, target_sum):
    dp = [float('inf')] * (target_sum + 1)
    dp[0] = 0
    prev_coin = 0

    for coin in sorted(coins):
        for i in range(coin, target_sum + 1):
            if coin < prev_coin:
                dp[i] = min(dp[i], dp[i - coin] + taxes[coin])
            else:
                dp[i] = min(dp[i], dp[i - coin] + taxes[coin] + taxes[prev_coin])
        prev_coin = coin

    return dp[-1] if dp[-1] != float('inf') else -1

coins = [30, 28, 81, 26, 24, 20, 5, 18, 33, 19, 30, 27, 6, 10, 22, 10, 33, 10, 15, 26, 9, 6, 22, 31, 36, 16, 4, 11, 24, 7, 17, 30, 3, 7, 8, 8, 34]
taxes = {24: 7, 22: 3, 11: 10, 28: 17, 7: 7, 20: 10, 5: 2, 8: 2, 9: 5, 15: 14, 81: 17, 30: 5, 31: 17, 33: 9, 18: 3, 36: 2, 16: 14, 10: 1, 19: 15, 3: 1, 34: 12, 26: 13, 6: 3, 4: 1, 27: 11, 17: 5}
target_sum = 387

print(taxed_coin_exchange(coins, taxes, target_sum))
