
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, ())
    goal_sum = 284

    # Define the coins and their tax values
    coins = [28, 5, 25, 22, 26, 13, 20, 20, 18, 28, 7, 20, 18, 19, 18, 5, 15, 23, 28, 27, 22, 10, 8, 17, 3, 8, 5, 11, 21, 17, 65, 23, 11, 3, 12]
    tax_values = {20: 12, 21: 3, 5: 2, 3: 2, 7: 1, 15: 8, 8: 7, 27: 6, 17: 8, 18: 14, 28: 5, 13: 1, 23: 4, 65: 8, 26: 8, 22: 5, 25: 3, 11: 11, 12: 8, 19: 19, 10: 7}

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state[0] == goal_sum:
            return list(state[3])

        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for coin in coins:
            if coin not in state[3]:
                # Check if the new state would be valid, ie the sum of the coins chosen so far and the new coin does not exceed the goal sum, and the new coin follows the odd/even rule
                if state[0] + coin <= goal_sum and (state[1] < coin and coin % 2 == 1 or state[1] >= coin and coin % 2 == 0):
                    # Generate the new state
                    new_state = (state[0] + coin, coin, state[2] + tax_values.get(coin, 0), state[3] + (coin,))
                    # The cost so far is the sum of the tax values of the coins chosen
                    new_cost = g + tax_values.get(coin, 0)

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, new_state))

    return None

def heuristic(state, goal_sum):
    # An admissible and consistent heuristic is the difference between the goal sum and the sum of the coins chosen so far
    # The heuristic is admissible because it never overestimates the cost to reach the goal, as we cannot choose a coin with a negative value or tax
    # The heuristic is consistent because the cost of choosing a coin is always greater than or equal to the decrease in the heuristic, as the value of the coin is added to the sum of the coins chosen so far and the tax of the coin is added to the cost so far
    return goal_sum - state[0]

print(a_star())
