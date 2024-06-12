
def taxed_coin_exchange(coins, target_sum, tax_values):
    dp = [[0 for _ in range(target_sum + 1)] for _ in range(len(coins) + 1)]
    
    for i in range(1, len(coins) + 1):
        for j in range(1, target_sum + 1):
            if coins[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-coins[i-1]] + tax_values[coins[i-1]])
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

coins = [9, 18, 7, 20, 4, 12, 5, 5, 18, 5, 2, 11, 5, 16, 19, 8, 10, 9, 12, 14, 17, 6, 14, 16, 20, 10, 10, 13, 4, 13, 7, 14, 14, 10, 2, 7, 14, 11, 16, 10, 10, 5, 14, 20, 4, 17]
target_sum = 206
tax_values = {17: 16, 8: 8, 6: 6, 16: 12, 5: 4, 14: 12, 18: 9, 12: 1, 19: 12, 4: 2, 7: 3, 10: 7, 11: 7, 13: 6, 2: 1, 9: 1, 20: 10}

result = taxed_coin_exchange(coins, target_sum, tax_values)
print(result)
