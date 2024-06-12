
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, ())
    goal_state = 337

    # Define the coins and their tax values
    coins = [21, 10, 19, 6, 20, 7, 23, 18, 4, 15, 4, 13, 2, 5, 32, 28, 113, 3, 9, 9, 11, 21, 112, 6, 6, 11, 29]
    tax_values = {10: 7, 5: 3, 11: 3, 23: 2, 21: 13, 19: 3, 18: 18, 29: 20, 3: 2, 9: 7, 20: 18, 6: 2, 112: 20, 2: 1, 4: 4, 7: 4, 32: 1, 15: 8, 13: 10, 28: 17, 113: 18}

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state[0] == goal_state:
            return list(state[3])

        # Generate all possible actions from the current state, which includes choosing any of the coins
        for coin in coins:
            # Check if the new state would be valid, ie the sum of the coins chosen so far and the new coin does not exceed the goal state
            if state[0] + coin <= goal_state:
                # The new state is valid, generate the new state
                new_state = (state[0] + coin, coin, state[2] + tax_values.get(coin, 0), state[3] + (coin,))
                # The cost so far is the sum of the tax values of the coins chosen
                new_cost = g + tax_values.get(coin, 0)

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The heuristic is the remaining sum to reach the goal state, as we are trying to minimize the tax paid
                    h = goal_state - new_state[0]
                    heapq.heappush(queue, (new_cost + h, new_cost, new_state))

    return None

print(a_star())
