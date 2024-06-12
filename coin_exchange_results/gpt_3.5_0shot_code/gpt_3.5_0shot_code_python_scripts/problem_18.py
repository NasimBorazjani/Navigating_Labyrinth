
coins = [10, 5, 6, 2, 16, 19, 18, 5, 11, 12, 11, 7, 13, 19, 11, 12, 8, 17, 5, 18, 3, 12, 10, 14, 20, 18, 10, 11, 20, 13, 8, 8, 2, 7, 17, 10, 7, 21, 9, 20, 17, 1, 8, 19, 17, 16, 17, 10, 20, 8, 16, 14, 9]
tax_values = {7: 2, 3: 2, 18: 1, 13: 3, 2: 2, 19: 17, 16: 6, 10: 1, 9: 9, 12: 7, 8: 7, 6: 3, 21: 18, 11: 10, 14: 13, 1: 1, 5: 5, 20: 18, 17: 14}

def minimize_tax(coins, target_sum):
    dp = [[0, []] for _ in range(target_sum + 1)]
    
    for coin in coins:
        for i in range(target_sum, coin - 1, -1):
            if dp[i - coin][0] + tax_values[coin] > dp[i][0]:
                dp[i] = [dp[i - coin][0] + tax_values[coin], dp[i - coin][1] + [coin]]
    
    return dp[target_sum][1]

subset = minimize_tax(coins, 211)
print(subset)
