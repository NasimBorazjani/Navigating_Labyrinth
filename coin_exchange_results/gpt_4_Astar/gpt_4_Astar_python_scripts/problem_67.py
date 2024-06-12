
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins, their tax values, the target sum, and the constraints on the coins
    coins = [8, 13, 16, 4, 35, 2, 19, 2, 21, 26, 28, 12, 58, 28, 12, 35, 33, 4, 19, 27, 61, 30, 17, 20, 27, 25, 30, 31, 9, 15, 4, 13, 11, 29]
    tax_values = {13: 1, 4: 1, 61: 2, 30: 19, 12: 4, 20: 16, 29: 10, 2: 2, 35: 17, 31: 17, 19: 15, 25: 11, 21: 8, 27: 16, 17: 17, 11: 7, 58: 12, 26: 4, 15: 14, 28: 10, 8: 5, 16: 5, 9: 8, 33: 13}
    target_sum = 384
    initial_state = (0, 0, 0, [])  # (sum_so_far, tax_so_far, last_coin, coins_chosen)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # If the sum of the coins chosen so far equals the target sum, return the coins chosen
        if state[0] == target_sum:
            return actions

        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for coin in coins:
            # Check if the new state would be valid, ie if the coin satisfies the constraints and the sum of the coins chosen so far and the new coin does not exceed the target sum
            if (coin >= state[2] and coin % 2 == 1 or coin < state[2] and coin % 2 == 0) and state[0] + coin <= target_sum:
                # Generate the new state
                new_state = (state[0] + coin, state[1] + tax_values[coin], coin, state[3] + [coin])
                # The cost so far is the sum of the tax values of the coins chosen, as the task is to minimize the total tax paid
                new_cost = g + tax_values[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, target_sum), new_cost, actions + [coin], new_state))
    return None

def heuristic(state, target):
    # An admissible and consistent heuristic for this problem is the difference between the target sum and the sum of the coins chosen so far
    # The heuristic relaxes the constraints on the coins that can be chosen and presumes we can choose any coin to reach the target sum
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to 1, the decrease in the difference between the target sum and the sum of the coins chosen so far
    return target - state[0]

print(a_star())
