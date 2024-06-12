
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [40, 28, 46, 16, 13, 15, 38, 39, 3, 8, 40, 41, 18, 48, 16, 25, 39, 14, 47, 46, 31, 16, 41, 45, 9, 26, 33, 46, 17, 23, 6, 46, 7, 43, 10, 28, 47, 15, 35, 20, 32, 4, 32, 9, 48, 7, 34, 46, 10, 39, 44]
    tax_values = {44: 6, 39: 15, 4: 2, 23: 11, 7: 2, 40: 10, 13: 10, 34: 8, 45: 9, 10: 3, 35: 18, 14: 2, 28: 5, 46: 12, 25: 3, 26: 18, 15: 11, 31: 2, 20: 15, 9: 7, 41: 13, 18: 16, 32: 11, 3: 3, 48: 20, 38: 4, 43: 6, 33: 9, 16: 13, 8: 4, 17: 1, 47: 17, 6: 5}
    target_sum = 485

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, actions, total_value, total_tax = heapq.heappop(queue)

        # If the total value of the coins chosen equals the target sum, return the list of actions
        if total_value == target_sum:
            return actions

        for coin in coins:
            # Check if the coin is not already chosen
            if coin not in actions:
                # Check if the coin value is even if it is smaller than the previous coin, and odd if it is larger than or equal to the previous coin
                if not actions or (coin < actions[-1] and coin % 2 == 0) or (coin >= actions[-1] and coin % 2 != 0):
                    # Calculate the new total value and total tax
                    new_total_value = total_value + coin
                    new_total_tax = total_tax + tax_values[coin]
                    # Generate the new state
                    new_actions = actions + [coin]
                    new_state = (new_total_value, new_total_tax, tuple(sorted(new_actions)))
                    # Calculate the cost of the new state as the total tax paid
                    new_cost = g + new_total_tax

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + new_total_tax, new_cost, new_actions, new_total_value, new_total_tax))

    return None


print(a_star())
