
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, 0)
    goal_state = 423

    # Define the coins and their tax values
    coins = [28, 11, 40, 15, 21, 6, 20, 6, 12, 22, 8, 18, 34, 24, 22, 30, 35, 41, 6, 39, 5, 15, 19, 8, 26, 38, 11, 29, 31, 14, 37, 28, 8, 11, 28, 27, 38]
    tax_values = {40: 1, 41: 13, 8: 5, 28: 2, 21: 18, 15: 7, 5: 4, 14: 13, 37: 12, 22: 12, 29: 3, 30: 15, 35: 4, 26: 19, 39: 7, 31: 14, 11: 7, 20: 3, 6: 2, 12: 8, 27: 13, 19: 19, 34: 5, 18: 9, 38: 16, 24: 17}

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state[0] == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes choosing any of the coins
        for coin in coins:
            # Check if the new state would be valid, ie the sum of the coins chosen so far and the new coin does not exceed the goal sum
            # And the new coin must satisfy the constraints on the value of the coin based on the value of the previous coin chosen
            if state[0] + coin <= goal_state and ((coin >= state[1] and coin % 2 == 1) or (coin < state[1] and coin % 2 == 0)):
                # Generate the new state
                new_state = (state[0] + coin, coin, state[2] + tax_values[coin], state[3] + 1)
                # The cost so far is the sum of the tax values of the coins chosen, as the task is to minimize the total tax paid
                new_cost = g + tax_values[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [coin], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the difference between the goal sum and the sum of the coins chosen so far
    # The heuristic relaxes the constraints on the value of the coins chosen based on the value of the previous coin chosen and presumes we can choose any coin to reach the goal sum
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to 0, and the heuristic estimate for the goal state is 0, as the difference between the goal sum and the sum of the coins chosen would be 0 in the goal state.
    return goal - state[0]

print(a_star())
