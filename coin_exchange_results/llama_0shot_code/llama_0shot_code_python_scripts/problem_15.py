
coins = [1, 2, 17, 12, 7, 17, 2, 20, 4, 4, 17, 19, 15, 16, 18, 21, 18, 10, 3, 9, 12, 13, 8, 16, 9, 14, 13, 5, 13, 6, 20, 6, 13, 12, 8, 14, 15, 7, 10, 3, 16, 16, 9, 3, 2, 6, 9, 14, 16, 20, 11, 4, 17]
tax = {8: 5, 5: 2, 19: 2, 4: 4, 9: 2, 3: 1, 2: 2, 12: 1, 13: 6, 6: 5, 11: 1, 17: 14, 7: 4, 16: 13, 21: 10, 14: 13, 1: 1, 18: 12, 10: 10, 15: 11, 20: 20}

# Sort the coins in descending order
coins.sort(reverse=True)

# Initialize the list for the minimum tax
min_tax = [float('inf')] * 214
min_tax[0] = 0

# Calculate the minimum tax
prev_coin = coins[0]
for coin in coins:
    total_value = coin + min_tax[coin - prev_coin]
    total_tax = tax[coin] + min(min_tax[total_value - coin], min_tax[total_value - coin - 1])
    min_tax[total_value] = min(min_tax[total_value], total_tax)
    prev_coin = coin

# The minimum tax paid for a total value of 213
min_tax_total = min_tax[213]

# Find the subset of coins chosen
subset = []
prev_total = 213
for coin in coins:
    if prev_total - coin >= 0 and min_tax[prev_total - coin] < min_tax[prev_total]:
        subset.append(coin)
        prev_total -= coin

# Reverse the subset to get the correct order
subset.reverse()

print(subset)
