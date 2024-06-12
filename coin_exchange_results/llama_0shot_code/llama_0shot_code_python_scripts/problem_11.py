
def taxed_coin_exchange(coins, taxes, total_value):
    dp = [float('inf')] * (total_value + 1)
    dp[0] = 0
    for coin in sorted(coins):
        for i in range(total_value, coin - 1, -1):
            dp[i] = min(dp[i], dp[i - coin] + taxes[coin])
    return dp[total_value]

coins = [21, 20, 21, 11, 23, 16, 16, 16, 3, 20, 2, 19, 16, 21, 18, 7, 20, 3, 16, 18, 7, 22, 3, 22, 7, 21, 12, 22, 5, 6, 17, 16, 8, 8, 14, 4, 18, 9, 4, 20, 2]
taxes = {6: 1, 7: 3, 9: 1, 18: 1, 2: 1, 11: 7, 5: 3, 12: 2, 3: 3, 22: 6, 14: 3, 20: 15, 4: 3, 17: 4, 16: 8, 23: 18, 21: 16, 19: 2, 8: 6}
total_value = 228

result = taxed_coin_exchange(coins, taxes, total_value)
print(result)
