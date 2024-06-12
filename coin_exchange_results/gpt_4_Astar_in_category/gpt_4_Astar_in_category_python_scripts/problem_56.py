
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, tuple(sorted([4, 33, 14, 32, 9, 32, 2, 35, 25, 10, 11, 6, 8, 26, 10, 25, 34, 21, 13, 15, 3, 15, 25, 3, 16, 3, 2, 25, 15, 23, 31, 35, 13, 14, 5, 7, 2, 18, 10, 8, 25, 30, 13, 35, 3, 26, 33, 2, 5, 26, 26, 28, 6])))
    goal_sum = 355
    tax_values = {26: 4, 34: 4, 7: 5, 28: 11, 35: 8, 18: 13, 25: 19, 14: 10, 23: 7, 6: 1, 10: 5, 21: 8, 13: 13, 2: 1, 3: 1, 30: 5, 4: 4, 31: 18, 11: 3, 9: 1, 8: 3, 5: 3, 32: 5, 15: 15, 33: 18, 16: 4}

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen to get to each state in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, coins_chosen, state = heapq.heappop(queue)

        # We can check if the current state is the goal state by checking if the sum of the coins chosen equals the goal sum
        if state[0] == goal_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for coin in state[3]:
            # Check if the new state would be valid, ie the coin chosen must be smaller than the previous one and have an even value, or larger than or equal to the previous coin and have an odd value
            if (coin < state[1] and coin % 2 == 0) or (coin >= state[1] and coin % 2 == 1):
                # Generate the new state
                new_state = (state[0] + coin, coin, state[2] + tax_values[coin], tuple([c for c in state[3] if c != coin]))
                # The cost so far is the sum of the tax values of the coins chosen, as our objective is to minimize the total tax paid
                new_cost = g + tax_values[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, coins_chosen + [coin], new_state))

    return None

def heuristic(state, goal_sum):
    # An admissible and consistent heuristic is the difference between the goal sum and the sum of the coins chosen so far
    # The heuristic relaxes the constraint that the coins chosen must be smaller than the previous one and have an even value, or larger than or equal to the previous coin and have an odd value, and presumes we can choose any of the remaining coins to reach the goal sum
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to the decrease in the heuristic, if the coin is chosen toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the difference between the goal sum and the sum of the coins chosen would be 0 in the goal state.
    return goal_sum - state[0]

print(a_star())
