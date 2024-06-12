
import heapq

def a_star():
    # Define the initial state of the problem
    coins = [39, 3, 38, 10, 3, 5, 6, 14, 32, 7, 30, 28, 17, 9, 8, 13, 17, 41, 25, 6, 19, 36, 5, 36, 8, 38, 6, 19, 25, 3, 22, 18, 3, 21, 57, 37, 42, 30, 54, 13, 36, 6, 13, 17, 10, 4, 36]
    taxes = {37: 2, 38: 4, 30: 18, 39: 18, 14: 1, 18: 1, 4: 1, 10: 8, 21: 10, 6: 5, 42: 13, 32: 10, 25: 2, 17: 15, 13: 2, 9: 4, 22: 17, 7: 5, 3: 2, 54: 7, 19: 15, 8: 2, 36: 17, 28: 6, 5: 5, 41: 9, 57: 12}
    goal_sum = 452
    initial_state = (0, 0, 0, [])  # (sum_so_far, tax_so_far, last_coin, coins_chosen)

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
                # The new sum is the sum so far plus the value of the new coin
                new_sum = state[0] + coin
                # The new tax is the tax so far plus the tax of the new coin
                new_tax = state[1] + taxes[coin]
                # The new coin becomes the last coin
                new_last_coin = coin
                # The new coins chosen includes all the coins chosen so far, plus the new coin
                new_coins_chosen = state[3] + [coin]
                # The new state includes all these new values
                new_state = (new_sum, new_tax, new_last_coin, new_coins_chosen)

                # Check if the new state is valid, ie if the sum of the coins chosen is less than or equal to the goal sum, and if the new coin follows the rules regarding even and odd values
                if new_sum <= goal_sum and (new_last_coin >= state[2] and new_last_coin % 2 == 1) or (new_last_coin < state[2] and new_last_coin % 2 == 0):
                    # The cost so far is the total tax paid, as our objective is to minimize the total tax paid
                    new_cost = g + taxes[coin]

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_sum, goal_sum), new_cost, new_state))

    return None

def heuristic(sum_so_far, goal_sum):
    # An admissible and consistent heuristic is the difference between the goal sum and the sum so far
    # The heuristic relaxes the constraint that the coins chosen must follow the rules regarding even and odd values, and presumes we can choose any of the remaining coins to reach the goal sum
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of choosing a new coin is the tax of the coin, which is always greater than or equal to 1, the decrease in the difference between the goal sum and the sum so far, if the coin is chosen
    return goal_sum - sum_so_far

print(a_star())
