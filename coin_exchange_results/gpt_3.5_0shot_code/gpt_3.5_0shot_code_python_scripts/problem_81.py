
coins = [13, 30, 19, 13, 34, 12, 16, 21, 24, 39, 37, 32, 3, 5, 30, 37, 29, 20, 15, 23, 30, 24, 12, 21, 19, 10, 26, 29, 3, 23, 20, 40, 22, 13, 2, 36, 8, 40, 6, 24, 24, 11, 26, 37, 16, 57, 39, 21, 17]
tax_values = {2: 2, 21: 6, 24: 9, 26: 2, 5: 3, 29: 10, 10: 7, 13: 13, 30: 17, 36: 15, 3: 1, 32: 7, 8: 5, 20: 2, 22: 3, 57: 19, 40: 8, 6: 4, 23: 8, 39: 3, 16: 5, 37: 6, 12: 9, 11: 11, 34: 6, 17: 2, 15: 10, 19: 17}

def minimize_tax(coins, target_sum):
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
    
    return selected_coins

target_sum = 412
selected_coins = minimize_tax(coins, target_sum)
print(selected_coins)
