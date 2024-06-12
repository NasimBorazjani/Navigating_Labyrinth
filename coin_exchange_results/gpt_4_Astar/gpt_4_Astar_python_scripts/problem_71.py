
import heapq

def a_star():
    # Define the initial state of the problem, which includes the coins available, the sum of the coins chosen so far, the tax paid so far, and the last coin chosen
    # The initial state has no coins chosen, thus the sum of the coins chosen and the tax paid are both 0, and the last coin chosen is None
    initial_state = ((18, 11, 14, 3, 7, 18, 40, 3, 35, 30, 24, 29, 34, 11, 17, 14, 14, 10, 5, 40, 4, 31, 25, 14, 39, 12, 26, 24, 3, 8, 34, 2, 22, 189, 40), 0, 0, None)
    # Define the goal sum of the coins
    goal_sum = 400
    # Define the tax values for each coin
    tax_values = {29: 9, 40: 8, 30: 5, 17: 16, 3: 3, 5: 3, 2: 2, 22: 17, 11: 1, 14: 4, 8: 5, 18: 11, 26: 8, 39: 15, 7: 1, 31: 2, 24: 17, 189: 5, 12: 4, 25: 10, 35: 18, 10: 1, 4: 3, 34: 16}

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

        # If the sum of the coins chosen is equal to the goal sum, return the coins chosen
        if sum_coins_chosen == goal_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing any of the available coins
        for coin in coins_available:
            # Check if the new state would be valid, ie if the sum of the coins chosen so far and the new coin does not exceed the goal sum, and if the new coin is smaller than the last coin chosen, it must be even, otherwise, if it is larger than or equal to the last coin chosen, it must be odd
            if sum_coins_chosen + coin <= goal_sum and (last_coin_chosen is None or (coin < last_coin_chosen and coin % 2 == 0) or (coin >= last_coin_chosen and coin % 2 == 1)):
                # Generate the new state
                new_state = (tuple(coin_ for coin_ in coins_available if coin_ != coin), sum_coins_chosen + coin, tax_paid + tax_values[coin], coin)
                # The cost so far is the tax paid, as the task is to minimize the total tax paid
                new_cost = g + tax_values[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_sum), new_cost, coins_chosen + [coin], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the difference between the goal sum and the sum of the coins chosen so far
    # The heuristic relaxes the constraints that the coins chosen must be unique, that the sum of the coins chosen must not exceed the goal sum, and that if a coin is smaller than the last coin chosen, it must be even, otherwise, if it is larger than or equal to the last coin chosen, it must be odd; ie It presumes we can choose any coin to reach the goal sum
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to 1, the decrease in the difference between the goal sum and the sum of the coins chosen so far
    return goal - state[1]

print(a_star())
