
coins = [28, 2, 4, 7, 11, 26, 14, 8, 23, 29, 18, 13, 26, 21, 10, 26, 8, 33, 9, 15, 4, 21, 19, 3, 7, 10, 4, 7, 16, 16, 11, 33, 12, 23, 5, 3, 26, 7, 17, 30, 22, 22, 6, 16, 18, 25, 26, 11, 13, 23, 17, 11, 20, 12]
tax = {10: 6, 18: 17, 33: 15, 16: 16, 3: 2, 30: 18, 13: 3, 21: 17, 23: 4, 12: 1, 7: 6, 17: 7, 4: 2, 6: 5, 2: 2, 11: 5, 14: 14, 29: 1, 20: 7, 8: 3, 15: 7, 28: 3, 26: 8, 19: 11, 9: 9, 22: 4, 5: 5, 25: 5}

# Sort the coins in descending order
coins.sort(reverse=True)

# Initialize the dp list
n = len(coins)
dp = [[float('inf')]*340 for _ in range(n+1)]
dp[0][0] = 0

# Dynamic programming
for i in range(1, n+1):
    for j in range(340):
        if j >= coins[i-1]:
            dp[i][j] = min(dp[i][j], dp[i-1][j-coins[i-1]] + tax[coins[i-1]])
        dp[i][j] = min(dp[i][j], dp[i-1][j])

# Find the subset of coins
subset = []
j = 339
for i in range(n, 0, -1):
    if dp[i][j] != dp[i-1][j]:
        subset.append(coins[i-1])
        j -= coins[i-1]

# Reverse the subset to get the correct order
subset.reverse()

# Print the subset in Python syntax
print(subset)
