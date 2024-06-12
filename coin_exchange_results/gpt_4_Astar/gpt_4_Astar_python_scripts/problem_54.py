
import heapq

def a_star():
    # Define the initial state of the problem
    coins = [4, 17, 14, 12, 1, 3, 12, 10, 14, 9, 30, 20, 11, 17, 11, 16, 22, 17, 30, 5, 10, 16, 19, 27, 6, 18, 20, 19, 32, 25, 30, 15, 30, 21, 19, 25, 31, 33, 19, 10, 8, 16, 8]
    taxes = {1: 1, 31: 13, 25: 13, 11: 3, 3: 1, 10: 8, 33: 14, 8: 4, 9: 9, 4: 1, 20: 4, 12: 8, 27: 13, 30: 14, 16: 10, 18: 9, 32: 5, 21: 20, 6: 4, 5: 5, 22: 11, 17: 11, 19: 2, 14: 10, 15: 6}
    target_sum = 328
    initial_state = (0, 0, [])  # (sum of coins, last coin, list of coins)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element.
    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If the sum of coins equals the target sum, return the list of coins
        if state[0] == target_sum:
            return actions

        # Generate all possible actions from the current state, which includes choosing each coin from the list
        for coin in coins:
            # Check if the new state would be valid, ie the sum of coins does not exceed the target sum and the coin follows the rules
            if state[0] + coin <= target_sum and (coin >= state[1] and coin % 2 == 1 or coin < state[1] and coin % 2 == 0):
                # Generate the new state
                new_state = (state[0] + coin, coin, state[2] + [coin])
                # The cost so far is the sum of taxes of the coins chosen
                new_cost = g + taxes[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, target_sum), new_cost, actions + [coin], new_state))
    return None

def heuristic(state, target_sum):
    # An admissible and consistent heuristic for this problem is the difference between the target sum and the sum of coins in the current state
    # The heuristic relaxes the constraints that the coins must follow the rules and presumes we can choose any coin to reach the target sum
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax of the coin, which is always greater than or equal to 1, the decrease in the difference between the target sum and the sum of coins
    return target_sum - state[0]

print(a_star())
