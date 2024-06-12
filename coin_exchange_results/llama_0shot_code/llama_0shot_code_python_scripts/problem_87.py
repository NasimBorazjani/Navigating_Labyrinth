
coins = [25, 41, 34, 19, 19, 36, 37, 13, 28, 26, 181, 7, 14, 6, 29, 36, 33, 7, 8, 43, 19, 9, 3, 2, 18, 40, 43, 22, 23, 21]
coin_tax = {21: 5, 26: 13, 36: 8, 28: 8, 34: 12, 3: 2, 6: 2, 23: 10, 2: 2, 9: 5, 41: 4, 29: 19, 7: 6, 18: 18, 43: 2, 8: 7, 181: 9, 25: 10, 33: 8, 14: 13, 13: 1, 22: 13, 40: 7, 37: 11, 19: 11}

total_value = 449
n = len(coins)

# Initialize dp array
dp = [float('inf')] * (total_value + 1)
dp[0] = 0

# Iterate over coins in descending order
for i in range(n):
    coin = coins[i]
    coin_tax_value = coin_tax[coin]
    for j in range(total_value, coin - 1, -1):
        dp[j] = min(dp[j], dp[j - coin] + coin_tax_value)

# Find the subset of coins
subset = []
j = total_value
for i in range(n - 1, -1, -1):
    coin = coins[i]
    if j >= coin and dp[j] == dp[j - coin] + coin_tax[coin]:
        subset.append(coin)
        j -= coin

# Reverse the subset to get the correct order
subset.reverse()

print(subset)
