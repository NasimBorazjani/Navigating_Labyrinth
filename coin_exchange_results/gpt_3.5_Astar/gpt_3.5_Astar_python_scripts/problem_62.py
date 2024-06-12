
import heapq
import math


def a_star():
    # Define the list of coins and their tax values
    coins = [35, 14, 9, 23, 25, 24, 21, 20, 12, 17, 12, 5, 2, 17, 25, 25, 26, 31, 7, 21, 10, 2, 27, 19, 32, 29, 11, 33, 3, 27, 17, 3, 18, 14, 2, 32, 14, 21, 12, 8, 3, 34, 13, 12, 2, 23, 13, 3, 3, 31, 23, 23, 6, 30, 30, 11, 21]
    tax_values = {3: 1, 32: 16, 6: 5, 20: 13, 13: 5, 31: 9, 23: 10, 35: 14, 24: 17, 11: 11, 9: 1, 12: 10, 5: 3, 8: 5, 34: 11, 17: 16, 25: 9, 26: 6, 30: 17, 27: 17, 7: 2, 18: 17, 33: 5, 14: 2, 29: 14, 10: 3, 2: 2, 21: 12, 19: 9}
    target_sum = 356

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    queue = [(0, 0, [], 0, 0, 0)]

    while queue:
        _, g, actions, total_tax, prev_coin, index = heapq.heappop(queue)

        if total_tax == target_sum:
            return actions

        for i in range(index, len(coins)):
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
