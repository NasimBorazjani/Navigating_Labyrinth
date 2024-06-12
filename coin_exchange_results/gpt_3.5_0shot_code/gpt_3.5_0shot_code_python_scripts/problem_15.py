
coins = [1, 2, 17, 12, 7, 17, 2, 20, 4, 4, 17, 19, 15, 16, 18, 21, 18, 10, 3, 9, 12, 13, 8, 16, 9, 14, 13, 5, 13, 6, 20, 6, 13, 12, 8, 14, 15, 7, 10, 3, 16, 16, 9, 3, 2, 6, 9, 14, 16, 20, 11, 4, 17]
tax_values = {8: 5, 5: 2, 19: 2, 4: 4, 9: 2, 3: 1, 2: 2, 12: 1, 13: 6, 6: 5, 11: 1, 17: 14, 7: 4, 16: 13, 21: 10, 14: 13, 1: 1, 18: 12, 10: 10, 15: 11, 20: 20}

def calculate_tax(coins_subset):
    total_tax = 0
    for coin in coins_subset:
        total_tax += tax_values[coin]
    return total_tax

def find_subset(coins, target_sum, prev_coin=None):
    if target_sum == 0:
        return []
    if not coins or target_sum < 0:
        return None
    
    for i in range(len(coins)):
        if coins[i] % 2 == 0 and (prev_coin is None or coins[i] < prev_coin):
            next_coin = coins[i]
            remaining_sum = target_sum - next_coin
            next_coins = coins[:i] + coins[i+1:]
            subset = find_subset(next_coins, remaining_sum, next_coin)
            if subset is not None:
                return [next_coin] + subset
        elif coins[i] % 2 != 0 and (prev_coin is None or coins[i] >= prev_coin):
            next_coin = coins[i]
            remaining_sum = target_sum - next_coin
            next_coins = coins[:i] + coins[i+1:]
            subset = find_subset(next_coins, remaining_sum, next_coin)
            if subset is not None:
                return [next_coin] + subset
    
    return None

subset = find_subset(coins, 213)
print(subset)
print("Total tax paid:", calculate_tax(subset))
