
def taxed_coin_exchange(coins, target_sum, tax_values):
    dp = [[0 for _ in range(target_sum + 1)] for _ in range(len(coins) + 1)]

    for i in range(1, len(coins) + 1):
        for j in range(1, target_sum + 1):
            if coins[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - coins[i - 1]] + tax_values[coins[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]

    selected_coins = []
    i, j = len(coins), target_sum
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_coins.append(coins[i - 1])
            j -= coins[i - 1]
        i -= 1

    return selected_coins[::-1]

coins = [28, 2, 4, 7, 11, 26, 14, 8, 23, 29, 18, 13, 26, 21, 10, 26, 8, 33, 9, 15, 4, 21, 19, 3, 7, 10, 4, 7, 16, 16, 11, 33, 12, 23, 5, 3, 26, 7, 17, 30, 22, 22, 6, 16, 18, 25, 26, 11, 13, 23, 17, 11, 20, 12]
target_sum = 339
tax_values = {10: 6, 18: 17, 33: 15, 16: 16, 3: 2, 30: 18, 13: 3, 21: 17, 23: 4, 12: 1, 7: 6, 17: 7, 4: 2, 6: 5, 2: 2, 11: 5, 14: 14, 29: 1, 20: 7, 8: 3, 15: 7, 28: 3, 26: 8, 19: 11, 9: 9, 22: 4, 5: 5, 25: 5}

selected_coins = taxed_coin_exchange(coins, target_sum, tax_values)
print(selected_coins)
