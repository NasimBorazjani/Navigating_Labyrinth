
import heapq

def a_star():
    # Define the initial state of the problem, which is an empty list of coins
    initial_state = []
    # Define the goal state of the problem, which is a sum of 445
    goal_state = 445
    # Define the coins and their tax values
    coins = [27, 23, 11, 23, 6, 197, 7, 21, 2, 22, 12, 38, 15, 32, 5, 19, 6, 28, 31, 31, 10, 10, 28, 24, 41, 6, 39, 16, 11, 37, 23, 7, 2]
    tax_values = {41: 14, 23: 15, 31: 19, 21: 18, 22: 2, 6: 3, 11: 5, 12: 11, 37: 10, 7: 2, 32: 19, 28: 10, 16: 12, 2: 2, 197: 7, 39: 18, 19: 18, 15: 4, 10: 9, 5: 4, 27: 10, 38: 3, 24: 5}
    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[tuple(initial_state)] = 0
    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [], initial_state)]
    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)
        # If the current state is the goal state, return the actions taken to reach it
        if sum(state) == goal_state:
            return actions
        # Generate all possible actions from the current state, which includes adding any of the remaining coins to the current state
        for coin in coins:
            # Check if the new state would be valid, ie the coin must be unique and the sum of the coins in the new state must not exceed the goal state
            if coin not in state and sum(state) + coin <= goal_state:
                # Check if the coin is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
                if not state or (coin < state[-1] and coin % 2 == 0) or (coin >= state[-1] and coin % 2 == 1):
                    # The action is valid, generate the new state
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
    # The heuristic is admissible because it never overestimates the cost to reach the goal state, as the remaining cost to reach the goal state is always greater than or equal to the difference between the goal state and the sum of the coins in the current state
    # The heuristic is consistent because the cost of moving from the current state to a successor state is always greater than or equal to the decrease in the heuristic, as the sum of the coins in the successor state is always greater than or equal to the sum of the coins in the current state
    return goal - sum(state)

print(a_star())
