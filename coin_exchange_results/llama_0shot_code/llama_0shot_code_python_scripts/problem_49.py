
def taxed_coin_exchange(coins, taxes, target_sum):
    dp = [float('inf')] * (target_sum + 1)
    dp[0] = 0
    prev_coin = 0
    for coin, tax in sorted(zip(coins, taxes), reverse=True):
        for i in range(target_sum, coin - 1, -1):
            if i >= prev_coin and (i - coin) % 2 == 0:
                dp[i] = min(dp[i], dp[i - coin] + tax)
            elif i < prev_coin and (i - coin) % 2 == 1:
                dp[i] = min(dp[i], dp[i - coin] + tax)
        prev_coin = coin
    return dp[-1] if dp[-1] != float('inf') else -1

coins = [18, 20, 11, 6, 81, 3, 9, 5, 14, 19, 30, 2, 19, 3, 9, 22, 21, 29, 6, 25, 10, 18, 27, 26, 25, 13, 15, 16, 3, 5, 23, 26, 25, 31, 15, 12]
taxes = [6, 3, 11, 1, 4, 1, 2, 1, 10, 16, 4, 1, 1, 2, 1, 14, 7, 9, 6, 1, 12, 15, 14, 11, 1, 15, 16, 11, 14, 15, 12]
target_sum = 324

print(taxed_coin_exchange(coins, taxes, target_sum))
