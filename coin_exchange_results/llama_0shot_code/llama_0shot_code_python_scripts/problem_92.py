
def taxed_coin_exchange(coins, taxes, total):
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(total, coin - 1, -1):
            dp[i] = min(dp[i], dp[i - coin] + taxes[coin])
    return dp[total] if dp[total] != float('inf') else -1

coins = [19, 11, 35, 3, 12, 23, 42, 45, 8, 12, 32, 82, 39, 12, 45, 12, 40, 38, 28, 6, 32, 37, 39, 9, 43, 12, 38, 4, 42, 44, 41, 37, 83, 5, 38]
taxes = {37: 6, 43: 18, 32: 16, 4: 4, 83: 4, 8: 5, 23: 18, 12: 6, 82: 16, 44: 20, 39: 1, 19: 8, 35: 7, 38: 11, 11: 3, 42: 5, 45: 12, 3: 1, 6: 2, 41: 3, 28: 18, 40: 2, 9: 6, 5: 4}
total = 466

coins.sort()
result = taxed_coin_exchange(coins, taxes, total)

if result != -1:
    print(f"The minimum tax paid is {result}.")
else:
    print("No solution found.")
