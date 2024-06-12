
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, 0)
    goal_state = 289

    # Define the coins and their tax values
    coins = [25, 22, 26, 12, 18, 12, 5, 6, 6, 21, 28, 26, 6, 26, 9, 11, 27, 24, 16, 1, 12, 5, 10, 23, 11, 10, 28, 2, 3, 7, 23, 28, 27, 12, 3, 3, 27, 21, 13, 8, 18, 25, 6, 7, 9, 25, 18, 18, 23, 12, 11, 15, 2, 16]
    tax = {10: 6, 24: 14, 5: 3, 3: 1, 16: 6, 27: 10, 13: 1, 12: 4, 21: 17, 8: 2, 28: 10, 6: 3, 1: 1, 18: 2, 25: 14, 11: 3, 23: 7, 7: 6, 26: 16, 15: 4, 2: 1, 9: 3, 22: 8}

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # If the current state is the goal state, return the actions taken
        if state[0] == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes choosing any of the coins
        for coin in coins:
            # Check if the new state would be valid, ie the sum of the coins chosen so far and the new coin does not exceed the goal sum
            if state[0] + coin <= goal_state:
                # Check if the coin chosen is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
                if (state[1] > coin and coin % 2 == 0) or (state[1] <= coin and coin % 2 == 1):
                    # Generate the new state
                    new_state = (state[0] + coin, coin, state[2] + tax[coin], state[3] + 1)
                    # The cost so far is the sum of the tax values of the coins chosen, as the task is to minimize the total tax paid
                    new_cost = g + tax[coin]

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [coin], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the difference between the goal sum and the sum of the coins chosen so far
    # The heuristic is admissible because it never overestimates the cost to reach the goal, as the minimum tax value for any coin is 1, and thus the minimum cost to reach the goal state from any state is the difference between the goal sum and the sum of the coins chosen so far
    # The heuristic is consistent because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to 1, which is the maximum decrease in the heuristic value, as the sum of the coins chosen so far increases by the value of the coin chosen
    return goal - state[0]

print(a_star())
