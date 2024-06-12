
import heapq

def a_star():
    # Define the initial state of the problem
    initial_state = (0, 0, 0, [])
    # Define the goal state of the problem
    goal_state = 289
    # Define the coins and their tax values
    coins = [25, 22, 26, 12, 18, 12, 5, 6, 6, 21, 28, 26, 6, 26, 9, 11, 27, 24, 16, 1, 12, 5, 10, 23, 11, 10, 28, 2, 3, 7, 23, 28, 27, 12, 3, 3, 27, 21, 13, 8, 18, 25, 6, 7, 9, 25, 18, 18, 23, 12, 11, 15, 2, 16]
    tax_values = {10: 6, 24: 14, 5: 3, 3: 1, 16: 6, 27: 10, 13: 1, 12: 4, 21: 17, 8: 2, 28: 10, 6: 3, 1: 1, 18: 2, 25: 14, 11: 3, 23: 7, 7: 6, 26: 16, 15: 4, 2: 1, 9: 3, 22: 8}
    # Define the number of coins
    num_coins = len(coins)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state[0] == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for i in range(state[1], num_coins):
            # The new state is valid if the sum of the coins chosen so far and the new coin does not exceed the goal state
            if state[0] + coins[i] <= goal_state:
                # The new state is also valid if the new coin is smaller than the previous one and has an even value, or if the new coin is larger than or equal to the previous coin and has an odd value
                if (state[2] > coins[i] and coins[i] % 2 == 0) or (state[2] <= coins[i] and coins[i] % 2 == 1):
                    # Generate the new state
                    new_state = (state[0] + coins[i], i + 1, coins[i], state[3] + [coins[i]])
                    # The cost so far is the sum of the tax values of the coins chosen, as our objective is to minimize the total tax paid
                    new_cost = g + tax_values[coins[i]]

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [coins[i]], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the difference between the goal state and the sum of the coins chosen so far
    # The heuristic relaxes the constraint that the coins chosen must satisfy the conditions on their values and presumes we can choose any of the remaining coins to reach the goal state
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to 1, the decrease in the difference between the goal state and the sum of the coins chosen so far
    return goal - state[0]

print(a_star())
