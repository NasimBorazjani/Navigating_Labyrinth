
coins = [25, 22, 26, 12, 18, 12, 5, 6, 6, 21, 28, 26, 6, 26, 9, 11, 27, 24, 16, 1, 12, 5, 10, 23, 11, 10, 28, 2, 3, 7, 23, 28, 27, 12, 3, 3, 27, 21, 13, 8, 18, 25, 6, 7, 9, 25, 18, 18, 23, 12, 11, 15, 2, 16]
tax_values = {10: 6, 24: 14, 5: 3, 3: 1, 16: 6, 27: 10, 13: 1, 12: 4, 21: 17, 8: 2, 28: 10, 6: 3, 1: 1, 18: 2, 25: 14, 11: 3, 23: 7, 7: 6, 26: 16, 15: 4, 2: 1, 9: 3, 22: 8}

def calculate_tax(coins_subset):
    total_tax = 0
    for coin in coins_subset:
        total_tax += tax_values[coin]
    return total_tax

def find_min_tax_subset(coins, target_sum, prev_coin=None):
    if target_sum == 0:
        return []
    
    min_tax_subset = None
    min_tax = float('inf')
    
    for coin in coins:
        if coin % 2 == 0 and (prev_coin is None or coin < prev_coin):
            continue
        if coin % 2 != 0 and (prev_coin is None or coin >= prev_coin):
            continue
        
        if coin <= target_sum:
            remaining_coins = coins.copy()
            remaining_coins.remove(coin)
            subset = find_min_tax_subset(remaining_coins, target_sum - coin, coin)
            if subset is not None:
                subset.append(coin)
                tax = calculate_tax(subset)
                if tax < min_tax:
                    min_tax = tax
                    min_tax_subset = subset
    
    return min_tax_subset

target_sum = 289
result = find_min_tax_subset(coins, target_sum)
print(result)
