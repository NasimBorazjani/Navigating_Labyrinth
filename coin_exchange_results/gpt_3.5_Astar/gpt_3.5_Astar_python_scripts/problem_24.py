
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [25, 29, 8, 11, 8, 25, 20, 16, 6, 4, 98, 7, 28, 24, 27, 16, 23, 26, 26, 99, 2, 7, 22, 7, 5, 24, 2]
    tax_values = {24: 5, 26: 16, 28: 20, 2: 1, 22: 16, 25: 11, 27: 7, 11: 4, 6: 3, 99: 17, 8: 5, 7: 5, 5: 3, 23: 5, 4: 4, 98: 16, 16: 3, 29: 5, 20: 19}
    
    # Encoding other variables given in the problem statement
    target_sum = 305
    coins.sort(reverse=True)  # Sort the coins in descending order to prioritize larger coins first
    num_coins = len(coins)

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0  # Initialize the cost to reach the initial state as 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen to get to each state in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], (0, 0, 0))]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If the current state is the goal state, return the coins chosen
        if state[0] == target_sum:
            return actions

        # Generate all possible actions from the current state, which includes choosing the next coin in the list
        for i in range(state[1], num_coins):
            coin = coins[i]
            # Check if the new state would be valid, ie if the sum of the coins chosen so far plus the new coin does not exceed the target sum
            if state[0] + coin <= target_sum:
                # Check if the coin chosen follows the tax rules
                if (i == 0 or (coin < coins[i - 1] and coin % 2 == 0) or (coin >= coins[i - 1] and coin % 2 != 0)):
                    # Generate the new state
                    new_state = (state[0] + coin, i + 1, state[2] + tax_values[coin])
                    # The cost so far is the total tax paid so far
                    new_cost = g + tax_values[coin]

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + new_cost, new_cost, actions + [coin], new_state))

    return None


print(a_star())
