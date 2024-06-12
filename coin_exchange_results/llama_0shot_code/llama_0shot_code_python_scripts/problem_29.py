
# Coins and their taxes
coins = [14, 12, 20, 4, 23, 28, 25, 27, 19, 21, 16, 29, 13, 17, 22, 10, 15, 2, 23, 18, 4, 5, 9, 7, 19, 8, 19, 9, 21, 29, 15, 15, 23, 8, 13, 20, 9, 13, 16, 3, 14, 11, 15, 2, 23, 18, 4]
taxes = {14: 2, 12: 11, 20: 5, 4: 2, 23: 12, 28: 1, 25: 8, 27: 3, 19: 1, 21: 6, 16: 2, 29: 7, 13: 5, 17: 2, 22: 15, 10: 1, 15: 1, 3: 2, 8: 5, 5: 4, 9: 1, 7: 2, 2: 2, 18: 17, 11: 1}

# Initialize dp array
dp = [float('inf')] * 296
dp[0] = 0

# Dynamic programming
for coin in coins:
    for i in range(coin, 296):
        dp[i] = min(dp[i], dp[i - coin] + taxes[coin])

# Find the minimum tax for sum 295
min_tax = dp[295]

# Backtrack to find the subset of coins
subset = []
remain = 295
for coin in sorted(coins, reverse=True):
    if remain >= coin and dp[remain - coin] + taxes[coin] == min_tax:
        subset.append(coin)
        remain -= coin

# Print the subset of coins
print(subset)
