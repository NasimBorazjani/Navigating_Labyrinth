
import heapq


def a_star():
    # Define the list of coins and their corresponding tax values
    coins = [8, 8, 6, 36, 7, 36, 33, 3, 31, 17, 21, 28, 41, 17, 23, 16, 39, 2, 3, 40, 23, 20, 5, 30, 8, 28, 17, 34, 38, 26, 16, 21, 15, 21, 11, 33, 5, 33, 2, 27, 26, 21, 14, 13, 7, 23]
    tax_values = {28: 16, 5: 1, 3: 3, 40: 18, 33: 20, 34: 12, 20: 4, 39: 13, 2: 2, 31: 11, 36: 2, 17: 14, 7: 1, 14: 6, 23: 12, 8: 1, 30: 15, 27: 13, 15: 2, 21: 3, 11: 6, 26: 14, 41: 2, 38: 10, 6: 5, 16: 4, 13: 11}
    target_sum = 403

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen yet
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, prev_coin, total_tax = heapq.heappop(queue)

        # If the total sum of the coins chosen equals the target sum, return the list of coins chosen
        if sum(coins_chosen) == target_sum:
            return coins_chosen

        for coin in coins:
            # Check if the coin is not already chosen
            if coin not in coins_chosen:
                # Check if the coin follows the rules of being smaller than the previous coin if it's even, and larger than or equal to the previous coin if it's odd
                if (coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0):
                    # Calculate the tax for the current coin
                    tax = tax_values[coin]
                    # Calculate the new total tax
                    new_total_tax = total_tax + tax
                    # Calculate the new cost, which is the total tax paid so far
                    new_cost = g + new_total_tax
                    # Create a new list of coins chosen
                    new_coins_chosen = coins_chosen + [coin]
                    # Update the previous coin to the current coin
                    new_prev_coin = coin

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if (new_cost < visited_costs.get((len(new_coins_chosen), new_total_tax), float('inf'))):
                        visited_costs[(len(new_coins_chosen), new_total_tax)] = new_cost
                        heapq.heappush(queue, (g + new_total_tax, new_cost, new_coins_chosen, new_prev_coin, new_total_tax))

    return None


print(a_star())
