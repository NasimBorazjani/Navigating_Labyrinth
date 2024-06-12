
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins, the target sum, the tax values, and the constraints on the coins
    coins = [10, 5, 6, 2, 16, 19, 18, 5, 11, 12, 11, 7, 13, 19, 11, 12, 8, 17, 5, 18, 3, 12, 10, 14, 20, 18, 10, 11, 20, 13, 8, 8, 2, 7, 17, 10, 7, 21, 9, 20, 17, 1, 8, 19, 17, 16, 17, 10, 20, 8, 16, 14, 9]
    target_sum = 211
    tax_values = {7: 2, 3: 2, 18: 1, 13: 3, 2: 2, 19: 17, 16: 6, 10: 1, 9: 9, 12: 7, 8: 7, 6: 3, 21: 18, 11: 10, 14: 13, 1: 1, 5: 5, 20: 18, 17: 14}
    # The initial state is represented as a tuple of the sum of the coins chosen so far, the tax paid so far, the coins chosen so far, and the remaining coins
    initial_state = (0, 0, [], coins)

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Unpack the information encoded in each state
        sum_coins, tax_paid, coins_chosen, remaining_coins = state

        # If the sum of the coins chosen equals the target sum, return the coins chosen
        if sum_coins == target_sum:
            return actions

        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for coin in remaining_coins:
            # Check if the new state, containing the new coin, would be valid; ie the sum of the coins chosen so far and the new coin must not exceed the target sum
            # And the coin must satisfy the constraints on the coins
            if sum_coins + coin <= target_sum and (not coins_chosen or (coin < coins_chosen[-1] and coin % 2 == 0) or (coin >= coins_chosen[-1] and coin % 2 == 1)):
                # Generate the new state
                new_state = (sum_coins + coin, tax_paid + tax_values[coin], coins_chosen + [coin], [c for c in remaining_coins if c != coin])
                # The additional cost of this state is the tax paid for the new coin as we are trying to minimize the total tax paid
                new_cost = g + tax_values[coin]

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # Relaxing the constraints on the coins to calculate the heuristic
                    h = heuristic(new_state, target_sum)
                    heapq.heappush(queue, (g + h, new_cost, actions + [coin], new_state))
    return None

def heuristic(state, target_sum):
    # Relax the constraints on the coins to compute an admissible and consistent heuristic
    # This heuristic considers the remaining sum to reach the target sum, filling the remaining sum with the smallest coin
    # The heuristic assumes we can fill the remaining sum with the smallest coin, even if the constraints on the coins are violated, thus reporting a lower cost estimate to reach the goal state, making it admissible
    # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of choosing a coin is the tax paid for the coin, which is always greater than or equal to the tax paid for the smallest coin
    # Also the cost of the goal state is 0, as the sum of the coins equals the target sum and there is no remaining sum to fill

    # Get the remaining sum to reach the target sum
    remaining_sum = target_sum - state[0]
    # Get the smallest coin
    smallest_coin = min(state[3])
    # Calculate the heuristic as the tax paid for the smallest coin times the number of smallest coins needed to fill the remaining sum
    h = (remaining_sum // smallest_coin) * tax_values[smallest_coin]
    return h

print(a_star())
