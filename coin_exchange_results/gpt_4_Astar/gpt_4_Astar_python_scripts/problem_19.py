
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins available, the sum of the coins chosen so far, the tax paid so far, and the value of the last coin chosen
    # The initial state has no coins chosen, thus the sum of the coins chosen and the tax paid so far are 0, and the value of the last coin chosen is 0
    initial_state = ((9, 20, 4, 23, 10, 11, 8, 6, 20, 8, 20, 12, 15, 20, 18, 16, 19, 21, 5, 6, 4, 5, 14, 5, 4, 18, 22, 7, 8, 15, 5, 15, 8, 19, 14, 12, 2, 5, 5, 15, 2, 6, 10, 18, 14, 13, 8, 10, 21, 14, 5, 18, 16, 6, 11), 0, 0, 0)
    # Define the goal sum of the coins
    goal_sum = 243
    # Define the tax values for each coin
    tax_values = {20: 3, 9: 2, 23: 1, 10: 3, 5: 4, 21: 14, 22: 5, 18: 7, 16: 4, 13: 5, 2: 1, 8: 2, 19: 16, 7: 3, 6: 6, 11: 3, 14: 8, 4: 2, 12: 7, 15: 14}

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
            # Check if the new state, containing the new coin, would be valid; ie the sum of the coins chosen so far plus the new coin must not exceed the goal sum, and the new coin must be even if it is smaller than the last coin chosen, or odd if it is larger than or equal to the last coin chosen
            if sum_coins + coin <= goal_sum and ((coin < last_coin and coin % 2 == 0) or (coin >= last_coin and coin % 2 == 1)):
                # Generate the new state
                new_state = (tuple(c for c in coins if c != coin), sum_coins + coin, tax_paid + tax_values[coin], coin)
                # The additional cost of this state is the tax paid for the new coin as we are trying to minimize the total tax paid
                new_cost = g + tax_values[coin]

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # Relaxing the constraints on the sum of the coins and the parity of the coins to calculate the heuristic
                    h = heuristic(new_state, goal_sum)
                    heapq.heappush(queue, (g + h, new_cost, actions + [coin], new_state))
    return None

def heuristic(state, goal_sum):
    # Relax the constraints on the sum of the coins and the parity of the coins to compute an admissible and consistent heuristic
    # This heuristic considers the difference between the goal sum and the sum of the coins chosen so far
    # The heuristic assumes we can choose any of the remaining coins to reach the goal sum, even if the sum of the coins exceeds the goal sum or the parity of the coins is not correct, thus reporting a lower cost estimate to reach the goal state, making it admissible
    # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of choosing a coin is the tax paid for the coin, which is always greater than or equal to 1, the decrease in the difference between the goal sum and the sum of the coins chosen so far
    # Also the cost of the goal state is 0, as the sum of the coins equals the goal sum and there are no more coins to choose
    return goal_sum - state[1]

print(a_star())
