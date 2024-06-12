
# List of coins and their tax values
coins = [26, 8, 34, 12, 20, 21, 35, 13, 28, 5, 16, 11, 24, 42, 16, 12, 34, 21, 27, 27, 20, 47, 9, 12, 38, 23, 43, 33, 26, 22, 38, 42, 20, 41, 47, 41, 24, 46, 35, 42, 9, 35, 13, 45, 24, 29, 45, 2, 41, 39, 24, 38, 39, 18, 5, 8, 36]
tax_values = {12: 8, 18: 6, 42: 8, 11: 9, 38: 13, 9: 9, 24: 15, 34: 1, 20: 5, 2: 2, 23: 2, 33: 12, 27: 8, 39: 11, 16: 1, 28: 12, 26: 11, 21: 7, 35: 7, 22: 19, 47: 9, 29: 12, 46: 3, 45: 9, 5: 1, 13: 13, 43: 8, 36: 11, 41: 4, 8: 8}

# Sort the coins in descending order
coins.sort(reverse=True)

# Initialize the total value and the remaining total value
total_value = sum(coins)
remaining_value = 477

# Initialize the list of chosen coins
chosen_coins = []

# Initialize the previous coin
prev_coin = None

# Loop through the sorted coins
for coin in coins:
    # If the remaining total value is 0, break the loop
    if remaining_value == 0:
        break
    # If the coin is smaller than the previous one and it's an odd number, continue to the next coin
    if prev_coin is not None and coin < prev_coin and coin % 2 == 1:
        continue
    # If the coin is larger than or equal to the previous one and it's an even number, continue to the next coin
    if prev_coin is not None and coin >= prev_coin and coin % 2 == 0:
        continue
    # If the coin is larger than the remaining total value, continue to the next coin
    if coin > remaining_value:
        continue
    # Subtract the tax value from the remaining total value
    remaining_value -= tax_values[coin]
    # Add the coin to the list of chosen coins
    chosen_coins.append(coin)
    # Update the previous coin
    prev_coin = coin

# Print the list of chosen coins
print(chosen_coins)
