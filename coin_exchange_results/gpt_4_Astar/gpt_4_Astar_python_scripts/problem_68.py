
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins available, the sum of the coins chosen so far, the tax paid so far, and the last coin chosen
    # The initial state has no coins chosen, thus the sum of the coins chosen and the tax paid are both 0, and the last coin chosen is None
    initial_state = (tuple([5, 29, 12, 96, 4, 13, 8, 23, 14, 25, 18, 23, 36, 32, 17, 37, 34, 7, 9, 32, 29, 37, 30, 40, 99, 9, 2, 40, 35, 14]), 0, 0, None)
    goal_sum = 427
    tax_values = {14: 4, 4: 2, 18: 12, 23: 12, 36: 15, 5: 1, 12: 3, 13: 13, 9: 7, 32: 8, 99: 16, 8: 7, 96: 17, 35: 13, 29: 19, 30: 19, 7: 1, 34: 16, 37: 15, 2: 2, 17: 3, 40: 18, 25: 9}

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
            # Check if the new state, containing the new coin, would be valid; ie the sum of the coins chosen must not exceed the goal sum and the coin must satisfy the even-odd condition
            if sum_coins + coin <= goal_sum and (last_coin is None or (coin < last_coin and coin % 2 == 0) or (coin >= last_coin and coin % 2 == 1)):
                # Generate the new state
                new_state = (tuple([c for c in coins if c != coin]), sum_coins + coin, tax_paid + tax_values[coin], coin)
                # The additional cost of this state is the tax paid for the new coin as we are trying to minimize the total tax paid
                new_cost = g + tax_values[coin]

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # Relaxing the even-odd condition to calculate the heuristic
                    h = heuristic(new_state, goal_sum, tax_values)
                    heapq.heappush(queue, (g + h, new_cost, actions + [coin], new_state))
    return None

def heuristic(state, goal_sum, tax_values):
    # Relax the even-odd condition to compute an admissible and consistent heuristic
    # This heuristic considers the sum of the minimum tax values for the remaining coins needed to reach the goal sum
    # The heuristic assumes we can choose any of the remaining coins to reach the goal sum, thus reporting a lower cost estimate to reach the goal state, making it admissible
    # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to the tax value of the coin used to fill that position in the heuristic
    # Also the cost of the goal state is 0, as the sum of the coins equals the goal sum and there are no remaining coins to choose

    coins, sum_coins, _, _ = state
    remaining_sum = goal_sum - sum_coins
    remaining_coins = sorted([tax_values[coin] for coin in coins if coin <= remaining_sum])
    h = 0
    while remaining_sum > 0 and remaining_coins:
        h += remaining_coins.pop(0)
        remaining_sum -= 1
    return h

print(a_star())
