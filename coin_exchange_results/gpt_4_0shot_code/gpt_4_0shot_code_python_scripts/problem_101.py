
def taxed_coin_exchange(coins, tax, total):
    n = len(coins)
    dp = [[0 for _ in range(total+1)] for _ in range(n+1)]
    for i in range(total+1):
        dp[0][i] = float('inf')
    for i in range(1, n+1):
        for j in range(1, total+1):
            if j < coins[i-1] or (i > 1 and coins[i-1] < coins[i-2] and coins[i-1] % 2 == 1) or (i > 1 and coins[i-1] >= coins[i-2] and coins[i-1] % 2 == 0):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-coins[i-1]] + tax[coins[i-1]])
    result = []
    i, j = n, total
    while i > 0 and j > 0:
        if dp[i][j] != dp[i-1][j]:
            result.append(coins[i-1])
            j -= coins[i-1]
        i -= 1
    return result[::-1]

coins = [29, 25, 15, 12, 40, 23, 36, 22, 16, 24, 51, 34, 46, 29, 20, 14, 21, 27, 15, 31, 15, 17, 9, 42, 30, 45, 14, 14, 30, 16, 44, 32, 6, 15, 5, 41, 18, 43, 36, 31, 27, 26, 6, 44, 33, 23, 7, 19]
tax = {41: 15, 22: 3, 9: 4, 34: 9, 32: 11, 36: 5, 18: 5, 40: 9, 46: 11, 45: 17, 33: 3, 14: 9, 12: 12, 7: 2, 43: 14, 25: 18, 31: 9, 51: 8, 24: 18, 17: 3, 16: 5, 19: 10, 6: 6, 27: 15, 42: 7, 23: 2, 29: 2, 21: 13, 30: 7, 44: 4, 5: 2, 20: 11, 26: 12, 15: 8}
total = 477
print(taxed_coin_exchange(coins, tax, total))
