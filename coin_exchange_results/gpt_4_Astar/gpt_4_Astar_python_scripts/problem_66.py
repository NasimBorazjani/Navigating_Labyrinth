
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins, their tax values, the target sum, and the constraints on the coins
    coins = [3, 35, 33, 20, 31, 29, 12, 31, 8, 10, 3, 17, 2, 28, 6, 25, 10, 13, 31, 25, 37, 35, 9, 15, 113, 26, 18, 34, 30]
    tax_values = {31: 11, 15: 6, 13: 13, 28: 1, 9: 6, 20: 1, 34: 15, 6: 5, 113: 20, 12: 6, 2: 1, 29: 10, 37: 2, 25: 11, 26: 10, 3: 3, 33: 19, 8: 7, 18: 6, 17: 7, 10: 8, 35: 11, 30: 16}
    target_sum = 384
    # The initial state is an empty list of coins, with a sum of 0
    initial_state = ([], 0)
    # The initial cost of the state is 0, as no coins have been chosen yet
    visited_costs = {}
    visited_costs[initial_state] = 0
    # The initial state is added to the queue of states to be visited
    queue = [(0, 0, [], initial_state)]

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
            if coin not in chosen_coins and sum_chosen_coins + coin <= target_sum and (not chosen_coins or (coin < chosen_coins[-1] and coin % 2 == 0) or (coin >= chosen_coins[-1] and coin % 2 == 1)):
                # Generate the new state
                new_state = (chosen_coins + [coin], sum_chosen_coins + coin)
                # The additional cost of this state is the tax value of the coin
                new_cost = g + tax_values[coin]

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The heuristic is 0, as we don't have an estimate of the remaining cost to reach the goal state
                    heapq.heappush(queue, (g, new_cost, actions + [coin], new_state))
    return None

print(a_star())
