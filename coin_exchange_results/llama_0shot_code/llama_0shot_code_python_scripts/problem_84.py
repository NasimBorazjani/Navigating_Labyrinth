
coins = [17, 4, 35, 10, 42, 11, 10, 11, 2, 14, 29, 31, 33, 3, 38, 4, 32, 9, 19, 14, 4, 39, 6, 36, 31, 25, 40, 8, 33, 31, 11, 34, 18, 2, 32, 40, 4, 16, 1, 36, 37, 3, 33, 20, 10, 8, 9, 20, 14, 35, 36, 22, 35, 4]
tax = {37: 11, 10: 3, 36: 8, 32: 3, 3: 1, 18: 16, 14: 5, 35: 5, 16: 15, 8: 5, 42: 20, 29: 4, 6: 1, 25: 9, 11: 4, 20: 15, 39: 6, 38: 14, 34: 6, 40: 11, 9: 2, 17: 6, 19: 8, 4: 4, 22: 20, 31: 3, 1: 1, 33: 18, 2: 2}
total_value = 426

# Initialize dp with infinity for all indices except 0
dp = [0] + [float('inf')] * total_value

# Iterate over the coins in increasing order
for coin in sorted(coins):
    # Update dp for all i from total_value to coin_value
    for i in range(total_value, coin - 1, -1):
        # The value of dp[i] is the minimum of its current value and the tax for the current coin plus dp[i - coin_value]
        dp[i] = min(dp[i], tax[coin] + dp[i - coin])

# The answer is the minimum of dp[i] for all i from total_value to 0
answer = min(dp[total_value:])

# Find the subset of coins that gives the answer
subset = []
remaining = total_value - answer
for coin in sorted(coins, reverse=True):
    while remaining >= coin and dp[remaining] == dp[remaining - coin] + tax[coin]:
        subset.append(coin)
        remaining -= coin

# Reverse the subset to get the correct order
subset.reverse()

# Print the subset in Python syntax
print(subset)
