
coins = [14, 19, 3, 8, 5, 107, 4, 10, 9, 2, 11, 7, 11, 11, 4, 10, 17, 14, 18, 10, 21, 13, 2, 13, 19, 5, 8, 4, 7, 6, 10]
tax = {17: 9, 107: 7, 13: 11, 10: 7, 19: 12, 9: 2, 4: 4, 14: 8, 21: 14, 6: 2, 5: 3, 2: 2, 3: 3, 7: 6, 18: 6, 8: 4, 11: 11}

dp = [float('inf')] * 216
dp[0] = 0

for coin in coins:
    for total in range(coin, 216):
        dp[total] = min(dp[total], dp[total - coin] + tax[coin])

total = 215
solution = []
while total > 0:
    for coin in coins:
        if dp[total] == dp[total - coin] + tax[coin]:
            solution.append(coin)
            total -= coin
            break

solution.reverse()
print(solution)
