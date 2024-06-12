
# List of coins and their taxes
coins = [25, 22, 26, 12, 18, 12, 5, 6, 6, 21, 28, 26, 6, 26, 9, 11, 27, 24, 16, 1, 12, 5, 10, 23, 11, 10, 28, 2, 3, 7, 23, 28, 27, 12, 3, 3, 27, 21, 13, 8, 18, 25, 6, 7, 9, 25, 18, 18, 23, 12, 11, 15, 2, 16]
taxes = {10: 6, 24: 14, 5: 3, 3: 1, 16: 6, 27: 10, 13: 1, 12: 4, 21: 17, 8: 2, 28: 10, 6: 3, 1: 1, 18: 2, 25: 14, 11: 3, 23: 7, 7: 6, 26: 16, 15: 4, 2: 1, 9: 3, 22: 8}

# Sort the coins in descending order
coins.sort(reverse=True)

# Initialize variables
total = 0
selected_coins = []

# Loop through the coins
for i in range(len(coins)):
    # If the current coin doesn't exceed the remaining total value and its value is even if it's smaller than the previous coin and odd if it's larger, subtract its value and tax from the remaining total
    if coins[i] <= 289 - total and (i == 0 or (coins[i] < selected_coins[-1] and coins[i] % 2 == 0) or (coins[i] >= selected_coins[-1] and coins[i] % 2 == 1)):
        total += coins[i]
        selected_coins.append(coins[i])
        total -= taxes[coins[i]]

# Print the selected coins
print(selected_coins)
