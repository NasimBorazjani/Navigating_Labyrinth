
coins = [22, 14, 13, 18, 2, 5, 14, 26, 28, 9, 20, 26, 11, 29, 2, 15, 13, 11, 28, 12, 14, 6, 3, 25, 12, 24, 4, 28, 27, 10, 20, 6, 8, 7, 37, 18, 3, 10, 27, 20, 21, 8, 11, 13, 5, 19, 4, 2]
tax = {2: 2, 14: 13, 29: 2, 13: 3, 25: 20, 28: 18, 11: 7, 9: 1, 3: 2, 15: 3, 8: 2, 7: 1, 12: 6, 26: 9, 19: 11, 24: 1, 22: 9, 27: 17, 6: 4, 18: 14, 21: 12, 4: 3, 37: 6, 20: 16, 5: 5, 10: 6}

dp = [float('inf')] * 294
dp[0] = 0

prev_coin = 0
for coin in sorted(coins):
    for i in range(coin, 294):
        if coin % 2 == 0 or coin >= prev_coin:
            dp[i] = min(dp[i], dp[i - coin] + tax[coin])
    prev_coin = coin

chosen_coins = []
total = 293
while total >= 0:
    chosen_coins.append(total)
    total -= dp[total]

print(chosen_coins[::-1])
