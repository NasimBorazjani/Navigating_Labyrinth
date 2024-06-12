
def taxed_coin_exchange(coins, taxes):
    dp = [float('inf')] * 251
    dp[0] = 0
    sorted_coins = sorted(coins, reverse=True)
    tax_map = {coin: tax for coin, tax in taxes.items()}

    for coin in sorted_coins:
        for total in range(coin, 251):
            dp[total] = min(dp[total], dp[total - coin] + tax_map[coin])

    result = []
    total = 250
    for coin in sorted_coins:
        while total >= coin and dp[total] == dp[total - coin] + tax_map[coin]:
            result.append(coin)
            total -= coin

    return result[::-1]

coins = [20, 25, 10, 4, 13, 3, 10, 17, 5, 25, 17, 2, 19, 24, 25, 10, 19, 8, 2, 20, 15, 84, 23, 87, 19, 8, 12, 17, 23, 6]
taxes = {12: 12, 19: 8, 84: 20, 24: 1, 5: 1, 3: 1, 4: 2, 87: 7, 10: 5, 25: 7, 6: 5, 20: 5, 15: 7, 23: 17, 13: 4, 17: 16, 2: 1, 8: 5}

print(taxed_coin_exchange(coins, taxes))
