
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins, their tax values, the target sum, and the constraints on the coins
    coins = [24, 10, 24, 3, 21, 7, 21, 26, 8, 14, 24, 5, 13, 10, 25, 6, 9, 4, 18, 4, 15, 4, 10, 23, 6, 13, 26, 20, 8, 10, 29, 27, 27, 20, 2, 15, 9, 9, 25, 8, 2, 27, 5, 22, 19, 26, 2, 29, 12, 9, 6, 12, 2, 15, 5, 16, 3, 29, 19]
    tax_values = {5: 2, 9: 8, 12: 5, 14: 4, 22: 8, 26: 3, 8: 7, 27: 2, 20: 13, 3: 3, 13: 3, 2: 1, 19: 19, 29: 4, 10: 3, 18: 14, 21: 12, 15: 12, 4: 3, 23: 5, 16: 9, 25: 16, 7: 4, 24: 17, 6: 6}
    target_sum = 300
    # The initial state is an empty list of coins, with a sum of 0
    initial_state = ([], 0)
    # The visited_costs dictionary stores the minimum tax paid to reach a state
    visited_costs = {}
    visited_costs[initial_state] = 0
    # The queue stores the states to be visited, with the priority of each state being the tax paid so far plus the estimated remaining tax
    queue = [(0, 0, [], initial_state)]

    while queue:
        # Pop the state with the lowest priority from the queue
        _, g, actions, state = heapq.heappop(queue)
        # Unpack the state
        chosen_coins, sum_chosen_coins = state
        # If the sum of the chosen coins equals the target sum, return the chosen coins
        if sum_chosen_coins == target_sum:
            return actions
        # If the sum of the chosen coins is less than the target sum, generate all possible actions from the current state, which includes choosing each of the remaining coins
        elif sum_chosen_coins < target_sum:
            for coin in coins:
                # Check if the new state, with the chosen coin, would be valid; ie the coin must not have been chosen before, and it must satisfy the constraints on the coins
                if (coin not in chosen_coins and
                    (not chosen_coins or
                     (coin < chosen_coins[-1] and coin % 2 == 0) or
                     (coin >= chosen_coins[-1] and coin % 2 == 1))):
                    # Generate the new state
                    new_state = (chosen_coins + [coin], sum_chosen_coins + coin)
                    # The additional cost of this state is the tax value of the chosen coin
                    new_cost = g + tax_values[coin]
                    # If the new state has not been visited before, or if a lower cost path to this state has been found, add it to the queue
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        # The heuristic is the minimum possible remaining tax, which is 0, as the remaining coins could have a tax value of 0
                        h = 0
                        heapq.heappush(queue, (g + h, new_cost, actions + [coin], new_state))
    return None

print(a_star())
