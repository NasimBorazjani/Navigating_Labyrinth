
# Coins and their tax values
coins = [26, 24, 8, 2, 11, 10, 11, 14, 20, 9, 13, 10, 25, 21, 7, 20, 15, 27, 18, 12, 23, 4, 2, 4, 22, 23, 15, 16, 24, 14, 22, 13, 15, 21, 5, 14, 2, 21, 14, 10, 2, 2, 24, 26, 17, 2, 20, 22, 3, 27, 8, 20, 2, 25, 7]
tax = {24: 18, 14: 4, 15: 10, 23: 15, 26: 12, 22: 4, 17: 8, 5: 2, 18: 2, 16: 3, 11: 3, 2: 1, 27: 9, 3: 3, 10: 5, 20: 4, 4: 2, 21: 4, 12: 1, 8: 6, 13: 2, 7: 2, 9: 6, 25: 15}

# Sort the coins in descending order
coins.sort(reverse=True)

# Initialize the minimum tax and previous coin for each sum
min_tax = [float('inf')] * 274
prev_coin = [None] * 274

# Iterate through each coin and calculate the minimum tax for each possible sum
for coin in coins:
    for total in range(coin, 274):
        if coin < prev_coin[total - coin]:
            if min_tax[total] > min_tax[total - coin] + tax[coin]:
                min_tax[total] = min_tax[total - coin] + tax[coin]
                prev_coin[total] = coin
        elif coin >= prev_coin[total - coin]:
            if min_tax[total] > min_tax[total] + tax[coin]:
                min_tax[total] = min_tax[total] + tax[coin]
                prev_coin[total] = coin

# Determine the subset of coins that minimize the total tax paid
total = 273
subset = []
while total > 0:
    subset.append(prev_coin[total])
    total -= prev_coin[total]

# Print the subset of coins in Python syntax
print(subset[::-1])
