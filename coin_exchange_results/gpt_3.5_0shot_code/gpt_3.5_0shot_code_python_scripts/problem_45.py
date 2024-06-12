
coins = [21, 10, 19, 6, 20, 7, 23, 18, 4, 15, 4, 13, 2, 5, 32, 28, 113, 3, 9, 9, 11, 21, 112, 6, 6, 11, 29]
tax_values = {10: 7, 5: 3, 11: 3, 23: 2, 21: 13, 19: 3, 18: 18, 29: 20, 3: 2, 9: 7, 20: 18, 6: 2, 112: 20, 2: 1, 4: 4, 7: 4, 32: 1, 15: 8, 13: 10, 28: 17, 113: 18}

def calculate_tax(coins_subset):
    total_tax = 0
    for coin in coins_subset:
        total_tax += tax_values[coin]
    return total_tax

def find_subset(coins, target_sum, prev_coin=None):
    if target_sum == 0:
        return []
    
    for i in range(len(coins)):
        if coins[i] % 2 == 0 and (prev_coin is None or coins[i] < prev_coin):
            continue
        if coins[i] % 2 != 0 and (prev_coin is not None and coins[i] < prev_coin):
            continue
        
        remaining_sum = target_sum - coins[i]
        if remaining_sum < 0:
            continue
        
        next_subset = find_subset(coins[i+1:], remaining_sum, coins[i])
        if next_subset is not None:
            return [coins[i]] + next_subset
    
    return None

subset = find_subset(coins, 337)
print(subset)
print("Total tax paid:", calculate_tax(subset))
