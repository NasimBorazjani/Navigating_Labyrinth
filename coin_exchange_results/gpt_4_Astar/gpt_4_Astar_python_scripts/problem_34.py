
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins, the sum of the coins, the tax paid so far, and the last coin chosen
    initial_state = ([22, 14, 13, 18, 2, 5, 14, 26, 28, 9, 20, 26, 11, 29, 2, 15, 13, 11, 28, 12, 14, 6, 3, 25, 12, 24, 4, 28, 27, 10, 20, 6, 8, 7, 37, 18, 3, 10, 27, 20, 21, 8, 11, 13, 5, 19, 4, 2], 0, 0, 0)
    # Define the goal sum of the coins
    goal_sum = 293
    # Define the tax values for each coin
    tax_values = {2: 2, 14: 13, 29: 2, 13: 3, 25: 20, 28: 18, 11: 7, 9: 1, 3: 2, 15: 3, 8: 2, 7: 1, 12: 6, 26: 9, 19: 11, 24: 1, 22: 9, 27: 17, 6: 4, 18: 14, 21: 12, 4: 3, 37: 6, 20: 16, 5: 5, 10: 6}

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Unpack the information encoded in each state
        coins, sum_coins, tax_paid, last_coin = state

        # If the sum of the coins chosen equals the goal sum, return the coins chosen
        if sum_coins == goal_sum:
            return actions

        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for coin in coins:
            # Check if the new state, containing the new coin, would be valid; ie the sum of the coins chosen must not exceed the goal sum and the coin must be even if it is smaller than the last coin chosen, or odd if it is larger than or equal to the last coin chosen
            if sum_coins + coin <= goal_sum and ((coin < last_coin and coin % 2 == 0) or (coin >= last_coin and coin % 2 == 1)):
                # Generate the new state
                new_state = (coins[:], sum_coins + coin, tax_paid + tax_values[coin], coin)
                # The additional cost of this state is the tax paid for the new coin as we are trying to minimize the total tax paid
                new_cost = g + tax_values[coin]

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The coin chosen must be added to the actions
                    heapq.heappush(queue, (g + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the difference between the goal sum and the sum of the coins chosen so far
    # The heuristic assumes we can choose any of the remaining coins to reach the goal sum, even if the coin is not even when it is smaller than the last coin chosen, or not odd when it is larger than or equal to the last coin chosen, thus reporting a lower cost estimate to reach the goal state, making it admissible
    # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of choosing a coin is the tax paid for the coin, which is always greater than or equal to 1, the decrease in the difference between the goal sum and the sum of the coins chosen so far
    # Also the cost of the goal state is 0, as the sum of the coins chosen equals the goal sum and there are no more coins to choose
    return goal - state[1]

print(a_star())
