
import heapq
import math


def a_star():
    # Define the list of coins and their tax values
    coins = [17, 19, 5, 17, 13, 2, 12, 4, 4, 15, 19, 7, 18, 15, 4, 6, 9, 2, 4, 11, 21, 17, 20, 4, 8, 2, 19, 16, 2, 12, 8, 16, 18, 3, 18, 13, 3, 15, 7, 18, 4, 14, 3, 5, 8, 7, 19, 9, 17, 5, 17, 6, 3, 5, 15]
    tax_values = {9: 9, 6: 1, 13: 4, 2: 1, 16: 3, 14: 4, 19: 16, 20: 2, 15: 3, 7: 3, 18: 14, 17: 15, 4: 2, 5: 5, 8: 8, 21: 10, 12: 11, 11: 7, 3: 2}
    target_sum = 210

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, actions, prev_coin, total_tax = heapq.heappop(queue)

        # If the total sum of coins chosen equals the target sum, return the list of coins chosen
        if total_tax == target_sum:
            return actions

        for coin in coins:
            # Check if the coin is valid based on the tax rules
            if (coin > prev_coin and coin % 2 == 1) or (coin < prev_coin and coin % 2 == 0):
                new_total_tax = total_tax + tax_values[coin]
                new_state = (coin, new_total_tax, g + tax_values[coin])
                if new_state not in visited_costs or g + tax_values[coin] < visited_costs[new_state]:
                    visited_costs[new_state] = g + tax_values[coin]
                    heapq.heappush(queue, (g + tax_values[coin] + heuristic(new_total_tax, target_sum), g + tax_values[coin], actions + [coin], coin, new_total_tax))
    return None


def heuristic(total_tax, target_sum):
    # An admissible and consistent heuristic is the absolute difference between the current total tax and the target sum
    # The heuristic relaxes the constraint that the tax value of each coin is fixed and presumes that the tax value can be minimized by choosing coins that bring the total tax closer to the target sum
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of the cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of choosing a coin is the tax value of that coin, which is always greater than or equal to the decrease in the absolute difference between the current total tax and the target sum
    return abs(total_tax - target_sum)


print(a_star())
