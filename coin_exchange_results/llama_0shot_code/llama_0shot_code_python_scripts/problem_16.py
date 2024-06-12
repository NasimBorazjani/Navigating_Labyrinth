
def taxed_coin_exchange(coins, tax):
    total_value = 223
    dp = [float('inf')] * (total_value + 1)
    dp[0] = 0
    sorted_coins = sorted(coins)
    for coin in sorted_coins:
        for i in range(total_value, coin - 1, -1):
            dp[i] = min(dp[i], dp[i - coin] + tax[coin])
    return dp[-1]

coins = [11, 13, 22, 11, 16, 20, 10, 10, 17, 21, 6, 6, 15, 15, 21, 6, 4, 16, 9, 11, 3, 13, 2, 9, 11, 1, 7, 2, 2, 12, 5, 2, 11, 16, 20, 9, 2, 4, 10, 17, 11, 22, 11, 2, 18, 23, 15, 22, 11, 15, 20, 9]
tax = {6: 2, 11: 9, 3: 3, 15: 2, 9: 1, 18: 13, 22: 13, 16: 5, 21: 2, 5: 2, 12: 4, 7: 5, 4: 3, 13: 2, 1: 1, 20: 14, 2: 1, 10: 4, 23: 15, 17: 9}

print(taxed_coin_exchange(coins, tax))
