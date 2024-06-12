
def taxed_coin_exchange(coins, tax):
    total_value = 359
    dp = [float('inf')] * (total_value + 1)
    dp[0] = 0
    prev_coin = 0
    for coin in sorted(coins):
        if coin < prev_coin and coin % 2 != 0:
            continue
        if coin >= prev_coin and coin % 2 == 0:
            continue
        for i in range(total_value, coin - 1, -1):
            dp[i] = min(dp[i], dp[i - coin] + tax[coin])
        prev_coin = coin
    return dp[-1] if dp[-1] != float('inf') else -1

coins = [23, 10, 22, 30, 5, 16, 2, 28, 25, 26, 30, 25, 35, 32, 10, 4, 24, 32, 34, 12, 11, 5, 5, 18, 16, 24, 3, 12, 11, 5, 2, 7, 19, 34, 7, 30, 17, 11, 16, 10, 31, 31, 34, 27, 3, 24]
tax = {24: 9, 26: 11, 17: 7, 7: 4, 12: 4, 35: 18, 5: 5, 31: 8, 2: 2, 3: 1, 27: 14, 34: 3, 30: 1, 23: 6, 4: 2, 10: 8, 18: 18, 25: 15, 28: 4, 32: 19, 11: 7, 16: 6, 19: 11, 22: 5}
print(taxed_coin_exchange(coins, tax))
