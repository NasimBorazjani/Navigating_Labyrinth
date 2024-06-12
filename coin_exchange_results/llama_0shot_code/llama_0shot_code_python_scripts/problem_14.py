
coins = [9, 18, 7, 20, 4, 12, 5, 5, 18, 5, 2, 11, 5, 16, 19, 8, 10, 9, 12, 14, 17, 6, 14, 16, 20, 10, 10, 13, 4, 13, 7, 14, 14, 10, 2, 7, 14, 11, 16, 10, 10, 5, 14, 20, 4, 17]
taxes = {17: 16, 8: 8, 6: 6, 16: 12, 5: 4, 14: 12, 18: 9, 12: 1, 19: 12, 4: 2, 7: 3, 10: 7, 11: 7, 13: 6, 2: 1, 9: 1, 20: 10}

coins.sort(reverse=True)

total_taxes = [float('inf')] * 207
total_taxes[0] = 0

for coin in coins:
    for total in range(coin, 207):
        total_taxes[total] = min(total_taxes[total], total_taxes[total - coin] + taxes[coin])

total_value = 206
selected_coins = []
while total_value > 0:
    for coin in coins:
        if total_taxes[total_value] == total_taxes[total_value - coin] + taxes[coin]:
            selected_coins.append(coin)
            total_value -= coin
            break

selected_coins.reverse()

print(selected_coins)
