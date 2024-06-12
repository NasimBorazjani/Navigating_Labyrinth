
# Sort the coins in descending order
coins = sorted([(value, tax) for value, tax in {6: 6, 8: 6, 16: 4, 15: 11, 12: 3, 10: 5, 20: 14, 9: 3, 17: 8, 7: 5, 5: 5, 2: 1, 11: 4, 23: 18, 19: 3, 13: 13, 18: 6, 4: 3, 21: 20}.items()] + [(val, 0) for val in [20, 19, 2, 12, 23, 18, 15, 13, 10, 6, 9, 4, 9, 16, 5, 8, 19, 6, 7, 2, 6, 15, 10, 9, 4, 6, 19, 10, 10, 16, 21, 17, 21, 16, 13, 6, 16, 8, 7, 11, 13, 7, 21, 15, 15, 6, 11, 19, 7]], reverse=True)

# Initialize the dp array
dp = [float('inf')] * (217)
dp[0] = 0

# Initialize the backtracking array
backtrack = [None] * (217)

# Dynamic programming
for value, tax in coins:
    for total in range(value, 217):
        if dp[total - value] != float('inf') and dp[total - value] + tax < dp[total]:
            dp[total] = dp[total - value] + tax
            backtrack[total] = value

# Backtrack to find the selected coins
total = 216
selected_coins = []
while total > 0:
    selected_coins.append(backtrack[total])
    total -= backtrack[total]

# Print the selected coins in Python syntax
print("[", ", ".join(map(str, selected_coins[::-1])), "]")
