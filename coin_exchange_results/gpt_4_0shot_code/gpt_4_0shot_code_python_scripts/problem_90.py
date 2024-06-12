
def taxed_coin_exchange(coins, tax, target):
    coins.sort()
    dp = [[float('inf')] * (target + 1) for _ in range(len(coins) + 1)]
    for i in range(len(coins) + 1):
        dp[i][0] = 0
    for i in range(1, len(coins) + 1):
        for j in range(1, target + 1):
            if j < coins[i - 1] or (i > 1 and coins[i - 1] < coins[i - 2] and coins[i - 1] % 2 != 0) or (i > 1 and coins[i - 1] >= coins[i - 2] and coins[i - 1] % 2 == 0):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - coins[i - 1]] + tax[coins[i - 1]])
    result = []
    i, j = len(coins), target
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            result.append(coins[i - 1])
            j -= coins[i - 1]
        i -= 1
    return result[::-1]

coins = [45, 45, 40, 38, 26, 3, 3, 21, 3, 35, 24, 9, 43, 10, 19, 5, 21, 36, 15, 18, 13, 33, 42, 34, 6, 20, 38, 25, 42, 19, 32, 9, 31, 4, 4, 25, 30, 8]
tax = {13: 7, 9: 1, 38: 9, 19: 4, 31: 18, 25: 18, 40: 13, 4: 2, 15: 8, 45: 2, 10: 10, 20: 18, 5: 3, 35: 12, 30: 8, 8: 5, 21: 5, 43: 12, 32: 10, 6: 2, 24: 18, 3: 2, 33: 7, 42: 4, 36: 10, 34: 6, 26: 5, 18: 6}
print(taxed_coin_exchange(coins, tax, 453))
