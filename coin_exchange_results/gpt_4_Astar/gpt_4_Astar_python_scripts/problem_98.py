
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins, the sum of the coins, the tax paid so far, and the last coin chosen
    initial_state = ([35, 14, 15, 111, 8, 4, 6, 37, 14, 33, 45, 32, 46, 41, 38, 19, 34, 14, 2, 4, 24, 36, 46, 33, 12, 2, 14, 28, 12, 21, 34, 26, 28, 27, 25, 4, 23, 43, 43, 20, 10, 13, 5, 36, 27, 36], 0, 0, 0)
    # Define the goal sum of the coins
    goal_sum = 462
    # Define the tax values for each coin
    tax_values = {33: 16, 21: 14, 4: 1, 13: 9, 23: 8, 2: 2, 12: 2, 41: 15, 46: 6, 45: 2, 34: 16, 24: 15, 19: 4, 5: 4, 35: 14, 6: 6, 37: 13, 26: 16, 43: 20, 15: 13, 111: 2, 38: 1, 10: 7, 32: 13, 20: 14, 27: 15, 36: 14, 25: 8, 14: 2, 28: 10, 8: 4}

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
            # Check if the new state, containing the new coin, would be valid; ie the coin must be smaller than the last coin chosen and have an even value, or be larger than or equal to the last coin chosen and have an odd value
            if (coin < last_coin and coin % 2 == 0) or (coin >= last_coin and coin % 2 == 1):
                # Generate the new state
                new_state = (coins[:], sum_coins + coin, tax_paid + tax_values[coin], coin)
                # The additional cost of this state is the tax paid for the new coin as we are trying to minimize the total tax paid
                new_cost = g + tax_values[coin]

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The coin chosen must be added to the actions
                    heapq.heappush(queue, (g + heuristic(sum_coins, goal_sum), new_cost, actions + [coin], new_state))
    return None

def heuristic(sum_coins, goal_sum):
    # An admissible and consistent heuristic for this problem is the difference between the goal sum and the sum of the coins chosen so far
    # The heuristic relaxes the constraints that the coins must be unique, that the coins must be smaller than the last coin chosen and have an even value, or be larger than or equal to the last coin chosen and have an odd value, and that the coins must have a tax value; ie It presumes we can choose any coin to reach the goal sum
    # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
    # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to 1, the decrease in the difference between the goal sum and the sum of the coins chosen so far
    # Also the cost of the goal state is 0, as the sum of the coins equals the goal sum and there are no more coins to choose
    return goal_sum - sum_coins

print(a_star())
