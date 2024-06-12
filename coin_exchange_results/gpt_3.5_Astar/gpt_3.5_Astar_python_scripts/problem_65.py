
import heapq


def a_star():
    # Define the list of coins and their corresponding tax values
    coins = [9, 30, 18, 32, 31, 20, 34, 9, 12, 18, 14, 16, 29, 37, 37, 6, 24, 10, 10, 35, 23, 4, 30, 121, 31, 16, 35]
    tax_values = {35: 20, 4: 2, 18: 11, 24: 10, 10: 7, 14: 3, 37: 1, 16: 14, 12: 7, 6: 2, 29: 18, 34: 19, 121: 10, 31: 7, 30: 12, 32: 12, 23: 8, 20: 8, 9: 9}
    target_sum = 406

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, prev_coin, total_tax = heapq.heappop(queue)

        # If the total sum of coins chosen equals the target sum, return the list of coins chosen
        if total_tax == target_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for coin in coins:
            # Check if the coin is valid based on the tax rules
            if (coin > prev_coin and coin % 2 == 1) or (coin < prev_coin and coin % 2 == 0):
                new_total_tax = total_tax + tax_values[coin]
                # If the new total tax does not exceed the target sum, add the coin to the list of coins chosen
                if new_total_tax <= target_sum:
                    new_state = (g + new_total_tax, new_total_tax, coins_chosen + [coin], coin, new_total_tax)
                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or g + new_total_tax < visited_costs[new_state]:
                        visited_costs[new_state] = g + new_total_tax
                        heapq.heappush(queue, (g + new_total_tax, g + new_total_tax, coins_chosen + [coin], coin, new_total_tax))

    return None


print(a_star())
