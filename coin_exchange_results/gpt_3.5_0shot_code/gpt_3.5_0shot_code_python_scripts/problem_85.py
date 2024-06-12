
coins = [38, 36, 40, 31, 39, 29, 36, 31, 16, 14, 16, 45, 40, 45, 257, 8, 39, 16, 2, 41, 9, 26, 22, 24]
tax_values = {9: 6, 14: 9, 24: 8, 26: 12, 16: 6, 45: 14, 8: 3, 22: 8, 38: 9, 40: 14, 31: 9, 257: 11, 36: 2, 2: 1, 41: 6, 29: 6, 39: 4}

def calculate_tax(coins_subset):
    total_tax = 0
    for coin in coins_subset:
        total_tax += tax_values[coin]
    return total_tax

def find_subset(coins, target_sum, prev_coin=None):
    if target_sum == 0:
        return []
    
    for i in range(len(coins)):
        if coins[i] % 2 == 0 and (prev_coin is None or coins[i] < prev_coin):
            new_target = target_sum - coins[i]
            if new_target >= 0:
                subset = find_subset(coins[i+1:], new_target, coins[i])
                if subset is not None:
                    return [coins[i]] + subset
        elif coins[i] % 2 != 0 and (prev_coin is None or coins[i] >= prev_coin):
            new_target = target_sum - coins[i]
            if new_target >= 0:
                subset = find_subset(coins[i+1:], new_target, coins[i])
                if subset is not None:
                    return [coins[i]] + subset
    return None

target_sum = 452
selected_coins = find_subset(coins, target_sum)
print(selected_coins)
print("Total tax paid:", calculate_tax(selected_coins))
