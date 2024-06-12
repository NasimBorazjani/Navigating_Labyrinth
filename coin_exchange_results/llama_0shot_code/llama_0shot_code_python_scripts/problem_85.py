
# List of coins and their taxes
coins = [38, 36, 40, 31, 39, 29, 36, 31, 16, 14, 16, 45, 40, 45, 257, 8, 39, 16, 2, 41, 9, 26, 22, 24]
taxes = {9: 6, 14: 9, 24: 8, 26: 12, 16: 6, 45: 14, 8: 3, 22: 8, 38: 9, 40: 14, 31: 9, 257: 11, 36: 2, 2: 1, 41: 6, 29: 6, 39: 4}

# Initialize dp array
dp = [float('inf')] * 453
dp[0] = 0

# Initialize previous coin
prev_coin = 0

# Dynamic programming
for coin in coins:
    for i in range(coin, 453):
        # Include the current coin in the subset
        include = dp[i - coin] + taxes[coin]
        # Exclude the current coin from the subset
        exclude = dp[i]
        # Update dp[i] with the minimum tax
        dp[i] = min(include, exclude)

# Find the subset of coins with minimum tax
min_tax = dp[452]
subset = []
for coin in sorted(coins, reverse=True):
    if dp[452 - coin] + taxes[coin] == min_tax:
        subset.append(coin)
        min_tax -= taxes[coin]

# Print the subset of coins
print(subset)
