
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins available, the sum of the coins chosen so far, the last coin chosen, and the total tax paid so far
    initial_state = ((3, 6, 9, 10, 13, 15, 18, 5, 21, 19, 12, 15, 5, 9, 4, 16, 8, 4, 7, 7, 7, 2, 16, 14, 18, 3, 89, 21, 12, 10, 7, 14, 4, 11, 6, 20), 0, None, 0)
    goal_sum = 229
    taxes = {14: 1, 89: 13, 2: 2, 5: 2, 4: 4, 6: 6, 8: 2, 16: 5, 21: 4, 20: 2, 18: 9, 11: 10, 10: 3, 12: 12, 15: 5, 13: 1, 3: 1, 19: 19, 7: 7, 9: 3}

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Unpack the information encoded in each state
        coins, sum_coins, last_coin, total_tax = state

        # If the sum of the coins chosen so far equals the goal sum, return the coins chosen
        if sum_coins == goal_sum:
            return actions

        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for coin in coins:
            # Check if the new state, containing the new coin, would be valid; ie the sum of the coins chosen so far plus the new coin must not exceed the goal sum and the new coin must be smaller than the last coin chosen and have an even value or be larger than or equal to the last coin chosen and have an odd value
            if sum_coins + coin <= goal_sum and (last_coin is None or (coin < last_coin and coin % 2 == 0) or (coin >= last_coin and coin % 2 == 1)):
                # Generate the new state
                new_state = (tuple(c for c in coins if c != coin), sum_coins + coin, coin, total_tax + taxes[coin])
                # The additional cost of this state is the tax of the new coin as we are trying to minimize the total tax paid
                new_cost = g + taxes[coin]

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The new coin must be added to the actions
                    heapq.heappush(queue, (g + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the difference between the goal sum and the sum of the coins chosen so far
    # The heuristic assumes we can choose any of the remaining coins to reach the goal sum, even if the coin is larger than the last coin chosen and has an even value or is smaller than the last coin chosen and has an odd value, thus reporting a lower cost estimate to reach the goal state, making it admissible
    # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of choosing a coin is the tax of the coin, which is always greater than or equal to 1, the decrease in the difference between the goal sum and the sum of the coins chosen so far
    # Also the cost of the goal state is 0, as the sum of the coins chosen equals the goal sum and there are no more coins to choose
    return goal - state[1]

print(a_star())
