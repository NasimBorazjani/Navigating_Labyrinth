
import heapq

def a_star():
    # Define the initial state of the problem
    coins = [23, 27, 20, 21, 8, 2, 2, 3, 21, 26, 16, 33, 22, 3, 25, 17, 5, 31, 3, 9, 12, 30, 11, 10, 7, 13, 2, 21, 8, 16, 5, 18, 32, 27, 7, 32, 7, 10, 11, 33, 18, 30, 7, 24, 21, 4, 25, 4, 23, 21, 23, 15, 26, 10]
    taxes = {16: 1, 18: 1, 9: 1, 11: 5, 5: 3, 2: 1, 21: 1, 33: 3, 7: 1, 4: 1, 30: 8, 23: 10, 17: 8, 15: 7, 13: 6, 20: 8, 32: 4, 10: 6, 3: 1, 12: 7, 27: 6, 31: 5, 22: 1, 26: 20, 24: 5, 8: 4, 25: 9}
    goal_sum = 334
    initial_state = (0, 0, 0, [])  # (sum_so_far, last_coin, total_tax, coins_chosen)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, state = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state[0] == goal_sum:
            return state[3]

        # Generate all valid actions from the current state, which includes choosing any of the remaining coins
        for coin in coins:
            if coin not in state[3]:
                # Check if the new state would be valid, ie if the coin is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
                if (coin < state[1] and coin % 2 == 0) or (coin >= state[1] and coin % 2 == 1):
                    # The actions is valid, generate the new state
                    new_sum = state[0] + coin
                    new_tax = state[2] + taxes[coin]
                    new_state = (new_sum, coin, new_tax, state[3] + [coin])

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_tax < visited_costs[new_state]:
                        visited_costs[new_state] = new_tax
                        heapq.heappush(queue, (g + heuristic(new_sum, goal_sum), new_tax, new_state))

    return None


def heuristic(sum_so_far, goal_sum):
    # An admissible and consistent heuristic is the difference between the goal sum and the sum so far
    # The heuristic relaxes the constraint that the coins chosen must follow the rules about even and odd values, and presumes we can choose any coin to reach the goal sum
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax of the coin, which is always greater than or equal to 1, the decrease in the difference between the goal sum and the sum so far, if the coin is chosen
    return goal_sum - sum_so_far


print(a_star())
