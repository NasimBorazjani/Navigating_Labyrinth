
import heapq

def a_star():
    # Define the initial state of the problem
    initial_state = (0, 0, 0, 0, [])
    # Define the goal state of the problem
    goal_sum = 303
    # Define the coins and their tax values
    coins = [22, 15, 4, 23, 19, 3, 5, 28, 22, 27, 13, 18, 14, 11, 22, 20, 27, 24, 21, 13, 25, 11, 6, 2, 30, 29, 4, 16, 3, 13, 3, 28, 28, 20, 15, 27, 4, 18, 20, 5, 16, 21, 25, 24, 23, 15, 22, 26]
    tax_values = {15: 2, 18: 17, 22: 16, 29: 7, 28: 5, 23: 1, 20: 17, 14: 3, 13: 2, 4: 2, 5: 3, 27: 10, 16: 6, 3: 2, 6: 3, 19: 8, 2: 1, 25: 6, 24: 19, 26: 18, 21: 10, 11: 1, 30: 4}
    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0
    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, initial_state)]
    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, state = heapq.heappop(queue)
        # If the current state is the goal state, return the coins chosen
        if state[0] == goal_sum:
            return state[4]
        # Generate all possible actions from the current state, which includes choosing each of the remaining coins
        for coin in coins:
            # Check if the new state would be valid, ie if the sum of the coins chosen so far and the new coin does not exceed the goal sum, and if the new coin is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
            if state[0] + coin <= goal_sum and (coin < state[1] and coin % 2 == 0 or coin >= state[1] and coin % 2 == 1):
                # Generate the new state
                new_state = (state[0] + coin, coin, state[2] + tax_values[coin], state[3] + 1, state[4] + [coin])
                # The cost so far is the sum of the tax values of the coins chosen, as our objective is to minimize the total tax paid
                new_cost = g + tax_values[coin]
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The heuristic is the remaining sum to reach the goal, as we are trying to minimize the total tax paid
                    h = goal_sum - new_state[0]
                    heapq.heappush(queue, (g + h, new_cost, new_state))
    return None

print(a_star())
