
def taxed_coin_exchange(coins, tax, target):
    coins.sort()
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    prev = [0] * (target + 1)
    for coin in coins:
        for i in range(coin, target + 1):
            if dp[i - coin] + tax[coin] < dp[i]:
                dp[i] = dp[i - coin] + tax[coin]
                prev[i] = coin
    if dp[target] == float('inf'):
        return []
    result = []
    while target > 0:
        result.append(prev[target])
        target -= prev[target]
    return result

coins = [13, 30, 19, 13, 34, 12, 16, 21, 24, 39, 37, 32, 3, 5, 30, 37, 29, 20, 15, 23, 30, 24, 12, 21, 19, 10, 26, 29, 3, 23, 20, 40, 22, 13, 2, 36, 8, 40, 6, 24, 24, 11, 26, 37, 16, 57, 39, 21, 17]
tax = {2: 2, 21: 6, 24: 9, 26: 2, 5: 3, 29: 10, 10: 7, 13: 13, 30: 17, 36: 15, 3: 1, 32: 7, 8: 5, 20: 2, 22: 3, 57: 19, 40: 8, 6: 4, 23: 8, 39: 3, 16: 5, 37: 6, 12: 9, 11: 11, 34: 6, 17: 2, 15: 10, 19: 17}
target = 412
print(taxed_coin_exchange(coins, tax, target))
