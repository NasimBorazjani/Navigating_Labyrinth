
coins = [46, 10, 4, 8, 2, 22, 26, 49, 4, 19, 2, 9, 23, 28, 6, 21, 9, 14, 15, 21, 22, 3, 14, 2, 28, 13, 20, 2, 28, 7, 16, 27, 22, 18, 28, 10, 14, 14, 4, 20, 18]
tax_values = {21: 14, 19: 16, 4: 3, 23: 10, 10: 3, 18: 7, 9: 3, 27: 13, 20: 12, 13: 9, 26: 17, 3: 3, 6: 6, 49: 16, 2: 2, 15: 7, 28: 13, 46: 10, 8: 3, 7: 6, 22: 20, 14: 5, 16: 8}

def minimize_tax(coins, target_sum):
    dp = [0] + [float('inf')] * target_sum
    prev = [-1] * (target_sum + 1)
    
    for coin in coins:
        for i in range(coin, target_sum + 1):
            if dp[i - coin] + tax_values[coin] < dp[i]:
                dp[i] = dp[i - coin] + tax_values[coin]
                prev[i] = coin
    
    result = []
    while target_sum > 0:
        result.append(prev[target_sum])
        target_sum -= prev[target_sum]
    
    return result

target_sum = 294
result = minimize_tax(coins, target_sum)
print(result)
