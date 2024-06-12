
import heapq


def a_star():
    # Define the list of coins and their corresponding tax values
    coins = [20, 25, 10, 4, 13, 3, 10, 17, 5, 25, 17, 2, 19, 24, 25, 10, 19, 8, 2, 20, 15, 84, 23, 87, 19, 8, 12, 17, 23, 6]
    tax_values = {12: 12, 19: 8, 84: 20, 24: 1, 5: 1, 3: 1, 4: 2, 87: 7, 10: 5, 25: 7, 6: 5, 20: 5, 15: 7, 23: 17, 13: 4, 17: 16, 2: 1, 8: 5}
    target_sum = 250

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, total_value, prev_coin = heapq.heappop(queue)

        # If the total value of the coins chosen so far equals the target sum, return the list of coins chosen
        if total_value == target_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for coin in coins:
            # Check if the coin is valid based on the given conditions
            if (coin not in coins_chosen and
                ((coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0))):
                # Calculate the new total value and tax paid
                new_total_value = total_value + coin
                new_tax_paid = sum(tax_values[c] for c in coins_chosen) + tax_values[coin]
                # The cost so far is the tax paid, as we aim to minimize the total tax paid
                new_cost = new_tax_paid

                if (new_total_value <= target_sum and
                    (new_total_value, new_tax_paid, coin) not in visited_costs or new_cost < visited_costs[(new_total_value, new_tax_paid, coin)]):
                    visited_costs[(new_total_value, new_tax_paid, coin)] = new_cost
                    heapq.heappush(queue, (g + new_cost, new_cost, coins_chosen + [coin], new_total_value, coin))

    return None


print(a_star())
