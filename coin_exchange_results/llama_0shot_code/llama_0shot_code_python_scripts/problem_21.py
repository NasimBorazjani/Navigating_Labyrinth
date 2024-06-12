
def taxed_coin_exchange(coins, taxes):
    sorted_coins = sorted(coins, reverse=True)
    dp = [float('inf')] * 211
    dp[0] = 0
    for coin in sorted_coins:
        for total_value in range(coin, 211):
            dp[total_value] = min(dp[total_value], taxes[coin] + dp[total_value - coin])
    subset = []
    total_value = 210
    for coin in sorted_coins:
        if total_value >= coin and dp[total_value] == dp[total_value - coin] + taxes[coin]:
            subset.append(coin)
            total_value -= coin
    return subset[::-1]

coins = [17, 19, 5, 17, 13, 2, 12, 4, 4, 15, 19, 7, 18, 15, 4, 6, 9, 2, 4, 11, 21, 17, 20, 4, 8, 2, 19, 16, 2, 12, 8, 16, 18, 3, 18, 13, 3, 15, 7, 18, 4, 14, 3, 5, 8, 7, 19, 9, 17, 5, 17, 6, 3, 5, 15]
taxes = {9: 9, 6: 1, 13: 4, 2: 1, 16: 3, 14: 4, 19: 16, 20: 2, 15: 3, 7: 3, 18: 14, 17: 15, 4: 2, 5: 5, 8: 8, 21: 10, 12: 11, 11: 7, 3: 2}
print(taxed_coin_exchange(coins, taxes))
