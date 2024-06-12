
coins = [40, 28, 46, 16, 13, 15, 38, 39, 3, 8, 40, 41, 18, 48, 16, 25, 39, 14, 47, 46, 31, 16, 41, 45, 9, 26, 33, 46, 17, 23, 6, 46, 7, 43, 10, 28, 47, 15, 35, 20, 32, 4, 32, 9, 48, 7, 34, 46, 10, 39, 44]
tax = {44: 6, 39: 15, 4: 2, 23: 11, 7: 2, 40: 10, 13: 10, 34: 8, 45: 9, 10: 3, 35: 18, 14: 2, 28: 5, 46: 12, 25: 3, 26: 18, 15: 11, 31: 2, 20: 15, 9: 7, 41: 13, 18: 16, 32: 11, 3: 3, 48: 20, 38: 4, 43: 6, 33: 9, 16: 13, 8: 4, 17: 1, 47: 17, 6: 5}

# Sort the coins in descending order
coins.sort(reverse=True)

# Initialize the lists to store the minimum total tax and the subset of coins
min_tax = [0] + [float('inf')] * 485
subset = [[]]

# Iterate over each coin
for coin in coins:
    # Iterate over each possible total value
    for total_value in range(coin, 486):
        # Calculate the total value and total tax if we were to select this coin
        value = total_value - coin
        new_tax = min_tax[value] + tax[coin]
        # If this combination gives a smaller total tax than the current minimum, update the minimum
        if new_tax < min_tax[total_value]:
            min_tax[total_value] = new_tax
            subset.append(subset[value] + [coin])

# The last element of the list of minimum total tax gives the minimum total tax for the entire set of coins
min_total_tax = min_tax[-1]

# Find the subset of coins that gives this minimum total tax
subset = subset[min_total_tax]

print(subset)
