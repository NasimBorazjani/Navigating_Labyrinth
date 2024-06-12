
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [20, 27, 20, 26, 2, 19, 25, 5, 14, 28, 7, 4, 20, 25, 9, 7, 3, 9, 27, 23, 2, 17, 25, 19, 10, 2, 8, 15, 3, 6, 24, 6, 22, 3, 10, 3, 2, 24, 7, 16, 2, 24, 21, 5, 23, 25, 10, 5, 20, 14, 24, 12, 11, 11, 13]
    tax_values = {14: 7, 15: 15, 2: 2, 22: 7, 7: 1, 25: 7, 10: 4, 11: 11, 16: 11, 27: 8, 3: 2, 13: 5, 19: 10, 8: 5, 23: 18, 5: 4, 12: 4, 28: 6, 6: 4, 21: 3, 20: 15, 26: 1, 4: 4, 9: 9, 24: 6, 17: 13}
    
    # Encoding other variables given in the problem statement
    target_sum = 284
    coins.sort(reverse=True)  # Sort the coins in descending order to prioritize larger coins first
    num_coins = len(coins)

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen yet
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, prev_coin, total_tax = heapq.heappop(queue)

        # If the total sum of the coins chosen so far equals the target sum, return the list of coins chosen
        if sum(coins_chosen) == target_sum:
            return coins_chosen

        for i in range(num_coins):
            # Check if the coin is valid based on the tax rules provided
            if (coins[i] % 2 == 0 and coins[i] < prev_coin) or (coins[i] % 2 != 0 and coins[i] >= prev_coin):
                new_total_tax = total_tax + tax_values[coins[i]]
                # Generate the new state
                new_coins_chosen = coins_chosen + [coins[i]]
                new_state = (g + new_total_tax, new_total_tax, new_coins_chosen, coins[i], new_total_tax)
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or g + new_total_tax < visited_costs[new_state]:
                    visited_costs[new_state] = g + new_total_tax
                    heapq.heappush(queue, (g + new_total_tax, new_total_tax, new_coins_chosen, coins[i], new_total_tax))
    return None


print(a_star())
