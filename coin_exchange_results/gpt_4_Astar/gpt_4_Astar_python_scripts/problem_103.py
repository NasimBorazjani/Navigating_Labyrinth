
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins, their tax values, the target sum, and the constraints on the coins
    coins = [40, 28, 46, 16, 13, 15, 38, 39, 3, 8, 40, 41, 18, 48, 16, 25, 39, 14, 47, 46, 31, 16, 41, 45, 9, 26, 33, 46, 17, 23, 6, 46, 7, 43, 10, 28, 47, 15, 35, 20, 32, 4, 32, 9, 48, 7, 34, 46, 10, 39, 44]
    tax_values = {44: 6, 39: 15, 4: 2, 23: 11, 7: 2, 40: 10, 13: 10, 34: 8, 45: 9, 10: 3, 35: 18, 14: 2, 28: 5, 46: 12, 25: 3, 26: 18, 15: 11, 31: 2, 20: 15, 9: 7, 41: 13, 18: 16, 32: 11, 3: 3, 48: 20, 38: 4, 43: 6, 33: 9, 16: 13, 8: 4, 17: 1, 47: 17, 6: 5}
    target_sum = 485
    # The initial state is an empty list of coins, with a sum of 0
    initial_state = ([], 0)
    # The goal state is a list of coins that add up to the target sum

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state[1] == target_sum:
            return actions

        # Generate all possible actions from the current state, which includes adding any of the remaining coins to the list of chosen coins
        for coin in coins:
            # Check if the new state would be valid, ie if the sum of the coins in the new state would not exceed the target sum, and if the coin satisfies the constraints
            if state[1] + coin <= target_sum and (not state[0] or (coin < state[0][-1] and coin % 2 == 0) or (coin >= state[0][-1] and coin % 2 == 1)):
                # Generate the new state
                new_state = (state[0] + [coin], state[1] + coin)
                # The cost so far is the sum of the tax values of the coins chosen, as our objective is to minimize the total tax paid
                new_cost = g + tax_values[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, target_sum), new_cost, actions + [coin], new_state))

    return None

def heuristic(state, target_sum):
    # An admissible and consistent heuristic for this problem is the difference between the target sum and the sum of the coins in the current state
    # The heuristic relaxes the constraints on the coins that can be chosen and presumes we can choose any coin to reach the target sum, thus reporting a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of adding a coin to the list of chosen coins is the tax value of the coin, which is always greater than or equal to 1, the decrease in the heuristic value, if the coin is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the difference between the target sum and the sum of the coins in the goal state would be 0
    return target_sum - state[1]

print(a_star())
