
import heapq
import math


def a_star():
    # Define the list of coins and their tax values
    coins = [21, 20, 21, 11, 23, 16, 16, 16, 3, 20, 2, 19, 16, 21, 18, 7, 20, 3, 16, 18, 7, 22, 3, 22, 7, 21, 12, 22, 5, 6, 17, 16, 8, 8, 14, 4, 18, 9, 4, 20, 2]
    tax_values = {6: 1, 7: 3, 9: 1, 18: 1, 2: 1, 11: 7, 5: 3, 12: 2, 3: 3, 22: 6, 14: 3, 20: 15, 4: 3, 17: 4, 16: 8, 23: 18, 21: 16, 19: 2, 8: 6}
    
    # Encoding other variables given in the problem statement
    target_sum = 228
    coins.sort(reverse=True)  # Sort the coins in descending order to prioritize larger coins first

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0  # Initialize the cost to reach each visited state

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen to reach each state in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, prev_coin, total_tax = heapq.heappop(queue)

        # If the total sum of coins chosen equals the target sum, return the coins chosen
        if sum(coins_chosen) == target_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for coin in coins:
            # Check if the coin can be chosen based on the given constraints
            if (coin not in coins_chosen and
                ((coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0))):
                # Calculate the tax for the current coin
                coin_tax = tax_values[coin]
                # Calculate the new total tax
                new_total_tax = total_tax + coin_tax
                # Calculate the new cost to reach the new state
                new_cost = g + coin_tax
                # Check if the new state is unvisited or we found a new path with a lower cost to reach this state
                if new_total_tax <= target_sum and (new_total_tax, new_cost) not in visited_costs:
                    visited_costs[(new_total_tax, new_cost)] = 1
                    heapq.heappush(queue, (g + new_cost, new_cost, coins_chosen + [coin], coin, new_total_tax))

    return None


print(a_star())
