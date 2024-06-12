
coins = [20, 25, 10, 4, 13, 3, 10, 17, 5, 25, 17, 2, 19, 24, 25, 10, 19, 8, 2, 20, 15, 84, 23, 87, 19, 8, 12, 17, 23, 6]
tax_values = {12: 12, 19: 8, 84: 20, 24: 1, 5: 1, 3: 1, 4: 2, 87: 7, 10: 5, 25: 7, 6: 5, 20: 5, 15: 7, 23: 17, 13: 4, 17: 16, 2: 1, 8: 5}

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

subset = find_subset(coins, 250)
print(subset)
print("Total tax paid:", calculate_tax(subset))
