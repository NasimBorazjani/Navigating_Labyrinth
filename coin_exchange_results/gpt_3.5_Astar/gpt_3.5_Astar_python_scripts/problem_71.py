
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [18, 11, 14, 3, 7, 18, 40, 3, 35, 30, 24, 29, 34, 11, 17, 14, 14, 10, 5, 40, 4, 31, 25, 14, 39, 12, 26, 24, 3, 8, 34, 2, 22, 189, 40]
    tax_values = {29: 9, 40: 8, 30: 5, 17: 16, 3: 3, 5: 3, 2: 2, 22: 17, 11: 1, 14: 4, 8: 5, 18: 11, 26: 8, 39: 15, 7: 1, 31: 2, 24: 17, 189: 5, 12: 4, 25: 10, 35: 18, 10: 1, 4: 3, 34: 16}
    target_sum = 400

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen to get to each state in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], (0, 0, 0))]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Unpack the information encoded in each state
        total_sum, prev_coin, prev_tax = state

        # If the total sum of coins chosen equals the target sum, return the list of coins chosen
        if total_sum == target_sum:
            return actions

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for coin in coins:
            # Check if the coin is not already chosen and the total sum with the new coin does not exceed the target sum
            if coin not in actions and total_sum + coin <= target_sum:
                # Check if the coin follows the rules of being even if smaller than the previous coin, and odd if larger or equal to the previous coin
                if (coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0):
                    # Calculate the tax for the current coin
                    tax = tax_values[coin]
                    # Generate the new state
                    new_state = (total_sum + coin, coin, tax)
                    # The cost of the new state is the tax of the current coin
                    new_cost = g + tax

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + tax, new_cost, actions + [coin], new_state))
    return None


print(a_star())
