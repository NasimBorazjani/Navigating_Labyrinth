
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, tuple(sorted([10, 16, 2, 18, 10, 16, 17, 32, 18, 33, 23, 20, 21, 25, 32, 24, 10, 27, 13, 27, 30, 13, 19, 20, 4, 5, 15, 8, 8, 34, 21, 14, 3, 20, 10, 18, 3, 14, 28, 6, 4, 8, 15, 4, 30, 30, 12, 20, 14, 10])))
    goal_sum = 357
    tax_values = {30: 12, 20: 19, 16: 7, 24: 14, 12: 3, 13: 4, 8: 2, 2: 1, 21: 2, 23: 12, 34: 13, 27: 16, 3: 3, 28: 3, 14: 13, 6: 4, 33: 17, 10: 8, 5: 3, 15: 12, 4: 2, 18: 2, 19: 5, 17: 1, 32: 2, 25: 12}

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen to get to each state in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state[1] == goal_sum:
            return actions

        # Generate all valid actions from the current state, which includes choosing any of the remaining coins
        for coin in state[3]:
            # Check if the new state would be valid, ie the sum of the coins chosen so far and the new coin must not exceed the goal sum
            # And the new coin must be smaller than the previous coin chosen and have an even value, or be larger than or equal to the previous coin chosen and have an odd value
            if state[1] + coin <= goal_sum and (coin < state[2] and coin % 2 == 0 or coin >= state[2] and coin % 2 == 1):
                # Generate the new state
                new_state = (state[0] + tax_values[coin], state[1] + coin, coin, tuple([c for c in state[3] if c != coin]))
                # The cost so far is the sum of the tax values of the coins chosen, as our objective is to minimize the total tax paid
                new_cost = g + tax_values[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))

    return None

def heuristic(state, goal_sum):
    # An admissible and consistent heuristic is the difference between the goal sum and the sum of the coins chosen so far
    # The heuristic relaxes the constraint that the coins chosen must be unique and presumes we can choose any coin to reach the goal sum
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to the decrease in the heuristic, if the coin is chosen toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the difference between the goal sum and the sum of the coins chosen would be 0 in the goal state.
    return goal_sum - state[1]

print(a_star())
