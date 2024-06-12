
coins = [4, 17, 8, 15, 6, 14, 2, 4, 16, 10, 6, 5, 14, 8, 18, 2, 17, 9, 17, 59, 3, 10, 21, 4, 9, 14, 14, 20, 14, 8, 14, 18, 5, 16, 14, 17, 5, 3]
tax_values = {15: 6, 5: 5, 17: 1, 14: 4, 2: 2, 8: 2, 10: 9, 59: 9, 16: 8, 4: 3, 18: 10, 20: 11, 21: 8, 6: 6, 9: 9, 3: 3}

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
                if subset is not None or new_target == 0:
                    return [coins[i]] + subset
    
    return None

target_sum = 214
selected_coins = find_subset(coins, target_sum)
selected_coins_tax = calculate_tax(selected_coins)

print(selected_coins)
print("Total tax paid:", selected_coins_tax)
