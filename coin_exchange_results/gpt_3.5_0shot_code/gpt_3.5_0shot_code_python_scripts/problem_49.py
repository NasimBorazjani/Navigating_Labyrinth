
# Define the list of coins and their tax values
coins = [18, 20, 11, 6, 81, 3, 9, 5, 14, 19, 30, 2, 19, 3, 9, 22, 21, 29, 6, 25, 10, 18, 27, 26, 25, 13, 15, 16, 3, 5, 23, 26, 25, 31, 15, 12]
tax_values = {11: 6, 6: 3, 16: 11, 23: 16, 18: 3, 31: 4, 9: 2, 3: 1, 22: 10, 10: 1, 30: 4, 81: 14, 2: 1, 14: 1, 13: 11, 15: 7, 19: 16, 25: 6, 12: 12, 29: 11, 26: 9, 5: 1, 27: 15, 20: 7, 21: 14}

# Sort the coins in descending order
coins.sort(reverse=True)

# Initialize variables to keep track of total sum and total tax
total_sum = 0
total_tax = 0
chosen_coins = []

# Iterate through the sorted coins list
for coin in coins:
    # Check if adding the current coin will exceed the target sum
    if total_sum + coin <= 324:
        # Check if the coin meets the conditions for being chosen
        if (len(chosen_coins) == 0) or (coin < chosen_coins[-1] and coin % 2 == 0) or (coin >= chosen_coins[-1] and coin % 2 != 0):
            total_sum += coin
            total_tax += tax_values[coin]
            chosen_coins.append(coin)

# Print the chosen coins and total tax paid
print(chosen_coins)
print("Total tax paid:", total_tax)
