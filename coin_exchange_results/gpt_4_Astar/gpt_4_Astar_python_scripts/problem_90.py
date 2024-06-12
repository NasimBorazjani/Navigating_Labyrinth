
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins available, the sum of the coins chosen so far, the tax paid so far, and the value of the last coin chosen
    initial_state = ((45, 45, 40, 38, 26, 3, 3, 21, 3, 35, 24, 9, 43, 10, 19, 5, 21, 36, 15, 18, 13, 33, 42, 34, 6, 20, 38, 25, 42, 19, 32, 9, 31, 4, 4, 25, 30, 8), 0, 0, 0)
    # Define the goal sum of the coins
    goal_sum = 453
    # Define the tax values for each coin
    tax_values = {13: 7, 9: 1, 38: 9, 19: 4, 31: 18, 25: 18, 40: 13, 4: 2, 15: 8, 45: 2, 10: 10, 20: 18, 5: 3, 35: 12, 30: 8, 8: 5, 21: 5, 43: 12, 32: 10, 6: 2, 24: 18, 3: 2, 33: 7, 42: 4, 36: 10, 34: 6, 26: 5, 18: 6}

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

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state[1] == goal_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for coin in state[0]:
            # Check if the new state would be valid, ie if the coin is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
            if (coin < state[3] and coin % 2 == 0) or (coin >= state[3] and coin % 2 == 1):
                # Generate the new state
                new_state = (tuple(coin_ for coin_ in state[0] if coin_ != coin), state[1] + coin, state[2] + tax_values[coin], coin)
                # The cost so far is the tax paid, as our objective is to minimize the total tax paid
                new_cost = g + tax_values[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_sum), new_cost, coins_chosen + [coin], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the difference between the goal sum and the sum of the coins chosen so far
    # The heuristic relaxes the constraint that the coins must be unique and presumes we can choose any coin to reach the goal sum
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to 1, the decrease in the difference between the goal sum and the sum of the coins chosen so far, if the coin is chosen toward the goal sum, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the difference between the goal sum and the sum of the coins chosen so far would be 0 in the goal state.
    return goal - state[1]

print(a_star())
