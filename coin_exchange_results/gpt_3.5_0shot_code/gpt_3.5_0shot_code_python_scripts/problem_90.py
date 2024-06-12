
coins = [45, 45, 40, 38, 26, 3, 3, 21, 3, 35, 24, 9, 43, 10, 19, 5, 21, 36, 15, 18, 13, 33, 42, 34, 6, 20, 38, 25, 42, 19, 32, 9, 31, 4, 4, 25, 30, 8]
tax_values = {13: 7, 9: 1, 38: 9, 19: 4, 31: 18, 25: 18, 40: 13, 4: 2, 15: 8, 45: 2, 10: 10, 20: 18, 5: 3, 35: 12, 30: 8, 8: 5, 21: 5, 43: 12, 32: 10, 6: 2, 24: 18, 3: 2, 33: 7, 42: 4, 36: 10, 34: 6, 26: 5, 18: 6}

def calculate_tax(coins_subset):
    total_tax = 0
    for coin in coins_subset:
        total_tax += tax_values[coin]
    return total_tax

def find_min_tax_subset(target_sum, prev_coin=None, index=0, subset=[]):
    if target_sum == 0:
        return subset
    if target_sum < 0 or index == len(coins):
        return None
    
    if prev_coin is None or (coins[index] > prev_coin and coins[index] % 2 != 0) or (coins[index] < prev_coin and coins[index] % 2 == 0):
        include_subset = find_min_tax_subset(target_sum - coins[index], coins[index], index + 1, subset + [coins[index]])
        exclude_subset = find_min_tax_subset(target_sum, prev_coin, index + 1, subset)
        
        if include_subset is None:
            return exclude_subset
        if exclude_subset is None:
            return include_subset
        
        if calculate_tax(include_subset) < calculate_tax(exclude_subset):
            return include_subset
        else:
            return exclude_subset
    else:
        return find_min_tax_subset(target_sum, prev_coin, index + 1, subset)

target_sum = 453
result = find_min_tax_subset(target_sum)
print(result)
