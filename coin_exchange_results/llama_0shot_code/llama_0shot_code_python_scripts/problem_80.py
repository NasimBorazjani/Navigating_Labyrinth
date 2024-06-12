
coins = [8, 7, 5, 24, 3, 18, 36, 39, 36, 25, 25, 33, 16, 20, 34, 9, 1, 22, 25, 13, 8, 37, 35, 39, 11, 26, 36, 25, 25, 27, 2, 4, 35, 2, 16, 22, 12, 15, 19, 2, 17, 25, 28, 12, 26, 17, 33, 5, 30, 3, 21, 3]
tax = {13: 7, 39: 4, 20: 18, 5: 1, 12: 7, 9: 5, 28: 20, 24: 11, 3: 3, 17: 3, 21: 9, 37: 6, 16: 8, 15: 1, 26: 10, 36: 6, 22: 9, 2: 2, 8: 1, 25: 20, 4: 3, 7: 5, 19: 7, 30: 6, 27: 12, 1: 1, 34: 7, 35: 5, 11: 6, 18: 12, 33: 4}

coins.sort(reverse=True)
dp = [(float('inf'), None)] * 398

for coin in coins:
    for i in range(coin, 398):
        if dp[i - coin][0] != float('inf') and dp[i - coin][0] + tax[coin] < dp[i][0]:
            dp[i] = (dp[i - coin][0] + tax[coin], coin)

selected_coins = []
total_value = 397
while total_value > 0:
    coin = dp[total_value][1]
    selected_coins.append(coin)
    total_value -= coin

print(selected_coins)
