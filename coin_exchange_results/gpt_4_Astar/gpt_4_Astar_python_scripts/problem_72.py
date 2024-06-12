
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins, their tax values, the target sum, and the constraints on the coins
    coins = [13, 3, 34, 36, 19, 31, 6, 7, 10, 24, 92, 3, 24, 33, 33, 22, 93, 13, 17, 28, 25, 16, 21, 16, 20, 26, 24, 16, 11, 18, 2, 30, 25, 23, 28, 21]
    tax_values = {3: 1, 23: 1, 34: 8, 17: 14, 20: 16, 11: 5, 28: 7, 13: 3, 22: 19, 16: 4, 26: 20, 93: 7, 31: 11, 6: 2, 36: 12, 33: 15, 18: 1, 19: 2, 7: 7, 21: 7, 10: 9, 24: 11, 30: 4, 25: 7, 2: 2, 92: 19}
    target_sum = 384
    initial_state = (0, 0, [], 0, 0)  # (sum_so_far, tax_so_far, coins_chosen, last_coin_chosen, index_of_last_coin_chosen)

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
        if state[0] == target_sum:
            return actions

        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for i in range(state[4] + 1, len(coins)):
            coin = coins[i]
            # Check if the new state would be valid, ie if the sum of the coins chosen so far and the new coin does not exceed the target sum
            # and if the new coin is smaller than the last coin chosen, it must have an even value, otherwise, if the coin is larger than or equal to the last coin chosen, it must have an odd value
            if state[0] + coin <= target_sum and (coin < state[3] and coin % 2 == 0 or coin >= state[3] and coin % 2 == 1):
                # Generate the new state
                new_state = (state[0] + coin, state[1] + tax_values[coin], state[2] + [coin], coin, i)
                # The cost so far is the sum of the tax values of the coins chosen, as our objective is to minimize the total tax paid
                new_cost = g + tax_values[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, target_sum), new_cost, actions + [coin], new_state))

    return None

def heuristic(state, target_sum):
    # An admissible and consistent heuristic for this problem is the difference between the target sum and the sum of the coins chosen so far
    # The heuristic relaxes the constraints that each coin can only be chosen once, that the coins must be chosen in a specific order, and that the coins must satisfy the even-odd rule, and presumes we can choose any coin to reach the target sum
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to 1, the decrease in the difference between the target sum and the sum of the coins chosen so far, if the coin is chosen toward the target sum, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the difference between the target sum and the sum of the coins chosen would be 0 in the goal state.
    return target_sum - state[0]

print(a_star())
