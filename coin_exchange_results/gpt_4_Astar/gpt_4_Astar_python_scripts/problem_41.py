
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins, the tax values, the target sum, and the constraints on the coins
    coins = [20, 27, 20, 26, 2, 19, 25, 5, 14, 28, 7, 4, 20, 25, 9, 7, 3, 9, 27, 23, 2, 17, 25, 19, 10, 2, 8, 15, 3, 6, 24, 6, 22, 3, 10, 3, 2, 24, 7, 16, 2, 24, 21, 5, 23, 25, 10, 5, 20, 14, 24, 12, 11, 11, 13]
    tax_values = {14: 7, 15: 15, 2: 2, 22: 7, 7: 1, 25: 7, 10: 4, 11: 11, 16: 11, 27: 8, 3: 2, 13: 5, 19: 10, 8: 5, 23: 18, 5: 4, 12: 4, 28: 6, 6: 4, 21: 3, 20: 15, 26: 1, 4: 4, 9: 9, 24: 6, 17: 13}
    target_sum = 284
    # The initial state is an empty list of coins, with a sum of 0
    initial_state = ([], 0)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # Unpack the information encoded in each state
        chosen_coins, sum_chosen_coins = state

        # If the sum of the chosen coins equals the target sum, return the chosen coins
        if sum_chosen_coins == target_sum:
            return actions

        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for coin in coins:
            # Check if the new state, containing the new coin, would be valid; ie the sum of the chosen coins must not exceed the target sum and the coin must satisfy the constraints
            if sum_chosen_coins + coin <= target_sum and (not chosen_coins or (coin < chosen_coins[-1] and coin % 2 == 0) or (coin >= chosen_coins[-1] and coin % 2 == 1)):
                # Generate the new state
                new_state = (chosen_coins + [coin], sum_chosen_coins + coin)
                # The additional cost of this state is the tax value of the coin as we are trying to minimize the total tax paid
                new_cost = g + tax_values[coin]

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The heuristic is 0 as we don't have any information about the remaining cost to reach the goal state
                    heapq.heappush(queue, (g, new_cost, actions + [coin], new_state))
    return None

print(a_star())
