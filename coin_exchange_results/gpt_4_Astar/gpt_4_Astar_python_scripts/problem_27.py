
import heapq

def a_star():
    # Define the initial state of the problem
    initial_state = (0, 0, 0, 0, [])
    # Define the goal state of the problem
    goal_state = 301
    # Define the coins and their tax values
    coins = [22, 4, 12, 26, 4, 9, 4, 28, 28, 8, 28, 19, 15, 20, 9, 161, 11, 28, 17, 10, 25, 15, 7, 28, 21, 24, 10, 13, 22, 4, 10, 14]
    tax_values = {15: 2, 17: 10, 10: 3, 12: 10, 21: 12, 4: 2, 22: 1, 11: 6, 26: 9, 14: 7, 24: 12, 161: 16, 20: 15, 9: 8, 8: 1, 13: 10, 28: 6, 7: 6, 25: 6, 19: 15}
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
        for i in range(len(coins)):
            # Check if the new state would be valid, ie if the coin is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
            if (state[1] > coins[i] and coins[i] % 2 == 0) or (state[1] <= coins[i] and coins[i] % 2 == 1):
                # Generate the new state
                new_state = (state[0] + coins[i], coins[i], state[2] + tax_values[coins[i]], i, state[4] + [coins[i]])
                # The cost so far is the sum of the tax values of the chosen coins
                new_cost = g + tax_values[coins[i]]
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [coins[i]], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the difference between the goal state and the current state
    # The heuristic relaxes the constraints that the coins must be unique and that the coins must satisfy the even/odd condition, and presumes we can choose any coin to reach the goal state
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to 1, the decrease in the difference between the goal state and the current state
    return goal - state[0]

print(a_star())
