
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins available, the sum of the coins chosen so far, the tax paid so far, and the value of the last coin chosen
    # The initial state has no coins chosen, thus the sum of the coins chosen and the tax paid so far are 0, and the value of the last coin chosen is 0
    initial_state = ((18, 23, 23, 36, 27, 10, 25, 14, 6, 43, 6, 31, 5, 43, 3, 13, 16, 8, 11, 6, 39, 44, 41, 28, 12, 8, 1, 14, 22, 23, 11, 24, 37, 9, 2, 31, 27, 10, 9, 38, 37, 4, 4, 17, 18, 36, 18, 32, 3, 12, 4, 42, 8, 4, 4, 16, 30, 40, 13, 41), 0, 0, 0)
    # Define the goal sum of the coins
    goal_sum = 441
    # Define the tax values for each coin
    tax_values = {6: 4, 18: 3, 38: 1, 23: 2, 16: 8, 12: 2, 4: 2, 24: 13, 28: 17, 30: 17, 1: 1, 9: 9, 27: 8, 11: 4, 37: 16, 41: 19, 13: 3, 31: 8, 44: 8, 22: 7, 43: 13, 10: 3, 17: 8, 36: 7, 39: 3, 25: 17, 40: 10, 8: 6, 32: 16, 14: 4, 2: 1, 42: 3, 3: 2, 5: 2}

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
            # Check if the new state, containing the new coin, would be valid; ie the sum of the coins chosen so far and the new coin must not exceed the goal sum, and the new coin must be even if it is smaller than the last coin chosen, or odd if it is larger than or equal to the last coin chosen
            if sum_coins + coin <= goal_sum and ((coin < last_coin and coin % 2 == 0) or (coin >= last_coin and coin % 2 == 1)):
                # Generate the new state
                new_state = (tuple(c for c in coins if c != coin), sum_coins + coin, tax_paid + tax_values[coin], coin)
                # The additional cost of this state is the tax paid for the new coin as we are trying to minimize the total tax paid
                new_cost = g + tax_values[coin]

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # Relaxing the constraints on the sum of the coins and the parity of the coins to calculate the heuristic
                    h = heuristic(new_state, goal_sum, tax_values)
                    heapq.heappush(queue, (g + h, new_cost, actions + [coin], new_state))
    return None

def heuristic(state, goal_sum, tax_values):
    # Relax the sum and parity constraints to compute an admissible and consistent heuristic
    # This heuristic considers the remaining sum to reach the goal sum, filling the remaining sum with the smallest unique coin, and paying the tax for that coin
    # The heuristic assumes we can fill the remaining sum with the smallest unique coin, even if the sum or parity constraints are violated, thus reporting a lower cost estimate to reach the goal state, making it admissible
    # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of choosing a coin is the tax paid for that coin, which is always greater than or equal to the tax paid for the coin used to fill that position in the heuristic
    # Also the cost of the goal state is 0, as the sum of the coins equals the goal sum and there are no remaining coins to choose

    # Get coins not used in the state currently
    used_coins = set(state[0])
    available_coins = sorted(list(set(range(1, 45)) - used_coins))
    h = 0
    remaining_sum = goal_sum - state[1]
    while remaining_sum > 0 and available_coins:
        coin = available_coins.pop(0)
        num_coin = min(remaining_sum // coin, 1)
        remaining_sum -= coin * num_coin
        h += tax_values[coin] * num_coin
    return h

print(a_star())
