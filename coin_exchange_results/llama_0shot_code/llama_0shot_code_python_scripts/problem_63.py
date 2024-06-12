
coins = [12, 12, 5, 32, 25, 3, 23, 49, 31, 6, 12, 23, 20, 14, 34, 17, 16, 16, 21, 18, 7, 30, 7, 27, 29, 14, 5, 9, 48, 33, 5, 18, 15, 29, 2, 28, 29, 25, 26, 6, 4, 4, 6, 8, 16, 5, 4, 4, 20, 25, 10, 6, 3, 24, 19]
tax = {20: 18, 16: 6, 19: 2, 27: 12, 25: 2, 6: 2, 26: 16, 23: 9, 28: 12, 49: 16, 33: 13, 30: 12, 8: 6, 21: 18, 31: 16, 48: 5, 15: 5, 10: 2, 3: 1, 29: 14, 32: 15, 5: 3, 4: 4, 34: 3, 17: 14, 12: 11, 7: 3, 9: 9, 14: 7, 24: 14, 18: 15, 2: 1}

# Sort the coins in increasing order
coins.sort()

# Initialize dp with infinity for all sums except 0
dp = [float('inf')] * (sum(coins) + 1)
dp[0] = 0

# Iterate over the coins
for coin in coins:
    # Update dp for all sums that can be obtained by adding the coin
    for i in range(coin, sum(coins) + 1):
        # If the coin is smaller than the previous one, add the tax to the minimum tax for the sum without the coin
        if coin < dp[i - coin]:
            dp[i] = min(dp[i], dp[i - coin] + tax[coin])
        # If the coin is larger than or equal to the previous one, add the tax to the minimum tax for the sum with the previous coin subtracted
        else:
            dp[i] = min(dp[i], dp[i - coin] + tax[coin] - tax[coin - 1])

# Find the minimum tax for the sum 348
min_tax = dp[348]

# If no solution is found, print 'No solution found'
if min_tax == float('inf'):
    print('No solution found')
else:
    # Initialize the list of chosen coins
    chosen_coins = []

    # Iterate over the coins in reverse order
    for coin in coins[::-1]:
        # If the coin is in the optimal solution, add it to the list and subtract its value from the sum
        if dp[348 - coin] == dp[348] - tax[coin]:
            chosen_coins.append(coin)
            348 -= coin

    # Reverse the list of chosen coins to get the correct order
    chosen_coins.reverse()

    # Print the list of chosen coins
    print(chosen_coins)
