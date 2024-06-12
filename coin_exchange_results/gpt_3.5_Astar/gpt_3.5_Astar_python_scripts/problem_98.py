
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [35, 14, 15, 111, 8, 4, 6, 37, 14, 33, 45, 32, 46, 41, 38, 19, 34, 14, 2, 4, 24, 36, 46, 33, 12, 2, 14, 28, 12, 21, 34, 26, 28, 27, 25, 4, 23, 43, 43, 20, 10, 13, 5, 36, 27, 36]
    tax_values = {33: 16, 21: 14, 4: 1, 13: 9, 23: 8, 2: 2, 12: 2, 41: 15, 46: 6, 45: 2, 34: 16, 24: 15, 19: 4, 5: 4, 35: 14, 6: 6, 37: 13, 26: 16, 43: 20, 15: 13, 111: 2, 38: 1, 10: 7, 32: 13, 20: 14, 27: 15, 36: 14, 25: 8, 14: 2, 28: 10, 8: 4}
    target_sum = 462

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], (0, 0, 0))]

    while queue:
        _, g, coins_chosen, state = heapq.heappop(queue)

        # Unpack the information encoded in each state
        total_sum, prev_coin, prev_tax = state

        # If the total sum of coins chosen equals the target sum, return the coins chosen
        if total_sum == target_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for coin in coins:
            # Check if the coin is not already chosen and the total sum of coins chosen plus the new coin does not exceed the target sum
            if coin not in coins_chosen and total_sum + coin <= target_sum:
                # Check if the coin follows the tax rules based on the previous coin chosen
                if (prev_coin == 0 or (coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0)):
                    # Calculate the tax for the new coin
                    tax = tax_values[coin]
                    # Calculate the new total tax
                    new_total_tax = prev_tax + tax
                    # Generate the new state
                    new_state = (total_sum + coin, coin, new_total_tax)
                    # The cost of the new state is the total tax paid so far
                    new_cost = new_total_tax

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + new_cost, new_cost, coins_chosen + [coin], new_state))
    return None


print(a_star())
