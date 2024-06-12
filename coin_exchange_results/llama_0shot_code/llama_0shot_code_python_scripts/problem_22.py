
coins = [10, 2, 5, 22, 15, 3, 4, 66, 3, 11, 21, 16, 69, 2, 19, 20, 9, 24, 24, 20, 12, 13, 21, 7, 7, 23, 25, 10]
tax = {66: 17, 9: 3, 15: 10, 7: 6, 3: 3, 13: 7, 11: 10, 25: 14, 22: 18, 24: 17, 12: 6, 23: 18, 2: 2, 10: 5, 19: 10, 20: 19, 5: 4, 16: 1, 21: 20, 69: 14, 4: 4}

dp = [float('inf')] * 269
dp[0] = 0
prev = [None] * 269

for coin in coins:
    for i in range(coin, 269):
        if dp[i - coin] + tax[coin] < dp[i]:
            dp[i] = dp[i - coin] + tax[coin]
            prev[i] = coin

# Construct the list of coins used
coins_used = []
i = 268
while i > 0:
    coins_used.append(prev[i])
    i -= prev[i]

# Reverse the list to get the correct order
coins_used = coins_used[::-1]

print(coins_used)
