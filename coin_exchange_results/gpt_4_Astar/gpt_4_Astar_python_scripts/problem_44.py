
import heapq

def a_star():
    # Define the initial state of the problem
    coins = [2, 27, 9, 80, 20, 81, 13, 24, 16, 6, 26, 12, 3, 26, 20, 8, 16, 8, 20, 22, 9, 34, 23, 8, 12, 34, 4, 6, 22, 19]
    taxes = {12: 9, 16: 12, 13: 5, 34: 8, 9: 9, 23: 4, 81: 2, 80: 20, 8: 1, 19: 19, 2: 2, 22: 13, 20: 7, 26: 11, 4: 1, 6: 2, 27: 4, 3: 1, 24: 12}
    goal_sum = 346
    initial_state = (0, 0, [], 0)  # (sum_so_far, last_coin, coins_chosen, total_tax)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state[0] == goal_sum:
            return actions

        # Generate all valid actions from the current state, which includes choosing any of the remaining coins
        for coin in coins:
            if coin not in actions:
                # Check if the new state would be valid, ie if the coin is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
                if (coin < state[1] and coin % 2 == 0) or (coin >= state[1] and coin % 2 == 1):
                    # The actions is valid, generate the new state
                    new_sum = state[0] + coin
                    new_tax = state[3] + taxes[coin]
                    new_state = (new_sum, coin, actions + [coin], new_tax)

                    # The cost so far is the total tax paid, as our objective is to minimize the total tax paid
                    new_cost = g + taxes[coin]

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_sum, goal_sum), new_cost, actions + [coin], new_state))

    return None

def heuristic(sum_so_far, goal_sum):
    # An admissible and consistent heuristic is the difference between the goal sum and the sum so far
    # The heuristic relaxes the constraint that the coins chosen must follow the rules about even and odd values, and presumes we can choose any of the remaining coins to reach the goal sum
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax of the coin, which is always greater than or equal to 1, the decrease in the difference between the goal sum and the sum so far, if the coin is chosen toward the goal sum, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the difference between the goal sum and the sum so far would be 0 in the goal state.
    return abs(goal_sum - sum_so_far)

print(a_star())
