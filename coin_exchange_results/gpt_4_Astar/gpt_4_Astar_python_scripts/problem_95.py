
import heapq

def a_star():
    # Define the initial state of the problem
    initial_state = (0, 0, 0, 0, [])
    # Define the goal state of the problem
    goal_sum = 488
    # Define the coins and their tax values
    coins = [26, 8, 19, 9, 36, 23, 42, 40, 13, 34, 40, 25, 11, 38, 10, 41, 19, 34, 91, 18, 14, 27, 14, 43, 42, 13, 2, 27, 90, 13, 3, 4, 44, 7, 48, 40, 35, 40, 10, 12, 25]
    tax_values = {44: 20, 11: 4, 19: 3, 4: 4, 10: 3, 14: 9, 90: 18, 48: 12, 91: 5, 8: 4, 7: 5, 9: 5, 12: 2, 42: 18, 36: 6, 35: 10, 34: 12, 25: 7, 27: 1, 3: 2, 26: 15, 40: 8, 43: 1, 18: 8, 23: 1, 13: 3, 41: 8, 38: 13, 2: 2}
    # Define the number of coins
    num_coins = len(coins)
    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0
    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [], initial_state)]
    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)
        # Unpack the information encoded in each state
        current_sum, last_coin, current_tax, current_coins = state
        # If the current sum is equal to the goal sum, return the actions
        if current_sum == goal_sum:
            return actions
        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for i in range(num_coins):
            coin = coins[i]
            # Check if the new state would be valid, ie if the coin is smaller than the last coin chosen, it must have an even value, otherwise, if the coin is larger than or equal to the last coin chosen, it must have an odd value
            if (coin < last_coin and coin % 2 == 0) or (coin >= last_coin and coin % 2 == 1):
                # Generate the new state
                new_sum = current_sum + coin
                new_tax = current_tax + tax_values[coin]
                new_coins = current_coins + [coin]
                new_state = (new_sum, coin, new_tax, new_coins)
                # The cost so far is the total tax paid, as our objective is to minimize the total tax paid
                new_cost = g + tax_values[coin]
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_sum, goal_sum), new_cost, actions + [coin], new_state))
    return None

def heuristic(current_sum, goal_sum):
    # An admissible and consistent heuristic for this problem is the difference between the current sum and the goal sum
    # The heuristic relaxes the constraints that the coins must be unique and that the coins must satisfy the even/odd rule, and presumes we can add any amount to the current sum to reach the goal sum
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to 1, the decrease in the difference between the current sum and the goal sum, if the coin is chosen
    return goal_sum - current_sum

print(a_star())
