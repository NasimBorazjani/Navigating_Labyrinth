
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins available, the sum of the coins chosen so far, the tax paid so far, and the last coin chosen
    # The initial state has no coins chosen, thus the sum of the coins chosen and the tax paid are both 0, and the last coin chosen is None
    initial_state = (frozenset([18, 20, 11, 6, 81, 3, 9, 5, 14, 19, 30, 2, 19, 3, 9, 22, 21, 29, 6, 25, 10, 18, 27, 26, 25, 13, 15, 16, 3, 5, 23, 26, 25, 31, 15, 12]), 0, 0, None)
    # Define the goal sum of the coins
    goal_sum = 324
    # Define the tax for each coin
    tax = {11: 6, 6: 3, 16: 11, 23: 16, 18: 3, 31: 4, 9: 2, 3: 1, 22: 10, 10: 1, 30: 4, 81: 14, 2: 1, 14: 1, 13: 11, 15: 7, 19: 16, 25: 6, 12: 12, 29: 11, 26: 9, 5: 1, 27: 15, 20: 7, 21: 14}

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

        # Check if the current state is the goal state
        if sum_coins_chosen == goal_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing any of the available coins
        for coin in coins_available:
            # Check if the new state would be valid, ie if the coin is smaller than the last coin chosen, it must have an even value, otherwise, if the coin is larger than or equal to the last coin chosen, it must have an odd value
            if (last_coin_chosen is None or
                (coin < last_coin_chosen and coin % 2 == 0) or
                (coin >= last_coin_chosen and coin % 2 == 1)):
                # Generate the new state
                new_state = (coins_available - {coin}, sum_coins_chosen + coin, tax_paid + tax[coin], coin)
                # The cost so far is the tax paid, as our objective is to minimize the total tax paid
                new_cost = g + tax[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_sum), new_cost, coins_chosen + [coin], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the difference between the goal sum and the sum of the coins chosen so far
    # The heuristic relaxes the constraints that each coin must be unique, that the coins must be chosen in a specific order, and that each coin carries a tax value; ie It presumes we can choose any coin to reach the goal sum, even if it has already been chosen, in any order, and without paying any tax
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to 1, the decrease in the difference between the goal sum and the sum of the coins chosen so far, if the coin is chosen toward the goal sum, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the difference between the goal sum and the sum of the coins chosen would be 0 in the goal state.
    return goal - state[1]

print(a_star())
