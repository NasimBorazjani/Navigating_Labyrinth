
import heapq

def a_star():
    # Define the initial state of the problem, which is an empty list of coins
    initial_state = []
    # Define the goal state of the problem, which is a list of coins that sum up to 427
    goal_sum = 427
    # Define the list of coins and their tax values
    coins = [5, 29, 12, 96, 4, 13, 8, 23, 14, 25, 18, 23, 36, 32, 17, 37, 34, 7, 9, 32, 29, 37, 30, 40, 99, 9, 2, 40, 35, 14]
    tax_values = {14: 4, 4: 2, 18: 12, 23: 12, 36: 15, 5: 1, 12: 3, 13: 13, 9: 7, 32: 8, 99: 16, 8: 7, 96: 17, 35: 13, 29: 19, 30: 19, 7: 1, 34: 16, 37: 15, 2: 2, 17: 3, 40: 18, 25: 9}
    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[tuple(initial_state)] = 0
    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [], initial_state)]
    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)
        # If the current state is the goal state, return the actions taken to reach it
        if sum(state) == goal_sum:
            return actions
        # Generate all possible actions from the current state, which includes adding any of the coins to the current state
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
    # An admissible and consistent heuristic is the difference between the goal sum and the sum of the coins in the state
    # The heuristic is admissible because it never overestimates the cost to reach the goal, as the sum of the coins in the state can only increase
    # The heuristic is consistent because the cost of adding a coin to the state is the tax value of the coin, which is always greater than or equal to the decrease in the heuristic, ie the increase in the sum of the coins in the state
    return goal_sum - sum(state)

print(a_star())
