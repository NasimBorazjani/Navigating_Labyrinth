
import heapq

def a_star():
    # Define the initial state of the problem, which is an empty list of coins
    initial_state = []
    # Define the goal state of the problem, which is a sum of 351
    goal_state = 351
    # Define the list of coins and their tax values
    coins = [30, 4, 10, 25, 2, 20, 23, 22, 29, 13, 21, 23, 23, 24, 3, 26, 29, 27, 15, 18, 28, 10, 22, 24, 2, 22, 13, 32, 8, 28, 31, 13, 27, 6, 35, 2, 20, 25, 24, 2, 16, 31, 3, 5, 23, 32, 24, 20, 13, 7, 11, 12]
    tax_values = {10: 8, 32: 8, 25: 5, 7: 2, 30: 9, 18: 3, 5: 2, 35: 14, 2: 1, 15: 10, 12: 6, 29: 14, 23: 12, 31: 14, 11: 3, 8: 7, 21: 5, 13: 3, 28: 3, 6: 1, 3: 2, 4: 2, 22: 5, 16: 9, 24: 4, 27: 16, 26: 6, 20: 20}

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[tuple(initial_state)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # If the sum of the coins in the current state equals the goal state, return the actions taken
        if sum(state) == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes adding any of the remaining coins to the current state
        for coin in coins:
            # Check if the new state would be valid, ie the coin must not already be in the state, and the sum of the coins in the new state must not exceed the goal state
            if coin not in state and sum(state) + coin <= goal_state:
                # If the coin is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
                if (not state or coin < state[-1]) and coin % 2 == 0 or (state and coin >= state[-1]) and coin % 2 == 1:
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
    # An admissible and consistent heuristic is the difference between the goal state and the sum of the coins in the current state
    # The heuristic is admissible because it never overestimates the cost to reach the goal state, as the sum of the coins in the state can never exceed the goal state
    # The heuristic is consistent because the cost of adding a coin to the state is always less than or equal to the decrease in the heuristic, which is the value of the coin
    return goal - sum(state)

print(a_star())
