
def taxed_coin_exchange(coins, taxes, total_value):
    dp = [float('inf')] * (total_value + 1)
    dp[0] = 0
    sorted_coins = sorted(coins, reverse=True)
    sorted_taxes = sorted(taxes.items(), key=lambda x: -x[1])

    for coin, coin_tax in sorted_taxes:
        for i in range(total_value, coin - 1, -1):
            dp[i] = min(dp[i], dp[i - coin] + coin_tax)

    chosen_coins = []
    for coin in sorted_coins:
        if dp[total_value] == float('inf'):
            break
        if total_value >= coin:
            chosen_coins.append(coin)
            total_value -= coin
    return chosen_coins[::-1]

coins = [27, 23, 11, 23, 6, 197, 7, 21, 2, 22, 12, 38, 15, 32, 5, 19, 6, 28, 31, 31, 10, 10, 28, 24, 41, 6, 39, 16, 11, 37, 23, 7, 2]
taxes = {41: 14, 23: 15, 31: 19, 21: 18, 22: 2, 6: 3, 11: 5, 12: 11, 37: 10, 7: 2, 32: 19, 28: 10, 16: 12, 2: 2, 197: 7, 39: 18, 19: 18, 15: 4, 10: 9, 5: 4, 27: 10, 38: 3, 24: 5}
total_value = 445

result = taxed_coin_exchange(coins, taxes, total_value)
print(result)
