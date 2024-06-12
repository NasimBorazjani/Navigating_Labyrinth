
coins = [14, 8, 11, 30, 3, 3, 27, 16, 19, 4, 6, 14, 7, 2, 39, 103, 15, 100, 27, 36, 7, 36, 13, 7, 18, 39, 14, 3, 28]
tax = {13: 11, 18: 8, 36: 15, 11: 4, 6: 1, 16: 8, 100: 12, 39: 10, 28: 9, 27: 20, 103: 6, 19: 5, 30: 14, 2: 1, 4: 3, 3: 3, 15: 10, 8: 5, 7: 2, 14: 14}
total_value = 410

# Initialize dp list
dp = [float('inf')] * (total_value + 1)
dp[0] = 0

# Sort coins in descending order
coins.sort(reverse=True)

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
