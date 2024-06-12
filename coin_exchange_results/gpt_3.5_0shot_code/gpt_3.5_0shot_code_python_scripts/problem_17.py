
def taxed_coin_exchange(coins, target_sum, tax_values):
    dp = [[0 for _ in range(target_sum + 1)] for _ in range(len(coins) + 1)]

    for i in range(1, len(coins) + 1):
        for j in range(1, target_sum + 1):
            if coins[i - 1] <= j:
                if coins[i - 1] % 2 == 0:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - coins[i - 1]] + tax_values[coins[i - 1]])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - coins[i - 1]])
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

coins = [4, 2, 18, 5, 18, 13, 22, 15, 5, 14, 15, 21, 23, 13, 19, 22, 6, 12, 19, 8, 15, 8, 12, 15, 11, 17, 7, 19, 23, 9, 3, 4, 12, 10, 11, 2, 22, 19, 19, 11, 18, 6, 10, 23, 20, 1, 6, 23, 8, 6]
target_sum = 233
tax_values = {21: 18, 1: 1, 13: 3, 20: 2, 19: 7, 5: 4, 18: 4, 4: 1, 15: 5, 12: 7, 17: 5, 22: 10, 8: 3, 7: 5, 23: 11, 9: 7, 10: 8, 3: 2, 14: 4, 6: 1, 2: 2, 11: 10}

result = taxed_coin_exchange(coins, target_sum, tax_values)
print(result)
