
def taxed_coin_exchange(coins, taxes, total_value):
    dp = [float('inf')] * (total_value + 1)
    dp[0] = 0
    prev_coin = 0
    for coin in sorted(coins, reverse=True):
        for i in range(total_value, coin - 1, -1):
            if coin % 2 == 0 and prev_coin % 2 == 1 or coin % 2 == 1 and prev_coin % 2 == 0:
                dp[i] = min(dp[i], dp[i - coin] + taxes[coin])
        prev_coin = coin
    return dp[-1] if dp[-1] != float('inf') else -1

coins = [25, 29, 8, 11, 8, 25, 20, 16, 6, 4, 98, 7, 28, 24, 27, 16, 23, 26, 26, 99, 2, 7, 22, 7, 5, 24, 2]
taxes = {24: 5, 26: 16, 28: 20, 2: 1, 22: 16, 25: 11, 27: 7, 11: 4, 6: 3, 99: 17, 8: 5, 7: 5, 5: 3, 23: 5, 4: 4, 98: 16, 16: 3, 29: 5, 20: 19}
total_value = 305

print(taxed_coin_exchange(coins, taxes, total_value))
