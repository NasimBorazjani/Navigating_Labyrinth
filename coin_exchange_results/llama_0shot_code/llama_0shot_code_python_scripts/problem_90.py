
# List of coins and their tax values
coins = [45, 45, 40, 38, 26, 3, 3, 21, 3, 35, 24, 9, 43, 10, 19, 5, 21, 36, 15, 18, 13, 33, 42, 34, 6, 20, 38, 25, 42, 19, 32, 9, 31, 4, 4, 25, 30, 8]
tax = {13: 7, 9: 1, 38: 9, 19: 4, 31: 18, 25: 18, 40: 13, 4: 2, 15: 8, 45: 2, 10: 10, 20: 18, 5: 3, 35: 12, 30: 8, 8: 5, 21: 5, 43: 12, 32: 10, 6: 2, 24: 18, 3: 2, 33: 7, 42: 4, 36: 10, 34: 6, 26: 5, 18: 6}

# Sort the coins in descending order
coins.sort(reverse=True)

# Initialize the total value and the result list
total_value = 453
result = []

# Loop through the coins
for coin in coins:
    if total_value >= coin:
        total_value -= coin
        result.append(coin)

# Check if the total value is 0
if total_value != 0:
    print("No solution found")
else:
    print(result)
