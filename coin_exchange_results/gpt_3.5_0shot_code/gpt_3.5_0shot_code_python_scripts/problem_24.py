
coins = [25, 29, 8, 11, 8, 25, 20, 16, 6, 4, 98, 7, 28, 24, 27, 16, 23, 26, 26, 99, 2, 7, 22, 7, 5, 24, 2]
tax_values = {24: 5, 26: 16, 28: 20, 2: 1, 22: 16, 25: 11, 27: 7, 11: 4, 6: 3, 99: 17, 8: 5, 7: 5, 5: 3, 23: 5, 4: 4, 98: 16, 16: 3, 29: 5, 20: 19}

def is_valid(prev_coin, curr_coin):
    if curr_coin < prev_coin:
        return curr_coin % 2 == 0
    else:
        return curr_coin % 2 != 0

def taxed_coin_exchange(coins, target):
    dp = [0] + [float('inf')] * target
    prev_coin = None
    for coin in coins:
        for i in range(coin, target + 1):
            if dp[i - coin] + tax_values[coin] < dp[i] and (prev_coin is None or is_valid(prev_coin, coin)):
                dp[i] = dp[i - coin] + tax_values[coin]
        prev_coin = coin

    selected_coins = []
    remaining = target
    for coin in reversed(coins):
        while remaining >= coin and dp[remaining] == dp[remaining - coin] + tax_values[coin]:
            selected_coins.append(coin)
            remaining -= coin

    return selected_coins

target = 305
selected_coins = taxed_coin_exchange(coins, target)
print(selected_coins)
