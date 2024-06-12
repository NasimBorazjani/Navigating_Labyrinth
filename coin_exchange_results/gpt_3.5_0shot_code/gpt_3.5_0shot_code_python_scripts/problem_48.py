
coins = [19, 21, 16, 6, 34, 23, 8, 10, 14, 10, 59, 15, 17, 32, 11, 15, 8, 29, 58, 12, 3, 5, 11, 34, 2, 12, 20, 6, 29, 23, 10, 34, 33, 18]
tax_values = {6: 5, 17: 7, 12: 10, 34: 9, 5: 1, 11: 7, 10: 8, 21: 19, 15: 3, 33: 6, 3: 2, 16: 12, 58: 19, 8: 7, 14: 5, 20: 8, 2: 2, 19: 19, 59: 14, 18: 15, 29: 8, 23: 6, 32: 5}

def calculate_tax(coins_subset):
    total_tax = 0
    for coin in coins_subset:
        total_tax += tax_values[coin]
    return total_tax

def find_min_tax_subset(target_sum, prev_coin=None, prev_coin_odd=True, coins_subset=[], min_tax=float('inf')):
    if sum(coins_subset) == target_sum:
        current_tax = calculate_tax(coins_subset)
        if current_tax < min_tax:
            min_tax = current_tax
            min_subset = coins_subset.copy()
    else:
        for coin in coins:
            if coin not in coins_subset:
                if prev_coin is None or (prev_coin_odd and coin % 2 == 0) or (not prev_coin_odd and coin % 2 != 0 and coin >= prev_coin):
                    new_subset = coins_subset.copy()
                    new_subset.append(coin)
                    min_tax = find_min_tax_subset(target_sum, coin, coin % 2 != 0, new_subset, min_tax)
    return min_tax

target_sum = 355
min_tax = find_min_tax_subset(target_sum)
print(min_subset)
