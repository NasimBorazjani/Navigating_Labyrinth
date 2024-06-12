
def taxed_coin_exchange(coins, tax):
    total_value = 324
    dp = [float('inf')] * (total_value + 1)
    dp[0] = 0
    prev_coin = 0

    for coin in sorted(coins):
        if coin < prev_coin:
            assert coin % 2 == 0, "coin should be even"
        else:
            assert coin % 2 == 1, "coin should be odd"
        prev_coin = coin

        for i in range(total_value, coin - 1, -1):
            dp[i] = min(dp[i], dp[i - coin] + tax[coin])

    return dp[-1] if dp[-1] != float('inf') else -1

coins = [11, 6, 147, 6, 19, 29, 28, 32, 18, 20, 12, 22, 4, 20, 27, 3, 3, 18, 19, 9, 2, 28, 31, 20, 2, 27, 22, 30, 3]
tax = {27: 18, 6: 2, 22: 12, 18: 11, 4: 3, 12: 4, 28: 6, 147: 10, 32: 6, 19: 3, 29: 12, 31: 19, 20: 4, 2: 2, 30: 17, 3: 2, 11: 10, 9: 2}

print(taxed_coin_exchange(coins, tax))
