
coins = [84, 2, 8, 16, 21, 10, 15, 4, 17, 16, 4, 85, 30, 13, 28, 2, 2, 11, 18, 9, 25, 5, 24, 14, 20, 30, 6]
target_sum = 309

tax_values = {15: 2, 18: 9, 28: 4, 84: 10, 2: 1, 24: 19, 30: 12, 5: 2, 9: 9, 21: 9, 11: 10, 16: 14, 4: 2, 17: 2, 85: 18, 6: 5, 8: 6, 13: 2, 10: 4, 25: 11, 20: 19, 14: 2}

def is_valid_subset(subset):
    for i in range(1, len(subset)):
        if (subset[i] < subset[i-1] and subset[i] % 2 != 0) or (subset[i] >= subset[i-1] and subset[i] % 2 == 0):
            return False
    return True

def calculate_tax(subset):
    total_tax = 0
    for coin in subset:
        total_tax += tax_values[coin]
    return total_tax

def find_min_tax_subset(coins, target_sum):
    min_tax = float('inf')
    min_tax_subset = []

    for i in range(1, 2**len(coins)):
        subset = [coins[j] for j in range(len(coins)) if (i & (1 << j))]
        if sum(subset) == target_sum and is_valid_subset(subset):
            tax = calculate_tax(subset)
            if tax < min_tax:
                min_tax = tax
                min_tax_subset = subset

    return min_tax_subset

result = find_min_tax_subset(coins, target_sum)
print(result)
