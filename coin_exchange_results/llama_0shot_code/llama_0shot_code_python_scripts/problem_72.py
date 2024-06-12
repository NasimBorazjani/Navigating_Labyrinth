
def taxed_coin_exchange(coins, taxes, target_sum):
    dp = [float('inf')] * (target_sum + 1)
    dp[0] = 0
    prev_coin = 0
    for coin in sorted(coins):
        for i in range(target_sum, coin - 1, -1):
            if coin % 2 == 0 and prev_coin % 2 == 1 or coin % 2 == 1 and prev_coin % 2 == 0:
                dp[i] = min(dp[i], dp[i - coin] + taxes[coin])
        prev_coin = coin
    return dp[-1] if dp[-1] != float('inf') else -1

coins = [13, 3, 34, 36, 19, 31, 6, 7, 10, 24, 92, 3, 24, 33, 33, 22, 93, 13, 17, 28, 25, 16, 21, 16, 20, 26, 24, 16, 11, 18, 2, 30, 25, 23, 28, 21]
taxes = {3: 1, 23: 1, 34: 8, 17: 14, 20: 16, 11: 5, 28: 7, 13: 3, 22: 19, 16: 4, 26: 20, 93: 7, 31: 11, 6: 2, 36: 12, 33: 15, 18: 1, 19: 2, 7: 7, 21: 7, 10: 9, 24: 11, 30: 4, 25: 7, 2: 2, 92: 19}
target_sum = 384

print(taxed_coin_exchange(coins, taxes, target_sum))
