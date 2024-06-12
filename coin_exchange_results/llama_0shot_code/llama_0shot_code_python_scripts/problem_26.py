
def taxed_coin_exchange(coins, tax):
    n = 307
    dp = [float('inf')] * (n + 1)
    prev = [None] * (n + 1)
    dp[0] = 0
    for coin in sorted(coins, reverse=True):
        for i in range(coin, n + 1):
            if dp[i - coin] + tax[coin] < dp[i]:
                dp[i] = dp[i - coin] + tax[coin]
                prev[i] = coin
    min_tax = dp[-1]
    subset = []
    i = n
    while i > 0:
        subset.append(prev[i])
        i -= prev[i]
    return subset[::-1]

coins = [29, 29, 22, 23, 23, 3, 26, 9, 15, 8, 21, 15, 29, 25, 71, 27, 23, 6, 7, 9, 15, 21, 6, 8, 19, 17, 18, 6, 26, 24, 24, 3, 25, 2]
tax = {24: 14, 2: 1, 25: 2, 26: 14, 18: 12, 27: 15, 29: 19, 19: 3, 15: 7, 9: 1, 8: 1, 21: 18, 6: 1, 71: 3, 23: 4, 17: 7, 7: 2, 22: 11, 3: 1, 2: 1}
print(taxed_coin_exchange(coins, tax))
