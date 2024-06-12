
coins = [21, 13, 10, 18, 21, 43, 42, 29, 14, 19, 9, 2, 15, 19, 32, 45, 24, 31, 25, 7, 21, 24, 29, 29, 4, 36, 29, 19, 29, 12, 3, 44, 40, 46, 33, 3, 28, 44, 25, 6, 36, 3, 4, 19, 31]
tax = {6: 3, 9: 7, 13: 11, 19: 11, 36: 17, 32: 11, 46: 1, 4: 3, 21: 14, 3: 1, 18: 5, 29: 18, 12: 9, 2: 2, 15: 14, 43: 11, 24: 5, 25: 15, 14: 10, 42: 11, 44: 7, 31: 11, 40: 2, 33: 10, 45: 20, 7: 6, 10: 3, 28: 5}

total_value = 474
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
