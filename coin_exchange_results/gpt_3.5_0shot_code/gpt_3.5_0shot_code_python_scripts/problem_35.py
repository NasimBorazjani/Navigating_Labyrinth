
coins = [27, 17, 6, 5, 20, 3, 4, 29, 25, 27, 20, 18, 18, 25, 2, 13, 15, 4, 12, 4, 26, 12, 26, 24, 17, 23, 2, 6, 2, 29, 3, 20, 12, 7, 9, 12, 26, 11, 2, 5, 10, 25, 3, 13, 7, 25]
tax_values = {2: 1, 13: 11, 26: 13, 5: 1, 4: 2, 9: 8, 15: 8, 18: 6, 20: 18, 3: 1, 17: 17, 6: 2, 10: 10, 12: 1, 23: 10, 7: 6, 29: 13, 25: 15, 11: 10, 27: 2, 24: 18}

def minimize_tax(coins, target_sum):
    dp = [[0, []] for _ in range(target_sum + 1)]
    
    for coin in coins:
        for i in range(target_sum, coin - 1, -1):
            if dp[i - coin][0] + tax_values[coin] > dp[i][0]:
                dp[i] = [dp[i - coin][0] + tax_values[coin], dp[i - coin][1] + [coin]]
    
    return dp[target_sum][1]

target_sum = 295
selected_coins = minimize_tax(coins, target_sum)
print(selected_coins)
