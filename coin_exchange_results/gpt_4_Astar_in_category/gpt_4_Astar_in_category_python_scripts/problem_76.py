
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, ())
    goal_sum = 403

    # Define the coins and their tax values
    coins = [8, 8, 6, 36, 7, 36, 33, 3, 31, 17, 21, 28, 41, 17, 23, 16, 39, 2, 3, 40, 23, 20, 5, 30, 8, 28, 17, 34, 38, 26, 16, 21, 15, 21, 11, 33, 5, 33, 2, 27, 26, 21, 14, 13, 7, 23]
    tax = {28: 16, 5: 1, 3: 3, 40: 18, 33: 20, 34: 12, 20: 4, 39: 13, 2: 2, 31: 11, 36: 2, 17: 14, 7: 1, 14: 6, 23: 12, 8: 1, 30: 15, 27: 13, 15: 2, 21: 3, 11: 6, 26: 14, 41: 2, 38: 10, 6: 5, 16: 4, 13: 11}

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # If the current state is the goal state, return the actions taken
        if state[0] == goal_sum:
            return actions

        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for coin in coins:
            # Check if the new state would be valid, ie the sum of the coins chosen so far and the new coin does not exceed the goal sum
            # And the coin chosen is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
            if state[0] + coin <= goal_sum and (coin < state[1] and coin % 2 == 0 or coin >= state[1] and coin % 2 == 1):
                # Generate the new state
                new_state = (state[0] + coin, coin, state[2] + tax[coin], state[3] + (coin,))
                # The cost so far is the sum of the tax values of the coins chosen, as the task is to minimize the total tax paid
                new_cost = g + tax[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The heuristic is the remaining sum to reach the goal, as the task is to minimize the total tax paid, thus the heuristic is 0
                    heapq.heappush(queue, (new_cost, new_cost, actions + [coin], new_state))

    return None

print(a_star())
