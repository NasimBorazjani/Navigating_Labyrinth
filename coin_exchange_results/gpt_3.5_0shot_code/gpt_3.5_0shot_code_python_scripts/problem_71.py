
coins = [18, 11, 14, 3, 7, 18, 40, 3, 35, 30, 24, 29, 34, 11, 17, 14, 14, 10, 5, 40, 4, 31, 25, 14, 39, 12, 26, 24, 3, 8, 34, 2, 22, 189, 40]
tax_values = {29: 9, 40: 8, 30: 5, 17: 16, 3: 3, 5: 3, 2: 2, 22: 17, 11: 1, 14: 4, 8: 5, 18: 11, 26: 8, 39: 15, 7: 1, 31: 2, 24: 17, 189: 5, 12: 4, 25: 10, 35: 18, 10: 1, 4: 3, 34: 16}

def is_valid_choice(prev_coin, curr_coin):
    if curr_coin < prev_coin:
        return curr_coin % 2 == 0
    else:
        return curr_coin % 2 != 0

def taxed_coin_exchange(coins, target):
    dp = [[0, []] for _ in range(target+1)]
    
    for coin in coins:
        for i in range(target, coin-1, -1):
            if is_valid_choice(dp[i-coin][1][-1] if dp[i-coin][1] else 0, coin):
                if dp[i-coin][0] + tax_values[coin] > dp[i][0]:
                    dp[i] = [dp[i-coin][0] + tax_values[coin], dp[i-coin][1] + [coin]]
    
    return dp[target][1]

subset = taxed_coin_exchange(coins, 400)
print(subset)
