
coins = [19, 21, 16, 6, 34, 23, 8, 10, 14, 10, 59, 15, 17, 32, 11, 15, 8, 29, 58, 12, 3, 5, 11, 34, 2, 12, 20, 6, 29, 23, 10, 34, 33, 18]
tax = {6: 5, 17: 7, 12: 10, 34: 9, 5: 1, 11: 7, 10: 8, 21: 19, 15: 3, 33: 6, 3: 2, 16: 12, 58: 19, 8: 7, 14: 5, 20: 8, 2: 2, 19: 19, 59: 14, 18: 15, 29: 8, 23: 6, 32: 5}

total_value = 355
n = len(coins)

# Initialize dp array
dp = [float('inf')] * (total_value + 1)
dp[0] = 0

# Iterate over the coins in increasing order
for i in range(n):
    coin = coins[i]
    for j in range(total_value, coin - 1, -1):
        dp[j] = min(dp[j], dp[j - coin] + tax[coin])

# Find the minimum tax for a subset of coins with sum total_value
min_tax = dp[total_value]

# Find the subset of coins
subset = []
j = total_value
for i in range(n - 1, -1, -1):
    coin = coins[i]
    if j >= coin and dp[j] == dp[j - coin] + tax[coin]:
        subset.append(coin)
        j -= coin

subset.append(j)  # Add the last coin
subset.reverse()  # Reverse the subset to get the correct order

print(subset)
