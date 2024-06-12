
coins = [17, 4, 35, 10, 42, 11, 10, 11, 2, 14, 29, 31, 33, 3, 38, 4, 32, 9, 19, 14, 4, 39, 6, 36, 31, 25, 40, 8, 33, 31, 11, 34, 18, 2, 32, 40, 4, 16, 1, 36, 37, 3, 33, 20, 10, 8, 9, 20, 14, 35, 36, 22, 35, 4]
tax_values = {37: 11, 10: 3, 36: 8, 32: 3, 3: 1, 18: 16, 14: 5, 35: 5, 16: 15, 8: 5, 42: 20, 29: 4, 6: 1, 25: 9, 11: 4, 20: 15, 39: 6, 38: 14, 34: 6, 40: 11, 9: 2, 17: 6, 19: 8, 4: 4, 22: 20, 31: 3, 1: 1, 33: 18, 2: 2}

def minimize_tax(coins, target_sum):
    dp = [[0, []] for _ in range(target_sum + 1)]
    
    for coin in coins:
        for i in range(target_sum, coin - 1, -1):
            if dp[i - coin][0] + tax_values[coin] < dp[i][0] and ((coin < dp[i - coin][1][-1] and coin % 2 == 0) or (coin >= dp[i - coin][1][-1] and coin % 2 != 0)):
                dp[i] = [dp[i - coin][0] + tax_values[coin], dp[i - coin][1] + [coin]]
    
    return dp[target_sum][1]

target_sum = 426
selected_coins = minimize_tax(coins, target_sum)
print(selected_coins)
