
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, ())
    goal_state = 322

    # Define the coins and their tax values
    coins = [25, 22, 28, 23, 5, 14, 28, 14, 20, 6, 22, 1, 25, 18, 30, 10, 19, 12, 17, 17, 6, 28, 21, 28, 21, 2, 20, 2, 19, 14, 31, 31, 14, 7, 20, 13, 7, 18, 22, 15, 6, 6, 21, 9, 18, 11, 20, 26, 15]
    tax_values = {11: 1, 14: 4, 7: 2, 25: 4, 12: 5, 20: 19, 13: 6, 15: 11, 30: 18, 1: 1, 2: 2, 31: 6, 10: 2, 23: 1, 6: 2, 21: 18, 18: 8, 28: 15, 17: 5, 26: 6, 22: 6, 9: 1, 19: 2, 5: 4}

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, state = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state[0] == goal_state:
            return list(state[3])

        # Generate all valid actions from the current state, which includes adding any of the coins to the current sum
        for coin in coins:
            # Check if the coin is valid, ie if the coin is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
            if (state[1] > coin and coin % 2 == 0) or (state[1] <= coin and coin % 2 == 1):
                # The action is valid, generate the new state
                new_state = (state[0] + coin, coin, state[2] + tax_values[coin], state[3] + (coin,))

                # The cost so far is the sum of the tax values of the coins chosen
                new_cost = g + tax_values[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the difference between the goal sum and the current sum
    # The heuristic relaxes the constraint that the coins must be unique and presumes we can reach the goal sum by adding the smallest possible coin (1) to the current sum
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of adding a coin to the current sum is always the tax value of the coin, which is always greater than or equal to 1 (the tax value of the smallest coin), which is exactly the decrease in the heuristic, if the coin is added to the current sum, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the difference between the goal sum and the current sum would be 0 in the goal state.
    return goal - state[0]

print(a_star())
