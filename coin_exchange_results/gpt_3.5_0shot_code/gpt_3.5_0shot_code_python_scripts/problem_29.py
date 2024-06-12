
coins = [5, 21, 4, 18, 17, 13, 27, 10, 27, 21, 25, 22, 27, 29, 28, 15, 16, 12, 7, 19, 8, 19, 9, 21, 29, 15, 15, 23, 8, 13, 20, 9, 13, 16, 3, 14, 11, 15, 2, 23, 18, 4]
tax_values = {14: 2, 12: 11, 20: 5, 4: 2, 23: 12, 28: 1, 25: 8, 27: 3, 19: 1, 21: 6, 16: 2, 29: 7, 13: 5, 17: 2, 22: 15, 10: 1, 15: 1, 3: 2, 8: 5, 5: 4, 9: 1, 7: 2, 2: 2, 18: 17, 11: 1}

def calculate_tax(coins_subset):
    total_tax = 0
    for coin in coins_subset:
        total_tax += tax_values[coin]
    return total_tax

def find_min_tax_subset(target_sum, prev_coin=None, index=0, subset=[]):
    if target_sum == 0:
        return subset
    if target_sum < 0 or index >= len(coins):
        return None
    
    for i in range(index, len(coins)):
        if coins[i] % 2 == 0 and (prev_coin is None or coins[i] < prev_coin):
            new_subset = subset.copy()
            new_subset.append(coins[i])
            result = find_min_tax_subset(target_sum - coins[i], coins[i], i+1, new_subset)
            if result is not None:
                return result
        elif coins[i] % 2 != 0 and (prev_coin is None or coins[i] >= prev_coin):
            new_subset = subset.copy()
            new_subset.append(coins[i])
            result = find_min_tax_subset(target_sum - coins[i], coins[i], i+1, new_subset)
            if result is not None:
                return result
    
    return None

target_sum = 295
min_tax_subset = find_min_tax_subset(target_sum)
print(min_tax_subset)
