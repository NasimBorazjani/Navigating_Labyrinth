
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, ())
    goal_state = 449

    # Define the coins and their tax values
    coins = [25, 41, 34, 19, 19, 36, 37, 13, 28, 26, 181, 7, 14, 6, 29, 36, 33, 7, 8, 43, 19, 9, 3, 2, 18, 40, 43, 22, 23, 21]
    tax_values = {21: 5, 26: 13, 36: 8, 28: 8, 34: 12, 3: 2, 6: 2, 23: 10, 2: 2, 9: 5, 41: 4, 29: 19, 7: 6, 18: 18, 43: 2, 8: 7, 181: 9, 25: 10, 33: 8, 14: 13, 13: 1, 22: 13, 40: 7, 37: 11, 19: 11}

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state[0] == goal_state:
            return list(state[3])

        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for coin in coins:
            if coin not in state[3]:
                # Check if the new state would be valid, ie the sum of the coins chosen so far and the new coin does not exceed the goal sum, and the new coin follows the even-odd rule
                if state[0] + coin <= goal_state and (coin >= state[1] and coin % 2 == 1 or coin < state[1] and coin % 2 == 0):
                    # Generate the new state
                    new_state = (state[0] + coin, coin, state[2] + tax_values[coin], state[3] + (coin,))
                    # The cost so far is the sum of the tax values of the coins chosen, as our objective is to minimize the total tax paid
                    new_cost = g + tax_values[coin]

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the remaining sum to reach the goal state
    # The heuristic is admissible because it never overestimates the cost to reach the goal state, as the remaining sum is always a lower bound on the remaining tax to be paid
    # The heuristic is consistent because the cost of choosing a coin is always greater than or equal to the decrease in the remaining sum, if the coin is chosen
    return goal - state[0]

print(a_star())
