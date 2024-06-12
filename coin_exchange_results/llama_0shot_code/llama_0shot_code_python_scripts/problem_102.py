
coins = [14, 29, 39, 40, 16, 35, 17, 37, 43, 30, 28, 26, 13, 13, 42, 30, 10, 7, 44, 5, 34, 7, 32, 11, 40, 35, 12, 34, 35, 38, 29, 42, 33, 26, 4, 36, 41, 35, 26, 34, 16, 6, 38, 13, 41, 23, 20]
tax = {11: 4, 10: 3, 41: 9, 34: 4, 7: 2, 17: 16, 29: 8, 37: 1, 44: 8, 30: 13, 32: 9, 20: 18, 23: 8, 6: 4, 5: 3, 14: 3, 13: 7, 35: 4, 33: 5, 39: 9, 40: 11, 28: 3, 4: 2, 43: 14, 42: 15, 38: 14, 16: 5, 36: 5, 12: 9, 26: 1}

total_value = 449
n = len(coins)

# Initialize dp array
dp = [float('inf')] * (total_value + 1)
dp[0] = 0

# Iterate over the coins in increasing order
for i in range(n):
    coin = coins[i]
    for j in range(total_value, coin - 1, -1):
        dp[j] = min(dp[j], dp[j - coin] + tax[coin])

# Find the subset of coins
subset = []
j = total_value
for i in range(n - 1, -1, -1):
    coin = coins[i]
    if j >= coin and dp[j] == dp[j - coin] + tax[coin]:
        subset.append(coin)
        j -= coin

subset.reverse()
print(subset)
