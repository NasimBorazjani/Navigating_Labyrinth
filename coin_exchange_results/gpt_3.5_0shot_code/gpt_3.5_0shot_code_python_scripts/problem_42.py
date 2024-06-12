
def taxed_coin_exchange(coins, target_sum, tax_values):
    dp = [[0 for _ in range(target_sum + 1)] for _ in range(len(coins) + 1)]

    for i in range(1, len(coins) + 1):
        for j in range(1, target_sum + 1):
            if coins[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - coins[i - 1]] + tax_values[coins[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]

    selected_coins = []
    i = len(coins)
    j = target_sum
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_coins.append(coins[i - 1])
            j -= coins[i - 1]
        i -= 1

    return selected_coins[::-1]

coins = [24, 10, 24, 3, 21, 7, 21, 26, 8, 14, 24, 5, 13, 10, 25, 6, 9, 4, 18, 4, 15, 4, 10, 23, 6, 13, 26, 20, 8, 10, 29, 27, 27, 20, 2, 15, 9, 9, 25, 8, 2, 27, 5, 22, 19, 26, 2, 29, 12, 9, 6, 12, 2, 15, 5, 16, 3, 29, 19]
target_sum = 300
tax_values = {5: 2, 9: 8, 12: 5, 14: 4, 22: 8, 26: 3, 8: 7, 27: 2, 20: 13, 3: 3, 13: 3, 2: 1, 19: 19, 29: 4, 10: 3, 18: 14, 21: 12, 15: 12, 4: 3, 23: 5, 16: 9, 25: 16, 7: 4, 24: 17, 6: 6}

result = taxed_coin_exchange(coins, target_sum, tax_values)
print(result)
