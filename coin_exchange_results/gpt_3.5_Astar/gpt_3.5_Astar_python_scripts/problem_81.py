
import heapq
import math


def a_star():
    # Define the list of coins and their tax values
    coins = [13, 30, 19, 13, 34, 12, 16, 21, 24, 39, 37, 32, 3, 5, 30, 37, 29, 20, 15, 23, 30, 24, 12, 21, 19, 10, 26, 29, 3, 23, 20, 40, 22, 13, 2, 36, 8, 40, 6, 24, 24, 11, 26, 37, 16, 57, 39, 21, 17]
    tax_values = {2: 2, 21: 6, 24: 9, 26: 2, 5: 3, 29: 10, 10: 7, 13: 13, 30: 17, 36: 15, 3: 1, 32: 7, 8: 5, 20: 2, 22: 3, 57: 19, 40: 8, 6: 4, 23: 8, 39: 3, 16: 5, 37: 6, 12: 9, 11: 11, 34: 6, 17: 2, 15: 10, 19: 17}
    target_sum = 412

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

            # Check if the coin is valid based on the rules provided
            if (coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0):
                new_total_tax = total_tax + tax
                if new_total_tax <= target_sum:
                    new_state = (total_tax + tax, coin, i + 1)
                    new_cost = g + tax

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + new_total_tax, new_cost, actions + [coin], total_tax + tax, coin, i + 1))

    return None


print(a_star())
