
coins = [9, 30, 18, 32, 31, 20, 34, 9, 12, 18, 14, 16, 29, 37, 37, 6, 24, 10, 10, 35, 23, 4, 30, 121, 31, 16, 35]
tax_values = {35: 20, 4: 2, 18: 11, 24: 10, 10: 7, 14: 3, 37: 1, 16: 14, 12: 7, 6: 2, 29: 18, 34: 19, 121: 10, 31: 7, 30: 12, 32: 12, 23: 8, 20: 8, 9: 9}

def minimize_tax(coins, target_sum):
    dp = [[0, []] for _ in range(target_sum + 1)]
    
    for coin in coins:
        for i in range(target_sum, coin - 1, -1):
            if dp[i - coin][0] + tax_values[coin] > dp[i][0] and ((coin < dp[i][1][-1] and coin % 2 == 0) or (coin >= dp[i][1][-1] and coin % 2 != 0) or i == 0):
                dp[i] = [dp[i - coin][0] + tax_values[coin], dp[i - coin][1] + [coin]]
    
    return dp[target_sum][1]

target_sum = 406
selected_coins = minimize_tax(coins, target_sum)
print(selected_coins)
