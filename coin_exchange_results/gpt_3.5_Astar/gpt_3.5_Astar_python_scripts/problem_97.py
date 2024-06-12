
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [39, 3, 38, 10, 3, 5, 6, 14, 32, 7, 30, 28, 17, 9, 8, 13, 17, 41, 25, 6, 19, 36, 5, 36, 8, 38, 6, 19, 25, 3, 22, 18, 3, 21, 57, 37, 42, 30, 54, 13, 36, 6, 13, 17, 10, 4, 36]
    tax_values = {37: 2, 38: 4, 30: 18, 39: 18, 14: 1, 18: 1, 4: 1, 10: 8, 21: 10, 6: 5, 42: 13, 32: 10, 25: 2, 17: 15, 13: 2, 9: 4, 22: 17, 7: 5, 3: 2, 54: 7, 19: 15, 8: 2, 36: 17, 28: 6, 5: 5, 41: 9, 57: 12}
    target_sum = 452

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen yet
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, prev_coin, total_tax = heapq.heappop(queue)

        # If the total sum of coins chosen equals the target sum, return the list of coins chosen
        if sum(coins_chosen) == target_sum:
            return coins_chosen

        for coin in coins:
            # Check if the coin is valid based on the tax rules
            if (coin > prev_coin and coin % 2 == 1) or (coin < prev_coin and coin % 2 == 0):
                new_total_tax = total_tax + tax_values[coin]
                # Generate the new state
                new_state = (g + new_total_tax, coin, coins_chosen + [coin], coin, new_total_tax)
                # The cost of the new state is the total tax paid so far
                new_cost = g + new_total_tax

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + new_total_tax, new_cost, coins_chosen + [coin], coin, new_total_tax))

    return None


print(a_star())
