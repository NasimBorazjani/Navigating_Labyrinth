
def taxed_coin_exchange(coins, taxes):
    dp = [float('inf')] * (472)
    dp[0] = 0
    chosen_coins = [0] * 472
    for coin in coins:
        for i in range(coin, 471, 2 if coin % 2 == 0 else 1):
            if dp[i - coin] + taxes[coin] < dp[i]:
                dp[i] = dp[i - coin] + taxes[coin]
                chosen_coins[i] = coin
    result = []
    i = 471
    while i > 0:
        if chosen_coins[i]:
            result.append(chosen_coins[i])
            i -= chosen_coins[i]
        else:
            i -= 1
    return result[::-1]

coins = [43, 41, 23, 24, 40, 11, 12, 9, 32, 32, 6, 15, 16, 20, 6, 39, 9, 12, 4, 251, 43, 24, 27, 20, 39, 37, 7, 43, 9, 13, 45, 27, 9, 15, 41, 25]
taxes = {9: 7, 32: 17, 24: 17, 15: 11, 4: 3, 39: 18, 41: 9, 25: 14, 27: 5, 40: 5, 43: 8, 11: 9, 20: 1, 45: 2, 16: 15, 251: 12, 37: 10, 13: 1, 23: 1, 7: 1, 12: 1, 6: 5}

print(taxed_coin_exchange(coins, taxes))
