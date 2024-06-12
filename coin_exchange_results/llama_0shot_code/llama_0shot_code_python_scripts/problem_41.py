
coins = [20, 27, 20, 26, 2, 19, 25, 5, 14, 28, 7, 4, 20, 25, 9, 7, 3, 9, 27, 23, 2, 17, 25, 19, 10, 2, 8, 15, 3, 6, 24, 6, 22, 3, 10, 3, 2, 24, 7, 16, 2, 24, 21, 5, 23, 25, 10, 5, 20, 14, 24, 12, 11, 11, 13]
tax = {14: 7, 15: 15, 2: 2, 22: 7, 7: 1, 25: 7, 10: 4, 11: 11, 16: 11, 27: 8, 3: 2, 13: 5, 19: 10, 8: 5, 23: 18, 5: 4, 12: 4, 28: 6, 6: 4, 21: 3, 20: 15, 26: 1, 4: 4, 9: 9, 24: 6, 17: 13}

dp = [float('inf')] * 285
dp[0] = 0
prev_coin = 0
for coin in coins:
    for i in range(coin, 285):
        if (prev_coin < coin and coin % 2 == 0) or (prev_coin >= coin and coin % 2 == 1):
            dp[i] = min(dp[i], dp[i-coin] + tax[coin])
        prev_coin = coin

chosen_coins = []
total = 284
while total >= 0:
    chosen_coins.append(total)
    total -= total - dp[total]
chosen_coins.reverse()

print(chosen_coins)
