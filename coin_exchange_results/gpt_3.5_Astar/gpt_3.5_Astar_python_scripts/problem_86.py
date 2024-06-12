
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [31, 8, 22, 27, 2, 25, 2, 8, 49, 26, 65, 6, 37, 49, 15, 21, 27, 5, 34, 28, 47, 15, 7, 42, 32, 20, 34, 48, 39, 7, 13]
    tax_values = {7: 1, 65: 16, 21: 18, 25: 18, 15: 14, 31: 15, 6: 2, 37: 2, 5: 1, 22: 1, 8: 7, 26: 2, 2: 1, 32: 8, 27: 2, 13: 8, 39: 17, 28: 11, 47: 6, 42: 10, 34: 15, 20: 8, 48: 11, 49: 13}
    target_sum = 490

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], (0, 0, 0))]

    while queue:
        _, g, coins_chosen, state = heapq.heappop(queue)

        # If the current state is the goal state, return the coins chosen so far
        if state[0] == target_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for i, coin in enumerate(coins):
            new_sum = state[0] + coin
            new_tax = state[1] + tax_values[coin]
            new_odd_even = 1 if coin % 2 == 1 else 0

            # Check if the new state would be valid, ie the sum of the coins chosen so far does not exceed the target sum, the tax is minimized, and the odd-even condition is met
            if new_sum <= target_sum and (new_tax < state[2] or new_tax == state[2] and new_odd_even == 1):
                new_state = (new_sum, new_tax, new_odd_even)
                new_cost = g + tax_values[coin]

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + new_cost, new_cost, coins_chosen + [coin], new_state))

    return None


print(a_star())
