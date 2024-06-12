
coins = [12, 5, 22, 10, 4, 26, 26, 31, 13, 30, 37, 14, 14, 38, 9, 30, 7, 16, 21, 37, 4, 24, 10, 41, 13, 16, 3, 40, 24, 117, 34, 7, 11, 14, 28, 37, 21, 32, 2, 15, 5, 13, 3, 28, 31, 22, 30, 32, 38, 25, 10, 4, 30]
tax_values = {10: 7, 2: 2, 14: 12, 15: 8, 13: 10, 9: 1, 38: 17, 117: 2, 16: 13, 25: 11, 31: 3, 32: 2, 22: 10, 7: 4, 12: 3, 4: 1, 40: 2, 34: 4, 41: 9, 30: 8, 11: 10, 26: 13, 28: 6, 3: 2, 37: 17, 5: 5, 21: 3, 24: 13}

def minimize_tax(coins, target_sum):
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
    i, j = len(coins), target_sum
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_coins.append(coins[i - 1])
            j -= coins[i - 1]
        i -= 1

    return selected_coins[::-1]

target_sum = 411
selected_coins = minimize_tax(coins, target_sum)
print(selected_coins)
