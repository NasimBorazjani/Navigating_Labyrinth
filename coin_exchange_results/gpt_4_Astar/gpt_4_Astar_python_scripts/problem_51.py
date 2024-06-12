
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins available, the sum of the coins chosen so far, the tax paid so far, and the value of the last coin chosen
    initial_state = ([31, 83, 19, 4, 13, 27, 13, 18, 21, 24, 9, 3, 2, 30, 16, 14, 31, 29, 27, 23, 18, 8, 32, 3, 3, 25, 17, 8, 32, 5, 2, 28, 30, 26, 25, 12, 12], 0, 0, 0)
    # Define the goal sum of the coins
    goal_sum = 335
    # Define the tax for each coin
    tax = {32: 1, 19: 12, 3: 1, 27: 14, 5: 3, 9: 5, 13: 11, 14: 10, 28: 6, 31: 15, 8: 8, 18: 18, 17: 7, 2: 2, 12: 9, 24: 16, 83: 6, 23: 9, 16: 15, 29: 4, 25: 5, 26: 18, 4: 1, 21: 10, 30: 10}

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
            # Check if the new state, containing the new coin, would be valid; ie the sum of the coins chosen so far plus the new coin must not exceed the goal sum, and the new coin must be even if it is smaller than the last coin chosen, or odd if it is larger than or equal to the last coin chosen
            if sum_coins + coin <= goal_sum and ((coin < last_coin and coin % 2 == 0) or (coin >= last_coin and coin % 2 == 1)):
                # Generate the new state
                new_state = (coins[:], sum_coins + coin, tax_paid + tax[coin], coin)
                # The additional cost of this state is the tax paid for the new coin as we are trying to minimize the total tax paid
                new_cost = g + tax[coin]

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
    # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of choosing a coin is the tax paid for the coin, which is always greater than or equal to 0, the decrease in the difference between the goal sum and the sum of the coins chosen so far
    # Also the cost of the goal state is 0, as the sum of the coins equals the goal sum and there are no more coins to choose
    return goal_sum - state[1]

print(a_star())
