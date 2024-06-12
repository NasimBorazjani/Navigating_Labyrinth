
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins available, the sum of the coins chosen so far, the tax paid so far, and the value of the last coin chosen
    initial_state = ((29, 25, 15, 12, 40, 23, 36, 22, 16, 24, 51, 34, 46, 29, 20, 14, 21, 27, 15, 31, 15, 17, 9, 42, 30, 45, 14, 14, 30, 16, 44, 32, 6, 15, 5, 41, 18, 43, 36, 31, 27, 26, 6, 44, 33, 23, 7, 19), 0, 0, 0)
    # Define the goal sum of the coins
    goal_sum = 477
    # Define the tax values for each coin
    tax_values = {41: 15, 22: 3, 9: 4, 34: 9, 32: 11, 36: 5, 18: 5, 40: 9, 46: 11, 45: 17, 33: 3, 14: 9, 12: 12, 7: 2, 43: 14, 25: 18, 31: 9, 51: 8, 24: 18, 17: 3, 16: 5, 19: 10, 6: 6, 27: 15, 42: 7, 23: 2, 29: 2, 21: 13, 30: 7, 44: 4, 5: 2, 20: 11, 26: 12, 15: 8}

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
            # Check if the new state would be valid, ie if the sum of the coins chosen so far and the new coin does not exceed the goal sum and if the new coin satisfies the constraints on the value of the coin
            if sum_coins + coin <= goal_sum and ((coin < last_coin and coin % 2 == 0) or (coin >= last_coin and coin % 2 == 1)):
                # Generate the new state
                new_state = (tuple(coin_ for coin_ in coins if coin_ != coin), sum_coins + coin, tax_paid + tax_values[coin], coin)
                # The additional cost of this state is the tax paid for the new coin as we are trying to minimize the total tax paid
                new_cost = g + tax_values[coin]

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # Relaxing the constraints on the value of the coins to calculate the heuristic
                    h = heuristic(new_state, goal_sum)
                    heapq.heappush(queue, (g + h, new_cost, actions + [coin], new_state))
    return None

def heuristic(state, goal_sum):
    # Relax the constraints on the value of the coins to compute an admissible and consistent heuristic
    # This heuristic considers the difference between the goal sum and the sum of the coins chosen so far, filling the remaining sum with the smallest coin available
    # The heuristic assumes xs can be filled with the smallest coin available, even if the constraints on the value of the coins are violated, thus reporting a lower cost estimate to reach the goal state, making it admissible
    # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of choosing a coin is the tax paid for the coin, which is always greater than or equal to the tax paid for the smallest coin
    # Also the cost of the goal state is 0, as the sum of the coins equals the goal sum and there are no more coins to choose

    # Get the smallest coin available
    smallest_coin = min(state[0])
    # Calculate the remaining sum to reach the goal sum
    remaining_sum = goal_sum - state[1]
    # Calculate the number of smallest coins needed to fill the remaining sum
    num_smallest_coins = remaining_sum // smallest_coin
    # Calculate the remaining sum after filling with the smallest coins
    remaining_sum %= smallest_coin
    # If there is still some remaining sum, we need to choose one more coin
    if remaining_sum > 0:
        num_smallest_coins += 1
    # The heuristic is the tax paid for the smallest coin times the number of smallest coins chosen
    h = tax_values[smallest_coin] * num_smallest_coins
    return h

print(a_star())
