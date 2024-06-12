
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins available, the sum of the coins chosen so far, the tax paid so far, and the value of the last coin chosen
    initial_state = ((36, 40, 17, 7, 15, 23, 18, 26, 29, 24, 15, 43, 13, 12, 31, 33, 30, 31, 26, 37, 14, 31, 43, 25, 30, 7, 37, 27, 221, 13, 26, 21), 0, 0, 0)
    goal_sum = 445
    taxes = {36: 14, 27: 19, 21: 6, 13: 8, 23: 17, 26: 17, 15: 6, 25: 7, 31: 20, 30: 5, 18: 14, 12: 6, 37: 2, 221: 18, 14: 13, 24: 10, 33: 4, 43: 11, 29: 18, 40: 1, 7: 6, 17: 2}

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
            # Check if the new state would be valid, ie if the sum of the coins chosen so far and the new coin does not exceed the goal sum and the new coin satisfies the even-odd condition
            if sum_coins + coin <= goal_sum and (coin >= last_coin and coin % 2 == 1 or coin < last_coin and coin % 2 == 0):
                # Generate the new state
                new_state = (tuple(coin_ for coin_ in coins if coin_ != coin), sum_coins + coin, tax_paid + taxes[coin], coin)
                # The additional cost of this state is the tax of the coin chosen as we are trying to minimize the total tax paid
                new_cost = g + taxes[coin]

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # Relaxing the even-odd condition to calculate the heuristic
                    h = heuristic(new_state, goal_sum, taxes)
                    heapq.heappush(queue, (g + h, new_cost, actions + [coin], new_state))
    return None

def heuristic(state, goal_sum, taxes):
    # Relax the even-odd condition to compute an admissible and consistent heuristic
    # This heuristic considers the sum of the smallest taxes of the remaining coins that add up to the remaining sum to reach the goal sum
    # The heuristic assumes we can choose any of the remaining coins to reach the goal sum, thus reporting a lower cost estimate to reach the goal state, making it admissible
    # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of choosing a coin is the tax of the coin, which is always greater than or equal to the tax used to fill that position in the heuristic
    # Also the cost of the goal state is 0, as the sum of the coins equals the goal sum and there are no more coins to choose

    remaining_sum = goal_sum - state[1]
    remaining_taxes = sorted([taxes[coin] for coin in state[0]])
    h = 0
    for tax in remaining_taxes:
        if remaining_sum - tax >= 0:
            h += tax
            remaining_sum -= tax
        else:
            break
    return h

print(a_star())
