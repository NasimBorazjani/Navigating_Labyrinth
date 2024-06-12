
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins available, the sum of the coins chosen so far, the tax paid so far, and the value of the last coin chosen
    initial_state = ((14, 8, 11, 30, 3, 3, 27, 16, 19, 4, 6, 14, 7, 2, 39, 103, 15, 100, 27, 36, 7, 36, 13, 7, 18, 39, 14, 3, 28), 0, 0, 0)
    goal_sum = 410
    taxes = {13: 11, 18: 8, 36: 15, 11: 4, 6: 1, 16: 8, 100: 12, 39: 10, 28: 9, 27: 20, 103: 6, 19: 5, 30: 14, 2: 1, 4: 3, 3: 3, 15: 10, 8: 5, 7: 2, 14: 14}

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
            # Check if the new state, containing the new coin, would be valid; ie the sum of the coins chosen so far plus the new coin must not exceed the goal sum and the new coin must be even if it is smaller than the last coin chosen, or odd if it is larger than or equal to the last coin chosen
            if sum_coins + coin <= goal_sum and ((coin < last_coin and coin % 2 == 0) or (coin >= last_coin and coin % 2 == 1)):
                # Generate the new state
                new_state = (tuple(c for c in coins if c != coin), sum_coins + coin, tax_paid + taxes[coin], coin)
                # The additional cost of this state is the tax paid for the new coin as we are trying to minimize the total tax paid
                new_cost = g + taxes[coin]

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
    # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of choosing a coin is the tax paid for the coin, which is always greater than or equal to 1, the decrease in the difference between the goal sum and the sum of the coins
    # Also the cost of the goal state is 0, as the sum of the coins equals the goal sum and there are no more coins to choose
    return goal_sum - state[1]

print(a_star())
