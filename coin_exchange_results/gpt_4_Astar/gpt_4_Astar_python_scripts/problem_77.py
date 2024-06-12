
import heapq

def a_star():
    # Define the initial state of the problem
    coins = [26, 32, 14, 36, 14, 8, 9, 3, 8, 18, 7, 23, 6, 20, 34, 8, 37, 19, 15, 6, 2, 13, 37, 7, 31, 2, 7, 4, 17, 9, 4, 22, 7, 16, 33, 14, 11, 30, 36, 14, 34, 37, 36, 37, 32, 38, 15, 17, 19, 14]
    taxes = {17: 16, 4: 2, 15: 2, 8: 1, 19: 5, 9: 4, 23: 7, 3: 2, 16: 13, 2: 1, 38: 13, 11: 2, 31: 6, 7: 6, 36: 8, 14: 8, 37: 17, 32: 5, 6: 1, 13: 11, 22: 9, 20: 8, 18: 4, 30: 6, 34: 2, 33: 1, 26: 3}
    goal_sum = 396
    initial_state = (0, 0, [], set(coins))

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Unpack the information encoded in each state
        current_sum, last_coin, coins_set = state

        # If the current sum of coins equals the goal sum, return the actions that led to this state
        if current_sum == goal_sum:
            return actions

        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for coin in coins_set:
            # Check if the new state would be valid, ie if the coin is smaller than the last coin chosen, it must have an even value, otherwise, if the coin is larger than or equal to the last coin chosen, it must have an odd value
            if (coin < last_coin and coin % 2 == 0) or (coin >= last_coin and coin % 2 == 1):
                # Generate the new state
                new_state = (current_sum + coin, coin, coins_set - {coin})
                # The cost so far is the sum of the taxes of the coins chosen, as our objective is to minimize the total tax paid
                new_cost = g + taxes[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The heuristic is the remaining sum to reach the goal sum, divided by the maximum coin value, multiplied by the minimum tax value, as we are trying to minimize the total tax paid
                    h = (goal_sum - current_sum) / max(coins_set) * min([taxes[coin] for coin in coins_set])
                    heapq.heappush(queue, (g + h, new_cost, actions + [coin], new_state))
    return None

print(a_star())
