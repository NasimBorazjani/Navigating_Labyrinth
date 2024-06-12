
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, [])
    goal_sum = 215

    # Define the coins and their tax values
    coins = [13, 19, 9, 4, 18, 17, 2, 14, 17, 17, 8, 6, 4, 10, 19, 37, 20, 19, 14, 7, 6, 11, 21, 9, 3, 10, 21, 20, 2, 17, 2]
    tax_values = {14: 2, 18: 9, 11: 10, 9: 6, 10: 9, 13: 10, 37: 9, 6: 5, 2: 2, 4: 1, 8: 3, 19: 10, 17: 7, 7: 6, 3: 3, 21: 3, 20: 4}

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
            return state[3]

        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for coin in coins:
            if coin not in state[3]:
                # Check if the new state would be valid, ie the sum of the coins chosen so far and the new coin does not exceed the goal sum
                # And the new coin is smaller than the previous one and has an even value, or the new coin is larger than or equal to the previous one and has an odd value
                if state[0] + coin <= goal_sum and (state[1] > coin and coin % 2 == 0 or state[1] <= coin and coin % 2 == 1):
                    # Generate the new state
                    new_state = (state[0] + coin, coin, state[2] + tax_values[coin], state[3] + [coin])
                    # The cost so far is the sum of the tax values of the coins chosen, as the task is to minimize the total tax paid
                    new_cost = g + tax_values[coin]

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        # The heuristic is the remaining sum to reach the goal, as we are trying to minimize the total tax paid, thus the heuristic is 0
                        heapq.heappush(queue, (new_cost, new_cost, new_state))

    return None

print(a_star())
