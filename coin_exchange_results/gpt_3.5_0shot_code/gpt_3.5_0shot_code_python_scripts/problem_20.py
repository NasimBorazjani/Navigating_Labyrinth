
coins = [12, 15, 3, 24, 10, 18, 10, 20, 21, 17, 9, 8, 2, 11, 5, 5, 3, 8, 6, 12, 20, 22, 4, 5, 17, 5, 14, 10, 15, 8, 9, 22, 4, 7, 15, 16, 4, 2, 5, 9, 24, 23, 3, 7, 20, 9, 12, 10, 4, 4, 8, 24, 11, 20, 2, 15]
tax_values = {20: 14, 15: 15, 6: 1, 14: 1, 7: 2, 18: 5, 2: 1, 16: 5, 21: 9, 3: 3, 12: 3, 17: 10, 22: 4, 10: 9, 4: 3, 11: 1, 5: 1, 23: 13, 24: 4, 9: 9, 8: 4}

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

target_sum = 246
selected_coins = find_subset(coins, target_sum)
total_tax_paid = calculate_tax(selected_coins)

print("Selected coins:", selected_coins)
print("Total tax paid:", total_tax_paid)
