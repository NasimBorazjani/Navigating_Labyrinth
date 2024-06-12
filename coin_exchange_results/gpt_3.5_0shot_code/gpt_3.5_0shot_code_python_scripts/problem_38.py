
def taxed_coin_exchange(coins, target_sum, tax_values):
    dp = [[0 for _ in range(target_sum + 1)] for _ in range(len(coins) + 1)]

    for i in range(1, len(coins) + 1):
        for j in range(1, target_sum + 1):
            if coins[i - 1] <= j:
                if coins[i - 1] % 2 == 0:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - coins[i - 1]] + tax_values[coins[i - 1]])
                else:
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

coins = [30, 24, 27, 14, 29, 17, 4, 21, 20, 14, 19, 23, 18, 4, 12, 9, 24, 26, 21, 17, 3, 13, 25, 20, 16, 12, 2, 9, 17, 5, 6, 24, 13, 11, 6, 15, 13, 5, 13, 25, 10, 15, 10, 3, 2, 18, 7, 23, 5, 18, 21, 6]
target_sum = 300
tax_values = {14: 11, 3: 1, 18: 5, 21: 1, 27: 2, 19: 14, 6: 6, 25: 8, 5: 3, 29: 4, 7: 6, 24: 10, 10: 2, 13: 9, 9: 1, 11: 8, 16: 10, 2: 1, 12: 12, 15: 4, 23: 17, 17: 9, 26: 13, 30: 17, 4: 3, 20: 6}

result = taxed_coin_exchange(coins, target_sum, tax_values)
print(result)
