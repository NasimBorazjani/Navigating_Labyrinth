
import heapq
import math


def a_star():
    # Define the list of coins and their tax values
    coins = [24, 10, 24, 3, 21, 7, 21, 26, 8, 14, 24, 5, 13, 10, 25, 6, 9, 4, 18, 4, 15, 4, 10, 23, 6, 13, 26, 20, 8, 10, 29, 27, 27, 20, 2, 15, 9, 9, 25, 8, 2, 27, 5, 22, 19, 26, 2, 29, 12, 9, 6, 12, 2, 15, 5, 16, 3, 29, 19]
    tax_values = {5: 2, 9: 8, 12: 5, 14: 4, 22: 8, 26: 3, 8: 7, 27: 2, 20: 13, 3: 3, 13: 3, 2: 1, 19: 19, 29: 4, 10: 3, 18: 14, 21: 12, 15: 12, 4: 3, 23: 5, 16: 9, 25: 16, 7: 4, 24: 17, 6: 6}
    target_sum = 300

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, actions, prev_coin, prev_tax = heapq.heappop(queue)

        # Calculate the sum of the coins chosen so far
        current_sum = sum(coins[i] for i in actions)

        # If the sum of the chosen coins equals the target sum, return the list of coins chosen
        if current_sum == target_sum:
            return actions

        for i, coin in enumerate(coins):
            # Check if the coin is valid based on the tax rules
            if (coin > prev_coin and coin % 2 == 0) or (coin <= prev_coin and coin % 2 != 0):
                # Calculate the new tax value based on the tax values dictionary
                new_tax = prev_tax + tax_values[coin]
                # Calculate the new cost as the sum of the tax values
                new_cost = g + new_tax

                # If the new state is valid and has not been visited before, add it to the queue
                if new_tax <= target_sum and (i, new_tax, new_cost) not in visited_costs:
                    visited_costs[(i, new_tax, new_cost)] = new_cost
                    heapq.heappush(queue, (g + new_cost, new_cost, actions + [i], coin, new_tax))

    return None


print(a_star())
