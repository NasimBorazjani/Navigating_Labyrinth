
def taxed_coin_exchange(coins, tax, total_value):
    dp = [float('inf')] * (total_value + 1)
    dp[0] = 0
    prev_coin = 0
    for coin in sorted(coins):
        if coin < prev_coin:
            if coin % 2 == 0:
                for i in range(coin, total_value + 1):
                    dp[i] = min(dp[i], dp[i - coin] + tax[coin])
        else:
            if coin % 2 == 1:
                for i in range(coin, total_value + 1):
                    dp[i] = min(dp[i], dp[i - coin] + tax[coin])
        prev_coin = coin
    return dp[-1]

coins = [9, 30, 18, 32, 31, 20, 34, 9, 12, 18, 14, 16, 29, 37, 37, 6, 24, 10, 10, 35, 23, 4, 30, 121, 31, 16, 35]
tax = {35: 20, 4: 2, 18: 11, 24: 10, 10: 7, 14: 3, 37: 1, 16: 14, 12: 7, 6: 2, 29: 18, 34: 19, 121: 10, 31: 7, 30: 12, 32: 12, 23: 8, 20: 8, 9: 9}
total_value = 406

print(taxed_coin_exchange(coins, tax, total_value))
