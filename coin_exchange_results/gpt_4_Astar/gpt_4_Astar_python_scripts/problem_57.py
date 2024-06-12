
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins, the sum of the coins, the tax paid so far, and the last coin chosen
    initial_state = ([25, 22, 28, 23, 5, 14, 28, 14, 20, 6, 22, 1, 25, 18, 30, 10, 19, 12, 17, 17, 6, 28, 21, 28, 21, 2, 20, 2, 19, 14, 31, 31, 14, 7, 20, 13, 7, 18, 22, 15, 6, 6, 21, 9, 18, 11, 20, 26, 15], 0, 0, 0)
    # Define the goal sum of the coins
    goal_sum = 322
    # Define the tax for each coin
    tax = {11: 1, 14: 4, 7: 2, 25: 4, 12: 5, 20: 19, 13: 6, 15: 11, 30: 18, 1: 1, 2: 2, 31: 6, 10: 2, 23: 1, 6: 2, 21: 18, 18: 8, 28: 15, 17: 5, 26: 6, 22: 6, 9: 1, 19: 2, 5: 4}

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
            # Check if the new state would be valid, ie if the coin is smaller than the last coin chosen, it must have an even value, otherwise, if the coin is larger than or equal to the last coin chosen, it must have an odd value
            if (coin < last_coin and coin % 2 == 0) or (coin >= last_coin and coin % 2 == 1):
                # Generate the new state
                new_state = (coins[:], sum_coins + coin, tax_paid + tax[coin], coin)
                # The cost so far is the tax paid, as the task is to minimize the total tax paid
                new_cost = g + tax[coin]

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(sum_coins, goal_sum), new_cost, actions + [coin], new_state))
    return None

def heuristic(sum_coins, goal_sum):
    # An admissible and consistent heuristic for this problem is the difference between the goal sum and the sum of the coins chosen so far
    # The heuristic relaxes the constraints that the coins must be unique, that the coins must satisfy the even-odd rule, and that the coins have a tax, and presumes we can choose any number of coins to reach the goal sum
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax of the coin, which is always greater than or equal to 1, the decrease in the difference between the goal sum and the sum of the coins chosen so far, if the coin is chosen toward the goal sum, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the difference between the goal sum and the sum of the coins chosen would be 0 in the goal state
    return abs(goal_sum - sum_coins)

print(a_star())
