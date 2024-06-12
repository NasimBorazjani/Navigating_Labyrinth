
import heapq


def a_star():
    # Define the list of coins and their corresponding tax values
    coins = [43, 41, 23, 24, 40, 11, 12, 9, 32, 32, 6, 15, 16, 20, 6, 39, 9, 12, 4, 251, 43, 24, 27, 20, 39, 37, 7, 43, 9, 13, 45, 27, 9, 15, 41, 25]
    tax_values = {9: 7, 32: 17, 24: 17, 15: 11, 4: 3, 39: 18, 41: 9, 25: 14, 27: 5, 40: 5, 43: 8, 11: 9, 20: 1, 45: 2, 16: 15, 251: 12, 37: 10, 13: 1, 23: 1, 7: 1, 12: 1, 6: 5}
    target_sum = 471

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen yet
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, total_value, prev_coin = heapq.heappop(queue)

        # If the total value of the coins chosen so far equals the target sum, return the list of coins chosen
        if total_value == target_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for coin in coins:
            # Check if the coin is valid to choose based on the given constraints
            if (coin not in coins_chosen and
                ((coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0))):
                # Calculate the tax for the chosen coin
                tax = tax_values[coin]
                # Calculate the new total value of the coins chosen
                new_total_value = total_value + coin + tax
                # The cost so far is the total tax paid
                new_cost = g + tax

                # If the new total value is less than or equal to the target sum and the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_total_value <= target_sum and (new_total_value, coin) not in visited_costs or new_cost < visited_costs[(new_total_value, coin)]:
                    visited_costs[(new_total_value, coin)] = new_cost
                    heapq.heappush(queue, (g + new_total_value, new_cost, coins_chosen + [coin], new_total_value, coin))

    return None


print(a_star())
