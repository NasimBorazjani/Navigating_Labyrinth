
import heapq


def a_star():
    # Define the list of coins and their corresponding tax values
    coins = [30, 24, 27, 14, 29, 17, 4, 21, 20, 14, 19, 23, 18, 4, 12, 9, 24, 26, 21, 17, 3, 13, 25, 20, 16, 12, 2, 9, 17, 5, 6, 24, 13, 11, 6, 15, 13, 5, 13, 25, 10, 15, 10, 3, 2, 18, 7, 23, 5, 18, 21, 6]
    tax_values = {14: 11, 3: 1, 18: 5, 21: 1, 27: 2, 19: 14, 6: 6, 25: 8, 5: 3, 29: 4, 7: 6, 24: 10, 10: 2, 13: 9, 9: 1, 11: 8, 16: 10, 2: 1, 12: 12, 15: 4, 23: 17, 17: 9, 26: 13, 30: 17, 4: 3, 20: 6}
    target_sum = 300

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    queue = [(0, 0, [], 0, 0, 0)]

    while queue:
        _, g, actions, total_tax, prev_coin, coins_sum = heapq.heappop(queue)

        if coins_sum == target_sum:
            return actions

        for coin in coins:
            # Check if the coin is valid based on the rules provided
            if (coin % 2 == 0 and coin > prev_coin) or (coin % 2 != 0 and coin <= prev_coin):
                new_total_tax = total_tax + tax_values[coin]
                new_coins_sum = coins_sum + coin

                if new_coins_sum <= target_sum:
                    new_state = (g + new_total_tax, new_total_tax, actions + [coin], coin, new_coins_sum)

                    if new_state not in visited_costs or g + new_total_tax < visited_costs[new_state]:
                        visited_costs[new_state] = g + new_total_tax
                        heapq.heappush(queue, (g + new_total_tax, new_total_tax, actions + [coin], coin, new_coins_sum))

    return None


print(a_star())
