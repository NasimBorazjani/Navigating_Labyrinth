
coins = [3, 6, 9, 10, 13, 15, 18, 5, 21, 19, 12, 15, 5, 9, 4, 16, 8, 4, 7, 7, 7, 2, 16, 14, 18, 3, 89, 21, 12, 10, 7, 14, 4, 11, 6, 20]
tax_values = {14: 1, 89: 13, 2: 2, 5: 2, 4: 4, 6: 6, 8: 2, 16: 5, 21: 4, 20: 2, 18: 9, 11: 10, 10: 3, 12: 12, 15: 5, 13: 1, 3: 1, 19: 19, 7: 7, 9: 3}

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

subset = find_subset(coins, 229)
print(subset)
print("Total tax paid:", calculate_tax(subset))
