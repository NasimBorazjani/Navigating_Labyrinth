
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, tuple(sorted([21, 20, 21, 11, 23, 16, 16, 16, 3, 20, 2, 19, 16, 21, 18, 7, 20, 3, 16, 18, 7, 22, 3, 22, 7, 21, 12, 22, 5, 6, 17, 16, 8, 8, 14, 4, 18, 9, 4, 20, 2], reverse=True)))
    goal_sum = 228
    tax_values = {6: 1, 7: 3, 9: 1, 18: 1, 2: 1, 11: 7, 5: 3, 12: 2, 3: 3, 22: 6, 14: 3, 20: 15, 4: 3, 17: 4, 16: 8, 23: 18, 21: 16, 19: 2, 8: 6}

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state[0] == goal_sum:
            return actions

        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for coin in state[3]:
            # Check if the new state would be valid, ie the sum of the coins chosen so far and the new coin does not exceed the goal sum
            # And the coin chosen is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
            if state[0] + coin <= goal_sum and (state[1] > coin and coin % 2 == 0 or state[1] <= coin and coin % 2 == 1):
                # Generate the new state
                new_state = (state[0] + coin, coin, state[2] + tax_values[coin], tuple([c for c in state[3] if c != coin]))
                # The cost so far is the sum of the tax values of the coins chosen, as the task is to minimize the total tax paid
                new_cost = g + tax_values[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))
    return None

def heuristic(state, goal_sum):
    # An admissible and consistent heuristic for this problem is the difference between the goal sum and the sum of the coins chosen so far
    # This heuristic relaxes the constraint that the coins chosen must satisfy the conditions on their relative values and presumes we can choose any of the remaining coins to reach the goal sum
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax value of the coin, which is always greater than or equal to 1, which is exactly the decrease in the difference between the goal sum and the sum of the coins chosen so far, if the coin is chosen. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
    return goal_sum - state[0]

print(a_star())
