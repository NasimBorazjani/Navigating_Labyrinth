
import heapq
import math


def a_star():
    # Define the list of coins and their tax values
    coins = [23, 27, 20, 21, 8, 2, 2, 3, 21, 26, 16, 33, 22, 3, 25, 17, 5, 31, 3, 9, 12, 30, 11, 10, 7, 13, 2, 21, 8, 16, 5, 18, 32, 27, 7, 32, 7, 10, 11, 33, 18, 30, 7, 24, 21, 4, 25, 4, 23, 21, 23, 15, 26, 10]
    tax_values = {16: 1, 18: 1, 9: 1, 11: 5, 5: 3, 2: 1, 21: 1, 33: 3, 7: 1, 4: 1, 30: 8, 23: 10, 17: 8, 15: 7, 13: 6, 20: 8, 32: 4, 10: 6, 3: 1, 12: 7, 27: 6, 31: 5, 22: 1, 26: 20, 24: 5, 8: 4, 25: 9}
    target_sum = 334

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    queue = [(0, 0, [], 0, 0, 0)]

    while queue:
        _, g, actions, total_tax, prev_coin, coins_index = heapq.heappop(queue)

        if total_tax == target_sum:
            return actions

        for i in range(coins_index, len(coins)):
            coin = coins[i]
            tax = tax_values[coin]
            new_total_tax = total_tax + tax

            # Check if the coin chosen is smaller than the previous one
            if coin < prev_coin:
                if coin % 2 == 0:
                    new_actions = actions + [coin]
                    new_state = (g + new_total_tax, new_total_tax, new_actions, coin, i + 1)
                    if new_state not in visited_costs or g + new_total_tax < visited_costs[new_state]:
                        visited_costs[new_state] = g + new_total_tax
                        heapq.heappush(queue, (g + new_total_tax, new_total_tax, new_actions, coin, i + 1))
            # Check if the coin chosen is larger than or equal to the previous one
            else:
                if coin % 2 != 0:
                    new_actions = actions + [coin]
                    new_state = (g + new_total_tax, new_total_tax, new_actions, coin, i + 1)
                    if new_state not in visited_costs or g + new_total_tax < visited_costs[new_state]:
                        visited_costs[new_state] = g + new_total_tax
                        heapq.heappush(queue, (g + new_total_tax, new_total_tax, new_actions, coin, i + 1))

    return None


print(a_star())
