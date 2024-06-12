
coins = [13, 19, 9, 4, 18, 17, 2, 14, 17, 17, 8, 6, 4, 10, 19, 37, 20, 19, 14, 7, 6, 11, 21, 9, 3, 10, 21, 20, 2, 17, 2]
tax = {14: 2, 18: 9, 11: 10, 9: 6, 10: 9, 13: 10, 37: 9, 6: 5, 2: 2, 4: 1, 8: 3, 19: 10, 17: 7, 7: 6, 3: 3, 21: 3, 20: 4}

dp = [float('inf')] * 216
dp[0] = 0

for coin in coins:
    for j in range(coin, 216):
        if dp[j - coin] != float('inf'):
            dp[j] = min(dp[j], dp[j - coin] + tax[coin])

total = 215
result = []
while total > 0:
    for coin in coins:
        if dp[total] == dp[total - coin] + tax[coin]:
            result.append(coin)
            total -= coin
            break

print(result)
