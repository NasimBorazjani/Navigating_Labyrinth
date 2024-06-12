
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

coins = [31, 83, 19, 4, 13, 27, 13, 18, 21, 24, 9, 3, 2, 30, 16, 14, 31, 29, 27, 23, 18, 8, 32, 3, 3, 25, 17, 8, 32, 5, 2, 28, 30, 26, 25, 12, 12]
tax_values = {32: 1, 19: 12, 3: 1, 27: 14, 5: 3, 9: 5, 13: 11, 14: 10, 28: 6, 31: 15, 8: 8, 18: 18, 17: 7, 2: 2, 12: 9, 24: 16, 83: 6, 23: 9, 16: 15, 29: 4, 25: 5, 26: 18, 4: 1, 21: 10, 30: 10}
target_sum = 335

result = taxed_coin_exchange(coins, target_sum, tax_values)
print(result)
