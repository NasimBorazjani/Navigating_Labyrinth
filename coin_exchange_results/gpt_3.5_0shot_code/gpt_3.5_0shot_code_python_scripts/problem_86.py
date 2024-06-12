
def taxed_coin_exchange(coins, target):
    tax_values = {7: 1, 65: 16, 21: 18, 25: 18, 15: 14, 31: 15, 6: 2, 37: 2, 5: 1, 22: 1, 8: 7, 26: 2, 2: 1, 32: 8, 27: 2, 13: 8, 39: 17, 28: 11, 47: 6, 42: 10, 34: 15, 20: 8, 48: 11, 49: 13}
    
    dp = [[0 for _ in range(target+1)] for _ in range(len(coins)+1)]
    
    for i in range(1, len(coins)+1):
        for j in range(1, target+1):
            if coins[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-coins[i-1]] + tax_values[coins[i-1]])
            else:
                dp[i][j] = dp[i-1][j]
    
    selected_coins = []
    i = len(coins)
    j = target
    while i > 0 and j > 0:
        if dp[i][j] != dp[i-1][j]:
            selected_coins.append(coins[i-1])
            j -= coins[i-1]
        i -= 1
    
    return selected_coins[::-1]

coins = [31, 8, 22, 27, 2, 25, 2, 8, 49, 26, 65, 6, 37, 49, 15, 21, 27, 5, 34, 28, 47, 15, 7, 42, 32, 20, 34, 48, 39, 7, 13]
target = 490

result = taxed_coin_exchange(coins, target)
print(result)
