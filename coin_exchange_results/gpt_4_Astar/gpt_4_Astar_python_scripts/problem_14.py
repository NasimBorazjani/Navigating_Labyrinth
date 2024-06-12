
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins available, the sum of the coins chosen so far, the tax paid so far, and the value of the last coin chosen
    initial_state = ((9, 18, 7, 20, 4, 12, 5, 5, 18, 5, 2, 11, 5, 16, 19, 8, 10, 9, 12, 14, 17, 6, 14, 16, 20, 10, 10, 13, 4, 13, 7, 14, 14, 10, 2, 7, 14, 11, 16, 10, 10, 5, 14, 20, 4, 17), 0, 0, 0)
    # Define the goal sum of the coins
    goal_sum = 206
    # Define the tax values for each coin
    tax_values = {17: 16, 8: 8, 6: 6, 16: 12, 5: 4, 14: 12, 18: 9, 12: 1, 19: 12, 4: 2, 7: 3, 10: 7, 11: 7, 13: 6, 2: 1, 9: 1, 20: 10}

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

        # If the sum of the coins chosen so far is equal to the goal sum, return the coins chosen
        if sum_coins_chosen == goal_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing any of the available coins
        for coin in coins_available:
            # Check if the new state would be valid, ie if the coin is smaller than the last coin chosen, it must have an even value, otherwise, if the coin is larger than or equal to the last coin chosen, it must have an odd value
            if (coin < last_coin_chosen and coin % 2 == 0) or (coin >= last_coin_chosen and coin % 2 == 1):
                # Generate the new state
                new_state = (tuple(coin_ for coin_ in coins_available if coin_ != coin), sum_coins_chosen + coin, tax_paid + tax_values[coin], coin)
                # The cost so far is the tax paid, as the task is to minimize the total tax paid
                new_cost = g + tax_values[coin]

                # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_sum), new_cost, coins_chosen + [coin], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the difference between the goal sum and the sum of the coins chosen so far
    # The heuristic relaxes the constraints that the coins chosen must be unique, that the coins chosen must follow the odd-even rule, and that the tax must be paid for each coin chosen; ie It presumes we can choose any coin to reach the goal sum, even if it has already been chosen, and that we do not have to pay any tax
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax paid for that coin, which is always greater than or equal to 1, the decrease in the difference between the goal sum and the sum of the coins chosen so far, if the coin is chosen
    return goal - state[1]

print(a_star())
