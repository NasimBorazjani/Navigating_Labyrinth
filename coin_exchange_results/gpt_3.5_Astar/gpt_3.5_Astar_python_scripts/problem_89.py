
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [27, 23, 11, 23, 6, 197, 7, 21, 2, 22, 12, 38, 15, 32, 5, 19, 6, 28, 31, 31, 10, 10, 28, 24, 41, 6, 39, 16, 11, 37, 23, 7, 2]
    tax_values = {41: 14, 23: 15, 31: 19, 21: 18, 22: 2, 6: 3, 11: 5, 12: 11, 37: 10, 7: 2, 32: 19, 28: 10, 16: 12, 2: 2, 197: 7, 39: 18, 19: 18, 15: 4, 10: 9, 5: 4, 27: 10, 38: 3, 24: 5}
    target_sum = 445

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen to reach the initial state
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
