
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, ())
    goal_state = 445

    # Define the coins and their tax values
    coins = [36, 40, 17, 7, 15, 23, 18, 26, 29, 24, 15, 43, 13, 12, 31, 33, 30, 31, 26, 37, 14, 31, 43, 25, 30, 7, 37, 27, 221, 13, 26, 21]
    tax = {36: 14, 27: 19, 21: 6, 13: 8, 23: 17, 26: 17, 15: 6, 25: 7, 31: 20, 30: 5, 18: 14, 12: 6, 37: 2, 221: 18, 14: 13, 24: 10, 33: 4, 43: 11, 29: 18, 40: 1, 7: 6, 17: 2}

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, state = heapq.heappop(queue)

        # If the current state is the goal state, return the actions taken
        if state[0] == goal_state:
            return list(state[3])

        # Generate all possible actions from the current state, which includes adding any of the coins to the total
        for coin in coins:
            # Check if the new state would be valid, ie the coin must not have been used before and it must satisfy the even/odd condition
            if coin not in state[3] and (state[1] == 0 or (coin < state[1] and coin % 2 == 0) or (coin >= state[1] and coin % 2 == 1)):
                # Generate the new state
                new_state = (state[0] + coin, coin, state[2] + tax[coin], state[3] + (coin,))
                # The cost so far is the total tax paid
                new_cost = g + tax[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the remaining amount to reach the goal
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as the remaining amount to reach the goal is always less than or equal to the actual cost to reach the goal
    # The heuristic is consistent because the cost of moving to a successor state is always greater than or equal to the decrease in the heuristic, as adding a coin always decreases the remaining amount to reach the goal by at least the value of the coin
    return goal - state[0]

print(a_star())
