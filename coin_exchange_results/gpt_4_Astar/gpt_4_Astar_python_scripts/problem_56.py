
import heapq

def a_star():
    # Define the initial state of the problem
    initial_state = (0, 0, 0, 0, [])
    # Define the goal state of the problem
    goal_sum = 355
    # Define the coins and their tax values
    coins = [4, 33, 14, 32, 9, 32, 2, 35, 25, 10, 11, 6, 8, 26, 10, 25, 34, 21, 13, 15, 3, 15, 25, 3, 16, 3, 2, 25, 15, 23, 31, 35, 13, 14, 5, 7, 2, 18, 10, 8, 25, 30, 13, 35, 3, 26, 33, 2, 5, 26, 26, 28, 6]
    tax_values = {26: 4, 34: 4, 7: 5, 28: 11, 35: 8, 18: 13, 25: 19, 14: 10, 23: 7, 6: 1, 10: 5, 21: 8, 13: 13, 2: 1, 3: 1, 30: 5, 4: 4, 31: 18, 11: 3, 9: 1, 8: 3, 5: 3, 32: 5, 15: 15, 33: 18, 16: 4}
    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0
    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, 0, 0, [])]
    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, last_coin, current_sum, actions = heapq.heappop(queue)
        # If the current state is the goal state, return the actions that led to this state
        if current_sum == goal_sum:
            return actions
        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for coin in coins:
            # Check if the new state would be valid, ie if the coin is smaller than the last coin chosen, it must have an even value, otherwise, if the coin is larger than or equal to the last coin chosen, it must have an odd value
            if (coin < last_coin and coin % 2 == 0) or (coin >= last_coin and coin % 2 == 1):
                # Generate the new state
                new_state = (g + tax_values[coin], g + tax_values[coin], coin, current_sum + coin, actions + [coin])
                # The cost so far is the sum of the tax values of the coins chosen
                new_cost = g + tax_values[coin]
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, new_state)
    return None

print(a_star())
