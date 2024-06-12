
def taxed_coin_exchange(coins, tax, total):
    n = len(coins)
    dp = [[0 for _ in range(total + 1)] for _ in range(n + 1)]
    for i in range(1, total + 1):
        dp[0][i] = float('inf')
    for i in range(1, n + 1):
        for j in range(1, total + 1):
            if j < coins[i - 1] or (i > 1 and coins[i - 1] < coins[i - 2] and coins[i - 1] % 2 != 0) or (i > 1 and coins[i - 1] >= coins[i - 2] and coins[i - 1] % 2 == 0):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - coins[i - 1]] + tax[coins[i - 1]])
    result = []
    i, j = n, total
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            result.append(coins[i - 1])
            j -= coins[i - 1]
        i -= 1
    result.reverse()
    return result

coins = [14, 2, 5, 8, 65, 5, 16, 2, 5, 2, 12, 17, 16, 15, 20, 4, 19, 9, 10, 64, 2, 10, 14, 2, 17]
tax = {20: 13, 4: 2, 17: 16, 19: 8, 64: 4, 5: 3, 14: 10, 10: 9, 65: 11, 16: 2, 12: 7, 8: 5, 2: 2, 15: 14, 9: 8}
total = 208
print(taxed_coin_exchange(coins, tax, total))
