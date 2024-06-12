
coins = [41, 4, 22, 8, 5, 5, 20, 4, 3, 19, 4, 13, 3, 18, 20, 9, 15, 3, 3, 14, 3, 14, 9, 4, 15, 19, 6, 15, 22, 19, 3, 3, 20, 9, 20, 11, 22, 15, 20]
tax_values = {20: 11, 15: 13, 9: 7, 8: 3, 3: 1, 6: 3, 5: 2, 13: 11, 4: 4, 22: 11, 19: 19, 11: 1, 14: 2, 41: 16, 18: 18}

def calculate_tax(coins_subset):
    total_tax = 0
    for coin in coins_subset:
        total_tax += tax_values[coin]
    return total_tax

def find_subset(coins, target_sum, prev_coin=None):
    if target_sum == 0:
        return []
    
    for i in range(len(coins)):
        if coins[i] >= prev_coin and coins[i] % 2 == 0:
            new_target = target_sum - coins[i]
            if new_target >= 0:
                subset = find_subset(coins[i+1:], new_target, coins[i])
                if subset is not None:
                    return [coins[i]] + subset
        elif coins[i] < prev_coin and coins[i] % 2 != 0:
            new_target = target_sum - coins[i]
            if new_target >= 0:
                subset = find_subset(coins[i+1:], new_target, coins[i])
                if subset is not None:
                    return [coins[i]] + subset
    return None

target_sum = 220
selected_coins = find_subset(coins, target_sum)
total_tax_paid = calculate_tax(selected_coins)

print(selected_coins)
print("Total tax paid:", total_tax_paid)
