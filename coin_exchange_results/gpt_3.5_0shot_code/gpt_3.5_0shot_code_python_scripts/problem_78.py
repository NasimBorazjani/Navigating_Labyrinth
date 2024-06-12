
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

coins = [29, 32, 2, 34, 7, 25, 7, 14, 33, 1, 26, 18, 13, 11, 32, 31, 13, 2, 28, 21, 38, 8, 11, 28, 26, 9, 4, 28, 34, 23, 18, 31, 35, 2, 25, 20, 15, 5, 12, 10, 7, 14, 17, 4, 13, 24, 11, 16, 14, 27, 29]
target_sum = 392
tax_values = {10: 1, 25: 18, 1: 1, 15: 7, 12: 1, 23: 16, 9: 7, 27: 15, 29: 16, 28: 2, 32: 12, 24: 6, 5: 1, 8: 1, 11: 8, 17: 13, 13: 6, 38: 6, 31: 19, 4: 2, 34: 12, 21: 3, 2: 2, 33: 12, 20: 13, 18: 1, 14: 13, 16: 8, 7: 5, 35: 16, 26: 10}

result = taxed_coin_exchange(coins, target_sum, tax_values)
print(result)
