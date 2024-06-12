
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins available, the sum of the coins chosen so far, the tax paid so far, and the value of the last coin chosen
    initial_state = ((30, 24, 27, 14, 29, 17, 4, 21, 20, 14, 19, 23, 18, 4, 12, 9, 24, 26, 21, 17, 3, 13, 25, 20, 16, 12, 2, 9, 17, 5, 6, 24, 13, 11, 6, 15, 13, 5, 13, 25, 10, 15, 10, 3, 2, 18, 7, 23, 5, 18, 21, 6), 0, 0, 0)
    # Define the tax values for each coin
    tax_values = {14: 11, 3: 1, 18: 5, 21: 1, 27: 2, 19: 14, 6: 6, 25: 8, 5: 3, 29: 4, 7: 6, 24: 10, 10: 2, 13: 9, 9: 1, 11: 8, 16: 10, 2: 1, 12: 12, 15: 4, 23: 17, 17: 9, 26: 13, 30: 17, 4: 3, 20: 6}
    # Define the goal sum of the coins
    goal_sum = 300

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Unpack the information encoded in each state
        coins, sum_coins, tax_paid, last_coin = state

        # If the sum of the coins chosen so far equals the goal sum, return the coins chosen
        if sum_coins == goal_sum:
            return actions

        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for coin in coins:
            # Check if the new state would be valid, ie if the coin is smaller than the last coin chosen, it must have an even value, otherwise, if the coin is larger than or equal to the last coin chosen, it must have an odd value
            if (coin < last_coin and coin % 2 == 0) or (coin >= last_coin and coin % 2 == 1):
                # Generate the new state
                new_state = (tuple(coin_ for coin_ in coins if coin_ != coin), sum_coins + coin, tax_paid + tax_values[coin], coin)
                # The cost so far is the tax paid so far, as the task is to minimize the total tax paid
                new_cost = g + tax_values[coin]

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The heuristic is the remaining sum to reach the goal sum, divided by the smallest coin remaining, times the smallest tax value, as we are trying to minimize the tax paid
                    h = heuristic(new_state, goal_sum, tax_values)
                    heapq.heappush(queue, (g + h, new_cost, actions + [coin], new_state))
    return None

def heuristic(state, goal_sum, tax_values):
    # The heuristic is the remaining sum to reach the goal sum, divided by the smallest coin remaining, times the smallest tax value
    # This heuristic relaxes the constraints that the coins must be unique and that the coins must be chosen in a specific order, ie it presumes we can choose the smallest coin remaining to reach the goal sum, even if the coin is not unique or if it violates the order constraint
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to the smallest tax value, the decrease in the heuristic cost, if the coin is chosen
    # Also the heuristic estimate for the goal state is 0, as the remaining sum to reach the goal sum would be 0 in the goal state
    remaining_sum = goal_sum - state[1]
    smallest_coin = min(state[0]) if state[0] else 1
    smallest_tax = min(tax_values.values())
    return remaining_sum // smallest_coin * smallest_tax

print(a_star())
