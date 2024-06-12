
coins = [69, 32, 32, 6, 19, 13, 21, 68, 32, 16, 21, 29, 20, 13, 21, 24, 26, 5, 23, 18, 16, 24, 2, 17, 15, 30, 26]
tax_values = {30: 3, 20: 11, 24: 15, 26: 6, 68: 2, 29: 5, 13: 2, 2: 1, 17: 2, 32: 11, 18: 4, 15: 9, 5: 3, 21: 11, 69: 19, 6: 3, 16: 4, 23: 17, 19: 15}

def calculate_tax(coins_subset):
    total_tax = 0
    for coin in coins_subset:
        total_tax += tax_values[coin]
    return total_tax

def find_subset(coins, target_sum, prev_coin=None):
    if target_sum == 0:
        return []
    
    for i in range(len(coins)):
        if coins[i] >= prev_coin and coins[i] % 2 == 1:
            remaining_sum = target_sum - coins[i]
            if remaining_sum >= 0:
                next_subset = find_subset(coins[i+1:], remaining_sum, coins[i])
                if next_subset is not None:
                    return [coins[i]] + next_subset
    
    return None

target_sum = 322
selected_coins = find_subset(coins, target_sum)
selected_coins_tax = calculate_tax(selected_coins)

print(selected_coins)
print(selected_coins_tax)
