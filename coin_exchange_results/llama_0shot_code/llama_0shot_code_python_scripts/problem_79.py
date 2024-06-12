
coins = [33, 4, 5, 9, 31, 26, 25, 19, 31, 33, 24, 6, 13, 17, 15, 37, 7, 21, 3, 23, 22, 7, 3, 11, 19, 28, 24, 32, 27, 31, 24, 12, 23, 22, 16, 6, 33, 8, 19, 13, 5, 11, 10, 4, 8, 16, 14, 17, 13, 9, 25, 17]
tax = {3: 3, 19: 1, 5: 2, 9: 4, 17: 4, 24: 11, 8: 5, 22: 10, 4: 2, 32: 10, 16: 1, 37: 5, 23: 12, 26: 18, 12: 1, 27: 9, 14: 5, 25: 13, 15: 8, 6: 6, 21: 13, 10: 3, 31: 17, 7: 3, 33: 10, 11: 2, 28: 10, 13: 10}
total_value = 389

# Initialize dp list
dp = [float('inf')] * (total_value + 1)
dp[0] = 0

# Iterate over coins in descending order
for coin in sorted(coins, reverse=True):
    for i in range(total_value, coin - 1, -1):
        dp[i] = min(dp[i], dp[i - coin] + tax[coin])

# Find the subset of coins
subset = []
i = total_value
for coin in sorted(coins, reverse=True):
    if i >= coin and dp[i] == dp[i - coin] + tax[coin]:
        subset.append(coin)
        i -= coin

print(subset)
