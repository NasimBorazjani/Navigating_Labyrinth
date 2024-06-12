
def taxed_coin_exchange(coins, target_sum, tax_values):
    dp = [[0 for _ in range(target_sum + 1)] for _ in range(len(coins) + 1)]
    
    for i in range(1, len(coins) + 1):
        for j in range(1, target_sum + 1):
            if coins[i - 1] <= j:
                if (coins[i - 1] % 2 == 0 and coins[i - 1] >= coins[i - 2]) or (coins[i - 1] % 2 != 0 and coins[i - 1] < coins[i - 2]):
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - coins[i - 1]] + tax_values[coins[i - 1]])
                else:
                    dp[i][j] = dp[i - 1][j]
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

coins = [35, 14, 15, 111, 8, 4, 6, 37, 14, 33, 45, 32, 46, 41, 38, 19, 34, 14, 2, 4, 24, 36, 46, 33, 12, 2, 14, 28, 12, 21, 34, 26, 28, 27, 25, 4, 23, 43, 43, 20, 10, 13, 5, 36, 27, 36]
target_sum = 462
tax_values = {33: 16, 21: 14, 4: 1, 13: 9, 23: 8, 2: 2, 12: 2, 41: 15, 46: 6, 45: 2, 34: 16, 24: 15, 19: 4, 5: 4, 35: 14, 6: 6, 37: 13, 26: 16, 43: 20, 15: 13, 111: 2, 38: 1, 10: 7, 32: 13, 20: 14, 27: 15, 36: 14, 25: 8, 14: 2, 28: 10, 8: 4}

selected_coins = taxed_coin_exchange(coins, target_sum, tax_values)
print(selected_coins)
