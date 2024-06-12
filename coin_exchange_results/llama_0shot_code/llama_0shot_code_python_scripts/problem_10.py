
# List of coins and their taxes
coins = [21, 18, 16, 12, 14, 11, 15, 4, 9, 23, 7, 20, 6, 8, 17, 13, 3, 2, 10, 18, 3, 16, 9, 3, 14, 23, 16]
taxes = [11, 16, 6, 5, 11, 8, 11, 3, 2, 14, 5, 12, 2, 3, 6, 3, 3, 1, 5, 6, 3, 3, 2, 11, 16, 3, 11, 5, 6]

# Initialize dp array
dp = [float('inf')] * 237
dp[0] = 0

# Initialize previous coin
prev_coin = 0

# Iterate over the coins
for coin, tax in zip(coins, taxes):
    for i in range(coin, 237):
        # If the coin is smaller than the previous one, it must be even
        if coin < prev_coin and coin % 2 != 0:
            continue
        # If the coin is larger than or equal to the previous one, it must be odd
        if coin >= prev_coin and coin % 2 == 0:
            continue
        # Update dp array
        dp[i] = min(dp[i], dp[i - coin] + tax)
    # Update previous coin
    prev_coin = coin

# Find the minimum tax for a subset of coins with sum 236
min_tax = dp[236]

# Backtrack to find the subset of coins
coins_chosen = []
i = 236
while i >= 0:
    if dp[i] == min_tax:
        coins_chosen.append(i)
        i -= 1
    else:
        i -= 1

# Reverse the list to get the correct order
coins_chosen = coins_chosen[::-1]

# Print the result
print(coins_chosen)
