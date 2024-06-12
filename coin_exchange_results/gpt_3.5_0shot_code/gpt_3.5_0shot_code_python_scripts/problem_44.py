
coins = [2, 27, 9, 80, 20, 81, 13, 24, 16, 6, 26, 12, 3, 26, 20, 8, 16, 8, 20, 22, 9, 34, 23, 8, 12, 34, 4, 6, 22, 19]
tax_values = {12: 9, 16: 12, 13: 5, 34: 8, 9: 9, 23: 4, 81: 2, 80: 20, 8: 1, 19: 19, 2: 2, 22: 13, 20: 7, 26: 11, 4: 1, 6: 2, 27: 4, 3: 1, 24: 12}

def calculate_tax(coins_subset):
    total_tax = 0
    for coin in coins_subset:
        total_tax += tax_values[coin]
    return total_tax

def find_subset(coins, target_sum, prev_coin=None):
    if target_sum == 0:
        return []
    
    for i in range(len(coins)):
        if coins[i] >= prev_coin and coins[i] % 2 == 0:
            new_target = target_sum - coins[i]
            if new_target >= 0:
                subset = find_subset(coins[i+1:], new_target, coins[i])
                if subset is not None:
                    return [coins[i]] + subset
    return None

target_sum = 346
selected_coins = find_subset(coins, target_sum)
total_tax = calculate_tax(selected_coins)

print(selected_coins)
print("Total tax paid:", total_tax)
