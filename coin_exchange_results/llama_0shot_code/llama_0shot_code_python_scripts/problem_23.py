
coins = [84, 2, 8, 16, 21, 10, 15, 4, 17, 16, 4, 85, 30, 13, 28, 2, 2, 11, 18, 9, 25, 5, 24, 14, 20, 30, 6]
coin_tax = {15: 2, 18: 9, 28: 4, 84: 10, 2: 1, 24: 19, 30: 12, 5: 2, 9: 9, 21: 9, 11: 10, 16: 14, 4: 2, 17: 2, 85: 18, 6: 5, 8: 6, 13: 2, 10: 4, 25: 11, 20: 19, 14: 2}
total_value = 309

# Initialize dp list
dp = [float('inf')] * (total_value + 1)
dp[0] = 0

# Iterate over the coins in descending order
for coin in sorted(coins, reverse=True):
    for i in range(total_value, coin - 1, -1):
        dp[i] = min(dp[i], dp[i - coin] + coin_tax[coin])

# Find the subset of coins
subset = []
i = total_value
for coin in sorted(coins, reverse=True):
    if i >= coin and dp[i] == dp[i - coin] + coin_tax[coin]:
        subset.append(coin)
        i -= coin

print(subset)
