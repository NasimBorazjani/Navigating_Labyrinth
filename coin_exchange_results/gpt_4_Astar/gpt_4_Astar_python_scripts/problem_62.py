
import heapq

def a_star():
    # Define the initial state of the problem
    initial_state = (0, 0, 0, 0, [])
    # Define the goal state of the problem
    goal_state = 356
    # Define the coins and their tax values
    coins = [35, 14, 9, 23, 25, 24, 21, 20, 12, 17, 12, 5, 2, 17, 25, 25, 26, 31, 7, 21, 10, 2, 27, 19, 32, 29, 11, 33, 3, 27, 17, 3, 18, 14, 2, 32, 14, 21, 12, 8, 3, 34, 13, 12, 2, 23, 13, 3, 3, 31, 23, 23, 6, 30, 30, 11, 21]
    tax_values = {3: 1, 32: 16, 6: 5, 20: 13, 13: 5, 31: 9, 23: 10, 35: 14, 24: 17, 11: 11, 9: 1, 12: 10, 5: 3, 8: 5, 34: 11, 17: 16, 25: 9, 26: 6, 30: 17, 27: 17, 7: 2, 18: 17, 33: 5, 14: 2, 29: 14, 10: 3, 2: 2, 21: 12, 19: 9}
    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0
    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, initial_state)]
    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, state = heapq.heappop(queue)
        # If the current state is the goal state, return the actions taken to reach the goal state
        if state[0] == goal_state:
            return state[4]
        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for i in range(state[1], len(coins)):
            # Check if the new state would be valid, ie if the coin is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
            if (state[2] > coins[i] and coins[i] % 2 == 0) or (state[2] <= coins[i] and coins[i] % 2 == 1):
                # Generate the new state
                new_state = (state[0] + coins[i], i + 1, coins[i], state[3] + tax_values[coins[i]], state[4] + [coins[i]])
                # The cost so far is the total tax paid, as our objective is to minimize the total tax paid
                new_cost = g + tax_values[coins[i]]
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the difference between the goal state and the current state
    # The heuristic relaxes the constraints that the coins must be unique and that the coins must satisfy the even-odd rule, and presumes we can reach the goal state by choosing any coin
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to 1, the decrease in the difference between the goal state and the current state, if the coin is chosen
    return goal - state[0]

print(a_star())
