
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

coins = [10, 16, 2, 18, 10, 16, 17, 32, 18, 33, 23, 20, 21, 25, 32, 24, 10, 27, 13, 27, 30, 13, 19, 20, 4, 5, 15, 8, 8, 34, 21, 14, 3, 20, 10, 18, 3, 14, 28, 6, 4, 8, 15, 4, 30, 30, 12, 20, 14, 10]
target_sum = 357
tax_values = {30: 12, 20: 19, 16: 7, 24: 14, 12: 3, 13: 4, 8: 2, 2: 1, 21: 2, 23: 12, 34: 13, 27: 16, 3: 3, 28: 3, 14: 13, 6: 4, 33: 17, 10: 8, 5: 3, 15: 12, 4: 2, 18: 2, 19: 5, 17: 1, 32: 2, 25: 12}

result = taxed_coin_exchange(coins, target_sum, tax_values)
print(result)
