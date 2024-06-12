
coins = [15, 2, 37, 38, 21, 30, 19, 28, 3, 35, 16, 32, 3, 28, 24, 27, 10, 1, 14, 3, 33, 6, 18, 37, 20, 19, 4, 31, 34, 39, 7, 13, 29, 38, 34, 14, 29, 13, 5, 33, 31, 24]
tax = {33: 10, 13: 12, 6: 1, 15: 2, 20: 15, 4: 3, 27: 7, 35: 5, 19: 18, 14: 13, 16: 4, 2: 2, 39: 19, 21: 18, 3: 2, 37: 14, 10: 1, 24: 3, 32: 2, 7: 4, 1: 1, 5: 4, 31: 4, 34: 7, 30: 8, 28: 11, 18: 9, 29: 2, 38: 1}

# Initialize dp list
dp = [float('inf')] * 400
dp[0] = 0

# Initialize coin list
coin_list = [0] * 400

# Fill dp list
for coin in coins:
    for i in range(coin, 397+1):
        if dp[i-coin] != float('inf'):
            new_tax = dp[i-coin] + tax[coin]
            if new_tax < dp[i]:
                dp[i] = new_tax
                coin_list[i] = coin

# Find the sum that gives minimum tax
min_tax_sum = min(range(397+1), key=dp.__getitem__)

# Backtrack to find the coins
coins_chosen = []
while min_tax_sum > 0:
    coins_chosen.append(coin_list[min_tax_sum])
    min_tax_sum -= coin_list[min_tax_sum]

# Reverse list to get correct order
coins_chosen = coins_chosen[::-1]

print(coins_chosen)
