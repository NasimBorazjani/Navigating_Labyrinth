
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins available, the sum of the coins chosen so far, the tax paid so far, and the value of the last coin chosen
    initial_state = ((19, 14, 29, 19, 29, 9, 17, 16, 25, 7, 8, 2, 23, 11, 28, 6, 29, 16, 19, 31, 30, 15, 7, 16, 23, 23, 10, 32, 8, 14, 7, 9, 6, 23, 77, 24, 22, 24, 22), 0, 0, 0)
    # Define the goal sum of the coins
    goal_sum = 351
    # Define the tax values for each coin
    tax_values = {15: 6, 29: 12, 19: 3, 30: 18, 14: 2, 77: 3, 6: 5, 17: 1, 32: 16, 9: 8, 22: 15, 31: 17, 25: 10, 24: 1, 28: 11, 2: 2, 7: 4, 8: 7, 11: 7, 23: 19, 10: 2, 16: 2}

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
            # Check if the new state would be valid, ie if the coin chosen is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
            if (coin < last_coin and coin % 2 == 0) or (coin >= last_coin and coin % 2 == 1):
                # Generate the new state
                new_state = (tuple(coin_ for coin_ in coins if coin_ != coin), sum_coins + coin, tax_paid + tax_values[coin], coin)
                # The cost so far is the tax paid, as the task is to minimize the total tax paid
                new_cost = g + tax_values[coin]

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the difference between the goal sum and the sum of the coins chosen so far
    # The heuristic relaxes the constraints that the coins chosen must be unique and that the coins chosen must follow the rules about their relative values, ie it presumes we can choose any coin to reach the goal sum
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to 1, the decrease in the difference between the goal sum and the sum of the coins chosen so far
    return goal - state[1]

print(a_star())
