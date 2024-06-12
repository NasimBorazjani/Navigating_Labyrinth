
import heapq

def a_star():
    # Define the initial state of the problem
    coins = [9, 2, 23, 20, 13, 4, 15, 16, 12, 21, 13, 9, 2, 14, 13, 14, 4, 19, 12, 6, 21, 23, 4, 18, 2, 23, 23, 6, 18, 23, 3, 16, 7, 2, 22, 16, 8, 10, 23, 17, 3, 18, 8]
    taxes = {9: 1, 17: 6, 2: 2, 22: 9, 13: 13, 16: 8, 12: 4, 4: 1, 21: 14, 14: 10, 19: 9, 10: 7, 7: 6, 8: 7, 6: 2, 23: 16, 18: 3, 20: 2, 3: 1, 15: 2}
    goal_sum = 230
    initial_state = (0, 0, [], 0, 0)  # (sum_so_far, tax_so_far, coins_chosen, last_coin, last_coin_index)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [], 0, 0)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, last_coin, last_coin_index = heapq.heappop(queue)

        # Check if the current state is the goal state
        if sum(actions) == goal_sum:
            return actions

        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for i in range(last_coin_index, len(coins)):
            coin = coins[i]
            # Check if the new state would be valid, ie if the coin is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
            if (coin < last_coin and coin % 2 == 0) or (coin >= last_coin and coin % 2 == 1):
                # Generate the new state
                new_sum = sum(actions) + coin
                new_tax = g + taxes[coin]
                new_actions = actions + [coin]
                new_state = (new_sum, new_tax, new_actions, coin, i + 1)

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_tax < visited_costs[new_state]:
                    visited_costs[new_state] = new_tax
                    heapq.heappush(queue, (new_tax + heuristic(new_sum, goal_sum), new_tax, new_actions, coin, i + 1))
    return None

def heuristic(sum_so_far, goal_sum):
    # An admissible and consistent heuristic for this problem is the difference between the goal sum and the sum so far
    # The heuristic relaxes the constraints that the coins must be unique and the coins must satisfy the even-odd rule, and presumes we can choose any coin to reach the goal sum
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax of the coin, which is always greater than or equal to 1, the decrease in the difference between the goal sum and the sum so far, if the coin is chosen toward the goal sum, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the difference between the goal sum and the sum so far would be 0 in the goal state
    return abs(goal_sum - sum_so_far)

print(a_star())
