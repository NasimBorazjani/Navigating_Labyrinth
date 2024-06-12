
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins, the sum of the coins, the tax paid so far, and the last coin chosen
    initial_state = ([21, 31, 30, 31, 10, 17, 13, 35, 12, 2, 16, 40, 23, 10, 29, 13, 23, 2, 9, 5, 107, 46, 23, 11, 42, 9, 46, 28, 44, 22, 106, 10], 0, 0, None)
    # Define the goal sum of the coins
    goal_sum = 465
    # Define the tax values for each coin
    tax_values = {13: 9, 106: 19, 28: 20, 44: 14, 9: 6, 35: 6, 22: 19, 46: 17, 11: 7, 40: 12, 17: 15, 10: 4, 12: 6, 30: 20, 2: 2, 23: 11, 42: 10, 16: 1, 107: 11, 21: 12, 5: 3, 31: 13, 29: 20}

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
            if (state[3] is None or (coin < state[3] and coin % 2 == 0) or (coin >= state[3] and coin % 2 == 1)):
                # Generate the new state
                new_state = (state[0][:], state[1] + coin, state[2] + tax_values[coin], coin)
                new_state[0].remove(coin)
                # The cost so far is the tax paid, as our objective is to minimize the total tax paid
                new_cost = g + tax_values[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_sum), new_cost, coins_chosen + [coin], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the difference between the goal sum and the current sum of the coins
    # The heuristic relaxes the constraint that the coins must be chosen according to the rules and presumes we can choose any of the remaining coins to reach the goal sum
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to 1, the decrease in the difference between the goal sum and the current sum, if the coin is chosen
    return goal - state[1]

print(a_star())
