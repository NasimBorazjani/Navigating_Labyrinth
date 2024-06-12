
def taxed_coin_exchange(coins, tax):
    coins.sort(reverse=True)
    dp = [float('inf')] * 215
    dp[0] = 0
    prev_coin = 0
    for coin in coins:
        for i in range(coin, 215):
            if i % 2 == 0 or i >= 2 * prev_coin:
                dp[i] = min(dp[i], dp[i - coin] + tax[coin])
        prev_coin = coin

    total_tax = dp[214]
    result = []
    for coin in coins:
        if total_tax >= tax[coin] and dp[214 - coin] + tax[coin] == dp[214]:
            result.append(coin)
            total_tax -= tax[coin]
    return result

coins = [4, 17, 8, 15, 6, 14, 2, 4, 16, 10, 6, 5, 14, 8, 18, 2, 17, 9, 17, 59, 3, 10, 21, 4, 9, 14, 14, 20, 14, 8, 14, 18, 5, 16, 14, 17, 5, 3]
tax = {15: 6, 5: 5, 17: 1, 14: 4, 2: 2, 8: 2, 10: 9, 59: 9, 16: 8, 4: 3, 18: 10, 20: 11, 21: 8, 6: 6, 9: 9, 3: 3}
print(taxed_coin_exchange(coins, tax))
