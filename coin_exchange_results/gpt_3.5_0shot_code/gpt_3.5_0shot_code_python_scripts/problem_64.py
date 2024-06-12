
coins = [14, 8, 11, 30, 3, 3, 27, 16, 19, 4, 6, 14, 7, 2, 39, 103, 15, 100, 27, 36, 7, 36, 13, 7, 18, 39, 14, 3, 28]
tax_values = {13: 11, 18: 8, 36: 15, 11: 4, 6: 1, 16: 8, 100: 12, 39: 10, 28: 9, 27: 20, 103: 6, 19: 5, 30: 14, 2: 1, 4: 3, 3: 3, 15: 10, 8: 5, 7: 2, 14: 14}

def calculate_tax(coins_subset):
    total_tax = 0
    for coin in coins_subset:
        total_tax += tax_values[coin]
    return total_tax

def find_subset(coins, target_sum, prev_coin=None, prev_coin_odd=True):
    if target_sum == 0:
        return []
    
    for i in range(len(coins)):
        if coins[i] >= prev_coin and prev_coin_odd == coins[i] % 2 == 0:
            continue
        if coins[i] <= prev_coin and prev_coin_odd == coins[i] % 2 != 0:
            continue
        
        remaining_sum = target_sum - coins[i]
        if remaining_sum >= 0:
            subset = find_subset(coins[i+1:], remaining_sum, coins[i], coins[i] % 2 != 0)
            if subset is not None:
                return [coins[i]] + subset
    
    return None

subset = find_subset(coins, 410)
print(subset)
print("Total tax paid:", calculate_tax(subset))
