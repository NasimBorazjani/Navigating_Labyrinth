
coins = [29, 25, 15, 12, 40, 23, 36, 22, 16, 24, 51, 34, 46, 29, 20, 14, 21, 27, 15, 31, 15, 17, 9, 42, 30, 45, 14, 14, 30, 16, 44, 32, 6, 15, 5, 41, 18, 43, 36, 31, 27, 26, 6, 44, 33, 23, 7, 19]
tax = {41: 15, 22: 3, 9: 4, 34: 9, 32: 11, 36: 5, 18: 5, 40: 9, 46: 11, 45: 17, 33: 3, 14: 9, 12: 12, 7: 2, 43: 14, 25: 18, 31: 9, 51: 8, 24: 18, 17: 3, 16: 5, 19: 10, 6: 6, 27: 15, 42: 7, 23: 2, 29: 2, 21: 13, 30: 7, 44: 4, 5: 2, 20: 11, 26: 12, 15: 8}
total_value = 477

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

# Backtrack to find the subset of coins
subset = []
i = total_value
while i > 0:
    if dp[i] != dp[i - 1] and dp[i] - tax[i] == dp[i - 1]:
        subset.append(i)
        i -= 1
    else:
        i -= coin

# Reverse the subset to get the correct order
subset.reverse()

# Print the subset as a list of numbers in Python syntax
print(subset)
