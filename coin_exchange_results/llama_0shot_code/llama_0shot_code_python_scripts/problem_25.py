
# Coins and their taxes
coins = [28, 5, 25, 22, 26, 13, 20, 20, 18, 28, 7, 20, 18, 19, 18, 5, 15, 23, 28, 27, 22, 10, 8, 17, 3, 8, 5, 11, 21, 17, 65, 23, 11, 3, 12]
taxes = {20: 12, 21: 3, 5: 2, 3: 2, 7: 1, 15: 8, 8: 7, 27: 6, 17: 8, 18: 14, 28: 5, 13: 1, 23: 4, 65: 8, 26: 8, 22: 5, 25: 3, 11: 11, 12: 8, 19: 19, 10: 7}

# Initialize the minimum tax list
min_taxes = [0] + [float('inf')] * 284

# Initialize the previous coin
prev_coin = 0

# For each coin
for coin in coins:
    # Calculate the total tax for all the values from its value to 284
    for total in range(coin, 285):
        # Check the conditions about the previous coin and the parity of the current coin value
        if (prev_coin < coin and coin % 2 == 0) or (prev_coin >= coin and coin % 2 == 1):
            # Update the minimum tax list
            min_taxes[total] = min(min_taxes[total], min_taxes[total - coin] + taxes[coin])
    # Update the previous coin
    prev_coin = coin

# Find the minimum tax for 284
min_tax = min_taxes[284]

# Initialize the result list
result = []

# For each total value from 284 to 0
for total in range(284, -1, -1):
    # If the total tax for the current total value is equal to the minimum tax
    if min_taxes[total] == min_tax:
        # Add the coin to the result list
        result.append(total)
        # Update the minimum tax
        min_tax -= taxes[total]

# Reverse the result list and print it
print(result[::-1])
