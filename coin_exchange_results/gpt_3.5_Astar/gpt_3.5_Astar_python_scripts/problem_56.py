
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [4, 33, 14, 32, 9, 32, 2, 35, 25, 10, 11, 6, 8, 26, 10, 25, 34, 21, 13, 15, 3, 15, 25, 3, 16, 3, 2, 25, 15, 23, 31, 35, 13, 14, 5, 7, 2, 18, 10, 8, 25, 30, 13, 35, 3, 26, 33, 2, 5, 26, 26, 28, 6]
    tax_values = {26: 4, 34: 4, 7: 5, 28: 11, 35: 8, 18: 13, 25: 19, 14: 10, 23: 7, 6: 1, 10: 5, 21: 8, 13: 13, 2: 1, 3: 1, 30: 5, 4: 4, 31: 18, 11: 3, 9: 1, 8: 3, 5: 3, 32: 5, 15: 15, 33: 18, 16: 4}
    
    # Encoding other variables given in the problem statement
    target_sum = 355
    coins.sort(reverse=True)  # Sort the coins in descending order to prioritize larger coins first

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0  # Initialize the cost to reach the initial state as 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [], (0, 0, 0))]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Unpack the information encoded in each state
        total_value, prev_coin, total_tax = state

        # If the total value of the coins chosen equals the target sum, return the list of coins chosen
        if total_value == target_sum:
            return actions

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for coin in coins:
            # Check if the coin satisfies the conditions based on the previous coin chosen
            if (coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0):
                # Calculate the new total value, previous coin, and total tax
                new_total_value = total_value + coin
                new_prev_coin = coin
                new_total_tax = total_tax + tax_values[coin]
                # Generate the new state
                new_state = (new_total_value, new_prev_coin, new_total_tax)
                # The cost of the new state is the total tax paid so far
                new_cost = new_total_tax

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + new_cost, new_cost, actions + [coin], new_state))

    return None


print(a_star())
