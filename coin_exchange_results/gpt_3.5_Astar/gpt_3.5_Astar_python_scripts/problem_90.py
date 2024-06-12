
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [45, 45, 40, 38, 26, 3, 3, 21, 3, 35, 24, 9, 43, 10, 19, 5, 21, 36, 15, 18, 13, 33, 42, 34, 6, 20, 38, 25, 42, 19, 32, 9, 31, 4, 4, 25, 30, 8]
    tax_values = {13: 7, 9: 1, 38: 9, 19: 4, 31: 18, 25: 18, 40: 13, 4: 2, 15: 8, 45: 2, 10: 10, 20: 18, 5: 3, 35: 12, 30: 8, 8: 5, 21: 5, 43: 12, 32: 10, 6: 2, 24: 18, 3: 2, 33: 7, 42: 4, 36: 10, 34: 6, 26: 5, 18: 6}
    target_sum = 453

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen to get to each state in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], (0, 0, 0))]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Unpack the information encoded in each state
        coins_sum, prev_coin, prev_tax = state

        # If the sum of coins equals the target sum, return the list of coins chosen
        if coins_sum == target_sum:
            return actions

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for coin in coins:
            # Check if the coin is not already chosen and the sum of coins plus the new coin does not exceed the target sum
            if coin not in actions and coins_sum + coin <= target_sum:
                # Check if the coin follows the rules of being even if smaller than the previous coin, and odd if larger or equal to the previous coin
                if (coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0):
                    # Calculate the tax for the new coin
                    new_tax = prev_tax + tax_values[coin]
                    # Generate the new state
                    new_state = (coins_sum + coin, coin, new_tax)
                    # The cost of the new state is the tax paid for the new coin
                    new_cost = g + tax_values[coin]

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + new_tax, new_cost, actions + [coin], new_state))
    return None


print(a_star())
