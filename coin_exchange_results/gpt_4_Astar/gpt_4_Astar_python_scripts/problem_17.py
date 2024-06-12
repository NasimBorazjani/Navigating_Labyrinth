
import heapq

def a_star():
    # Define the initial state of the problem
    initial_state = (0, 0, 0, [])
    # Define the goal state of the problem
    goal_state = 233
    # Define the coins and their tax values
    coins = [4, 2, 18, 5, 18, 13, 22, 15, 5, 14, 15, 21, 23, 13, 19, 22, 6, 12, 19, 8, 15, 8, 12, 15, 11, 17, 7, 19, 23, 9, 3, 4, 12, 10, 11, 2, 22, 19, 19, 11, 18, 6, 10, 23, 20, 1, 6, 23, 8, 6]
    tax_values = {21: 18, 1: 1, 13: 3, 20: 2, 19: 7, 5: 4, 18: 4, 4: 1, 15: 5, 12: 7, 17: 5, 22: 10, 8: 3, 7: 5, 23: 11, 9: 7, 10: 8, 3: 2, 14: 4, 6: 1, 2: 2, 11: 10}
    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0
    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [], initial_state)]
    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)
        # If the current state is the goal state, return the actions taken to reach it
        if state[0] == goal_state:
            return actions
        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for coin in coins:
            # Check if the new state would be valid, ie if the sum of the coins chosen so far and the new coin does not exceed the goal state
            if state[0] + coin <= goal_state:
                # Generate the new state
                new_state = (state[0] + coin, coin, state[2] + tax_values[coin], state[3] + [coin])
                # The cost so far is the sum of the tax values of the coins chosen
                new_cost = g + tax_values[coin]
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [coin], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the difference between the goal state and the sum of the coins chosen so far
    # The heuristic relaxes the constraint that the coins chosen must be unique and presumes we can choose any coin to reach the goal state
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to 1, the decrease in the heuristic value, if the coin is chosen
    return goal - state[0]

print(a_star())
