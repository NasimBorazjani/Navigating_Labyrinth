
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

coins = [12, 26, 9, 14, 11, 25, 28, 17, 18, 18, 9, 16, 2, 11, 31, 25, 4, 23, 9, 3, 24, 22, 3, 14, 32, 30, 19, 7, 4, 22, 33, 13, 25, 15, 14, 28, 20, 3, 4, 3, 32, 10, 6, 29, 25]
target_sum = 325
tax_values = {29: 2, 9: 7, 17: 4, 18: 9, 26: 6, 33: 11, 16: 12, 4: 3, 31: 12, 6: 2, 11: 8, 23: 14, 7: 1, 30: 8, 12: 8, 13: 2, 20: 13, 24: 16, 14: 8, 19: 8, 10: 8, 32: 14, 3: 2, 2: 2, 25: 19, 22: 18, 15: 5, 28: 9}

result = taxed_coin_exchange(coins, target_sum, tax_values)
print(result)
