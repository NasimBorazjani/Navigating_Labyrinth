
def taxed_coin_exchange(coins, tax, total):
    coins.sort()
    dp = [[0 for _ in range(total + 1)] for _ in range(len(coins) + 1)]
    for i in range(1, total + 1):
        dp[0][i] = float('inf')
    for i in range(1, len(coins) + 1):
        for j in range(1, total + 1):
            if j < coins[i - 1] or (i > 1 and coins[i - 1] < coins[i - 2] and coins[i - 1] % 2 != 0) or (i > 1 and coins[i - 1] >= coins[i - 2] and coins[i - 1] % 2 == 0):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - coins[i - 1]] + tax[coins[i - 1]])
    result = []
    i, j = len(coins), total
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            result.append(coins[i - 1])
            j -= coins[i - 1]
        i -= 1
    return result[::-1]

coins = [35, 14, 9, 23, 25, 24, 21, 20, 12, 17, 12, 5, 2, 17, 25, 25, 26, 31, 7, 21, 10, 2, 27, 19, 32, 29, 11, 33, 3, 27, 17, 3, 18, 14, 2, 32, 14, 21, 12, 8, 3, 34, 13, 12, 2, 23, 13, 3, 3, 31, 23, 23, 6, 30, 30, 11, 21]
tax = {3: 1, 32: 16, 6: 5, 20: 13, 13: 5, 31: 9, 23: 10, 35: 14, 24: 17, 11: 11, 9: 1, 12: 10, 5: 3, 8: 5, 34: 11, 17: 16, 25: 9, 26: 6, 30: 17, 27: 17, 7: 2, 18: 17, 33: 5, 14: 2, 29: 14, 10: 3, 2: 2, 21: 12, 19: 9}
total = 356
print(taxed_coin_exchange(coins, tax, total))
