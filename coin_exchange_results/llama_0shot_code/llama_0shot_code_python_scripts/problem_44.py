
coins = [2, 27, 9, 80, 20, 81, 13, 24, 16, 6, 26, 12, 3, 26, 20, 8, 16, 8, 20, 22, 9, 34, 23, 8, 12, 34, 4, 6, 22, 19]
tax = {12: 9, 16: 12, 13: 5, 34: 8, 9: 9, 23: 4, 81: 2, 80: 20, 8: 1, 19: 19, 2: 2, 22: 13, 20: 7, 26: 11, 4: 1, 6: 2, 27: 4, 3: 1, 24: 12}

coins.sort(reverse=True)
dp = [float('inf')] * 347
dp[0] = 0

for coin in coins:
    for i in range(coin, 347):
        dp[i] = min(dp[i], dp[i-coin] + tax[coin])

min_tax = dp[-1]
chosen_coins = []
total = 346

for coin in coins:
    if total >= coin and dp[total] == dp[total-coin] + tax[coin]:
        chosen_coins.append(coin)
        total -= coin

print(chosen_coins)
