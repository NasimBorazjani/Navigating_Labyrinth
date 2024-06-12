
coins = [22, 4, 12, 26, 4, 9, 4, 28, 28, 8, 28, 19, 15, 20, 9, 161, 11, 28, 17, 10, 25, 15, 7, 28, 21, 24, 10, 13, 22, 4, 10, 14]
tax_values = {15: 2, 17: 10, 10: 3, 12: 10, 21: 12, 4: 2, 22: 1, 11: 6, 26: 9, 14: 7, 24: 12, 161: 16, 20: 15, 9: 8, 8: 1, 13: 10, 28: 6, 7: 6, 25: 6, 19: 15}

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
        
        if coins[i] <= target_sum:
            subset = find_subset(coins[i+1:], target_sum-coins[i], coins[i], coins[i] % 2 != 0)
            if subset is not None:
                return [coins[i]] + subset
    
    return None

subset = find_subset(coins, 301)
print(subset)
print("Total tax paid:", calculate_tax(subset))
