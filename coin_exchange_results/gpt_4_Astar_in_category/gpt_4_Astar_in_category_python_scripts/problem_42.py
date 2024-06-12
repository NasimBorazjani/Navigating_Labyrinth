
import heapq

def a_star():
    # Define the initial state of the problem, which is an empty list of coins
    initial_state = []
    # Define the goal state of the problem, which is a sum of 300
    goal_state = 300
    # Define the list of coins and their tax values
    coins = [24, 10, 24, 3, 21, 7, 21, 26, 8, 14, 24, 5, 13, 10, 25, 6, 9, 4, 18, 4, 15, 4, 10, 23, 6, 13, 26, 20, 8, 10, 29, 27, 27, 20, 2, 15, 9, 9, 25, 8, 2, 27, 5, 22, 19, 26, 2, 29, 12, 9, 6, 12, 2, 15, 5, 16, 3, 29, 19]
    tax_values = {5: 2, 9: 8, 12: 5, 14: 4, 22: 8, 26: 3, 8: 7, 27: 2, 20: 13, 3: 3, 13: 3, 2: 1, 19: 19, 29: 4, 10: 3, 18: 14, 21: 12, 15: 12, 4: 3, 23: 5, 16: 9, 25: 16, 7: 4, 24: 17, 6: 6}

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[tuple(initial_state)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if sum(state) == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes adding any of the coins to the current state
        for coin in coins:
            # Check if the new state would be valid, ie the coin must not already be in the state and the sum of the state and the coin must not exceed the goal state
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
    # An admissible and consistent heuristic is the difference between the goal state and the sum of the state
    # The heuristic is admissible because it never overestimates the cost to reach the goal state, as the sum of the state can never exceed the goal state
    # The heuristic is consistent because the cost of moving to a successor state is always 1, which is exactly the decrease in the heuristic, if the successor state is closer to the goal state
    return goal - sum(state)

print(a_star())
