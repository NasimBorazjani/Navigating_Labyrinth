
coins = [7, 2, 20, 24, 9, 24, 29, 6, 32, 26, 17, 61, 33, 14, 12, 20, 15, 34, 60, 18, 18, 37, 25, 9, 9, 21, 24, 30, 28, 3, 21, 32, 13, 10, 4, 2, 33, 36, 13, 24, 27, 7, 21, 4, 8, 17, 22, 3, 21, 12]
tax = {28: 10, 36: 13, 18: 13, 17: 8, 24: 3, 37: 19, 60: 16, 13: 5, 14: 8, 30: 18, 20: 5, 27: 16, 26: 11, 2: 2, 21: 3, 7: 7, 8: 6, 3: 3, 25: 20, 22: 8, 15: 12, 12: 4, 32: 11, 9: 5, 34: 15, 4: 2, 29: 5, 33: 6, 6: 6, 10: 3, 61: 10}

coins.sort(reverse=True)
n = len(coins)

dp = [[(float('inf'), None)]*(390) for _ in range(n+1)]
dp[0][0] = (0, None)

for i in range(1, n+1):
    for j in range(390):
        if j >= coins[i-1]:
            if dp[i-1][j-coins[i-1]][0] + tax[coins[i-1]] < dp[i-1][j][0]:
                dp[i][j] = (dp[i-1][j-coins[i-1]][0] + tax[coins[i-1]], coins[i-1])
            else:
                dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j]

min_tax, _ = dp[n][389]
coins_chosen = []
i, j = n, 389
while i > 0:
    if dp[i][j][1] == coins[i-1]:
        coins_chosen.append(coins[i-1])
        j -= coins[i-1]
    i -= 1
coins_chosen.reverse()

print(coins_chosen)
