
# List of coins and their taxes
coins = [21, 10, 19, 6, 20, 7, 23, 18, 4, 15, 4, 13, 2, 5, 32, 28, 113, 3, 9, 9, 11, 21, 112, 6, 6, 11, 29]
taxes = {10: 7, 5: 3, 11: 3, 23: 2, 21: 13, 19: 3, 18: 18, 29: 20, 3: 2, 9: 7, 20: 18, 6: 2, 112: 20, 2: 1, 4: 4, 7: 4, 32: 1, 15: 8, 13: 10, 28: 17, 113: 18}

# Initialize variables
total_tax = 0
chosen_coins = []
prev_coin = None

# Sort the coins in descending order
coins.sort(reverse=True)

# Iterate over the coins
for coin in coins:
    # If the coin is smaller than the previous one and has an even value, or
    # if it is larger than the previous one and has an odd value, update the total tax
    if (prev_coin is not None and coin < prev_coin and coin % 2 == 0) or (prev_coin is not None and coin >= prev_coin and coin % 2 == 1):
        total_tax += taxes[coin]
    # Add the coin to the chosen coins
    chosen_coins.append(coin)
    prev_coin = coin

# Print the chosen coins
print(chosen_coins)
