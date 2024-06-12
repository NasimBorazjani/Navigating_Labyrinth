
def taxed_coin_exchange(coins, tax, total):
    n = len(coins)
    dp = [[0 if j == 0 else float('inf') for j in range(total + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, total + 1):
            if coins[i - 1] <= j:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - coins[i - 1]] + tax[coins[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]
    result = []
    i, j = n, total
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            result.append(coins[i - 1])
            j -= coins[i - 1]
        i -= 1
    result.reverse()
    return result

coins = [2, 27, 9, 80, 20, 81, 13, 24, 16, 6, 26, 12, 3, 26, 20, 8, 16, 8, 20, 22, 9, 34, 23, 8, 12, 34, 4, 6, 22, 19]
tax = {12: 9, 16: 12, 13: 5, 34: 8, 9: 9, 23: 4, 81: 2, 80: 20, 8: 1, 19: 19, 2: 2, 22: 13, 20: 7, 26: 11, 4: 1, 6: 2, 27: 4, 3: 1, 24: 12}
total = 346
print(taxed_coin_exchange(coins, tax, total))
