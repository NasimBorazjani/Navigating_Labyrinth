
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

coins = [17, 19, 5, 17, 13, 2, 12, 4, 4, 15, 19, 7, 18, 15, 4, 6, 9, 2, 4, 11, 21, 17, 20, 4, 8, 2, 19, 16, 2, 12, 8, 16, 18, 3, 18, 13, 3, 15, 7, 18, 4, 14, 3, 5, 8, 7, 19, 9, 17, 5, 17, 6, 3, 5, 15]
tax_values = {9: 9, 6: 1, 13: 4, 2: 1, 16: 3, 14: 4, 19: 16, 20: 2, 15: 3, 7: 3, 18: 14, 17: 15, 4: 2, 5: 5, 8: 8, 21: 10, 12: 11, 11: 7, 3: 2}
target_sum = 210

result = taxed_coin_exchange(coins, target_sum, tax_values)
print(result)
