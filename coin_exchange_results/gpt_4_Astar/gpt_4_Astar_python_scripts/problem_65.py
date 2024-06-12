
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins available, the sum of the coins chosen so far, the tax paid so far, and the value of the last coin chosen
    # The initial state has no coins chosen, thus the sum of the coins chosen and the tax paid are 0, and the value of the last coin chosen is None
    initial_state = (tuple([9, 30, 18, 32, 31, 20, 34, 9, 12, 18, 14, 16, 29, 37, 37, 6, 24, 10, 10, 35, 23, 4, 30, 121, 31, 16, 35]), 0, 0, None)
    goal_sum = 406
    taxes = {35: 20, 4: 2, 18: 11, 24: 10, 10: 7, 14: 3, 37: 1, 16: 14, 12: 7, 6: 2, 29: 18, 34: 19, 121: 10, 31: 7, 30: 12, 32: 12, 23: 8, 20: 8, 9: 9}

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
            # Check if the new state, with the new coin chosen, would be valid; ie the sum of the coins chosen must not exceed the goal sum and the coin must satisfy the even-odd rule
            if sum_coins + coin <= goal_sum and (last_coin is None or (coin < last_coin and coin % 2 == 0) or (coin >= last_coin and coin % 2 == 1)):
                # Generate the new state
                new_coins = list(coins[:])
                new_coins.remove(coin)
                new_sum_coins = sum_coins + coin
                new_tax_paid = tax_paid + taxes[coin]
                new_state = (tuple(new_coins), new_sum_coins, new_tax_paid, coin)
                # The additional cost of this state is the tax paid for the new coin as we are trying to minimize the total tax paid
                new_cost = g + taxes[coin]

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # Relaxing the even-odd rule to calculate the heuristic
                    h = heuristic(new_state, goal_sum, taxes)
                    heapq.heappush(queue, (g + h, new_cost, actions + [coin], new_state))
    return None

def heuristic(state, goal_sum, taxes):
    # Relax the even-odd rule to compute an admissible and consistent heuristic
    # This heuristic considers the sum of the minimum taxes of the remaining coins needed to reach the goal sum
    # The heuristic assumes we can choose any of the remaining coins to reach the goal sum, thus reporting a lower cost estimate to reach the goal state, making it admissible
    # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of choosing a coin is the tax of the coin, which is always greater than or equal to the tax used to fill that position in the heuristic
    # Also the cost of the goal state is 0, as the sum of the coins equals the goal sum and there are no remaining coins to choose

    remaining_sum = goal_sum - state[1]
    remaining_coins = sorted(list(state[0]), key=lambda x: taxes[x])
    h = 0
    for coin in remaining_coins:
        if coin <= remaining_sum:
            h += taxes[coin]
            remaining_sum -= coin
        if remaining_sum == 0:
            break
    return h

print(a_star())
