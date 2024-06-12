
# Problem data
coins = [26, 8, 19, 9, 36, 23, 42, 40, 13, 34, 40, 25, 11, 38, 10, 41, 19, 34, 91, 18, 14, 27, 14, 43, 42, 13, 2, 27, 90, 13, 3, 4, 44, 7, 48, 40, 35, 40, 10, 12, 25]
tax = {44: 20, 11: 4, 19: 3, 4: 4, 10: 3, 14: 9, 90: 18, 48: 12, 91: 5, 8: 4, 7: 5, 9: 5, 12: 2, 42: 18, 36: 6, 35: 10, 34: 12, 25: 7, 27: 1, 3: 2, 26: 15, 40: 8, 43: 1, 18: 8, 23: 1, 13: 3, 41: 8, 38: 13, 2: 2}

# Sort coins in descending order based on value - tax
coins.sort(key=lambda x: x - tax[x], reverse=True)

# Initialize dp list
dp = [float('inf')] * 489
dp[0] = 0

# Iterate over each coin
for coin in coins:
    for i in range(488, coin - 1, -1):
        dp[i] = min(dp[i], dp[i - coin] + tax[coin])

# The answer is the minimum tax paid for a subset of coins with total value exactly 488
print(dp[488])
