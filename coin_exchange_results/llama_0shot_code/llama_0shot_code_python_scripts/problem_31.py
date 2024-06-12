
# Problem data
coins = [12, 23, 57, 18, 6, 5, 21, 15, 14, 23, 5, 16, 9, 8, 19, 8, 19, 6, 8, 3, 12, 2, 14, 3, 3, 4, 26, 6, 6, 25, 9, 13, 20, 24, 6, 26, 14, 25, 5, 26]
tax = {6: 2, 12: 3, 9: 2, 2: 1, 14: 1, 16: 12, 21: 10, 4: 1, 8: 5, 26: 7, 23: 7, 57: 11, 15: 15, 19: 13, 25: 15, 13: 4, 5: 3, 24: 4, 3: 3, 18: 4, 20: 10}
target = 260

# Sort coins in descending order based on their value minus tax
coins.sort(key=lambda x: x - tax[x], reverse=True)

# Initialize variables for selected coins and total value
selected_coins = []
total_value = 0

# Iterate over the sorted list of coins
for coin in coins:
    # Check if adding the current coin would result in a total value that is less than or equal to 260
    if total_value + coin <= target:
        # Add the coin to the selected coins and update the total value
        selected_coins.append(coin)
        total_value += coin
    else:
        # If the total value is already greater than 260, stop the loop
        break

# Check if the total value is equal to 260
if total_value != target:
    # If it's not, return an empty list
    selected_coins = []

# Return the list of selected coins
print(selected_coins)
