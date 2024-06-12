
coins = [29, 32, 2, 34, 7, 25, 7, 14, 33, 1, 26, 18, 13, 11, 32, 31, 13, 2, 28, 21, 38, 8, 11, 28, 26, 9, 4, 28, 34, 23, 18, 31, 35, 2, 25, 20, 15, 5, 12, 10, 7, 14, 17, 4, 13, 24, 11, 16, 14, 27, 29]
tax = {10: 1, 25: 18, 1: 1, 15: 7, 12: 1, 23: 16, 9: 7, 27: 15, 29: 16, 28: 2, 32: 12, 24: 6, 5: 1, 8: 1, 11: 8, 17: 13, 13: 6, 38: 6, 31: 19, 4: 2, 34: 12, 21: 3, 2: 2, 33: 12, 20: 13, 18: 1, 14: 13, 16: 8, 7: 5, 35: 16, 26: 10}

coins.sort(reverse=True)
dp = [(float('inf'), None)] * 393
dp[0] = (0, None)

for coin in coins:
    for i in range(coin, 393):
        if dp[i - coin][0] + tax[coin] < dp[i][0]:
            dp[i] = (dp[i - coin][0] + tax[coin], coin)

selected_coins = []
total_value = 392
while total_value >= 0:
    coin = dp[total_value][1]
    if coin is not None:
        selected_coins.append(coin)
        total_value -= coin
    else:
        break

selected_coins.reverse()
print(selected_coins)
