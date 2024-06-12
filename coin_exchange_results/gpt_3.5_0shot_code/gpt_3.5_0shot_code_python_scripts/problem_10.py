
coins = [6, 20, 15, 14, 23, 6, 8, 15, 11, 2, 16, 21, 17, 10, 23, 20, 21, 16, 13, 3, 7, 4, 9, 21, 7, 13, 10, 18, 11, 9, 13, 12, 15, 17, 2, 8, 18, 3, 16, 9, 3, 14, 23, 16]
tax_values = {21: 11, 18: 16, 16: 6, 12: 5, 14: 11, 11: 8, 15: 11, 4: 3, 9: 2, 23: 14, 7: 5, 20: 12, 6: 2, 8: 3, 17: 6, 13: 3, 3: 3, 2: 1, 10: 5}

target_sum = 236

def calculate_tax(coins_subset):
    total_tax = 0
    for coin in coins_subset:
        total_tax += tax_values[coin]
    return total_tax

def find_min_tax_subset(coins, target_sum):
    min_tax = float('inf')
    min_tax_subset = []
    
    for i in range(1 << len(coins)):
        subset = [coins[j] for j in range(len(coins)) if (i & (1 << j))]
        
        if sum(subset) == target_sum:
            valid_subset = True
            for k in range(1, len(subset)):
                if subset[k] < subset[k-1]:
                    if subset[k] % 2 != 0:
                        valid_subset = False
                        break
                else:
                    if subset[k] % 2 == 0:
                        valid_subset = False
                        break
            
            if valid_subset:
                current_tax = calculate_tax(subset)
                if current_tax < min_tax:
                    min_tax = current_tax
                    min_tax_subset = subset
    
    return min_tax_subset

result = find_min_tax_subset(coins, target_sum)
print(result)
