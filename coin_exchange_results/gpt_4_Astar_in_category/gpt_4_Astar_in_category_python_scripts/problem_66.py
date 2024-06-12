
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, tuple(sorted([3, 35, 33, 20, 31, 29, 12, 31, 8, 10, 3, 17, 2, 28, 6, 25, 10, 13, 31, 25, 37, 35, 9, 15, 113, 26, 18, 34, 30], reverse=True)))
    goal_sum = 384
    tax_values = {31: 11, 15: 6, 13: 13, 28: 1, 9: 6, 20: 1, 34: 15, 6: 5, 113: 20, 12: 6, 2: 1, 29: 10, 37: 2, 25: 11, 26: 10, 3: 3, 33: 19, 8: 7, 18: 6, 17: 7, 10: 8, 35: 11, 30: 16}

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

        # Check if the current state is the goal state
        if state[0] == goal_sum:
            return actions

        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for coin in state[3]:
            # Check if the new state would be valid, ie the sum of the coins chosen so far and the new coin does not exceed the goal sum
            # And the new coin must be smaller than the previous one and have an even value, or be larger than or equal to the previous coin and have an odd value
            if state[0] + coin <= goal_sum and (state[1] > coin and coin % 2 == 0 or state[1] <= coin and coin % 2 == 1):
                # Generate the new state
                new_state = (state[0] + coin, coin, state[2] + tax_values.get(coin, 0), tuple([c for c in state[3] if c != coin]))
                # The cost so far is the sum of the tax values of the coins chosen, as the task is to minimize the total tax paid
                new_cost = g + tax_values.get(coin, 0)

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the difference between the goal sum and the sum of the coins chosen so far
    # The heuristic relaxes the constraint that the coins chosen must be unique and presumes we can reach the goal sum by choosing the same coin repeatedly
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to 0, which is exactly the decrease in the heuristic, if the coin is chosen, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the sum of the coins chosen would be equal to the goal sum in the goal state.
    return goal - state[0]

print(a_star())
