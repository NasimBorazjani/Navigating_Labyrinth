
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, ())
    goal_state = 411

    # Define the coins and their tax values
    coins = [12, 5, 22, 10, 4, 26, 26, 31, 13, 30, 37, 14, 14, 38, 9, 30, 7, 16, 21, 37, 4, 24, 10, 41, 13, 16, 3, 40, 24, 117, 34, 7, 11, 14, 28, 37, 21, 32, 2, 15, 5, 13, 3, 28, 31, 22, 30, 32, 38, 25, 10, 4, 30]
    tax = {10: 7, 2: 2, 14: 12, 15: 8, 13: 10, 9: 1, 38: 17, 117: 2, 16: 13, 25: 11, 31: 3, 32: 2, 22: 10, 7: 4, 12: 3, 4: 1, 40: 2, 34: 4, 41: 9, 30: 8, 11: 10, 26: 13, 28: 6, 3: 2, 37: 17, 5: 5, 21: 3, 24: 13}

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
        if state[1] == goal_state:
            return list(state[3])

        # Generate all possible actions from the current state, which includes adding any of the coins to the current sum
        for coin in coins:
            # Check if the new state would be valid, ie the sum of the coins does not exceed the goal state and the coin follows the rules of the problem
            if state[1] + coin <= goal_state and (coin % 2 == 1 if coin >= state[2] else coin % 2 == 0):
                # Generate the new state
                new_state = (state[0] + 1, state[1] + coin, coin, state[3] + (coin,))
                # The cost so far is the sum of the tax values of the coins chosen
                new_cost = g + tax[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the difference between the goal state and the current sum of the coins
    # This heuristic is admissible because it never overestimates the cost to reach the goal state, as we cannot reach the goal state without adding at least this amount of coins
    # This heuristic is consistent because the cost of moving to a successor state is always greater than or equal to the decrease in the heuristic, as we are always adding coins to the current sum
    return goal - state[1]

print(a_star())
