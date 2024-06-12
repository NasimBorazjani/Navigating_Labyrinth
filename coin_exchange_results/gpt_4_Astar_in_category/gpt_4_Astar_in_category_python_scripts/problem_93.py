
import heapq

def a_star():
    # Define the initial state of the problem, which is an empty list of coins
    initial_state = []
    # Define the goal state of the problem, which is a sum of 471
    goal_state = 471
    # Define the list of coins and their tax values
    coins = [43, 41, 23, 24, 40, 11, 12, 9, 32, 32, 6, 15, 16, 20, 6, 39, 9, 12, 4, 251, 43, 24, 27, 20, 39, 37, 7, 43, 9, 13, 45, 27, 9, 15, 41, 25]
    tax_values = {9: 7, 32: 17, 24: 17, 15: 11, 4: 3, 39: 18, 41: 9, 25: 14, 27: 5, 40: 5, 43: 8, 11: 9, 20: 1, 45: 2, 16: 15, 251: 12, 37: 10, 13: 1, 23: 1, 7: 1, 12: 1, 6: 5}

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[tuple(initial_state)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # If the sum of the coins in the current state is equal to the goal state, return the actions taken
        if sum(state) == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes adding any of the remaining coins to the current state
        for coin in coins:
            # Check if the new state would be valid, ie the coin must not already be in the state, and the sum of the coins in the new state must not exceed the goal state
            if coin not in state and sum(state) + coin <= goal_state:
                # The coin must be smaller than the previous one and have an even value, or be larger than or equal to the previous coin and have an odd value
                if (state and coin < state[-1] and coin % 2 == 0) or (not state or (coin >= state[-1] and coin % 2 == 1)):
                    # Generate the new state
                    new_state = state + [coin]
                    # The cost so far is the sum of the tax values of the coins in the state
                    new_cost = g + tax_values[coin]

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if tuple(new_state) not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                        visited_costs[tuple(new_state)] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [coin], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the difference between the goal state and the sum of the coins in the current state
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as the sum of the coins in the state can never exceed the goal state
    # It's consistent because the cost of adding a coin to the state is always less than or equal to the decrease in the heuristic, which is the value of the coin
    return goal - sum(state)

print(a_star())
