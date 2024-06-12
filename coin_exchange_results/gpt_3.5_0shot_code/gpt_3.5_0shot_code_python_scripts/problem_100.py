
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

coins = [19, 11, 3, 37, 9, 29, 42, 12, 2, 13, 15, 11, 25, 14, 31, 17, 24, 45, 5, 18, 42, 21, 28, 23, 26, 40, 27, 42, 12, 13, 16, 14, 31, 38, 9, 24, 27, 36, 13, 27, 15, 43, 9, 14, 34, 7, 15, 12, 31, 44]
tax_values = {37: 7, 45: 7, 29: 6, 27: 2, 2: 2, 40: 6, 13: 9, 17: 2, 9: 2, 15: 12, 36: 2, 26: 18, 44: 5, 42: 4, 38: 8, 43: 2, 12: 4, 24: 20, 28: 15, 16: 7, 21: 13, 23: 5, 19: 4, 25: 16, 3: 2, 18: 13, 34: 16, 31: 2, 5: 4, 14: 2, 7: 1, 11: 8}
target_sum = 449

result = taxed_coin_exchange(coins, target_sum, tax_values)
print(result)
