
def taxed_coin_exchange(coins, taxes, target_sum):
    dp = [float('inf')] * (target_sum + 1)
    dp[0] = 0
    prev_coin = 0
    for coin in sorted(coins):
        for i in range(coin, target_sum + 1):
            if coin % 2 == 0 and prev_coin % 2 == 1 and coin < prev_coin:
                dp[i] = min(dp[i], dp[i - coin] if i - coin >= 0 else float('inf'))
            else:
                dp[i] = min(dp[i], taxes[coin] + (dp[i - coin] if i - coin >= 0 else float('inf')))
        prev_coin = coin
    return dp[-1] if dp[-1] != float('inf') else -1

coins = [23, 27, 20, 21, 8, 2, 2, 3, 21, 26, 16, 33, 22, 3, 25, 17, 5, 31, 3, 9, 12, 30, 11, 10, 7, 13, 2, 21, 8, 16, 5, 18, 32, 27, 7, 32, 7, 10, 11, 33, 18, 30, 7, 24, 21, 4, 25, 4, 23, 21, 23, 15, 26, 10]
taxes = {16: 1, 18: 1, 9: 1, 11: 5, 5: 3, 2: 1, 21: 1, 33: 3, 7: 1, 4: 1, 30: 8, 23: 10, 17: 8, 15: 7, 13: 6, 20: 8, 32: 4, 10: 6, 3: 1, 12: 7, 27: 6, 31: 5, 22: 1, 26: 20, 24: 5, 8: 4, 25: 9}
target_sum = 334

result = taxed_coin_exchange(coins, taxes, target_sum)
print(result)
