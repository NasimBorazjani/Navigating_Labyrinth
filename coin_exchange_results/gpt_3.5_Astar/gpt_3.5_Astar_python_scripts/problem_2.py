
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [13, 10, 12, 10, 16, 7, 9, 14, 13, 18, 36, 11, 7, 14, 7, 8, 19, 7, 39, 13, 3, 18, 20, 4, 3, 18, 15, 2, 19, 16]
    tax_values = {15: 5, 36: 15, 39: 9, 9: 8, 13: 3, 2: 2, 18: 10, 12: 12, 3: 3, 8: 8, 11: 6, 10: 4, 4: 4, 14: 10, 7: 3, 16: 16, 20: 18, 19: 17}
    target_sum = 203

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
            # Check if the coin is not already chosen and the total value of the coins chosen so far plus the value of the new coin does not exceed the target sum
            if coin not in coins_chosen and total_value + coin <= target_sum:
                # Check if the coin follows the rules of being even if smaller than the previous coin and odd if larger or equal to the previous coin
                if (coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0):
                    # Calculate the tax for the current coin
                    tax = tax_values[coin]
                    # Calculate the new total cost, which is the sum of the tax for the current coin and the total tax paid so far
                    new_cost = g + tax
                    # Calculate the new total value of the coins chosen so far
                    new_total_value = total_value + coin
                    # Update the previous coin to the current coin for the next iteration
                    new_prev_coin = coin
                    # Add the new state to the priority queue
                    heapq.heappush(queue, (g + new_cost, new_cost, coins_chosen + [coin], new_total_value, new_prev_coin))

    return None


print(a_star())
