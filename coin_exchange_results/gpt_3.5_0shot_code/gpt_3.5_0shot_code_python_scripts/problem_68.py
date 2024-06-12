
coins = [5, 29, 12, 96, 4, 13, 8, 23, 14, 25, 18, 23, 36, 32, 17, 37, 34, 7, 9, 32, 29, 37, 30, 40, 99, 9, 2, 40, 35, 14]
tax_values = {14: 4, 4: 2, 18: 12, 23: 12, 36: 15, 5: 1, 12: 3, 13: 13, 9: 7, 32: 8, 99: 16, 8: 7, 96: 17, 35: 13, 29: 19, 30: 19, 7: 1, 34: 16, 37: 15, 2: 2, 17: 3, 40: 18, 25: 9}

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
            continue
        if coins[i] < prev_coin and coins[i] % 2 != 0:
            continue
        
        if coins[i] <= target_sum:
            subset = find_subset(coins[i+1:], target_sum-coins[i], coins[i])
            if subset is not None:
                return [coins[i]] + subset
    
    return None

subset = find_subset(coins, 427)
print(subset)
print("Total tax paid:", calculate_tax(subset))
