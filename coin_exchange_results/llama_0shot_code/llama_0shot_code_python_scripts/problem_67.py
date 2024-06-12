
def taxed_coin_exchange(coins, taxes, target_sum):
    dp = [float('inf')] * (target_sum + 1)
    dp[0] = 0
    prev_coin = 0
    for coin in sorted(coins):
        for i in range(target_sum, coin - 1, -1):
            if coin < prev_coin:
                if dp[i - coin] + taxes[coin] < dp[i]:
                    dp[i] = dp[i - coin] + taxes[coin]
            elif coin >= prev_coin:
                if dp[i - coin] + taxes[coin] < dp[i]:
                    dp[i] = dp[i - coin] + taxes[coin]
        prev_coin = coin
    return dp[target_sum]

coins = [8, 13, 16, 4, 35, 2, 19, 2, 21, 26, 28, 12, 58, 28, 12, 35, 33, 4, 19, 27, 61, 30, 17, 20, 27, 25, 30, 31, 9, 15, 4, 13, 11, 29]
taxes = {13: 1, 4: 1, 61: 2, 30: 19, 12: 4, 20: 16, 29: 10, 2: 2, 35: 17, 31: 17, 19: 15, 25: 11, 21: 8, 27: 16, 17: 17, 11: 7, 58: 12, 26: 4, 15: 14, 28: 10, 8: 5, 16: 5, 9: 8, 33: 13}
target_sum = 384

result = taxed_coin_exchange(coins, taxes, target_sum)
print(result)
