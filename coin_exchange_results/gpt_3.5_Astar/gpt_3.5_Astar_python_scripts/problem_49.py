
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [18, 20, 11, 6, 81, 3, 9, 5, 14, 19, 30, 2, 19, 3, 9, 22, 21, 29, 6, 25, 10, 18, 27, 26, 25, 13, 15, 16, 3, 5, 23, 26, 25, 31, 15, 12]
    tax_values = {11: 6, 6: 3, 16: 11, 23: 16, 18: 3, 31: 4, 9: 2, 3: 1, 22: 10, 10: 1, 30: 4, 81: 14, 2: 1, 14: 1, 13: 11, 15: 7, 19: 16, 25: 6, 12: 12, 29: 11, 26: 9, 5: 1, 27: 15, 20: 7, 21: 14}
    target_sum = 324

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen at the start
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, prev_coin, prev_tax = heapq.heappop(queue)

        # If the sum of the coins chosen so far equals the target sum, return the coins chosen
        if sum(coins_chosen) == target_sum:
            return coins_chosen

        for coin in coins:
            # Check if the coin is valid based on the tax rules
            if (coin > prev_coin and coin % 2 == 1) or (coin < prev_coin and coin % 2 == 0):
                # Calculate the tax for the current coin
                tax = tax_values[coin]
                # Calculate the total tax paid so far
                total_tax = prev_tax + tax
                # Calculate the new cost to reach the current state
                new_cost = g + total_tax

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if (new_cost < visited_costs.get((coin, total_tax), float('inf'))):
                    visited_costs[(coin, total_tax)] = new_cost
                    heapq.heappush(queue, (g + 1, new_cost, coins_chosen + [coin], coin, total_tax))

    return None


print(a_star())
