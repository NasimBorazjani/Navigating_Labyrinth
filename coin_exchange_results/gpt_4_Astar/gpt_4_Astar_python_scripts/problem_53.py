
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins available, the sum of the coins chosen so far, the tax paid so far, and the value of the last coin chosen
    # The initial state has no coins chosen, thus the sum of the coins chosen and the tax paid are both 0, and the value of the last coin chosen is 0
    initial_state = ((23, 10, 22, 30, 5, 16, 2, 28, 25, 26, 30, 25, 35, 32, 10, 4, 24, 32, 34, 12, 11, 5, 5, 18, 16, 24, 3, 12, 11, 5, 2, 7, 19, 34, 7, 30, 17, 11, 16, 10, 31, 31, 34, 27, 3, 24), 0, 0, 0)
    # Define the goal sum of the coins
    goal_sum = 359
    # Define the tax values for each coin
    tax_values = {24: 9, 26: 11, 17: 7, 7: 4, 12: 4, 35: 18, 5: 5, 31: 8, 2: 2, 3: 1, 27: 14, 34: 3, 30: 1, 23: 6, 4: 2, 10: 8, 18: 18, 25: 15, 28: 4, 32: 19, 11: 7, 16: 6, 19: 11, 22: 5}

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
            # Check if the new state would be valid, ie if the coin chosen is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
            if (coin < state[3] and coin % 2 == 0) or (coin >= state[3] and coin % 2 == 1):
                # Generate the new state
                new_state = (tuple(remaining_coin for remaining_coin in state[0] if remaining_coin != coin), state[1] + coin, state[2] + tax_values[coin], coin)
                # The cost so far is the tax paid, as our objective is to minimize the total tax paid
                new_cost = g + tax_values[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_sum), new_cost, coins_chosen + [coin], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the difference between the goal sum and the sum of the coins chosen so far
    # The heuristic relaxes the constraints that the coins chosen must be unique and that the coins chosen must follow the rules about the value of the coin relative to the previous coin chosen, ie it presumes we can choose any coin to reach the goal sum
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to 1, the decrease in the difference between the goal sum and the sum of the coins chosen so far, if the coin is chosen toward the goal sum, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the difference between the goal sum and the sum of the coins chosen would be 0 in the goal state
    return goal - state[1]

print(a_star())
