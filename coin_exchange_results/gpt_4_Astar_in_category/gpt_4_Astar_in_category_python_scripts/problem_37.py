
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, ())
    goal_sum = 303

    # Define the coins and their tax values
    coins = [22, 15, 4, 23, 19, 3, 5, 28, 22, 27, 13, 18, 14, 11, 22, 20, 27, 24, 21, 13, 25, 11, 6, 2, 30, 29, 4, 16, 3, 13, 3, 28, 28, 20, 15, 27, 4, 18, 20, 5, 16, 21, 25, 24, 23, 15, 22, 26]
    tax = {15: 2, 18: 17, 22: 16, 29: 7, 28: 5, 23: 1, 20: 17, 14: 3, 13: 2, 4: 2, 5: 3, 27: 10, 16: 6, 3: 2, 6: 3, 19: 8, 2: 1, 25: 6, 24: 19, 26: 18, 21: 10, 11: 1, 30: 4}

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
            # And the new coin must satisfy the constraints on the value of the coin relative to the previous coin chosen
            if state[0] + coin <= goal_sum and (state[1] < coin and coin % 2 == 1 or state[1] > coin and coin % 2 == 0):
                # Generate the new state
                new_state = (state[0] + coin, coin, state[2] + tax[coin], state[3] + (coin,))
                # The cost so far is the sum of the tax values of the coins chosen, as the task is to minimize the total tax paid
                new_cost = g + tax[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, new_state))

    return None

def heuristic(state, goal_sum):
    # An admissible and consistent heuristic for this problem is the difference between the goal sum and the sum of the coins chosen so far
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as each coin chosen increases the sum of the coins and reduces the difference to the goal sum
    # It's consistent because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to the decrease in the difference to the goal sum, if the coin is chosen. Thus h(n) can never be greater than c(n, n’) + h(n’)
    return goal_sum - state[0]

print(a_star())
