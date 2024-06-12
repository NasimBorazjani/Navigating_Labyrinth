
# Coins and their taxes
coins = [26, 32, 14, 36, 14, 8, 9, 3, 8, 18, 7, 23, 6, 20, 34, 8, 37, 19, 15, 6, 2, 13, 37, 7, 31, 2, 7, 4, 17, 9, 4, 22, 7, 16, 33, 14, 11, 30, 36, 14, 34, 37, 36, 37, 32, 38, 15, 17, 19, 14]
taxes = {17: 16, 4: 2, 15: 2, 8: 1, 19: 5, 9: 4, 23: 7, 3: 2, 16: 13, 2: 1, 38: 13, 11: 2, 31: 6, 7: 6, 36: 8, 14: 8, 37: 17, 32: 5, 6: 1, 13: 11, 22: 9, 20: 8, 18: 4, 30: 6, 34: 2, 33: 1, 26: 3}

# Sort coins in descending order
coins.sort(reverse=True)

# Initialize variables
total_value = 0
total_tax = 0
chosen_coins = []

# Loop through coins
for coin in coins:
    # If the coin doesn't exceed the remaining total value and its value is even if it's smaller than the last chosen coin and odd otherwise
    if coin <= (396 - total_value - total_tax) and (len(chosen_coins) == 0 or coin <= chosen_coins[-1] and coin % 2 == 0 or coin > chosen_coins[-1] and coin % 2 == 1):
        # Add the coin to the chosen coins
        chosen_coins.append(coin)
        # Subtract the coin value and its tax from the remaining total value
        total_value += coin
        total_tax += taxes[coin]

# Print the chosen coins
print(chosen_coins)
