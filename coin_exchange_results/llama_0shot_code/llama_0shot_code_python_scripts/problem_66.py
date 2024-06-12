
coins = [3, 35, 33, 20, 31, 29, 12, 31, 8, 10, 3, 17, 2, 28, 6, 25, 10, 13, 31, 25, 37, 35, 9, 15, 113, 26, 18, 34, 30]
tax = {31: 11, 15: 6, 13: 13, 28: 1, 9: 6, 20: 1, 34: 15, 6: 5, 113: 20, 12: 6, 2: 1, 29: 10, 37: 2, 25: 11, 26: 10, 3: 3, 33: 19, 8: 7, 18: 6, 17: 7, 10: 8, 35: 11, 30: 16}
total_value = 384

# Initialize dp list
dp = [float('inf')] * (total_value + 1)
dp[0] = 0

# Iterate over the coins in descending order
for coin in sorted(coins, reverse=True):
    for i in range(total_value, coin - 1, -1):
        # Update dp[i]
        dp[i] = min(dp[i], dp[i-coin] + tax[coin])

# Find the minimum tax for a subset of coins with sum total_value
min_tax = dp[total_value]

# Backtrack to find the subset of coins
coins_chosen = []
i = total_value
while i > 0:
    if dp[i] != dp[i-1] and dp[i] == dp[i-coins[0]] + tax[coins[0]]:
        coins_chosen.append(coins[0])
        i -= coins[0]
    else:
        coins.pop(0)

# Reverse the list to get the correct order
coins_chosen = coins_chosen[::-1]

print(coins_chosen)
