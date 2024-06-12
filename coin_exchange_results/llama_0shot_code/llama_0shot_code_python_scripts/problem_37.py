
coins = [22, 15, 4, 23, 19, 3, 5, 28, 22, 27, 13, 18, 14, 11, 22, 20, 27, 24, 21, 13, 25, 11, 6, 2, 30, 29, 4, 16, 3, 13, 3, 28, 28, 20, 15, 27, 4, 18, 20, 5, 16, 21, 25, 24, 23, 15, 22, 26]
tax = {15: 2, 18: 17, 22: 16, 29: 7, 28: 5, 23: 1, 20: 17, 14: 3, 13: 2, 4: 2, 5: 3, 27: 10, 16: 6, 3: 2, 6: 3, 19: 8, 2: 1, 25: 6, 24: 19, 26: 18, 21: 10, 11: 1, 30: 4}
total_value = 303

# Initialize dp list
dp = [float('inf')] * (total_value + 1)
dp[0] = 0

# Iterate over the coins in increasing order
for coin in sorted(coins):
    for i in range(total_value, coin - 1, -1):
        dp[i] = min(dp[i], dp[i - coin] + tax[coin])

# Find the subset of coins
subset = []
i = total_value
while i > 0:
    if dp[i] != dp[i - coins[0]]:
        subset.append(coins[0])
        i -= coins[0]
    else:
        coins.pop(0)

# Reverse the subset list to get the correct order
subset.reverse()

print(subset)
