
coins = [27, 23, 11, 23, 6, 197, 7, 21, 2, 22, 12, 38, 15, 32, 5, 19, 6, 28, 31, 31, 10, 10, 28, 24, 41, 6, 39, 16, 11, 37, 23, 7, 2]
tax_values = {41: 14, 23: 15, 31: 19, 21: 18, 22: 2, 6: 3, 11: 5, 12: 11, 37: 10, 7: 2, 32: 19, 28: 10, 16: 12, 2: 2, 197: 7, 39: 18, 19: 18, 15: 4, 10: 9, 5: 4, 27: 10, 38: 3, 24: 5}

def minimize_tax(coins, target):
    dp = [0] + [float('inf')] * target
    prev = [-1] * (target + 1)
    
    for coin in coins:
        for i in range(coin, target + 1):
            if dp[i - coin] + tax_values[coin] < dp[i]:
                dp[i] = dp[i - coin] + tax_values[coin]
                prev[i] = coin
    
    result = []
    while target > 0:
        coin = prev[target]
        result.append(coin)
        target -= coin
    
    return result

target = 445
result = minimize_tax(coins, target)
print(result)
