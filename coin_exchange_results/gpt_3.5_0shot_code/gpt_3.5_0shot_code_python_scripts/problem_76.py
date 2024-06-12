
coins = [8, 8, 6, 36, 7, 36, 33, 3, 31, 17, 21, 28, 41, 17, 23, 16, 39, 2, 3, 40, 23, 20, 5, 30, 8, 28, 17, 34, 38, 26, 16, 21, 15, 21, 11, 33, 5, 33, 2, 27, 26, 21, 14, 13, 7, 23]
tax_values = {28: 16, 5: 1, 3: 3, 40: 18, 33: 20, 34: 12, 20: 4, 39: 13, 2: 2, 31: 11, 36: 2, 17: 14, 7: 1, 14: 6, 23: 12, 8: 1, 30: 15, 27: 13, 15: 2, 21: 3, 11: 6, 26: 14, 41: 2, 38: 10, 6: 5, 16: 4, 13: 11}

def minimize_tax(coins, target_sum, prev_coin, is_even, tax_values, memo):
    if target_sum == 0:
        return []
    if target_sum < 0 or len(coins) == 0:
        return None
    if (len(coins), target_sum, prev_coin, is_even) in memo:
        return memo[(len(coins), target_sum, prev_coin, is_even)]
    
    coin = coins[0]
    rest = coins[1:]
    
    if (coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0):
        with_coin = minimize_tax(rest, target_sum - coin, coin, coin % 2 == 0, tax_values, memo)
        if with_coin is not None:
            with_coin.append(coin)
            with_tax = sum([tax_values[c] for c in with_coin])
            without_coin = minimize_tax(rest, target_sum, prev_coin, is_even, tax_values, memo)
            without_tax = sum([tax_values[c] for c in without_coin]) if without_coin is not None else float('inf')
            
            if with_tax < without_tax:
                memo[(len(coins), target_sum, prev_coin, is_even)] = with_coin
                return with_coin
    
    memo[(len(coins), target_sum, prev_coin, is_even)] = minimize_tax(rest, target_sum, prev_coin, is_even, tax_values, memo)
    return memo[(len(coins), target_sum, prev_coin, is_even)]

target_sum = 403
prev_coin = float('inf')
is_even = True
memo = {}
result = minimize_tax(coins, target_sum, prev_coin, is_even, tax_values, memo)
print(result)
