
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins available, the sum of the coins chosen so far, the tax paid so far, and the value of the last coin chosen
    # The initial state has no coins chosen, thus the sum of the coins chosen and the tax paid so far are 0, and the value of the last coin chosen is 0
    initial_state = ((20, 19, 2, 12, 23, 18, 15, 13, 10, 6, 9, 4, 9, 16, 5, 8, 19, 6, 7, 2, 6, 15, 10, 9, 4, 6, 19, 10, 10, 16, 21, 17, 21, 16, 13, 6, 16, 8, 7, 11, 13, 7, 21, 15, 15, 6, 11, 19, 7), 0, 0, 0)
    # Define the goal sum of the coins
    goal_sum = 216
    # Define the tax values for each coin
    tax_values = {6: 6, 8: 6, 16: 4, 15: 11, 12: 3, 10: 5, 20: 14, 9: 3, 17: 8, 7: 5, 5: 5, 2: 1, 11: 4, 23: 18, 19: 3, 13: 13, 18: 6, 4: 3, 21: 20}

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
                    # The coin chosen must be added to the actions
                    heapq.heappush(queue, (g + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the difference between the goal sum and the sum of the coins chosen so far
    # The heuristic assumes we can choose any of the remaining coins to reach the goal sum, even if the coin is larger than the goal sum or does not satisfy the even-odd rule, thus reporting a lower cost estimate to reach the goal state, making it admissible
    # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of choosing a coin is the tax paid for the coin, which is always greater than or equal to 1, the decrease in the difference between the goal sum and the sum of the coins chosen so far
    # Also the cost of the goal state is 0, as the sum of the coins chosen equals the goal sum and there are no more coins to choose
    return goal - state[1]

print(a_star())
