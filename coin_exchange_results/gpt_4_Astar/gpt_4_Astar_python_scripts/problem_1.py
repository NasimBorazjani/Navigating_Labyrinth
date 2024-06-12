
import heapq

def a_star():
    # Define the initial state of the problem
    initial_state = (0, 0, 0, [])
    # Define the goal state of the problem
    goal_sum = 208
    # Define the coins and their tax values
    coins = [14, 2, 5, 8, 65, 5, 16, 2, 5, 2, 12, 17, 16, 15, 20, 4, 19, 9, 10, 64, 2, 10, 14, 2, 17]
    tax_values = {20: 13, 4: 2, 17: 16, 19: 8, 64: 4, 5: 3, 14: 10, 10: 9, 65: 11, 16: 2, 12: 7, 8: 5, 2: 2, 15: 14, 9: 8}
    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0
    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, [], initial_state)]
    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)
        # If the current state is the goal state, return the actions taken to reach it
        if state[0] == goal_sum:
            return actions
        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for coin in coins:
            # Check if the new state would be valid, ie if the sum of the coins chosen so far and the new coin does not exceed the goal sum
            # and if the new coin is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
            if state[0] + coin <= goal_sum and (state[1] > coin and coin % 2 == 0 or state[1] <= coin and coin % 2 == 1):
                # Generate the new state
                new_state = (state[0] + coin, coin, state[2] + tax_values[coin])
                # The cost so far is the sum of the tax values of the coins chosen, as our objective is to minimize the total tax paid
                new_cost = g + tax_values[coin]
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the difference between the goal sum and the sum of the coins chosen so far
    # The heuristic relaxes the constraint that the coins chosen must satisfy the conditions about their values relative to the previous coin chosen and presumes we can choose any of the remaining coins to reach the goal sum
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to 1, the decrease in the difference between the goal sum and the sum of the coins chosen so far, if the coin is chosen toward the goal sum
    return goal - state[0]

print(a_star())
