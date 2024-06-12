
import heapq

def a_star():
    # Define the initial state of the problem, which is an empty list of coins
    initial_state = []
    # Define the goal state of the problem, which is a list of coins that sum up to 294
    goal_sum = 294
    # Define the list of coins and their tax values
    coins = [46, 10, 4, 8, 2, 22, 26, 49, 4, 19, 2, 9, 23, 28, 6, 21, 9, 14, 15, 21, 22, 3, 14, 2, 28, 13, 20, 2, 28, 7, 16, 27, 22, 18, 28, 10, 14, 14, 4, 20, 18]
    tax_values = {21: 14, 19: 16, 4: 3, 23: 10, 10: 3, 18: 7, 9: 3, 27: 13, 20: 12, 13: 9, 26: 17, 3: 3, 6: 6, 49: 16, 2: 2, 15: 7, 28: 13, 46: 10, 8: 3, 7: 6, 22: 20, 14: 5, 16: 8}

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[tuple(initial_state)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # If the sum of the coins in the current state equals the goal sum, return the actions taken
        if sum(state) == goal_sum:
            return actions

        # Generate all possible actions from the current state, which includes adding any of the remaining coins to the current state
        for coin in coins:
            # Check if the new state would be valid, ie the sum of the coins in the new state must not exceed the goal sum
            # And the coin must satisfy the constraints on the value of the coin relative to the previous coin chosen
            if sum(state) + coin <= goal_sum and (not state or (state[-1] <= coin and coin % 2 == 1) or (state[-1] > coin and coin % 2 == 0)):
                # Generate the new state
                new_state = state + [coin]
                # The cost so far is the sum of the tax values of the coins in the new state
                new_cost = g + tax_values[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if tuple(new_state) not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                    visited_costs[tuple(new_state)] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))
    return None

def heuristic(state, goal_sum):
    # An admissible and consistent heuristic for this problem is the difference between the goal sum and the sum of the coins in the current state
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as the sum of the coins in any state can never exceed the goal sum
    # The heuristic is consistent because the cost of adding a coin to the current state is the tax value of the coin, which is always greater than or equal to the decrease in the heuristic cost, if the coin is added to the state
    return goal_sum - sum(state)

print(a_star())
