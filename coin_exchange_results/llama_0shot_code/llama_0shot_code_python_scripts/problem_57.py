
def taxed_coin_exchange(coins, tax):
    total_value = 322
    dp = [float('inf')] * (total_value + 1)
    dp[0] = 0
    prev_coin = 0

    for coin in sorted(coins):
        for i in range(total_value, coin - 1, -1):
            if coin % 2 == 0 and prev_coin % 2 == 1 or coin % 2 == 1 and prev_coin % 2 == 0:
                dp[i] = min(dp[i], dp[i - coin] + tax[coin])
        prev_coin = coin

    return dp[-1] if dp[-1] != float('inf') else -1

coins = [25, 22, 28, 23, 5, 14, 28, 14, 20, 6, 22, 1, 25, 18, 30, 10, 19, 12, 17, 17, 6, 28, 21, 28, 21, 2, 20, 2, 19, 14, 31, 31, 14, 7, 20, 13, 7, 18, 22, 15, 6, 6, 21, 9, 18, 11, 20, 26, 15]
tax = {11: 1, 14: 4, 7: 2, 25: 4, 12: 5, 20: 19, 13: 6, 15: 11, 30: 18, 1: 1, 2: 2, 31: 6, 10: 2, 23: 1, 6: 2, 21: 18, 18: 8, 28: 15, 17: 5, 26: 6, 22: 6, 9: 1, 19: 2, 5: 4}

print(taxed_coin_exchange(coins, tax))
