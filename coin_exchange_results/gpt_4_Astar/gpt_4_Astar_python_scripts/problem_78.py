
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins, their tax values, the target sum, and the constraints on the coins
    coins = [29, 32, 2, 34, 7, 25, 7, 14, 33, 1, 26, 18, 13, 11, 32, 31, 13, 2, 28, 21, 38, 8, 11, 28, 26, 9, 4, 28, 34, 23, 18, 31, 35, 2, 25, 20, 15, 5, 12, 10, 7, 14, 17, 4, 13, 24, 11, 16, 14, 27, 29]
    tax_values = {10: 1, 25: 18, 1: 1, 15: 7, 12: 1, 23: 16, 9: 7, 27: 15, 29: 16, 28: 2, 32: 12, 24: 6, 5: 1, 8: 1, 11: 8, 17: 13, 13: 6, 38: 6, 31: 19, 4: 2, 34: 12, 21: 3, 2: 2, 33: 12, 20: 13, 18: 1, 14: 13, 16: 8, 7: 5, 35: 16, 26: 10}
    target_sum = 392

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[()] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen to get to each state in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], ())]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        # The goal state is where the sum of the coins chosen equals the target sum
        if sum(state) == target_sum:
            return actions

        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for coin in coins:
            # Check if the new state would be valid, ie if the coin is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
            if (not state or (coin < state[-1] and coin % 2 == 0) or (coin >= state[-1] and coin % 2 == 1)):
                # Generate the new state
                new_state = state + (coin,)
                # The cost so far is the sum of the tax values of the coins chosen, as our objective is to minimize the total tax paid
                new_cost = g + tax_values[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, target_sum), new_cost, actions + [coin], new_state))
    return None

def heuristic(state, target_sum):
    # An admissible and consistent heuristic for this problem is the difference between the target sum and the sum of the coins chosen so far
    # The heuristic relaxes the constraints on the coins that can be chosen and presumes we can choose any coin to reach the target sum
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to 1, the decrease in the difference between the target sum and the sum of the coins chosen so far
    return target_sum - sum(state)

print(a_star())
