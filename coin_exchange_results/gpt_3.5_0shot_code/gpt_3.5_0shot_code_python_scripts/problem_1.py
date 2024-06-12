
coins = [14, 2, 5, 8, 65, 5, 16, 2, 5, 2, 12, 17, 16, 15, 20, 4, 19, 9, 10, 64, 2, 10, 14, 2, 17]
tax_values = {20: 13, 4: 2, 17: 16, 19: 8, 64: 4, 5: 3, 14: 10, 10: 9, 65: 11, 16: 2, 12: 7, 8: 5, 2: 2, 15: 14, 9: 8}

def calculate_tax(coins_subset):
    total_tax = 0
    for coin in coins_subset:
        total_tax += tax_values[coin]
    return total_tax

def find_subset(coins, target_sum, prev_coin=None, prev_coin_odd=True):
    if target_sum == 0:
        return []
    
    for i in range(len(coins)):
        if coins[i] >= prev_coin and prev_coin_odd == coins[i] % 2 == 0:
            continue
        if coins[i] <= prev_coin and prev_coin_odd == coins[i] % 2 != 0:
            continue
        
        new_target = target_sum - coins[i]
        if new_target >= 0:
            subset = find_subset(coins[i+1:], new_target, coins[i], coins[i] % 2 != 0)
            if subset is not None:
                return [coins[i]] + subset
    
    return None

subset = find_subset(coins, 208)
print(subset)
print("Total tax paid:", calculate_tax(subset))
