
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [3, 6, 9, 10, 13, 15, 18, 5, 21, 19, 12, 15, 5, 9, 4, 16, 8, 4, 7, 7, 7, 2, 16, 14, 18, 3, 89, 21, 12, 10, 7, 14, 4, 11, 6, 20]
    tax_values = {14: 1, 89: 13, 2: 2, 5: 2, 4: 4, 6: 6, 8: 2, 16: 5, 21: 4, 20: 2, 18: 9, 11: 10, 10: 3, 12: 12, 15: 5, 13: 1, 3: 1, 19: 19, 7: 7, 9: 3}
    target_sum = 229

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen to get to each state in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], (0, 0, 0))]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If the current state is the goal state, return the coins chosen
        if state[0] == target_sum:
            return actions

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for i, coin in enumerate(coins):
            new_sum = state[0] + coin
            new_tax = state[1] + tax_values[coin]
            new_odd_even = 1 if coin % 2 != 0 else 0

            # Check if the new state is valid, ie the sum of the coins chosen does not exceed the target sum, the tax is minimized, and the odd-even condition is met
            if new_sum <= target_sum and (new_tax < state[2] or new_tax == state[2] and new_odd_even < state[2]):

                # Generate the new state
                new_state = (new_sum, new_tax, new_odd_even)
                # The cost of the new state is the tax paid for the new coin
                new_cost = g + tax_values[coin]

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + new_cost, new_cost, actions + [coin], new_state))

    return None


print(a_star())
