
import heapq

def a_star():
    # Define the initial state of the problem, which is an empty list of coins
    initial_state = []
    # Define the goal state of the problem, which is a sum of 346
    goal_state = 346
    # Define the list of coins and their tax values
    coins = [2, 27, 9, 80, 20, 81, 13, 24, 16, 6, 26, 12, 3, 26, 20, 8, 16, 8, 20, 22, 9, 34, 23, 8, 12, 34, 4, 6, 22, 19]
    tax_values = {12: 9, 16: 12, 13: 5, 34: 8, 9: 9, 23: 4, 81: 2, 80: 20, 8: 1, 19: 19, 2: 2, 22: 13, 20: 7, 26: 11, 4: 1, 6: 2, 27: 4, 3: 1, 24: 12}
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
            # Check if the new state would be valid, ie the sum of the coins in the new state must not exceed the goal sum and the coin must satisfy the even-odd condition
            if sum(state) + coin <= goal_state and (not state or (state[-1] <= coin and coin % 2 == 1) or (state[-1] > coin and coin % 2 == 0)):
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
    # An admissible and consistent heuristic is the difference between the goal sum and the current sum
    # The heuristic is admissible because it never overestimates the cost to reach the goal, as the cost of adding a coin to the state is always greater than or equal to the difference between the goal sum and the current sum
    # The heuristic is consistent because the cost of moving to a successor state is always greater than or equal to the decrease in the heuristic, as the cost of adding a coin to the state is always greater than or equal to the value of the coin
    return goal - sum(state)

print(a_star())
