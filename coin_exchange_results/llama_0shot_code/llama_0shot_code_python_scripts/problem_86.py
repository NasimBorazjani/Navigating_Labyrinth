
coins = [31, 8, 22, 27, 2, 25, 2, 8, 49, 26, 65, 6, 37, 49, 15, 21, 27, 5, 34, 28, 47, 15, 7, 42, 32, 20, 34, 48, 39, 7, 13]
tax = {7: 1, 65: 16, 21: 18, 25: 18, 15: 14, 31: 15, 6: 2, 37: 2, 5: 1, 22: 1, 8: 7, 26: 2, 2: 1, 32: 8, 27: 2, 13: 8, 39: 17, 28: 11, 47: 6, 42: 10, 34: 15, 20: 8, 48: 11, 49: 13}
total_value = 490

# Initialize dp with infinity for all values except 0
dp = [float('inf')] * (total_value + 1)
dp[0] = 0

# Iterate over the coins in increasing order
for coin in sorted(coins):
    # Update dp for all i from total_value to coin_value
    for i in range(total_value, coin - 1, -1):
        dp[i] = min(dp[i], dp[i - coin] + tax[coin])

# Find the minimum tax paid for a subset of coins with sum total_value
min_tax = dp[total_value]

# Find the subset of coins
subset = []
remaining = total_value
for coin in sorted(coins, reverse=True):
    if dp[remaining] == dp[remaining - coin] + tax[coin]:
        subset.append(coin)
        remaining -= coin

# Reverse the subset to get the correct order
subset = subset[::-1]

# Print the result
print(subset)
