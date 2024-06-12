
coins = [22, 25, 37, 5, 46, 10, 23, 23, 3, 6, 34, 32, 34, 2, 3, 8, 4, 28, 32, 24, 15, 38, 17, 35, 9, 12, 12, 22, 34, 48, 39, 30, 7, 18, 10, 46, 30, 36, 49, 27, 22, 19, 9, 24, 43, 15]
tax = {18: 11, 17: 7, 7: 6, 43: 2, 22: 3, 24: 11, 9: 3, 36: 10, 46: 4, 10: 3, 39: 5, 5: 5, 35: 15, 28: 8, 15: 2, 34: 6, 27: 3, 38: 11, 30: 20, 23: 18, 25: 10, 12: 1, 4: 1, 49: 16, 37: 6, 48: 17, 2: 2, 8: 4, 3: 1, 6: 3, 19: 10, 32: 19}
total_value = 463

# Initialize dp with infinity for all indices except 0
dp = [0] + [float('inf')] * total_value

# Iterate over the coins in increasing order
for coin in sorted(coins):
    # Update dp for all i from total_value to coin_value
    for i in range(total_value, coin - 1, -1):
        # The value of dp[i] is the minimum of its current value and the tax for the coin plus dp[i - coin_value]
        dp[i] = min(dp[i], tax[coin] + dp[i - coin])

# The solution is the list of coins whose sum of values is dp[-1]
solution = []
remaining_value = total_value
for coin in sorted(coins, reverse=True):
    if dp[remaining_value] == dp[remaining_value - coin] - tax[coin]:
        solution.append(coin)
        remaining_value -= coin

# Print the solution in Python syntax
print(solution)
