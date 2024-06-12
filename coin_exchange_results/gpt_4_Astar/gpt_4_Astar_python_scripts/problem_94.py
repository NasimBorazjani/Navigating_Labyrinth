
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins, their tax values, the target sum, and the constraints on the coins
    coins = [21, 13, 10, 18, 21, 43, 42, 29, 14, 19, 9, 2, 15, 19, 32, 45, 24, 31, 25, 7, 21, 24, 29, 29, 4, 36, 29, 19, 29, 12, 3, 44, 40, 46, 33, 3, 28, 44, 25, 6, 36, 3, 4, 19, 31]
    tax_values = {6: 3, 9: 7, 13: 11, 19: 11, 36: 17, 32: 11, 46: 1, 4: 3, 21: 14, 3: 1, 18: 5, 29: 18, 12: 9, 2: 2, 15: 14, 43: 11, 24: 5, 25: 15, 14: 10, 42: 11, 44: 7, 31: 11, 40: 2, 33: 10, 45: 20, 7: 6, 10: 3, 28: 5}
    target_sum = 474
    initial_state = (0, 0, [], 0, 0)  # (sum_so_far, tax_so_far, coins_chosen, last_coin_chosen, last_coin_index)

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

        # Generate all valid actions from the current state, which includes choosing any of the remaining coins
        for i in range(state[4] + 1, len(coins)):
            coin = coins[i]
            # Check if the new state would be valid, ie if the sum of the coins chosen so far and the new coin does not exceed the target sum
            # and if the new coin is smaller than the last coin chosen, it must have an even value, otherwise, if the coin is larger than or equal to the last coin chosen, it must have an odd value
            if state[0] + coin <= target_sum and (coin < state[3] and coin % 2 == 0 or coin >= state[3] and coin % 2 == 1):
                # The actions is valid, generate the new state
                new_state = (state[0] + coin, state[1] + tax_values[coin], state[2] + [coin], coin, i)
                # The cost so far is the sum of the tax values of the coins chosen, as our objective is to minimize the total tax paid
                new_cost = g + tax_values[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, target_sum), new_cost, actions + [coin], new_state))

    return None

def heuristic(state, target_sum):
    # An admissible and consistent heuristic is the difference between the target sum and the sum of the coins chosen so far
    # The heuristic relaxes the constraints that the coins must be unique and the sum of the coins chosen must not exceed the target sum, and presumes we can choose any coin to reach the target sum
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to 1, the decrease in the difference between the target sum and the sum of the coins chosen so far, if the coin is chosen toward the target sum, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the difference between the target sum and the sum of the coins chosen would be 0 in the goal state.
    return target_sum - state[0]

print(a_star())
