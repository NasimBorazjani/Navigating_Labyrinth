
coins = [19, 2, 25, 9, 6, 24, 4, 26, 17, 11, 11, 2, 17, 2, 5, 6, 3, 3, 3, 18, 26, 18, 21, 3, 5, 8, 12, 15, 8, 18, 24, 5, 19, 7, 18, 25, 12, 13, 12, 2, 25, 16, 17, 16, 3, 3]
tax = {26: 12, 25: 20, 17: 13, 13: 4, 16: 13, 11: 10, 24: 5, 5: 4, 8: 6, 7: 5, 4: 4, 12: 9, 18: 12, 3: 2, 21: 17, 19: 7, 2: 2, 9: 9, 6: 2, 15: 4}

dp = [float('inf')]*265
dp[0] = 0

for coin in coins:
    for i in range(coin, 265):
        dp[i] = min(dp[i], dp[i-coin]+tax[coin])

min_tax = float('inf')
chosen_coins = []

for i in range(264, -1, -1):
    if dp[i] < min_tax:
        min_tax = dp[i]
        chosen_coins = [i]
    elif dp[i] == min_tax:
        chosen_coins.append(i)

print(chosen_coins[::-1])
