
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins available, the sum of the coins chosen so far, the tax paid so far, and the value of the last coin chosen
    # The initial state has no coins chosen, thus the sum of the coins chosen and the tax paid so far are 0, and the value of the last coin chosen is None
    initial_state = (tuple([38, 36, 40, 31, 39, 29, 36, 31, 16, 14, 16, 45, 40, 45, 257, 8, 39, 16, 2, 41, 9, 26, 22, 24]), 0, 0, None)
    goal_sum = 452
    tax_values = {9: 6, 14: 9, 24: 8, 26: 12, 16: 6, 45: 14, 8: 3, 22: 8, 38: 9, 40: 14, 31: 9, 257: 11, 36: 2, 2: 1, 41: 6, 29: 6, 39: 4}

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
            # Check if the new state, with the new coin chosen, would be valid; ie the sum of the coins chosen so far, with the addition of the new coin, must not exceed the goal sum
            # And if the coin chosen is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
            if sum_coins + coin <= goal_sum and (last_coin is None or (coin < last_coin and coin % 2 == 0) or (coin >= last_coin and coin % 2 == 1)):
                # Generate the new state
                new_state = (tuple([c for c in coins if c != coin]), sum_coins + coin, tax_paid + tax_values[coin], coin)
                # The additional cost of this state is the tax paid for the new coin as we are trying to minimize the total tax paid
                new_cost = g + tax_values[coin]

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The coin chosen must be added to the actions
                    heapq.heappush(queue, (g + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the difference between the goal sum and the sum of the coins chosen so far
    # The heuristic relaxes the constraints that the coins chosen must be unique, that the sum of the coins chosen must not exceed the goal sum, and that if the coin chosen is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
    # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
    # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of choosing a coin is the tax paid for the coin, which is always greater than or equal to 1, the decrease in the difference between the goal sum and the sum of the coins chosen so far
    # Also the cost of the goal state is 0, as the sum of the coins chosen equals the goal sum and there are no more coins to choose
    return goal - state[1]

print(a_star())
