
coins = [9, 2, 23, 20, 13, 4, 15, 16, 12, 21, 13, 9, 2, 14, 13, 14, 4, 19, 12, 6, 21, 23, 4, 18, 2, 23, 23, 6, 18, 23, 3, 16, 7, 2, 22, 16, 8, 10, 23, 17, 3, 18, 8]
tax_values = {9: 1, 17: 6, 2: 2, 22: 9, 13: 13, 16: 8, 12: 4, 4: 1, 21: 14, 14: 10, 19: 9, 10: 7, 7: 6, 8: 7, 6: 2, 23: 16, 18: 3, 20: 2, 3: 1, 15: 2}

def calculate_tax(coins_subset):
    total_tax = 0
    for coin in coins_subset:
        total_tax += tax_values[coin]
    return total_tax

def find_subset(coins, target_sum, prev_coin=None, prev_coin_odd=True):
    if target_sum == 0:
        return []
    
    for i in range(len(coins)):
        if coins[i] >= prev_coin and prev_coin_odd and coins[i] % 2 == 0:
            continue
        if coins[i] < prev_coin and not prev_coin_odd and coins[i] % 2 != 0:
            continue
        
        new_target = target_sum - coins[i]
        if new_target >= 0:
            subset = find_subset(coins[i+1:], new_target, coins[i], coins[i] % 2 != 0)
            if subset is not None:
                return [coins[i]] + subset
    
    return None

subset = find_subset(coins, 230)
print(subset)
print("Total tax paid:", calculate_tax(subset))
