
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, 0)
    goal_state = 452

    # Define the coins and their tax values
    coins = [39, 3, 38, 10, 3, 5, 6, 14, 32, 7, 30, 28, 17, 9, 8, 13, 17, 41, 25, 6, 19, 36, 5, 36, 8, 38, 6, 19, 25, 3, 22, 18, 3, 21, 57, 37, 42, 30, 54, 13, 36, 6, 13, 17, 10, 4, 36]
    tax = {37: 2, 38: 4, 30: 18, 39: 18, 14: 1, 18: 1, 4: 1, 10: 8, 21: 10, 6: 5, 42: 13, 32: 10, 25: 2, 17: 15, 13: 2, 9: 4, 22: 17, 7: 5, 3: 2, 54: 7, 19: 15, 8: 2, 36: 17, 28: 6, 5: 5, 41: 9, 57: 12}

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state[0] == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for coin in coins:
            # Check if the new state would be valid, ie the sum of the coins chosen so far and the new coin does not exceed the goal sum
            # And the new coin must be smaller than the previous one and have an even value, or be larger than or equal to the previous coin and have an odd value
            if state[0] + coin <= goal_state and (coin < state[1] and coin % 2 == 0 or coin >= state[1] and coin % 2 == 1):
                # Generate the new state
                new_state = (state[0] + coin, coin, state[2] + tax[coin], state[3] + 1)
                # The cost so far is the sum of the tax values of the coins chosen, as our objective is to minimize the total tax paid
                new_cost = g + tax[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [coin], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the difference between the goal sum and the sum of the coins chosen so far
    # The heuristic relaxes the constraint that the coins chosen must be unique and presumes we can reach the goal sum by choosing the same coin repeatedly
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to the decrease in the heuristic, if the coin is chosen toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the difference between the goal sum and the sum of the coins chosen would be 0 in the goal state
    return goal - state[0]

print(a_star())
