
coins = [23, 10, 22, 30, 5, 16, 2, 28, 25, 26, 30, 25, 35, 32, 10, 4, 24, 32, 34, 12, 11, 5, 5, 18, 16, 24, 3, 12, 11, 5, 2, 7, 19, 34, 7, 30, 17, 11, 16, 10, 31, 31, 34, 27, 3, 24]
tax_values = {24: 9, 26: 11, 17: 7, 7: 4, 12: 4, 35: 18, 5: 5, 31: 8, 2: 2, 3: 1, 27: 14, 34: 3, 30: 1, 23: 6, 4: 2, 10: 8, 18: 18, 25: 15, 28: 4, 32: 19, 11: 7, 16: 6, 19: 11, 22: 5}

def minimize_tax(coins, tax_values, target_sum):
    dp = [[0, []] for _ in range(target_sum + 1)]
    
    for coin in coins:
        for i in range(target_sum, coin - 1, -1):
            if dp[i - coin][0] + tax_values[coin] < dp[i][0] and ((coin < dp[i][1][-1] and coin % 2 == 0) or (coin >= dp[i][1][-1] and coin % 2 != 0) or not dp[i][1]):
                dp[i] = [dp[i - coin][0] + tax_values[coin], dp[i - coin][1] + [coin]]
    
    return dp[target_sum][1]

target_sum = 359
selected_coins = minimize_tax(coins, tax_values, target_sum)
print(selected_coins)
