
def taxed_coin_exchange(coins, target):
    tax_values = {44: 20, 11: 4, 19: 3, 4: 4, 10: 3, 14: 9, 90: 18, 48: 12, 91: 5, 8: 4, 7: 5, 9: 5, 12: 2, 42: 18, 36: 6, 35: 10, 34: 12, 25: 7, 27: 1, 3: 2, 26: 15, 40: 8, 43: 1, 18: 8, 23: 1, 13: 3, 41: 8, 38: 13, 2: 2}
    
    dp = [[0 for _ in range(target+1)] for _ in range(len(coins)+1)]
    
    for i in range(1, len(coins)+1):
        for j in range(1, target+1):
            if coins[i-1] <= j:
                if coins[i-1] % 2 == 0:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-coins[i-1]] + tax_values[coins[i-1]])
                else:
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

coins = [26, 8, 19, 9, 36, 23, 42, 40, 13, 34, 40, 25, 11, 38, 10, 41, 19, 34, 91, 18, 14, 27, 14, 43, 42, 13, 2, 27, 90, 13, 3, 4, 44, 7, 48, 40, 35, 40, 10, 12, 25]
target = 488

result = taxed_coin_exchange(coins, target)
print(result)
