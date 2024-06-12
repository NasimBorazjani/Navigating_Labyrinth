
coins = [3, 35, 33, 20, 31, 29, 12, 31, 8, 10, 3, 17, 2, 28, 6, 25, 10, 13, 31, 25, 37, 35, 9, 15, 113, 26, 18, 34, 30]
tax_values = {31: 11, 15: 6, 13: 13, 28: 1, 9: 6, 20: 1, 34: 15, 6: 5, 113: 20, 12: 6, 2: 1, 29: 10, 37: 2, 25: 11, 26: 10, 3: 3, 33: 19, 8: 7, 18: 6, 17: 7, 10: 8, 35: 11, 30: 16}

def is_valid_choice(prev_coin, curr_coin):
    if curr_coin < prev_coin:
        return curr_coin % 2 == 0
    else:
        return curr_coin % 2 != 0

def taxed_coin_exchange(coins, target_sum):
    dp = [[0, []] for _ in range(target_sum + 1)]

    for coin in coins:
        for i in range(target_sum, coin - 1, -1):
            if is_valid_choice(dp[i - coin][0], coin):
                if dp[i - coin][0] + tax_values[coin] > dp[i][0]:
                    dp[i][0] = dp[i - coin][0] + tax_values[coin]
                    dp[i][1] = dp[i - coin][1] + [coin]

    return dp[target_sum][1]

target_sum = 384
selected_coins = taxed_coin_exchange(coins, target_sum)
print(selected_coins)
