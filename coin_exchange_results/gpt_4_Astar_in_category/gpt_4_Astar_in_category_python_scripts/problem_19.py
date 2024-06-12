
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, 0)
    goal_sum = 243

    # Define the coins and their tax values
    coins = [9, 20, 4, 23, 10, 11, 8, 6, 20, 8, 20, 12, 15, 20, 18, 16, 19, 21, 5, 6, 4, 5, 14, 5, 4, 18, 22, 7, 8, 15, 5, 15, 8, 19, 14, 12, 2, 5, 5, 15, 2, 6, 10, 18, 14, 13, 8, 10, 21, 14, 5, 18, 16, 6, 11]
    tax_values = {20: 3, 9: 2, 23: 1, 10: 3, 5: 4, 21: 14, 22: 5, 18: 7, 16: 4, 13: 5, 2: 1, 8: 2, 19: 16, 7: 3, 6: 6, 11: 3, 14: 8, 4: 2, 12: 7, 15: 14}

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
        if state[0] == goal_sum:
            return actions

        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for coin in coins:
            # Check if the new state would be valid, ie the sum of the coins chosen so far and the new coin does not exceed the goal sum
            # And the new coin must be smaller than the previous one and have an even value, or be larger than or equal to the previous coin and have an odd value
            if state[0] + coin <= goal_sum and (coin < state[1] and coin % 2 == 0 or coin >= state[1] and coin % 2 == 1):
                # Generate the new state
                new_state = (state[0] + coin, coin, state[2] + 1, state[3] + tax_values[coin])
                # The cost so far is the sum of the tax values of the coins chosen, as the task is to minimize the total tax paid
                new_cost = g + tax_values[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the difference between the goal sum and the sum of the coins chosen so far
    # The heuristic relaxes the constraint that the coins chosen must be unique and presumes we can choose any coin to reach the goal sum
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to the decrease in the heuristic, if the coin is chosen toward its goal sum, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the difference between the goal sum and the sum of the coins chosen would be 0 in the goal state.
    return goal - state[0]

print(a_star())
