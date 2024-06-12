
def taxed_coin_exchange(coins, target_sum, tax_values):
    dp = [[0 for _ in range(target_sum + 1)] for _ in range(len(coins) + 1)]
    
    for i in range(1, len(coins) + 1):
        for j in range(1, target_sum + 1):
            if coins[i-1] <= j:
                if coins[i-1] % 2 == 0:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-coins[i-1]] + tax_values[coins[i-1]])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-coins[i-1]])
            else:
                dp[i][j] = dp[i-1][j]
    
    selected_coins = []
    i = len(coins)
    j = target_sum
    while i > 0 and j > 0:
        if dp[i][j] != dp[i-1][j]:
            selected_coins.append(coins[i-1])
            j -= coins[i-1]
        i -= 1
    
    return selected_coins[::-1]

coins = [39, 3, 38, 10, 3, 5, 6, 14, 32, 7, 30, 28, 17, 9, 8, 13, 17, 41, 25, 6, 19, 36, 5, 36, 8, 38, 6, 19, 25, 3, 22, 18, 3, 21, 57, 37, 42, 30, 54, 13, 36, 6, 13, 17, 10, 4, 36]
target_sum = 452
tax_values = {37: 2, 38: 4, 30: 18, 39: 18, 14: 1, 18: 1, 4: 1, 10: 8, 21: 10, 6: 5, 42: 13, 32: 10, 25: 2, 17: 15, 13: 2, 9: 4, 22: 17, 7: 5, 3: 2, 54: 7, 19: 15, 8: 2, 36: 17, 28: 6, 5: 5, 41: 9, 57: 12}

result = taxed_coin_exchange(coins, target_sum, tax_values)
print(result)
