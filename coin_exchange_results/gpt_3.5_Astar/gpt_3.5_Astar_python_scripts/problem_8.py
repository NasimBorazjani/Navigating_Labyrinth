
import heapq


def a_star():
    # Define the list of coins and their corresponding tax values
    coins = [4, 17, 8, 15, 6, 14, 2, 4, 16, 10, 6, 5, 14, 8, 18, 2, 17, 9, 17, 59, 3, 10, 21, 4, 9, 14, 14, 20, 14, 8, 14, 18, 5, 16, 14, 17, 5, 3]
    tax_values = {15: 6, 5: 5, 17: 1, 14: 4, 2: 2, 8: 2, 10: 9, 59: 9, 16: 8, 4: 3, 18: 10, 20: 11, 21: 8, 6: 6, 9: 9, 3: 3}

    # Encoding other variables given in the problem statement
    target_sum = 214
    num_coins = len(coins)

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, prev_coin, total_tax = heapq.heappop(queue)

        # If the total sum of coins chosen equals the target sum, return the coins chosen
        if total_tax == target_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for i in range(num_coins):
            # Check if the coin is valid to be chosen based on the given conditions
            if (coins[i] % 2 == 0 and coins[i] > prev_coin) or (coins[i] % 2 != 0 and coins[i] <= prev_coin):
                # Calculate the tax for the current coin
                tax = tax_values[coins[i]]
                # Generate the new state
                new_total_tax = total_tax + tax
                new_coins_chosen = coins_chosen + [coins[i]]
                new_prev_coin = coins[i]
                new_cost = g + tax

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_total_tax <= target_sum and (i, new_total_tax, new_prev_coin) not in visited_costs or new_cost < visited_costs[(i, new_total_tax, new_prev_coin)]:
                    visited_costs[(i, new_total_tax, new_prev_coin)] = new_cost
                    heapq.heappush(queue, (g + new_total_tax, new_cost, new_coins_chosen, new_prev_coin, new_total_tax))

    return None


print(a_star())
