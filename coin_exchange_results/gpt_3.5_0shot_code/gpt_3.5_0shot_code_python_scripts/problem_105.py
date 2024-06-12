
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

coins = [26, 8, 34, 12, 20, 21, 35, 13, 28, 5, 16, 11, 24, 42, 16, 12, 34, 21, 27, 27, 20, 47, 9, 12, 38, 23, 43, 33, 26, 22, 38, 42, 20, 41, 47, 41, 24, 46, 35, 42, 9, 35, 13, 45, 24, 29, 45, 2, 41, 39, 24, 38, 39, 18, 5, 8, 36]
target_sum = 477
tax_values = {12: 8, 18: 6, 42: 8, 11: 9, 38: 13, 9: 9, 24: 15, 34: 1, 20: 5, 2: 2, 23: 2, 33: 12, 27: 8, 39: 11, 16: 1, 28: 12, 26: 11, 21: 7, 35: 7, 22: 19, 47: 9, 29: 12, 46: 3, 45: 9, 5: 1, 13: 13, 43: 8, 36: 11, 41: 4, 8: 8}

result = taxed_coin_exchange(coins, target_sum, tax_values)
print(result)
