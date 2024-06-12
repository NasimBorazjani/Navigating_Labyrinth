
coins = [14, 19, 3, 8, 5, 107, 4, 10, 9, 2, 11, 7, 11, 11, 4, 10, 17, 14, 18, 10, 21, 13, 2, 13, 19, 5, 8, 4, 7, 6, 10]
tax_values = {17: 9, 107: 7, 13: 11, 10: 7, 19: 12, 9: 2, 4: 4, 14: 8, 21: 14, 6: 2, 5: 3, 2: 2, 3: 3, 7: 6, 18: 6, 8: 4, 11: 11}

def calculate_tax(coins_subset):
    total_tax = 0
    for coin in coins_subset:
        total_tax += tax_values[coin]
    return total_tax

def find_subset(coins, target_sum, prev_coin=None, prev_coin_odd=True):
    if target_sum == 0:
        return []
    
    for i in range(len(coins)):
        if coins[i] >= prev_coin and prev_coin_odd == coins[i] % 2:
            new_target = target_sum - coins[i]
            if new_target >= 0:
                subset = find_subset(coins[i+1:], new_target, coins[i], not prev_coin_odd)
                if subset is not None:
                    return [coins[i]] + subset
    return None

target_sum = 215
selected_coins = find_subset(coins, target_sum)
selected_coins_tax = calculate_tax(selected_coins)

print(selected_coins)
print(f"Total tax paid: {selected_coins_tax}")
