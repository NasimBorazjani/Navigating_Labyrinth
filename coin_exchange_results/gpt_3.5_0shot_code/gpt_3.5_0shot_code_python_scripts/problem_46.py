
coins = [11, 6, 147, 6, 19, 29, 28, 32, 18, 20, 12, 22, 4, 20, 27, 3, 3, 18, 19, 9, 2, 28, 31, 20, 2, 27, 22, 30, 3]
tax_values = {27: 18, 6: 2, 22: 12, 18: 11, 4: 3, 12: 4, 28: 6, 147: 10, 32: 6, 19: 3, 29: 12, 31: 19, 20: 4, 2: 2, 30: 17, 3: 2, 11: 10, 9: 2}

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

subset = find_subset(coins, 324)
print(subset)
print("Total tax paid:", calculate_tax(subset))
