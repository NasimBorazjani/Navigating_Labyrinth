
def taxed_coin_exchange(coins, taxes, total_value):
    dp = [float('inf')] * (total_value + 1)
    dp[0] = 0
    sorted_coins = sorted(coins, reverse=True)
    sorted_taxes = [taxes[coin] for coin in sorted_coins]

    for coin, tax in zip(sorted_coins, sorted_taxes):
        for i in range(total_value, coin - 1, -1):
            dp[i] = min(dp[i], dp[i - coin] + tax)

    return dp[-1]

coins = [18, 26, 17, 17, 16, 27, 30, 3, 4, 2, 24, 26, 29, 23, 2, 31, 25, 25, 4, 24, 14, 29, 4, 34, 34, 23, 35, 23, 28, 18, 8, 10, 17, 8, 22, 32]
taxes = {27: 14, 14: 1, 18: 3, 22: 9, 10: 8, 3: 2, 32: 20, 35: 16, 8: 3, 30: 20, 25: 18, 4: 3, 28: 12, 26: 16, 29: 2, 24: 20, 16: 6, 17: 3, 31: 9, 2: 2, 23: 17, 34: 17}
total_value = 342

print(taxed_coin_exchange(coins, taxes, total_value))
