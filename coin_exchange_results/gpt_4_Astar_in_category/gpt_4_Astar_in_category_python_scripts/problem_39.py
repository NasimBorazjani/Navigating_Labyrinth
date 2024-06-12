
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, 0)
    goal_sum = 273

    # Define the coins and their tax values
    coins = [26, 24, 8, 2, 11, 10, 11, 14, 20, 9, 13, 10, 25, 21, 7, 20, 15, 27, 18, 12, 23, 4, 2, 4, 22, 23, 15, 16, 24, 14, 22, 13, 15, 21, 5, 14, 2, 21, 14, 10, 2, 2, 24, 26, 17, 2, 20, 22, 3, 27, 8, 20, 2, 25, 7]
    tax_values = {24: 18, 14: 4, 15: 10, 23: 15, 26: 12, 22: 4, 17: 8, 5: 2, 18: 2, 16: 3, 11: 3, 2: 1, 27: 9, 3: 3, 10: 5, 20: 4, 4: 2, 21: 4, 12: 1, 8: 6, 13: 2, 7: 2, 9: 6, 25: 15}

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state[0] == goal_sum:
            return actions

        # Generate all possible actions from the current state, which includes choosing any of the coins
        for coin in coins:
            # Check if the new state would be valid, ie the sum of the coins chosen so far and the new coin does not exceed the goal sum
            # And the new coin must be smaller than the previous coin and have an even value or be larger than or equal to the previous coin and have an odd value
            if state[0] + coin <= goal_sum and ((coin < state[1] and coin % 2 == 0) or (coin >= state[1] and coin % 2 == 1)):
                # Generate the new state
                new_state = (state[0] + coin, coin, state[2] + tax_values[coin], state[3] + 1)
                # The cost so far is the sum of the tax values of the coins chosen, as the task is to minimize the total tax paid
                new_cost = g + tax_values[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the difference between the goal sum and the sum of the coins chosen so far
    # The heuristic is admissible because it never overestimates the cost to reach the goal, as the minimum tax value of a coin is 1 and the minimum number of coins required to reach the goal sum is the difference between the goal sum and the sum of the coins chosen so far
    # The heuristic is consistent because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to 1, which is the decrease in the heuristic cost, if the coin is chosen
    return goal - state[0]

print(a_star())
