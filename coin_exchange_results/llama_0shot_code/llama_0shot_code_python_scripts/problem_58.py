
coins = [10, 16, 2, 18, 10, 16, 17, 32, 18, 33, 23, 20, 21, 25, 32, 24, 10, 27, 13, 27, 30, 13, 19, 20, 4, 5, 15, 8, 8, 34, 21, 14, 3, 20, 10, 18, 3, 14, 28, 6, 4, 8, 15, 4, 30, 30, 12, 20, 14, 10]
tax = {30: 12, 20: 19, 16: 7, 24: 14, 12: 3, 13: 4, 8: 2, 2: 1, 21: 2, 23: 12, 34: 13, 27: 16, 3: 3, 28: 3, 14: 13, 6: 4, 33: 17, 10: 8, 5: 3, 15: 12, 4: 2, 18: 2, 19: 5, 17: 1, 32: 2, 25: 12}
total_value = 357

# Initialize dp with infinity for all values except 0
dp = [float('inf')] * (total_value + 1)
dp[0] = 0

# Iterate over the coins in increasing order
for coin in sorted(coins):
    # Update dp for all i from total_value to coin_value
    for i in range(total_value, coin - 1, -1):
        dp[i] = min(dp[i], dp[i - coin] + tax[coin])

# Find the minimum tax paid for a subset of coins with sum total_value
min_tax = dp[total_value]

# Find the subset of coins
coins_chosen = []
remaining_value = total_value
for coin in sorted(coins, reverse=True):
    if dp[remaining_value] == dp[remaining_value - coin] + tax[coin]:
        coins_chosen.append(coin)
        remaining_value -= coin

# Reverse the order of coins_chosen to get the correct solution
coins_chosen = coins_chosen[::-1]

print(coins_chosen)
