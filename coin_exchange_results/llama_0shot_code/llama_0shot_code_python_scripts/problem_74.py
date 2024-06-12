
coins = [5, 15, 15, 77, 12, 38, 41, 30, 31, 30, 13, 19, 9, 2, 23, 37, 14, 34, 29, 22, 22, 4, 16, 2, 12, 17, 9, 18, 19, 21, 4, 28, 40, 11, 30, 24, 19, 9, 10, 76, 34]
tax = {13: 8, 29: 10, 4: 4, 2: 2, 77: 17, 16: 10, 11: 2, 22: 18, 17: 10, 18: 18, 38: 7, 9: 6, 5: 2, 41: 14, 31: 3, 12: 10, 19: 5, 24: 16, 40: 6, 14: 4, 34: 13, 15: 3, 23: 20, 76: 16, 37: 2, 21: 2, 28: 3, 10: 2, 30: 16}
total_value = 419

# Initialize dp list
dp = [float('inf')] * (total_value + 1)
dp[0] = 0

# Iterate over the coins in descending order
for coin in sorted(coins, reverse=True):
    for i in range(total_value, coin - 1, -1):
        dp[i] = min(dp[i], dp[i - coin] + tax[coin])

# Find the subset of coins
subset = []
i = total_value
while i > 0:
    if dp[i] != dp[i - coins[0]]:
        subset.append(i)
        i -= coins[0]
    else:
        coins.pop(0)

# Reverse the subset list to get the correct order
subset = subset[::-1]

print(subset)
