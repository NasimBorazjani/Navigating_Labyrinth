
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [26, 19, 7, 24, 27, 15, 9, 9, 9, 26, 15, 23, 6, 6, 24, 8, 21, 6, 6, 7, 25, 22, 8, 2, 7, 5, 8, 18, 14, 15, 24, 10, 4, 23, 21, 8, 18, 12, 16]
    tax_values = {24: 14, 27: 10, 22: 14, 16: 7, 14: 12, 6: 3, 8: 7, 23: 6, 18: 18, 5: 3, 25: 8, 7: 6, 12: 3, 15: 8, 9: 2, 19: 15, 2: 1, 4: 1, 26: 15, 10: 8, 21: 19}
    
    # Encoding other variables given in the problem statement
    target_sum = 267
    coins.sort(reverse=True)  # Sort the coins in descending order to prioritize larger coins first
    num_coins = len(coins)

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, total_tax, last_coin_index = heapq.heappop(queue)

        # If the total sum of coins chosen equals the target sum, return the coins chosen
        if sum(coins_chosen) == target_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for i in range(last_coin_index, num_coins):
            new_coin = coins[i]
            # Check if the new coin can be chosen based on the given conditions
            if (new_coin % 2 == 0 and new_coin < coins_chosen[-1]) or (new_coin % 2 != 0 and new_coin >= coins_chosen[-1]):
                # Calculate the tax for the new coin
                new_tax = tax_values[new_coin]
                # Generate the new state
                new_coins_chosen = coins_chosen + [new_coin]
                new_total_tax = total_tax + new_tax
                new_state = (g + new_tax, new_total_tax, new_coins_chosen, i)

                if new_state not in visited_costs or new_total_tax < visited_costs[new_state]:
                    visited_costs[new_state] = new_total_tax
                    heapq.heappush(queue, (g + new_tax, new_total_tax, new_coins_chosen, i))
    return None


print(a_star())
