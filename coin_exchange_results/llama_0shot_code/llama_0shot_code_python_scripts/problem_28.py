
def taxed_coin_exchange(coins, taxes):
    n = len(coins)
    dp = [float('inf')] * 268
    dp[0] = 0
    prev = [None] * 268
    for i in range(n):
        coin = coins[i]
        tax = taxes[coin]
        for j in range(coin, 268):
            if (prev[j-coin] is None or (coin % 2 == 0 and prev[j-coin] < coin) or (coin % 2 == 1 and prev[j-coin] >= coin)) and dp[j-coin] + tax < dp[j]:
                dp[j] = dp[j-coin] + tax
                prev[j] = coin
    if dp[-1] == float('inf'):
        return None
    result = []
    total = 267
    while total >= 0:
        result.append(prev[total])
        total -= prev[total]
    return result[::-1]

coins = [26, 19, 7, 24, 27, 15, 9, 9, 9, 26, 15, 23, 6, 6, 24, 8, 21, 6, 6, 7, 25, 22, 8, 2, 7, 5, 8, 18, 14, 15, 24, 10, 4, 23, 21, 8, 18, 12, 16]
taxes = {24: 14, 27: 10, 22: 14, 16: 7, 14: 12, 6: 3, 8: 7, 23: 6, 18: 18, 5: 3, 25: 8, 7: 6, 12: 3, 15: 8, 9: 2, 19: 15, 2: 1, 4: 1, 26: 15, 10: 8, 21: 19}
print(taxed_coin_exchange(coins, taxes))
