
coins = [4, 2, 18, 5, 18, 13, 22, 15, 5, 14, 15, 21, 23, 13, 19, 22, 6, 12, 19, 8, 15, 8, 12, 15, 11, 17, 7, 19, 23, 9, 3, 4, 12, 10, 11, 2, 22, 19, 19, 11, 18, 6, 10, 23, 20, 1, 6, 23, 8, 6]
tax = {21: 18, 1: 1, 13: 3, 20: 2, 19: 7, 5: 4, 18: 4, 4: 1, 15: 5, 12: 7, 17: 5, 22: 10, 8: 3, 7: 5, 23: 11, 9: 7, 10: 8, 3: 2, 14: 4, 6: 1, 2: 2, 11: 10}

total_value = 233
n = len(coins)

# Initialize dp array
dp = [float('inf')] * (total_value + 1)
dp[0] = 0

# Iterate over the coins in increasing order
for i in range(n):
    coin = coins[i]
    for j in range(total_value, coin - 1, -1):
        dp[j] = min(dp[j], dp[j - coin] + tax[coin])

# Find the minimum tax for a subset of coins with sum equal to total_value
min_tax = dp[total_value]

# Find the subset of coins
subset = []
j = total_value
for i in range(n - 1, -1, -1):
    coin = coins[i]
    if j >= coin and dp[j] == dp[j - coin] + tax[coin]:
        subset.append(coin)
        j -= coin

# Reverse the subset to get the correct order
subset = subset[::-1]

print(subset)
