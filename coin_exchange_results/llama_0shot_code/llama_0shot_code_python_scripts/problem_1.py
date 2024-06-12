
coins = [14, 2, 5, 8, 65, 5, 16, 2, 5, 2, 12, 17, 16, 15, 20, 4, 19, 9, 10, 64, 2, 10, 14, 2, 17]
tax = {20: 13, 4: 2, 17: 16, 19: 8, 64: 4, 5: 3, 14: 10, 10: 9, 65: 11, 16: 2, 12: 7, 8: 5, 2: 2, 15: 14, 9: 8}

# Sort the coins in descending order
coins.sort(reverse=True)

# Initialize dp array
n = len(coins)
dp = [float('inf')] * (208 + 1)
dp[-1] = 0

# Dynamic programming
for i in range(n):
    for j in range(208, coins[i] - 1, -1):
        if i > 0 and coins[i] < coins[i - 1] and coins[i] % 2 == 1:
            continue
        if i < n - 1 and coins[i] > coins[i + 1] and coins[i] % 2 == 0:
            continue
        dp[j] = min(dp[j], dp[j - coins[i]] + tax[coins[i]])

# Reconstruct the subset of coins
result = []
sum_ = 208
for i in range(n):
    if dp[sum_] != dp[sum_ - coins[i]] + tax[coins[i]]:
        continue
    result.append(coins[i])
    sum_ -= coins[i]

print(result)
