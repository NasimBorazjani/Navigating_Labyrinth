
import heapq
import math


def a_star():
    # Define the list of coins and their tax values
    coins = [10, 5, 6, 2, 16, 19, 18, 5, 11, 12, 11, 7, 13, 19, 11, 12, 8, 17, 5, 18, 3, 12, 10, 14, 20, 18, 10, 11, 20, 13, 8, 8, 2, 7, 17, 10, 7, 21, 9, 20, 17, 1, 8, 19, 17, 16, 17, 10, 20, 8, 16, 14, 9]
    tax_values = {7: 2, 3: 2, 18: 1, 13: 3, 2: 2, 19: 17, 16: 6, 10: 1, 9: 9, 12: 7, 8: 7, 6: 3, 21: 18, 11: 10, 14: 13, 1: 1, 5: 5, 20: 18, 17: 14}
    target_sum = 211

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, actions, total_tax, last_coin = heapq.heappop(queue)

        # If the total sum of coins chosen equals the target sum, return the list of coins chosen
        if total_tax == target_sum:
            return actions

        for coin in coins:
            # Check if the coin is valid to be chosen based on the given conditions
            if (coin > last_coin and coin % 2 == 1) or (coin < last_coin and coin % 2 == 0):
                new_total_tax = total_tax + tax_values[coin]
                new_last_coin = coin
                new_state = (g + new_total_tax, new_total_tax, actions + [coin], new_last_coin)
                new_cost = g + new_total_tax

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_total_tax, target_sum)
                    heapq.heappush(queue, (g + h, new_cost, actions + [coin], new_total_tax, new_last_coin))

    return None


def heuristic(total_tax, target_sum):
    # An admissible and consistent heuristic is the absolute difference between the current total tax and the target sum
    # The heuristic relaxes the constraint that the tax value of each coin must be considered, as it only considers the total tax paid so far
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of the cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one coin to another is the tax value of the coin, which is always greater than or equal to the decrease in the absolute difference between the current total tax and the target sum
    return abs(total_tax - target_sum)


print(a_star())
