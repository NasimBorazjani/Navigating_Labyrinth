
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [14, 19, 3, 8, 5, 107, 4, 10, 9, 2, 11, 7, 11, 11, 4, 10, 17, 14, 18, 10, 21, 13, 2, 13, 19, 5, 8, 4, 7, 6, 10]
    tax_values = {17: 9, 107: 7, 13: 11, 10: 7, 19: 12, 9: 2, 4: 4, 14: 8, 21: 14, 6: 2, 5: 3, 2: 2, 3: 3, 7: 6, 18: 6, 8: 4, 11: 11}
    target_sum = 215

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far and the total tax paid so far in a list; no coins chosen and no tax paid to reach the initial state
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, total_tax, current_sum = heapq.heappop(queue)

        # If the current sum equals the target sum, return the coins chosen
        if current_sum == target_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for coin in coins:
            # Check if the coin can be chosen based on the given constraints
            if (coin not in coins_chosen and
                ((coin < coins_chosen[-1] and coin % 2 == 0) or
                 (coin >= coins_chosen[-1] and coin % 2 != 0))):
                # Calculate the new total tax and the new sum of coins chosen
                new_total_tax = total_tax + tax_values[coin]
                new_sum = current_sum + coin
                # Generate the new state
                new_coins_chosen = coins_chosen + [coin]
                new_state = (g + new_total_tax, new_total_tax, new_coins_chosen, new_sum, new_sum)
                # The cost of the new state is the total tax paid so far
                new_cost = g + new_total_tax

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + new_total_tax, new_total_tax, new_coins_chosen, new_sum, new_sum))

    return None


print(a_star())
