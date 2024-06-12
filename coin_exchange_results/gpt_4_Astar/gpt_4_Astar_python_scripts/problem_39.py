
import heapq

def a_star():
    # Define the initial state of the problem
    initial_state = (0, 0, 0, [])
    # Define the goal state of the problem
    goal_state = 273
    # Define the coins and their tax values
    coins = [26, 24, 8, 2, 11, 10, 11, 14, 20, 9, 13, 10, 25, 21, 7, 20, 15, 27, 18, 12, 23, 4, 2, 4, 22, 23, 15, 16, 24, 14, 22, 13, 15, 21, 5, 14, 2, 21, 14, 10, 2, 2, 24, 26, 17, 2, 20, 22, 3, 27, 8, 20, 2, 25, 7]
    tax_values = {24: 18, 14: 4, 15: 10, 23: 15, 26: 12, 22: 4, 17: 8, 5: 2, 18: 2, 16: 3, 11: 3, 2: 1, 27: 9, 3: 3, 10: 5, 20: 4, 4: 2, 21: 4, 12: 1, 8: 6, 13: 2, 7: 2, 9: 6, 25: 15}
    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0
    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, initial_state)]
    # While there are un-visited states
    while queue:
        # Pop the state with the lowest cost from the queue
        _, state = heapq.heappop(queue)
        # If the current state is the goal state, return the coins chosen
        if state[0] == goal_state:
            return state[3]
        # Generate all possible actions from the current state, which includes choosing each of the remaining coins
        for coin in coins:
            # Check if the new state would be valid, ie if the coin is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
            if (state[1] > coin and coin % 2 == 0) or (state[1] <= coin and coin % 2 == 1):
                # Generate the new state
                new_state = (state[0] + coin, coin, state[2] + tax_values[coin], state[3] + [coin])
                # The cost so far is the total tax paid
                new_cost = state[2] + tax_values[coin]
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The heuristic is the remaining sum to reach the goal state
                    h = goal_state - new_state[0]
                    heapq.heappush(queue, (new_cost + h, new_state))
    return None

print(a_star())
