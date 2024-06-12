
coins = [39, 3, 38, 10, 3, 5, 6, 14, 32, 7, 30, 28, 17, 9, 8, 13, 17, 41, 25, 6, 19, 36, 5, 36, 8, 38, 6, 19, 25, 3, 22, 18, 3, 21, 57, 37, 42, 30, 54, 13, 36, 6, 13, 17, 10, 4, 36]
tax = {37: 2, 38: 4, 30: 18, 39: 18, 14: 1, 18: 1, 4: 1, 10: 8, 21: 10, 6: 5, 42: 13, 32: 10, 25: 2, 17: 15, 13: 2, 9: 4, 22: 17, 7: 5, 3: 2, 54: 7, 19: 15, 8: 2, 36: 17, 28: 6, 5: 5, 41: 9, 57: 12}

coins.sort(reverse=True)
min_tax = [0] + [float('inf')] * 452

for coin in coins:
    for total in range(coin, 453):
        min_tax[total] = min(min_tax[total], min_tax[total - coin] + tax.get(coin, 0))

selected_coins = []
total = 452
for coin in coins:
    if total >= coin and min_tax[total] == min_tax[total - coin] + tax.get(coin, 0):
        selected_coins.append(coin)
        total -= coin

print(selected_coins)
