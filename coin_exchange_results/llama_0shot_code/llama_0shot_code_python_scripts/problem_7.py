
# Sort the coins in descending order
coins = [41, 4, 22, 8, 5, 5, 20, 4, 3, 19, 4, 13, 3, 18, 20, 9, 15, 3, 3, 14, 3, 14, 9, 4, 15, 19, 6, 15, 22, 19, 3, 3, 20, 9, 20, 11, 22, 15, 20]
coins.sort(reverse=True)

# Create a dictionary to store the coins and their corresponding tax
coin_tax = {20: 11, 15: 13, 9: 7, 8: 3, 3: 1, 6: 3, 5: 2, 13: 11, 4: 4, 22: 11, 19: 19, 11: 1, 14: 2, 41: 16, 18: 18}

# Initialize variables to store the selected coins and the total value
selected_coins = []
total_value = 0

# Iterate over the sorted coins
for i, coin in enumerate(coins):
    # Check if adding the current coin to the total value violates the condition about the previous coin
    if i > 0 and coin < selected_coins[-1] and coin % 2 == 1:
        continue
    # Add the current coin to the total value and its tax
    total_value += coin
    # Add the coin to the list of selected coins
    selected_coins.append(coin)
    # If the total value is greater than or equal to 220, stop the loop
    if total_value >= 220:
        break

# Print the list of selected coins
print(selected_coins)
