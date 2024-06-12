
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [84, 2, 8, 16, 21, 10, 15, 4, 17, 16, 4, 85, 30, 13, 28, 2, 2, 11, 18, 9, 25, 5, 24, 14, 20, 30, 6]
    tax_values = {15: 2, 18: 9, 28: 4, 84: 10, 2: 1, 24: 19, 30: 12, 5: 2, 9: 9, 21: 9, 11: 10, 16: 14, 4: 2, 17: 2, 85: 18, 6: 5, 8: 6, 13: 2, 10: 4, 25: 11, 20: 19, 14: 2}
    target_sum = 309

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen yet
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, total_value, prev_coin = heapq.heappop(queue)

        # If the total value of the coins chosen equals the target sum, return the list of coins chosen
        if total_value == target_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for coin in coins:
            # Check if the coin can be chosen based on the given conditions
            if (coin % 2 == 0 and coin > prev_coin) or (coin % 2 != 0 and coin <= prev_coin):
                new_total_value = total_value + coin
                new_tax = tax_values[coin]
                new_cost = g + new_tax

                if new_total_value <= target_sum and (new_total_value, new_tax, coin) not in visited_costs:
                    visited_costs[(new_total_value, new_tax, coin)] = new_cost
                    heapq.heappush(queue, (g + new_tax, new_cost, coins_chosen + [coin], new_total_value, coin))

    return None


print(a_star())
