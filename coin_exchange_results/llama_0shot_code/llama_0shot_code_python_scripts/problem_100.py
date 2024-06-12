
# List of coins and their taxes
coins = [19, 11, 3, 37, 9, 29, 42, 12, 2, 13, 15, 11, 25, 14, 31, 17, 24, 45, 5, 18, 42, 21, 28, 23, 26, 40, 27, 42, 12, 13, 16, 14, 31, 38, 9, 24, 27, 36, 13, 27, 15, 43, 9, 14, 34, 7, 15, 12, 31, 44]
taxes = {37: 7, 45: 7, 29: 6, 27: 2, 2: 2, 40: 6, 13: 9, 17: 2, 9: 2, 15: 12, 36: 2, 26: 18, 44: 5, 42: 4, 38: 8, 43: 2, 12: 4, 24: 20, 28: 15, 16: 7, 21: 13, 23: 5, 19: 4, 25: 16, 3: 2, 18: 13, 34: 16, 31: 2, 5: 4, 14: 2, 7: 1, 11: 8}

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
