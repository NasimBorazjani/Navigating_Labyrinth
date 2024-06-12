
coins = [10, 2, 5, 22, 15, 3, 4, 66, 3, 11, 21, 16, 69, 2, 19, 20, 9, 24, 24, 20, 12, 13, 21, 7, 7, 23, 25, 10]
tax_values = {66: 17, 9: 3, 15: 10, 7: 6, 3: 3, 13: 7, 11: 10, 25: 14, 22: 18, 24: 17, 12: 6, 23: 18, 2: 2, 10: 5, 19: 10, 20: 19, 5: 4, 16: 1, 21: 20, 69: 14, 4: 4}

def is_valid_choice(prev_coin, curr_coin):
    if curr_coin < prev_coin:
        return curr_coin % 2 == 0
    else:
        return curr_coin % 2 != 0

def taxed_coin_exchange(coins, target_sum):
    dp = [[0, []] for _ in range(target_sum + 1)]

    for coin in coins:
        for i in range(target_sum, coin - 1, -1):
            if dp[i - coin][0] + tax_values[coin] < dp[i][0] and is_valid_choice(dp[i - coin][1][-1], coin):
                dp[i][0] = dp[i - coin][0] + tax_values[coin]
                dp[i][1] = dp[i - coin][1] + [coin]

    return dp[target_sum][1]

subset = taxed_coin_exchange(coins, 268)
print(subset)
