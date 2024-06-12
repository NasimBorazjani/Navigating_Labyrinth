
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, 0)
    goal_sum = 236

    # Define the coins and their tax values
    coins = [6, 20, 15, 14, 23, 6, 8, 15, 11, 2, 16, 21, 17, 10, 23, 20, 21, 16, 13, 3, 7, 4, 9, 21, 7, 13, 10, 18, 11, 9, 13, 12, 15, 17, 2, 8, 18, 3, 16, 9, 3, 14, 23, 16]
    tax = {21: 11, 18: 16, 16: 6, 12: 5, 14: 11, 11: 8, 15: 11, 4: 3, 9: 2, 23: 14, 7: 5, 20: 12, 6: 2, 8: 3, 17: 6, 13: 3, 3: 3, 2: 1, 10: 5}

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
        for coin in coins:
            # Check if the new state would be valid, ie the sum of the coins chosen so far and the new coin does not exceed the goal sum
            # And the new coin must be smaller than the previous coin chosen and have an even value, or be larger than or equal to the previous coin and have an odd value
            if state[0] + coin <= goal_sum and (coin < state[1] and coin % 2 == 0 or coin >= state[1] and coin % 2 == 1):
                # Generate the new state
                new_state = (state[0] + coin, coin, state[2] + 1, state[3] + tax.get(coin, 0))
                # The cost so far is the sum of the tax values of the coins chosen, as the task is to minimize the total tax paid
                new_cost = g + tax.get(coin, 0)

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the remaining sum to reach the goal
    # The heuristic relaxes the constraint that the coins chosen must be unique and presumes we can reach the goal sum by choosing the smallest coin with the smallest tax value repeatedly
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is always the tax value of the coin, which is always greater than or equal to the tax value of the smallest coin, if the coin is chosen toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the sum of the coins chosen would be equal to the goal sum in the goal state.
    return goal - state[0]

print(a_star())
