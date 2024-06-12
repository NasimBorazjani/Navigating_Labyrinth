
coins = [29, 29, 22, 23, 23, 3, 26, 9, 15, 8, 21, 15, 29, 25, 71, 27, 23, 6, 7, 9, 15, 21, 6, 8, 19, 17, 18, 6, 26, 24, 24, 3, 25, 2]
target_sum = 307
tax_values = {24: 14, 2: 1, 25: 2, 26: 14, 18: 12, 27: 15, 29: 19, 19: 3, 15: 7, 9: 1, 8: 1, 21: 18, 6: 1, 71: 3, 23: 4, 17: 7, 7: 2, 22: 11, 3: 1}

def calculate_tax(coins):
    total_tax = 0
    for coin in coins:
        total_tax += tax_values[coin]
    return total_tax

def is_valid_choice(prev_coin, current_coin):
    if current_coin < prev_coin:
        return current_coin % 2 == 0
    else:
        return current_coin % 2 != 0

def find_subset(coins, target_sum):
    dp = [[0, []] for _ in range(target_sum + 1)]
    
    for coin in coins:
        for i in range(target_sum, coin - 1, -1):
            if is_valid_choice(dp[i - coin][1][-1] if dp[i - coin][1] else 0, coin):
                if dp[i][0] < dp[i - coin][0] + tax_values[coin]:
                    dp[i][0] = dp[i - coin][0] + tax_values[coin]
                    dp[i][1] = dp[i - coin][1] + [coin]
    
    return dp[target_sum][1]

subset = find_subset(coins, target_sum)
print(subset)
