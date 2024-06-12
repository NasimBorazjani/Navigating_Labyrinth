
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins available, the sum of the coins chosen so far, the tax paid so far, and the value of the last coin chosen
    # The initial state has no coins chosen, thus the sum of the coins chosen and the tax paid so far are 0, and the value of the last coin chosen is None
    initial_state = (tuple([22, 25, 37, 5, 46, 10, 23, 23, 3, 6, 34, 32, 34, 2, 3, 8, 4, 28, 32, 24, 15, 38, 17, 35, 9, 12, 12, 22, 34, 48, 39, 30, 7, 18, 10, 46, 30, 36, 49, 27, 22, 19, 9, 24, 43, 15]), 0, 0, None)
    # Define the goal sum of the coins
    goal_sum = 463
    # Define the tax values for each coin
    tax_values = {18: 11, 17: 7, 7: 6, 43: 2, 22: 3, 24: 11, 9: 3, 36: 10, 46: 4, 10: 3, 39: 5, 5: 5, 35: 15, 28: 8, 15: 2, 34: 6, 27: 3, 38: 11, 30: 20, 23: 18, 25: 10, 12: 1, 4: 1, 49: 16, 37: 6, 48: 17, 2: 2, 8: 4, 3: 1, 6: 3, 19: 10, 32: 19}

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen to get to each state in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, coins_chosen, state = heapq.heappop(queue)

        # Unpack the information encoded in each state
        coins_available, sum_coins_chosen, tax_paid, last_coin_chosen = state

        # If the sum of the coins chosen is the goal sum, return the coins chosen
        if sum_coins_chosen == goal_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing any of the available coins
        for coin in coins_available:
            # Check if the new state would be valid, ie if the sum of the coins chosen so far and the new coin does not exceed the goal sum, and if the new coin is smaller than the last coin chosen, it must have an even value, otherwise, if the new coin is larger than or equal to the last coin chosen, it must have an odd value
            if sum_coins_chosen + coin <= goal_sum and (last_coin_chosen is None or (coin < last_coin_chosen and coin % 2 == 0) or (coin >= last_coin_chosen and coin % 2 == 1)):
                # Generate the new state
                new_state = (tuple(coin for coin in coins_available if coin != coin), sum_coins_chosen + coin, tax_paid + tax_values[coin], coin)
                # The cost so far is the tax paid, as the task is to minimize the total tax paid
                new_cost = g + tax_values[coin]

                # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_sum), new_cost, coins_chosen + [coin], new_state))
    return None

def heuristic(state, goal_sum):
    # An admissible and consistent heuristic for this problem is the difference between the goal sum and the sum of the coins chosen so far
    # The heuristic relaxes the constraints that the coins chosen must be unique, that the sum of the coins chosen must not exceed the goal sum, and that if a coin is smaller than the last coin chosen, it must have an even value, otherwise, if a coin is larger than or equal to the last coin chosen, it must have an odd value; ie It presumes we can choose any coin to reach the goal sum
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to 1, the decrease in the difference between the goal sum and the sum of the coins chosen so far, if the coin is chosen toward the goal sum, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the difference between the goal sum and the sum of the coins chosen would be 0 in the goal state.
    return goal_sum - state[1]

print(a_star())
