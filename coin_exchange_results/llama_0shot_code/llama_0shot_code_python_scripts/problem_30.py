
coins = [46, 10, 4, 8, 2, 22, 26, 49, 4, 19, 2, 9, 23, 28, 6, 21, 9, 14, 15, 21, 22, 3, 14, 2, 28, 13, 20, 2, 28, 7, 16, 27, 22, 18, 28, 10, 14, 14, 4, 20, 18]
tax = {21: 14, 19: 16, 4: 3, 23: 10, 10: 3, 18: 7, 9: 3, 27: 13, 20: 12, 13: 9, 26: 17, 3: 3, 6: 6, 49: 16, 2: 2, 15: 7, 28: 13, 46: 10, 8: 3, 7: 6, 22: 20, 14: 5, 16: 8}

# Sort the coins in descending order
coins.sort(reverse=True)

# Create a dictionary to store the remaining totals and their corresponding minimum taxes
remainders = {0: 0}

# Iterate over the sorted coins
for coin in coins:
    # Calculate the tax for the current coin
    coin_tax = tax[coin]
    
    # Create a new dictionary for the remaining totals after choosing the current coin
    new_remainders = {}
    
    # Iterate over the remaining totals
    for total, total_tax in remainders.items():
        # Check if the current coin can be included in the solution
        if coin <= total:
            # Calculate the new total and tax
            new_total = total - coin
            new_tax = total_tax + coin_tax
            
            # Update the minimum tax for the new total
            if new_total not in new_remainders or new_tax < new_remainders[new_total]:
                new_remainders[new_total] = new_tax
    
    # Update the remainders
    remainders = new_remainders

# The minimum tax for the total value 294 is the answer
answer = remainders[294]

# Print the answer
print(answer)
