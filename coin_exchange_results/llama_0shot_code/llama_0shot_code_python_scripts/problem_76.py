
# List of coins and their taxes
coins = [8, 8, 6, 36, 7, 36, 33, 3, 31, 17, 21, 28, 41, 17, 23, 16, 39, 2, 3, 40, 23, 20, 5, 30, 8, 28, 17, 34, 38, 26, 16, 21, 15, 21, 11, 33, 5, 33, 2, 27, 26, 21, 14, 13, 7, 23]
taxes = {28: 16, 5: 1, 3: 3, 40: 18, 33: 20, 34: 12, 20: 4, 39: 13, 2: 2, 31: 11, 36: 2, 17: 14, 7: 1, 14: 6, 23: 12, 8: 1, 30: 15, 27: 13, 15: 2, 21: 3, 11: 6, 26: 14, 41: 2, 38: 10, 6: 5, 16: 4, 13: 11}

# Sort the coins in descending order
coins.sort(reverse=True)

# Initialize the total value and the list of chosen coins
total_value = 0
chosen_coins = []

# Loop through the sorted coins
for coin in coins:
    # If the coin doesn't exceed the remaining total value and its value is even if it's smaller than the last chosen coin and odd otherwise
    if coin <= 403 - total_value and (not chosen_coins or (coin < chosen_coins[-1] and coin % 2 == 0) or (coin >= chosen_coins[-1] and coin % 2 == 1)):
        # Subtract the tax from the remaining total value
        total_value -= taxes[coin]
        # Add the coin to the list of chosen coins
        chosen_coins.append(coin)
        # If the total value reaches 403, stop the loop
        if total_value == 403:
            break

# Print the list of chosen coins
print(chosen_coins)
