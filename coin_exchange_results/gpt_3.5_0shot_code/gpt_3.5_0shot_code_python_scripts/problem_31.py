
coins = [12, 23, 57, 18, 6, 5, 21, 15, 14, 23, 5, 16, 9, 8, 19, 8, 19, 6, 8, 3, 12, 2, 14, 3, 3, 4, 26, 6, 6, 25, 9, 13, 20, 24, 6, 26, 14, 25, 5, 26]
tax_values = {6: 2, 12: 3, 9: 2, 2: 1, 14: 1, 16: 12, 21: 10, 4: 1, 8: 5, 26: 7, 23: 7, 57: 11, 15: 15, 19: 13, 25: 15, 13: 4, 5: 3, 24: 4, 3: 3, 18: 4, 20: 10}

def minimize_tax(coins, target_sum):
    dp = [[0, []] for _ in range(target_sum + 1)]
    
    for coin in coins:
        for i in range(target_sum, coin - 1, -1):
            if dp[i - coin][0] + tax_values[coin] < dp[i][0] and ((coin < dp[i][1][-1] and coin % 2 == 0) or (coin >= dp[i][1][-1] and coin % 2 != 0) or not dp[i][1]):
                dp[i] = [dp[i - coin][0] + tax_values[coin], dp[i - coin][1] + [coin]]
    
    return dp[target_sum][1]

target_sum = 260
selected_coins = minimize_tax(coins, target_sum)
print(selected_coins)
