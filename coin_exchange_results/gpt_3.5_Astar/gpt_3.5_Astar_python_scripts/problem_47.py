
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [18, 26, 17, 17, 16, 27, 30, 3, 4, 2, 24, 26, 29, 23, 2, 31, 25, 25, 4, 24, 14, 29, 4, 34, 34, 23, 35, 23, 28, 18, 8, 10, 17, 8, 22, 32]
    tax_values = {27: 14, 14: 1, 18: 3, 22: 9, 10: 8, 3: 2, 32: 20, 35: 16, 8: 3, 30: 20, 25: 18, 4: 3, 28: 12, 26: 16, 29: 2, 24: 20, 16: 6, 17: 3, 31: 9, 2: 2, 23: 17, 34: 17}
    target_sum = 342

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
            # Check if the coin can be chosen based on the given conditions
            if (coin % 2 == 0 and coin >= state[1]) or (coin % 2 != 0 and coin < state[1]):
                # Calculate the new total value and tax paid
                new_total = state[0] + coin
                new_tax = state[2] + tax_values[coin]
                # Generate the new state
                new_state = (new_total, coin, new_tax)
                # The cost of the new state is the total tax paid so far
                new_cost = new_tax

                if new_total <= target_sum and (new_state not in visited_costs or new_cost < visited_costs[new_state]):
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + new_tax, new_cost, actions + [coin], new_state))

    return None


print(a_star())
