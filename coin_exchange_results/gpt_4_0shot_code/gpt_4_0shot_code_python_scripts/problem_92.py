
def taxed_coin_exchange(coins, tax, total):
    coins.sort()
    dp = [[float('inf')] * (total + 1) for _ in range(len(coins) + 1)]
    dp[0][0] = 0
    for i in range(1, len(coins) + 1):
        for j in range(total + 1):
            if j < coins[i - 1] or (i > 1 and coins[i - 1] < coins[i - 2] and coins[i - 1] % 2 != 0) or (i > 1 and coins[i - 1] >= coins[i - 2] and coins[i - 1] % 2 == 0):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - coins[i - 1]] + tax[coins[i - 1]])
    chosen_coins = []
    i, j = len(coins), total
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            chosen_coins.append(coins[i - 1])
            j -= coins[i - 1]
        i -= 1
    return chosen_coins[::-1]

coins = [19, 11, 35, 3, 12, 23, 42, 45, 8, 12, 32, 82, 39, 12, 45, 12, 40, 38, 28, 6, 32, 37, 39, 9, 43, 12, 38, 4, 42, 44, 41, 37, 83, 5, 38]
tax = {37: 6, 43: 18, 32: 16, 4: 4, 83: 4, 8: 5, 23: 18, 12: 6, 82: 16, 44: 20, 39: 1, 19: 8, 35: 7, 38: 11, 11: 3, 42: 5, 45: 12, 3: 1, 6: 2, 41: 3, 28: 18, 40: 2, 9: 6, 5: 4}
total = 466
print(taxed_coin_exchange(coins, tax, total))
