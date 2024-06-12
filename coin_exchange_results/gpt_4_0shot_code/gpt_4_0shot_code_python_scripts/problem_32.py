
def taxed_coin_exchange(coins, tax, target):
    n = len(coins)
    dp = [[0 if j == 0 else float('inf') for j in range(target+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, target+1):
            if coins[i-1] <= j:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-coins[i-1]] + tax[coins[i-1]])
            else:
                dp[i][j] = dp[i-1][j]
    result = []
    i, j = n, target
    while i > 0 and j > 0:
        if dp[i][j] != dp[i-1][j]:
            result.append(coins[i-1])
            j -= coins[i-1]
        i -= 1
    result.reverse()
    return result

coins = [19, 2, 25, 9, 6, 24, 4, 26, 17, 11, 11, 2, 17, 2, 5, 6, 3, 3, 3, 18, 26, 18, 21, 3, 5, 8, 12, 15, 8, 18, 24, 5, 19, 7, 18, 25, 12, 13, 12, 2, 25, 16, 17, 16, 3, 3]
tax = {26: 12, 25: 20, 17: 13, 13: 4, 16: 13, 11: 10, 24: 5, 5: 4, 8: 6, 7: 5, 4: 4, 12: 9, 18: 12, 3: 2, 21: 17, 19: 7, 2: 2, 9: 9, 6: 2, 15: 4}
target = 264
print(taxed_coin_exchange(coins, tax, target))
