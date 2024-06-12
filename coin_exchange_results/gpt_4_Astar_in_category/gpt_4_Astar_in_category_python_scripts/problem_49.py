
import heapq

def a_star():
    # Define the initial state of the problem, which is an empty list of coins
    initial_state = []
    # Define the goal state of the problem, which is a list of coins that sum up to 324
    goal_sum = 324
    # Define the list of coins and their tax values
    coins = [18, 20, 11, 6, 81, 3, 9, 5, 14, 19, 30, 2, 19, 3, 9, 22, 21, 29, 6, 25, 10, 18, 27, 26, 25, 13, 15, 16, 3, 5, 23, 26, 25, 31, 15, 12]
    tax_values = {11: 6, 6: 3, 16: 11, 23: 16, 18: 3, 31: 4, 9: 2, 3: 1, 22: 10, 10: 1, 30: 4, 81: 14, 2: 1, 14: 1, 13: 11, 15: 7, 19: 16, 25: 6, 12: 12, 29: 11, 26: 9, 5: 1, 27: 15, 20: 7, 21: 14}
    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[tuple(initial_state)] = 0
    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [], initial_state)]
    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)
        # If the sum of the coins in the current state is equal to the goal sum, return the actions taken to reach this state
        if sum(state) == goal_sum:
            return actions
        # Generate all possible actions from the current state, which includes adding any of the remaining coins to the current state
        for coin in coins:
            # Check if the new state would be valid, ie the coin must not already be in the state, and the sum of the coins in the new state must not exceed the goal sum
            if coin not in state and sum(state) + coin <= goal_sum:
                # Check if the coin is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
                if not state or (coin < state[-1] and coin % 2 == 0) or (coin >= state[-1] and coin % 2 == 1):
                    # The action is valid, generate the new state
                    new_state = state + [coin]
                    # The cost so far is the sum of the tax values of the coins in the state
                    new_cost = g + tax_values[coin]
                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if tuple(new_state) not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                        visited_costs[tuple(new_state)] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))
    return None

def heuristic(state, goal_sum):
    # An admissible and consistent heuristic is the difference between the goal sum and the sum of the coins in the current state
    # The heuristic is admissible because it never overestimates the cost to reach the goal, as the sum of the coins in any state can never exceed the goal sum
    # The heuristic is consistent because the cost of adding a coin to the state is always less than or equal to the decrease in the heuristic, which is the value of the coin
    return goal_sum - sum(state)

print(a_star())
