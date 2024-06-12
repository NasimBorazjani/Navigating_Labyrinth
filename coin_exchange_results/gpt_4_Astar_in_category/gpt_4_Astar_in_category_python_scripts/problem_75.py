
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, ())
    goal_sum = 408

    # Define the coins and their tax values
    coins = [8, 31, 28, 24, 19, 18, 26, 31, 43, 32, 3, 21, 21, 10, 36, 40, 19, 38, 3, 5, 24, 12, 11, 14, 40, 7, 19, 4, 22, 5, 33, 31, 40, 7, 5, 34, 33, 22, 14, 6, 14, 29]
    tax = {31: 12, 40: 17, 32: 19, 26: 14, 12: 1, 5: 3, 36: 1, 33: 5, 3: 2, 6: 1, 34: 19, 18: 18, 8: 7, 21: 11, 43: 20, 22: 20, 4: 4, 11: 6, 28: 20, 7: 3, 38: 13, 24: 12, 19: 16, 10: 7, 14: 9, 29: 3}

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
        if state[1] == goal_sum:
            return list(state[3])

        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for coin in coins:
            # Check if the new state would be valid, ie the sum of the coins chosen so far and the new coin does not exceed the goal sum
            # And the new coin must be smaller than the previous coin and have an even value or be larger than or equal to the previous coin and have an odd value
            if state[1] + coin <= goal_sum and (coin < state[2] and coin % 2 == 0 or coin >= state[2] and coin % 2 == 1):
                # Generate the new state
                new_state = (state[0] + 1, state[1] + coin, coin, state[3] + (coin,))
                # The cost so far is the sum of the tax values of the coins chosen, as the task is to minimize the total tax paid
                new_cost = g + tax[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, new_state))

    return None

def heuristic(state, goal_sum):
    # An admissible and consistent heuristic is the difference between the goal sum and the sum of the coins chosen so far
    # The heuristic is admissible because it never overestimates the cost to reach the goal, as the minimum tax value of a coin is 1 and the minimum number of coins required to reach the goal sum is the difference between the goal sum and the sum of the coins chosen so far
    # The heuristic is consistent because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to 1, which is the maximum decrease in the heuristic value, if the coin chosen does not cause the sum of the coins chosen so far to exceed the goal sum
    return goal_sum - state[1]

print(a_star())
