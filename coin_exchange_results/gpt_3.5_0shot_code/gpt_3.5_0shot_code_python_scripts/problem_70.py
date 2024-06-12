
coins = [30, 28, 81, 26, 24, 20, 5, 18, 33, 19, 30, 27, 6, 10, 22, 10, 33, 10, 15, 26, 9, 6, 22, 31, 36, 16, 4, 11, 24, 7, 17, 30, 3, 7, 8, 8, 34]
tax_values = {24: 7, 22: 3, 11: 10, 28: 17, 7: 7, 20: 10, 5: 2, 8: 2, 9: 5, 15: 14, 81: 17, 30: 5, 31: 17, 33: 9, 18: 3, 36: 2, 16: 14, 10: 1, 19: 15, 3: 1, 34: 12, 26: 13, 6: 3, 4: 1, 27: 11, 17: 5}

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
            continue
        if coins[i] < prev_coin and coins[i] % 2 != 0:
            continue
        
        if coins[i] <= target_sum:
            subset = find_subset(coins[i+1:], target_sum-coins[i], coins[i])
            if subset is not None:
                return [coins[i]] + subset
    
    return None

target_sum = 387
selected_coins = find_subset(coins, target_sum)
total_tax = calculate_tax(selected_coins)

print(selected_coins)
print("Total tax paid:", total_tax)
