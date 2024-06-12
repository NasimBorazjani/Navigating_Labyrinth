
coins = [12, 15, 3, 24, 10, 18, 10, 20, 21, 17, 9, 8, 2, 11, 5, 5, 3, 8, 6, 12, 20, 22, 4, 5, 17, 5, 14, 10, 15, 8, 9, 22, 4, 7, 15, 16, 4, 2, 5, 9, 24, 23, 3, 7, 20, 9, 12, 10, 4, 4, 8, 24, 11, 20, 2, 15]
tax = {20: 14, 15: 15, 6: 1, 14: 1, 7: 2, 18: 5, 2: 1, 16: 5, 21: 9, 3: 3, 12: 3, 17: 10, 22: 4, 10: 9, 4: 3, 11: 1, 5: 1, 23: 13, 24: 4, 9: 9, 8: 4}
total_value = 246

# Sort coins in descending order
coins.sort(reverse=True)

# Initialize dp list
dp = [float('inf')] * (total_value + 1)
dp[0] = 0

# Iterate over the coins
for coin in coins:
    for i in range(total_value, coin - 1, -1):
        dp[i] = min(dp[i], dp[i - coin] + tax[coin])

# Find the minimum tax for a subset of coins with sum total_value
min_tax = dp[total_value]

# Backtrack to find the subset of coins
subset = []
i = total_value
while i > 0:
    if dp[i] != dp[i - coins[-1]]:
        subset.append(coins[-1])
        i -= coins[-1]
    coins.pop()

# Reverse the subset list to get the correct order
subset.reverse()

# Print the subset list
print(subset)
