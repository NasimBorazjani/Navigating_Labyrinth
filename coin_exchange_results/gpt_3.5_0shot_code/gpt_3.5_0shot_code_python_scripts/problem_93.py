
coins = [43, 41, 23, 24, 40, 11, 12, 9, 32, 32, 6, 15, 16, 20, 6, 39, 9, 12, 4, 251, 43, 24, 27, 20, 39, 37, 7, 43, 9, 13, 45, 27, 9, 15, 41, 25]
tax_values = {9: 7, 32: 17, 24: 17, 15: 11, 4: 3, 39: 18, 41: 9, 25: 14, 27: 5, 40: 5, 43: 8, 11: 9, 20: 1, 45: 2, 16: 15, 251: 12, 37: 10, 13: 1, 23: 1, 7: 1, 12: 1, 6: 5}

def is_valid_choice(prev_coin, curr_coin):
    if curr_coin < prev_coin:
        return curr_coin % 2 == 0
    else:
        return curr_coin % 2 != 0

def calculate_tax(coins_chosen):
    total_tax = 0
    for coin in coins_chosen:
        total_tax += tax_values[coin]
    return total_tax

def find_subset(coins, target_sum, prev_coin=None, index=0, subset=[]):
    if target_sum == 0:
        return subset
    if index >= len(coins):
        return None

    curr_coin = coins[index]
    if is_valid_choice(prev_coin, curr_coin):
        subset_with_curr = find_subset(coins, target_sum - curr_coin, curr_coin, index + 1, subset + [curr_coin])
        subset_without_curr = find_subset(coins, target_sum, prev_coin, index + 1, subset)

        if subset_with_curr is None:
            return subset_without_curr
        if subset_without_curr is None:
            return subset_with_curr

        tax_with_curr = calculate_tax(subset_with_curr)
        tax_without_curr = calculate_tax(subset_without_curr)

        if tax_with_curr < tax_without_curr:
            return subset_with_curr
        else:
            return subset_without_curr
    else:
        return find_subset(coins, target_sum, prev_coin, index + 1, subset)

result = find_subset(coins, 471)
print(result)
