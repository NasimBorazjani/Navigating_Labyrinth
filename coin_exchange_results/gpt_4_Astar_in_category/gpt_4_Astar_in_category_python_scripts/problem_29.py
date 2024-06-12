
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, 0)
    goal_state = 295

    # Define the coins and their tax values
    coins = [5, 21, 4, 18, 17, 13, 27, 10, 27, 21, 25, 22, 27, 29, 28, 15, 16, 12, 7, 19, 8, 19, 9, 21, 29, 15, 15, 23, 8, 13, 20, 9, 13, 16, 3, 14, 11, 15, 2, 23, 18, 4]
    tax_values = {14: 2, 12: 11, 20: 5, 4: 2, 23: 12, 28: 1, 25: 8, 27: 3, 19: 1, 21: 6, 16: 2, 29: 7, 13: 5, 17: 2, 22: 15, 10: 1, 15: 1, 3: 2, 8: 5, 5: 4, 9: 1, 7: 2, 2: 2, 18: 17, 11: 1}

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state[0] == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes adding any of the coins to the total
        for coin in coins:
            # Check if the new state would be valid, ie the coin must be smaller than the previous one and have an even value, or larger than or equal to the previous coin and have an odd value
            if (coin < state[1] and coin % 2 == 0) or (coin >= state[1] and coin % 2 == 1):
                # Generate the new state
                new_state = (state[0] + coin, coin, state[2] + 1, state[3] + tax_values[coin])
                # The cost so far is the total tax paid
                new_cost = g + tax_values[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [coin], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the difference between the goal state and the current state
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as the cost of adding a coin to the total is always greater than or equal to 1
    # The heuristic is consistent because the cost of moving to a successor state is always 1, which is exactly the decrease in the heuristic, if the successor state is closer to the goal state
    return goal - state[0]

print(a_star())
