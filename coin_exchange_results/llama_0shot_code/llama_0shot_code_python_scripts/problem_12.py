
coins = [9, 2, 23, 20, 13, 4, 15, 16, 12, 21, 13, 9, 2, 14, 13, 14, 4, 19, 12, 6, 21, 23, 4, 18, 2, 23, 23, 6, 18, 23, 3, 16, 7, 2, 22, 16, 8, 10, 23, 17, 3, 18, 8]
tax = {9: 1, 17: 6, 2: 2, 22: 9, 13: 13, 16: 8, 12: 4, 4: 1, 21: 14, 14: 10, 19: 9, 10: 7, 7: 6, 8: 7, 6: 2, 23: 16, 18: 3, 20: 2, 3: 1, 15: 2}

dp = [float('inf')] * 231
dp[0] = 0

for coin in sorted(coins, reverse=True):
    for i in range(coin, 231):
        if dp[i-coin]+tax[coin] < dp[i]:
            dp[i] = dp[i-coin]+tax[coin]

chosen_coins = []
total = 230
for coin in sorted(coins, reverse=True):
    if total >= coin and dp[total-coin] + tax[coin] == dp[total]:
        chosen_coins.append(coin)
        total -= coin

print(chosen_coins)
