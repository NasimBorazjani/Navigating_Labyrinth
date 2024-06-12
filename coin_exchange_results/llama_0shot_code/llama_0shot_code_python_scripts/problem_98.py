
coins = [35, 14, 15, 111, 8, 4, 6, 37, 14, 33, 45, 32, 46, 41, 38, 19, 34, 14, 2, 4, 24, 36, 46, 33, 12, 2, 14, 28, 12, 21, 34, 26, 28, 27, 25, 4, 23, 43, 43, 20, 10, 13, 5, 36, 27, 36]
tax = {33: 16, 21: 14, 4: 1, 13: 9, 23: 8, 2: 2, 12: 2, 41: 15, 46: 6, 45: 2, 34: 16, 24: 15, 19: 4, 5: 4, 35: 14, 6: 6, 37: 13, 26: 16, 43: 20, 15: 13, 111: 2, 38: 1, 10: 7, 32: 13, 20: 14, 27: 15, 36: 14, 25: 8, 14: 2, 28: 10, 8: 4}

total_value = 462
n = len(coins)

# Initialize dp array
dp = [float('inf')] * (total_value + 1)
dp[0] = 0

# Iterate over coins in descending order
for i in range(n):
    coin = coins[i]
    coin_tax = tax[coin]
    for j in range(total_value, coin - 1, -1):
        dp[j] = min(dp[j], dp[j - coin] + coin_tax)

# Find the subset of coins
subset = []
j = total_value
for i in range(n - 1, -1, -1):
    coin = coins[i]
    if j >= coin and dp[j] == dp[j - coin] + tax[coin]:
        subset.append(coin)
        j -= coin

# Reverse the subset to get the correct order
subset.reverse()

print(subset)
