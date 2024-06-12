
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins available, the sum of the coins chosen so far, the tax paid so far, and the value of the last coin chosen
    initial_state = ((11, 13, 22, 11, 16, 20, 10, 10, 17, 21, 6, 6, 15, 15, 21, 6, 4, 16, 9, 11, 3, 13, 2, 9, 11, 1, 7, 2, 2, 12, 5, 2, 11, 16, 20, 9, 2, 4, 10, 17, 11, 22, 11, 2, 18, 23, 15, 22, 11, 15, 20, 9), 0, 0, 0)
    goal_sum = 223
    tax_values = {6: 2, 11: 9, 3: 3, 15: 2, 9: 1, 18: 13, 22: 13, 16: 5, 21: 2, 5: 2, 12: 4, 7: 5, 4: 3, 13: 2, 1: 1, 20: 14, 2: 1, 10: 4, 23: 15, 17: 9}

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
            # Check if the new state, containing the new coin, would be valid; ie the sum of the coins chosen so far plus the new coin must not exceed the goal sum and the new coin must satisfy the even-odd condition
            if sum_coins + coin <= goal_sum and ((coin < last_coin and coin % 2 == 0) or (coin >= last_coin and coin % 2 == 1)):
                # Generate the new state
                new_state = (tuple(c for c in coins if c != coin), sum_coins + coin, tax_paid + tax_values[coin], coin)
                # The additional cost of this state is the tax paid for the new coin as we are trying to minimize the total tax paid
                new_cost = g + tax_values[coin]

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The new coin must be added to the list of coins chosen
                    heapq.heappush(queue, (g + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the difference between the goal sum and the sum of the coins chosen so far
    # The heuristic assumes we can choose any of the remaining coins to reach the goal sum, even if the sum of the coins chosen exceeds the goal sum or the even-odd condition is violated, thus reporting a lower cost estimate to reach the goal state, making it admissible
    # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of choosing a coin is the tax paid for the coin, which is always greater than or equal to 1, the decrease in the difference between the goal sum and the sum of the coins chosen
    # Also the cost of the goal state is 0, as the sum of the coins chosen equals the goal sum and there are no more coins to choose
    return goal - state[1]

print(a_star())
