
import heapq


def a_star():
    # Define the list of coins and their corresponding tax values
    coins = [13, 19, 9, 4, 18, 17, 2, 14, 17, 17, 8, 6, 4, 10, 19, 37, 20, 19, 14, 7, 6, 11, 21, 9, 3, 10, 21, 20, 2, 17, 2]
    tax_values = {14: 2, 18: 9, 11: 10, 9: 6, 10: 9, 13: 10, 37: 9, 6: 5, 2: 2, 4: 1, 8: 3, 19: 10, 17: 7, 7: 6, 3: 3, 21: 3, 20: 4}
    target_sum = 215

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, total_value, prev_coin = heapq.heappop(queue)

        # If the total value of the coins chosen so far equals the target sum, return the list of coins chosen
        if total_value == target_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for coin in coins:
            # Check if the coin is valid to choose based on the given conditions
            if (coin not in coins_chosen and
                ((coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0))):
                # Calculate the tax for the current coin
                tax = tax_values[coin]
                # Calculate the new total value and cost of the new state
                new_total_value = total_value + coin
                new_cost = g + tax

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if (new_total_value <= target_sum and
                    (new_total_value, new_cost) not in visited_costs or new_cost < visited_costs[(new_total_value, new_cost)]):
                    visited_costs[(new_total_value, new_cost)] = new_cost
                    heapq.heappush(queue, (g + new_cost, new_cost, coins_chosen + [coin], new_total_value, coin))

    return None


print(a_star())
