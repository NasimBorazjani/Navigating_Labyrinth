
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, ())
    goal_state = 342

    # Define the coins and their tax values
    coins = [18, 26, 17, 17, 16, 27, 30, 3, 4, 2, 24, 26, 29, 23, 2, 31, 25, 25, 4, 24, 14, 29, 4, 34, 34, 23, 35, 23, 28, 18, 8, 10, 17, 8, 22, 32]
    tax_values = {27: 14, 14: 1, 18: 3, 22: 9, 10: 8, 3: 2, 32: 20, 35: 16, 8: 3, 30: 20, 25: 18, 4: 3, 28: 12, 26: 16, 29: 2, 24: 20, 16: 6, 17: 3, 31: 9, 2: 2, 23: 17, 34: 17}

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
            if (coin < state[1] and coin % 2 == 0) or (coin >= state[1] and coin % 2 == 1):
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
    # The heuristic is admissible because it never overestimates the cost to reach the goal, as the minimum tax value is 1 and the minimum coin value is 2
    # The heuristic is consistent because the cost of adding a coin to the current sum is always greater than or equal to the decrease in the heuristic, which is the value of the coin
    return goal - state[0]

print(a_star())
