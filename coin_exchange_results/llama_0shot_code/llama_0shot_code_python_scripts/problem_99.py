
coins = [37, 4, 1, 15, 2, 7, 8, 33, 35, 14, 47, 36, 41, 44, 13, 31, 3, 7, 27, 25, 26, 38, 10, 19, 7, 18, 32, 45, 29, 35, 44, 17, 40, 13, 14, 40, 28, 15, 23, 11, 7, 16, 7, 35, 31, 45, 14, 22, 7, 36, 31]
tax = {44: 2, 1: 1, 36: 14, 26: 2, 22: 10, 33: 13, 16: 12, 23: 1, 41: 6, 8: 6, 18: 3, 13: 5, 2: 2, 7: 5, 29: 13, 25: 19, 3: 1, 45: 12, 35: 13, 17: 6, 47: 13, 10: 8, 15: 14, 31: 13, 4: 2, 14: 2, 32: 11, 40: 3, 11: 4, 28: 7, 37: 12, 27: 11, 19: 17, 38: 18}
total_value = 465

# Initialize dp with infinity for all values except 0
dp = [float('inf')] * (total_value + 1)
dp[0] = 0

# Iterate over the coins in increasing order
for coin in sorted(coins):
    # Update dp[i] for all i from total_value to coin_value
    for i in range(total_value, coin - 1, -1):
        dp[i] = min(dp[i], dp[i - coin] + tax[coin])

# Find the minimum tax for a subset of coins with sum total_value
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
