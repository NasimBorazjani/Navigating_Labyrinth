
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

coins = [4, 17, 14, 12, 1, 3, 12, 10, 14, 9, 30, 20, 11, 17, 11, 16, 22, 17, 30, 5, 10, 16, 19, 27, 6, 18, 20, 19, 32, 25, 30, 15, 30, 21, 19, 25, 31, 33, 19, 10, 8, 16, 8]
target_sum = 328
tax_values = {1: 1, 31: 13, 25: 13, 11: 3, 3: 1, 10: 8, 33: 14, 8: 4, 9: 9, 4: 1, 20: 4, 12: 8, 27: 13, 30: 14, 16: 10, 18: 9, 32: 5, 21: 20, 6: 4, 5: 5, 22: 11, 17: 11, 19: 2, 14: 10, 15: 6}

result = taxed_coin_exchange(coins, target_sum, tax_values)
print(result)
