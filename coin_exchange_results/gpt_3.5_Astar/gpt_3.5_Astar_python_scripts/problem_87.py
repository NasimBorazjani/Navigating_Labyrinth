
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [25, 41, 34, 19, 19, 36, 37, 13, 28, 26, 181, 7, 14, 6, 29, 36, 33, 7, 8, 43, 19, 9, 3, 2, 18, 40, 43, 22, 23, 21]
    tax_values = {21: 5, 26: 13, 36: 8, 28: 8, 34: 12, 3: 2, 6: 2, 23: 10, 2: 2, 9: 5, 41: 4, 29: 19, 7: 6, 18: 18, 43: 2, 8: 7, 181: 9, 25: 10, 33: 8, 14: 13, 13: 1, 22: 13, 40: 7, 37: 11, 19: 11}
    target_sum = 449

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen yet
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, total_value, last_coin = heapq.heappop(queue)

        # If the total value of the coins chosen so far equals the target sum, return the list of coins chosen
        if total_value == target_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for coin in coins:
            # Check if the coin is valid to be chosen based on the given conditions
            if (coin not in coins_chosen and
                ((coin < last_coin and coin % 2 == 0) or (coin >= last_coin and coin % 2 != 0))):
                # Calculate the new total value and tax paid
                new_total_value = total_value + coin
                new_tax_paid = sum(tax_values[c] for c in coins_chosen) + tax_values[coin]
                # The cost of the new state is the tax paid so far
                new_cost = new_tax_paid

                if new_total_value <= target_sum and (new_total_value, new_tax_paid, coin) not in visited_costs:
                    visited_costs[(new_total_value, new_tax_paid, coin)] = new_cost
                    heapq.heappush(queue, (g + new_cost, new_cost, coins_chosen + [coin], new_total_value, coin))

    return None


print(a_star())
