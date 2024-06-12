
import heapq


def a_star():
    # Define the list of coins and their corresponding tax values
    coins = [22, 4, 12, 26, 4, 9, 4, 28, 28, 8, 28, 19, 15, 20, 9, 161, 11, 28, 17, 10, 25, 15, 7, 28, 21, 24, 10, 13, 22, 4, 10, 14]
    tax_values = {15: 2, 17: 10, 10: 3, 12: 10, 21: 12, 4: 2, 22: 1, 11: 6, 26: 9, 14: 7, 24: 12, 161: 16, 20: 15, 9: 8, 8: 1, 13: 10, 28: 6, 7: 6, 25: 6, 19: 15}
    target_sum = 301

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen yet
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, total_value, prev_coin = heapq.heappop(queue)

        # If the total value of the coins chosen so far equals the target sum, return the list of coins chosen
        if total_value == target_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for coin in coins:
            # Check if the coin can be chosen based on the given conditions
            if (coin not in coins_chosen and
                ((coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0))):
                # Calculate the tax for the current coin
                tax = tax_values[coin]
                # Calculate the new total value and cost
                new_total_value = total_value + coin
                new_cost = g + tax

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if (new_total_value <= target_sum and
                    (new_total_value, new_cost) not in visited_costs or new_cost < visited_costs[(new_total_value, new_cost)]):
                    visited_costs[(new_total_value, new_cost)] = new_cost
                    heapq.heappush(queue, (g + new_cost, new_cost, coins_chosen + [coin], new_total_value, coin))

    return None


print(a_star())
