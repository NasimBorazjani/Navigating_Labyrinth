
coins = [8, 13, 16, 4, 35, 2, 19, 2, 21, 26, 28, 12, 58, 28, 12, 35, 33, 4, 19, 27, 61, 30, 17, 20, 27, 25, 30, 31, 9, 15, 4, 13, 11, 29]
tax_values = {13: 1, 4: 1, 61: 2, 30: 19, 12: 4, 20: 16, 29: 10, 2: 2, 35: 17, 31: 17, 19: 15, 25: 11, 21: 8, 27: 16, 17: 17, 11: 7, 58: 12, 26: 4, 15: 14, 28: 10, 8: 5, 16: 5, 9: 8, 33: 13}

def calculate_tax(coins_subset):
    total_tax = 0
    for coin in coins_subset:
        total_tax += tax_values[coin]
    return total_tax

def find_subset(coins, target_sum, prev_coin=None, prev_coin_odd=True):
    if target_sum == 0:
        return []
    
    for i in range(len(coins)):
        if coins[i] >= prev_coin and prev_coin_odd == coins[i] % 2:
            subset = find_subset(coins[i+1:], target_sum - coins[i], coins[i], not prev_coin_odd)
            if subset is not None:
                return [coins[i]] + subset
    
    return None

target_sum = 384
selected_coins = find_subset(coins, target_sum)
total_tax = calculate_tax(selected_coins)

print("Selected coins:", selected_coins)
print("Total tax paid:", total_tax)
