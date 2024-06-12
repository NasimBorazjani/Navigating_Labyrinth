
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, 0)
    goal_state = 250

    # Define the coins and their tax values
    coins = [20, 25, 10, 4, 13, 3, 10, 17, 5, 25, 17, 2, 19, 24, 25, 10, 19, 8, 2, 20, 15, 84, 23, 87, 19, 8, 12, 17, 23, 6]
    tax_values = {12: 12, 19: 8, 84: 20, 24: 1, 5: 1, 3: 1, 4: 2, 87: 7, 10: 5, 25: 7, 6: 5, 20: 5, 15: 7, 23: 17, 13: 4, 17: 16, 2: 1, 8: 5}

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # If the current state is the goal state, return the actions taken
        if state[0] == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for coin in coins:
            # Check if the new state would be valid, ie the sum of the coins chosen so far and the new coin does not exceed the goal state
            if state[0] + coin <= goal_state:
                # The new state is valid, generate the new state
                new_state = (state[0] + coin, coin, state[2] + tax_values.get(coin, 0), state[3] + 1)
                # The cost so far is the sum of the tax values of the coins chosen
                new_cost = g + tax_values.get(coin, 0)

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [coin], new_state))

        # Remove the coins that have been used from the list
        coins = [coin for coin in coins if coin != state[1]]

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the difference between the goal state and the sum of the coins chosen so far
    # The heuristic is admissible because it never overestimates the cost to reach the goal state, as the sum of the coins chosen can never exceed the goal state
    # The heuristic is consistent because the cost of choosing a coin is always less than or equal to the decrease in the heuristic, which is the value of the coin chosen
    return goal - state[0]

print(a_star())
