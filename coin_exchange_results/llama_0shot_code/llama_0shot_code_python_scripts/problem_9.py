
coins = [3, 6, 9, 10, 13, 15, 18, 5, 21, 19, 12, 15, 5, 9, 4, 16, 8, 4, 7, 7, 7, 2, 16, 14, 18, 3, 89, 21, 12, 10, 7, 14, 4, 11, 6, 20]
taxes = {14: 1, 89: 13, 2: 2, 5: 2, 4: 4, 6: 6, 8: 2, 16: 5, 21: 4, 20: 2, 18: 9, 11: 10, 10: 3, 12: 12, 15: 5, 13: 1, 3: 1, 19: 19, 7: 7, 9: 3}

# Sort the coins in descending order
coins.sort(reverse=True)

# Initialize the total taxes list
total_taxes = [float('inf')] * 230
total_taxes[0] = 0

# Update the total taxes list for all coins
for coin in coins:
    for total in range(coin, 230):
        total_taxes[total] = min(total_taxes[total], total_taxes[total - coin] + taxes[coin])

# Get the subset of coins
subset = []
total = 229
while total > 0:
    for coin in coins:
        if total >= coin and total_taxes[total] == total_taxes[total - coin] + taxes[coin]:
            subset.append(coin)
            total -= coin
            break

# Reverse the subset to get the correct order
subset.reverse()

print(subset)
