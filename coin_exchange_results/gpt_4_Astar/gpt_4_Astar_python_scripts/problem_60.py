
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins, the target sum, the tax values, and the constraints on the coins
    coins = [28, 2, 4, 7, 11, 26, 14, 8, 23, 29, 18, 13, 26, 21, 10, 26, 8, 33, 9, 15, 4, 21, 19, 3, 7, 10, 4, 7, 16, 16, 11, 33, 12, 23, 5, 3, 26, 7, 17, 30, 22, 22, 6, 16, 18, 25, 26, 11, 13, 23, 17, 11, 20, 12]
    target_sum = 339
    tax_values = {10: 6, 18: 17, 33: 15, 16: 16, 3: 2, 30: 18, 13: 3, 21: 17, 23: 4, 12: 1, 7: 6, 17: 7, 4: 2, 6: 5, 2: 2, 11: 5, 14: 14, 29: 1, 20: 7, 8: 3, 15: 7, 28: 3, 26: 8, 19: 11, 9: 9, 22: 4, 5: 5, 25: 5}
    initial_state = (0, 0, 0, [])

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Unpack the information encoded in each state
        sum_coins, last_coin, tax_paid, coins_chosen = state

        # If the sum of the coins chosen equals the target sum, return the coins chosen
        if sum_coins == target_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for coin in coins:
            # Check if the new state, containing the new coin, would be valid; ie the coin must satisfy the constraints on the coins
            if (coin < last_coin and coin % 2 == 0) or (coin >= last_coin and coin % 2 == 1):
                # Generate the new state
                new_state = (sum_coins + coin, coin, tax_paid + tax_values[coin], coins_chosen + [coin])
                # The additional cost of this state is the tax paid for the coin as we are trying to minimize the total tax paid
                new_cost = g + tax_values[coin]

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # Relaxing the constraints on the sum of the coins and the constraints on the coins to calculate the heuristic
                    h = heuristic(new_state, target_sum)
                    heapq.heappush(queue, (g + h, new_cost, actions + [coin], new_state))
    return None

def heuristic(state, target_sum):
    # Relax the constraints on the sum of the coins and the constraints on the coins to compute an admissible and consistent heuristic
    # This heuristic considers the difference between the target sum and the sum of the coins chosen so far
    # The heuristic assumes we can choose any coin to reach the target sum, thus reporting a lower cost estimate to reach the goal state, making it admissible
    # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of choosing a coin is the tax paid for the coin, which is always greater than or equal to 0, the decrease in the difference between the target sum and the sum of the coins chosen so far
    # Also the cost of the goal state is 0, as the sum of the coins equals the target sum and there are no more coins to choose

    sum_coins = state[0]
    return target_sum - sum_coins

print(a_star())
