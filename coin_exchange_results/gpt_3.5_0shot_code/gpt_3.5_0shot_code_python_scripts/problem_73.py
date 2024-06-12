
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

coins = [15, 2, 37, 38, 21, 30, 19, 28, 3, 35, 16, 32, 3, 28, 24, 27, 10, 1, 14, 3, 33, 6, 18, 37, 20, 19, 4, 31, 34, 39, 7, 13, 29, 38, 34, 14, 29, 13, 5, 33, 31, 24]
tax_values = {33: 10, 13: 12, 6: 1, 15: 2, 20: 15, 4: 3, 27: 7, 35: 5, 19: 18, 14: 13, 16: 4, 2: 2, 39: 19, 21: 18, 3: 2, 37: 14, 10: 1, 24: 3, 32: 2, 7: 4, 1: 1, 5: 4, 31: 4, 34: 7, 30: 8, 28: 11, 18: 9, 29: 2, 38: 1}

target_sum = 397
result = taxed_coin_exchange(coins, target_sum, tax_values)
print(result)
