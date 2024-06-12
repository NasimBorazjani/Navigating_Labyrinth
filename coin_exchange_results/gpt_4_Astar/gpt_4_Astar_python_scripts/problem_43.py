
import heapq

def a_star():
    # Define the initial state of the problem
    coins = [69, 32, 32, 6, 19, 13, 21, 68, 32, 16, 21, 29, 20, 13, 21, 24, 26, 5, 23, 18, 16, 24, 2, 17, 15, 30, 26]
    taxes = {30: 3, 20: 11, 24: 15, 26: 6, 68: 2, 29: 5, 13: 2, 2: 1, 17: 2, 32: 11, 18: 4, 15: 9, 5: 3, 21: 11, 69: 19, 6: 3, 16: 4, 23: 17, 19: 15}
    goal_sum = 322
    initial_state = (0, 0, [], tuple(coins))

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Unpack the information encoded in each state
        state_sum, last_coin, state_coins = state

        # If the sum of the coins in the current state is the goal sum, return the actions
        if state_sum == goal_sum:
            return actions

        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for coin in state_coins:
            # Check if the new state would be valid, ie if the coin is smaller than the last coin chosen, it must have an even value, otherwise, if the coin is larger than or equal to the last coin chosen, it must have an odd value
            if (coin < last_coin and coin % 2 == 0) or (coin >= last_coin and coin % 2 == 1):
                # Generate the new state
                new_state_sum = state_sum + coin
                new_state_coins = list(state_coins)
                new_state_coins.remove(coin)
                new_state = (new_state_sum, coin, tuple(new_state_coins))
                # The additional cost of this state is the tax of the coin
                new_cost = g + taxes[coin]

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The heuristic is the difference between the goal sum and the sum of the coins in the current state
                    h = heuristic(new_state_sum, goal_sum)
                    heapq.heappush(queue, (g + h, new_cost, actions + [coin], new_state))
    return None

def heuristic(state_sum, goal_sum):
    # An admissible and consistent heuristic for this problem is the difference between the goal sum and the sum of the coins in the current state
    # The heuristic relaxes the constraints that the coins must be unique and that the coins must satisfy the even-odd rule, thus reporting a lower cost estimate to reach the goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax of the coin, which is always greater than or equal to 1, the decrease in the difference between the goal sum and the sum of the coins in the current state
    return abs(goal_sum - state_sum)

print(a_star())
