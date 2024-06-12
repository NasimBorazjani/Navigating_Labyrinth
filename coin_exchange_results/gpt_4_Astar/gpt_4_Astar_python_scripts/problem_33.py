
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins, their tax values, the target sum, and the constraints on the coins
    coins = [9, 11, 7, 9, 12, 19, 29, 21, 11, 10, 26, 22, 18, 29, 19, 11, 18, 23, 26, 16, 18, 4, 22, 25, 17, 18, 12, 23, 3, 17, 17, 15, 22, 25, 27, 2, 26, 22, 21, 28, 10, 23, 15]
    tax_values = {28: 16, 10: 8, 21: 8, 18: 12, 27: 6, 7: 7, 2: 2, 19: 4, 17: 13, 26: 11, 12: 1, 9: 5, 25: 15, 29: 20, 11: 2, 15: 8, 22: 1, 16: 13, 4: 4, 3: 3, 23: 18}
    target_sum = 296

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[()] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen to get to each state in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], ())]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, coins_chosen, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        # The goal state is where the sum of the coins chosen equals the target sum
        if sum(coins_chosen) == target_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for coin in coins:
            # Check if the new state would be valid, ie if the coin is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
            if (not coins_chosen or (coin < coins_chosen[-1] and coin % 2 == 0) or (coin >= coins_chosen[-1] and coin % 2 == 1)) and coin in state:
                # Generate the new state
                new_state = list(state[:])
                new_state.remove(coin)
                new_state = tuple(new_state)
                # The cost so far is the sum of the tax values of the coins chosen, as our objective is to minimize the total tax paid
                new_cost = g + tax_values[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, target_sum - sum(coins_chosen + [coin])), new_cost, coins_chosen + [coin], new_state))
    return None

def heuristic(state, remaining_sum):
    # An admissible and consistent heuristic for this problem is the minimum tax value of the remaining coins times the remaining sum divided by the minimum coin value
    # This heuristic relaxes the constraints that each coin is unique and that the coins must satisfy the constraints on their values, and presumes we can choose the coin with the minimum tax value to reach the remaining sum
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin to reach a successor state is the tax value of the coin, which is always greater than or equal to the minimum tax value, the decrease in the heuristic cost, if the coin is chosen toward the remaining sum, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the remaining sum would be 0 in the goal state.
    if state:
        min_tax_value = min(tax_values[coin] for coin in state)
        min_coin_value = min(state)
        return min_tax_value * (remaining_sum // min_coin_value)
    else:
        return 0

print(a_star())
