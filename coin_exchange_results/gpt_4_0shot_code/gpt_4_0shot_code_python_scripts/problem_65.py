
def taxed_coin_exchange(coins, tax, total):
    coins.sort()
    dp = [[0 for _ in range(total + 1)] for _ in range(len(coins) + 1)]
    for i in range(1, total + 1):
        dp[0][i] = float('inf')
    for i in range(1, len(coins) + 1):
        for j in range(1, total + 1):
            if j < coins[i - 1] or (i > 1 and j >= coins[i - 1] and coins[i - 1] % 2 == 0 and coins[i - 1] < coins[i - 2]):
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

coins = [9, 30, 18, 32, 31, 20, 34, 9, 12, 18, 14, 16, 29, 37, 37, 6, 24, 10, 10, 35, 23, 4, 30, 121, 31, 16, 35]
tax = {35: 20, 4: 2, 18: 11, 24: 10, 10: 7, 14: 3, 37: 1, 16: 14, 12: 7, 6: 2, 29: 18, 34: 19, 121: 10, 31: 7, 30: 12, 32: 12, 23: 8, 20: 8, 9: 9}
total = 406
print(taxed_coin_exchange(coins, tax, total))
