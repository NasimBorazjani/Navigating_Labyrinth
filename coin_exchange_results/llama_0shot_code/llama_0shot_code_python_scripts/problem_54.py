
def taxed_coin_exchange(coins, taxes, target_sum):
    dp = [float('inf')] * (target_sum + 1)
    dp[0] = 0
    prev_coin = 0
    for coin, tax in sorted(zip(coins, taxes), reverse=True):
        for i in range(target_sum, coin - 1, -1):
            if i >= prev_coin and (i - coin) % 2 == 0:
                dp[i] = min(dp[i], dp[i - coin] + tax)
        prev_coin = coin
    return dp[-1] if dp[-1] != float('inf') else -1

coins = [4, 17, 14, 12, 1, 3, 12, 10, 14, 9, 30, 20, 11, 17, 11, 16, 22, 17, 30, 5, 10, 16, 19, 27, 6, 18, 20, 19, 32, 25, 30, 15, 30, 21, 19, 25, 31, 33, 19, 10, 8, 16, 8]
taxes = [1, 13, 13, 10, 1, 1, 8, 8, 10, 9, 14, 4, 3, 14, 11, 11, 10, 11, 14, 5, 8, 9, 13, 4, 9, 20, 5, 14, 6, 14, 10, 20, 11, 11, 6, 5, 1, 4, 8, 9, 4, 10, 11, 13, 14, 14, 5, 6, 1, 4, 8]
target_sum = 328

print(taxed_coin_exchange(coins, taxes, target_sum))
