
def taxed_coin_exchange(coins, tax, total):
    n = len(coins)
    dp = [[0 for _ in range(total + 1)] for _ in range(n + 1)]
    for i in range(total + 1):
        dp[0][i] = float('inf')
    for i in range(1, n + 1):
        for j in range(1, total + 1):
            if coins[i - 1] <= j:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - coins[i - 1]] + tax[coins[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]
    res = []
    i, j = n, total
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            res.append(coins[i - 1])
            j -= coins[i - 1]
        i -= 1
    return res[::-1]

coins = [11, 6, 147, 6, 19, 29, 28, 32, 18, 20, 12, 22, 4, 20, 27, 3, 3, 18, 19, 9, 2, 28, 31, 20, 2, 27, 22, 30, 3]
tax = {27: 18, 6: 2, 22: 12, 18: 11, 4: 3, 12: 4, 28: 6, 147: 10, 32: 6, 19: 3, 29: 12, 31: 19, 20: 4, 2: 2, 30: 17, 3: 2, 11: 10, 9: 2}
total = 324
print(taxed_coin_exchange(coins, tax, total))
