
coins = [19, 11, 35, 3, 12, 23, 42, 45, 8, 12, 32, 82, 39, 12, 45, 12, 40, 38, 28, 6, 32, 37, 39, 9, 43, 12, 38, 4, 42, 44, 41, 37, 83, 5, 38]
tax_values = {37: 6, 43: 18, 32: 16, 4: 4, 83: 4, 8: 5, 23: 18, 12: 6, 82: 16, 44: 20, 39: 1, 19: 8, 35: 7, 38: 11, 11: 3, 42: 5, 45: 12, 3: 1, 6: 2, 41: 3, 28: 18, 40: 2, 9: 6, 5: 4}

def is_valid_choice(prev_coin, curr_coin):
    if curr_coin < prev_coin:
        return curr_coin % 2 == 0
    else:
        return curr_coin % 2 != 0

def taxed_coin_exchange(coins, target_sum):
    dp = [[0, []] for _ in range(target_sum + 1)]
    
    for coin in coins:
        for i in range(target_sum, coin - 1, -1):
            if dp[i - coin][0] + tax_values[coin] > dp[i][0] and is_valid_choice(dp[i - coin][1][-1], coin):
                dp[i][0] = dp[i - coin][0] + tax_values[coin]
                dp[i][1] = dp[i - coin][1] + [coin]
    
    return dp[target_sum][1]

target_sum = 466
selected_coins = taxed_coin_exchange(coins, target_sum)
print(selected_coins)
