
def taxed_coin_exchange(coins, tax, total):
    coins.sort()
    dp = [[float('inf')] * (total + 1) for _ in range(len(coins) + 1)]
    dp[0][0] = 0
    for i in range(1, len(coins) + 1):
        for j in range(total + 1):
            if j < coins[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - coins[i - 1]] + tax[coins[i - 1]])
    result = []
    i, j = len(coins), total
    while j > 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            result.append(coins[i - 1])
            j -= coins[i - 1]
            i -= 1
    return result[::-1]

coins = [18, 23, 23, 36, 27, 10, 25, 14, 6, 43, 6, 31, 5, 43, 3, 13, 16, 8, 11, 6, 39, 44, 41, 28, 12, 8, 1, 14, 22, 23, 11, 24, 37, 9, 2, 31, 27, 10, 9, 38, 37, 4, 4, 17, 18, 36, 18, 32, 3, 12, 4, 42, 8, 4, 4, 16, 30, 40, 13, 41]
tax = {6: 4, 18: 3, 38: 1, 23: 2, 16: 8, 12: 2, 4: 2, 24: 13, 28: 17, 30: 17, 1: 1, 9: 9, 27: 8, 11: 4, 37: 16, 41: 19, 13: 3, 31: 8, 44: 8, 22: 7, 43: 13, 10: 3, 17: 8, 36: 7, 39: 3, 25: 17, 40: 10, 8: 6, 32: 16, 14: 4, 2: 1, 42: 3, 3: 2, 5: 2}
total = 441
print(taxed_coin_exchange(coins, tax, total))
