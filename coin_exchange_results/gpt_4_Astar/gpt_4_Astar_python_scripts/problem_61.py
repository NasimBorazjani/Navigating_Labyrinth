
import heapq

def a_star():
    # Define the initial state of the problem
    coins = [30, 4, 10, 25, 2, 20, 23, 22, 29, 13, 21, 23, 23, 24, 3, 26, 29, 27, 15, 18, 28, 10, 22, 24, 2, 22, 13, 32, 8, 28, 31, 13, 27, 6, 35, 2, 20, 25, 24, 2, 16, 31, 3, 5, 23, 32, 24, 20, 13, 7, 11, 12]
    taxes = {10: 8, 32: 8, 25: 5, 7: 2, 30: 9, 18: 3, 5: 2, 35: 14, 2: 1, 15: 10, 12: 6, 29: 14, 23: 12, 31: 14, 11: 3, 8: 7, 21: 5, 13: 3, 28: 3, 6: 1, 3: 2, 4: 2, 22: 5, 16: 9, 24: 4, 27: 16, 26: 6, 20: 20}
    goal_sum = 351
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
    # The heuristic relaxes the constraint that the coins must be unique and presumes we can reach the goal sum by adding any number to the sum so far
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving from the current state to a successor state is always 1, which is exactly the decrease in the heuristic, if the successor state is closer to the goal state, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the difference between the goal sum and the sum so far would be 0 in the goal state.
    return abs(goal_sum - sum_so_far)

print(a_star())
