
def taxed_coin_exchange(coins, taxes):
    n = len(coins)
    dp = [float('inf')] * (428)
    dp[0] = 0
    for i in range(n):
        coin = coins[i]
        tax = taxes[coin]
        for j in range(coin, 428):
            dp[j] = min(dp[j], dp[j - coin] + tax)
    chosen_coins = []
    total_tax = dp[427]
    for i in range(427, -1, -1):
        if dp[i] == total_tax:
            chosen_coins.append(i)
            total_tax -= taxes[i]
    return chosen_coins[::-1]

coins = [5, 29, 12, 96, 4, 13, 8, 23, 14, 25, 18, 23, 36, 32, 17, 37, 34, 7, 9, 32, 29, 37, 30, 40, 99, 9, 2, 40, 35, 14]
taxes = {14: 4, 4: 2, 18: 12, 23: 12, 36: 15, 5: 1, 12: 3, 13: 13, 9: 7, 32: 8, 99: 16, 8: 7, 96: 17, 35: 13, 29: 19, 30: 19, 7: 1, 34: 16, 37: 15, 2: 2, 17: 3, 40: 18, 25: 9}

print(taxed_coin_exchange(coins, taxes))
