
# tax values for each coin
tax = {20: 13, 10: 8, 16: 2, 15: 3, 21: 1, 14: 12, 13: 8, 6: 4, 7: 6, 9: 3, 22: 18, 4: 3, 19: 12, 5: 3, 8: 6, 17: 9, 3: 2, 18: 1, 2: 1, 83: 14, 7: 6}

# sort the coins in descending order
coins = sorted([c for c in tax.keys() if c <= 239] + [239], reverse=True)

# initialize dp with infinity
dp = [float('inf')] * (239 + 1)
dp[0] = 0

# dynamic programming
for i in range(len(coins)):
    for j in range(coins[i], 239 + 1):
        if i == 0 or (coins[i] >= coins[i-1] and coins[i] % 2 == 1) or (coins[i] < coins[i-1] and coins[i] % 2 == 0):
            dp[j] = min(dp[j], dp[j - coins[i]] + tax[coins[i]])

# find the minimum tax paid for all sums from the value of the last coin to 239
min_tax = min(dp[coins[-1]:])

# find the subset of coins that sum up to 239 and minimize the total tax
subset = []
for i in range(len(coins)):
    if dp[239] == dp[239 - coins[i]] + tax[coins[i]]:
        subset.append(coins[i])
        dp[239] -= coins[i]

# reverse the subset to get the correct order
subset = subset[::-1]

print(subset)
