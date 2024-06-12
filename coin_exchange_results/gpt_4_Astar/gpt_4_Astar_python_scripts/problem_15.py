
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins, the sum of the coins, the tax paid so far, and the last coin chosen
    initial_state = ([1, 2, 17, 12, 7, 17, 2, 20, 4, 4, 17, 19, 15, 16, 18, 21, 18, 10, 3, 9, 12, 13, 8, 16, 9, 14, 13, 5, 13, 6, 20, 6, 13, 12, 8, 14, 15, 7, 10, 3, 16, 16, 9, 3, 2, 6, 9, 14, 16, 20, 11, 4, 17], 0, 0, 0)
    # Define the tax values for each coin
    tax_values = {8: 5, 5: 2, 19: 2, 4: 4, 9: 2, 3: 1, 2: 2, 12: 1, 13: 6, 6: 5, 11: 1, 17: 14, 7: 4, 16: 13, 21: 10, 14: 13, 1: 1, 18: 12, 10: 10, 15: 11, 20: 20}
    # Define the goal sum of the coins
    goal_sum = 213

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen to get to each state in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state[1] == goal_sum:
            return actions

        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for coin in state[0]:
            # Check if the new state would be valid, ie if the coin is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
            if (coin < state[3] and coin % 2 == 0) or (coin >= state[3] and coin % 2 == 1):
                # Generate the new state
                new_state = (state[0][:], state[1] + coin, state[2] + tax_values[coin], coin)
                # The cost so far is the tax paid, as our objective is to minimize the total tax paid
                new_cost = g + tax_values[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the difference between the goal sum and the current sum of the coins
    # The heuristic relaxes the constraint that the coins must be chosen according to the rules and presumes we can choose any of the remaining coins to reach the goal sum
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to 1, the decrease in the difference between the goal sum and the current sum, if the coin is chosen according to the rules, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the difference between the goal sum and the current sum would be 0 in the goal state.
    return goal - state[1]

print(a_star())
