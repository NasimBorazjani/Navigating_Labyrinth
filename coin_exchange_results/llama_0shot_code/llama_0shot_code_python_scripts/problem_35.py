
# Coins and their taxes
coins = [27, 17, 6, 5, 20, 3, 4, 29, 25, 27, 20, 18, 18, 25, 2, 13, 15, 4, 12, 4, 26, 12, 26, 24, 17, 23, 2, 6, 2, 29, 3, 20, 12, 7, 9, 12, 26, 11, 2, 5, 10, 25, 3, 13, 7, 25]
taxes = {2: 1, 13: 11, 26: 13, 5: 1, 4: 2, 9: 8, 15: 8, 18: 6, 20: 18, 3: 1, 17: 17, 6: 2, 10: 10, 12: 1, 23: 10, 7: 6, 29: 13, 25: 15, 11: 10, 27: 2, 24: 18}

# Sort coins in descending order
coins.sort(reverse=True)

# Initialize variables
total_value = 295
chosen_coins = []

# Loop through coins
for i in range(len(coins)):
    coin = coins[i]
    
    # If the coin doesn't exceed the remaining total value and its tax is paid
    if coin <= total_value:
        # Subtract the coin value and its tax from the remaining total value
        total_value -= (coin - taxes[coin])
        chosen_coins.append(coin)
        
        # If the total value reaches 0, stop the loop
        if total_value == 0:
            break

# Print the list of chosen coins
print(chosen_coins)
