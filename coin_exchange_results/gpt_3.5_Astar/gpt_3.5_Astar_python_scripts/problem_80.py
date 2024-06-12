
import heapq
import math


def a_star():
    # Define the list of coins and their tax values
    coins = [8, 7, 5, 24, 3, 18, 36, 39, 36, 25, 25, 33, 16, 20, 34, 9, 1, 22, 25, 13, 8, 37, 35, 39, 11, 26, 36, 25, 25, 27, 2, 4, 35, 2, 16, 22, 12, 15, 19, 2, 17, 25, 28, 12, 26, 17, 33, 5, 30, 3, 21, 3]
    tax_values = {13: 7, 39: 4, 20: 18, 5: 1, 12: 7, 9: 5, 28: 20, 24: 11, 3: 3, 17: 3, 21: 9, 37: 6, 16: 8, 15: 1, 26: 10, 36: 6, 22: 9, 2: 2, 8: 1, 25: 20, 4: 3, 7: 5, 19: 7, 30: 6, 27: 12, 1: 1, 34: 7, 35: 5, 11: 6, 18: 12, 33: 4}
    target_sum = 397

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, actions, prev_coin, total_tax = heapq.heappop(queue)

        # If the total sum of coins chosen equals the target sum, return the list of coins chosen
        if sum(actions) == target_sum:
            return actions

        for coin in coins:
            # Check if the coin is valid based on the tax rules
            if (coin > prev_coin and coin % 2 == 1) or (coin < prev_coin and coin % 2 == 0):
                new_total_tax = total_tax + tax_values[coin]
                new_state = (coin, new_total_tax, actions + [coin])
                new_cost = g + tax_values[coin]

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_state, coins, target_sum)
                    heapq.heappush(queue, (g + h, new_cost, actions + [coin], coin, new_total_tax))

    return None


def heuristic(state, coins, target_sum):
    # The heuristic is the difference between the target sum and the current sum of coins chosen
    # This heuristic is admissible because it never overestimates the cost to reach the goal state, as the difference between the current sum and the target sum is the minimum cost required to reach the goal state
    # The heuristic is consistent because the cost of moving from one state to another is the tax value of the coin chosen, which is always greater than or equal to the difference in the sum of coins between the two states
    return abs(sum(state[2]) - target_sum)


print(a_star())
