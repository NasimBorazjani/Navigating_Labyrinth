
# Coins and their taxes
coins = [9, 11, 7, 9, 12, 19, 29, 21, 11, 10, 26, 22, 18, 29, 19, 11, 18, 23, 26, 16, 18, 4, 22, 25, 17, 18, 12, 23, 3, 17, 17, 15, 22, 25, 27, 2, 26, 22, 21, 28, 10, 23, 15]
taxes = {28: 16, 10: 8, 21: 8, 18: 12, 27: 6, 7: 7, 2: 2, 19: 4, 17: 13, 26: 11, 12: 1, 9: 5, 25: 15, 29: 20, 11: 2, 15: 8, 22: 1, 16: 13, 4: 4, 3: 3, 23: 18}

# Sort coins in descending order
coins.sort(reverse=True)

# Initialize variables
total_value = 296
chosen_coins = []

# Loop through the sorted coins
for coin in coins:
    if total_value >= coin:
        chosen_coins.append(coin)
        total_value -= coin

# Check if the last chosen coin breaks the rule of even/odd value
if len(chosen_coins) > 1 and chosen_coins[-1] % 2 == chosen_coins[-2] % 2:
    chosen_coins.pop()
    total_value += chosen_coins[-1]

# Calculate the total tax
total_tax = sum(taxes[coin] for coin in chosen_coins)

# Print the result
print(chosen_coins)
print(total_tax)
