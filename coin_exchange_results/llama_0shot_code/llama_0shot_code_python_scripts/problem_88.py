
coins = [21, 31, 30, 31, 10, 17, 13, 35, 12, 2, 16, 40, 23, 10, 29, 13, 23, 2, 9, 5, 107, 46, 23, 11, 42, 9, 46, 28, 44, 22, 106, 10]
tax = {13: 9, 106: 19, 28: 20, 44: 14, 9: 6, 35: 6, 22: 19, 46: 17, 11: 7, 40: 12, 17: 15, 10: 4, 12: 6, 30: 20, 2: 2, 23: 11, 42: 10, 16: 1, 107: 11, 21: 12, 5: 3, 31: 13, 29: 20}
total_value = 465

# Initialize dp list
dp = [float('inf')] * (total_value + 1)
dp[0] = 0

# Iterate over the coins
for coin in coins:
    for i in range(total_value, coin - 1, -1):
        dp[i] = min(dp[i], dp[i - coin] + tax[coin])

# Find the subset of coins
subset = []
i = total_value
while i > 0:
    if dp[i] != dp[i - 1]:
        subset.append(i)
        i -= 1
    else:
        i -= coin

# Reverse the subset and print
subset.reverse()
print(subset)
