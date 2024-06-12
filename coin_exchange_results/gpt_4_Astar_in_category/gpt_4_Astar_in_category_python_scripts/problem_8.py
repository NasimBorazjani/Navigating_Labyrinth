
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, ())
    goal_sum = 214

    # Define the coins and their tax values
    coins = [4, 17, 8, 15, 6, 14, 2, 4, 16, 10, 6, 5, 14, 8, 18, 2, 17, 9, 17, 59, 3, 10, 21, 4, 9, 14, 14, 20, 14, 8, 14, 18, 5, 16, 14, 17, 5, 3]
    tax_values = {15: 6, 5: 5, 17: 1, 14: 4, 2: 2, 8: 2, 10: 9, 59: 9, 16: 8, 4: 3, 18: 10, 20: 11, 21: 8, 6: 6, 9: 9, 3: 3}

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
        if state[0] == goal_sum:
            return list(state[3])

        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for coin in coins:
            # Check if the new state would be valid, ie the sum of the coins chosen so far and the new coin does not exceed the goal sum
            # And the new coin must be smaller than the previous coin and have an even value or be larger than or equal to the previous coin and have an odd value
            if state[0] + coin <= goal_sum and (state[1] > coin and coin % 2 == 0 or state[1] <= coin and coin % 2 == 1):
                # Generate the new state
                new_state = (state[0] + coin, coin, state[2] + tax_values[coin], state[3] + (coin,))
                # The cost so far is the sum of the tax values of the coins chosen, as the task is to minimize the total tax paid
                new_cost = g + tax_values[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The heuristic is the remaining sum to reach the goal, as the task is to minimize the total tax paid, not the number of coins chosen
                    h = goal_sum - new_state[0]
                    heapq.heappush(queue, (new_cost + h, new_cost, new_state))

    return None

print(a_star())
