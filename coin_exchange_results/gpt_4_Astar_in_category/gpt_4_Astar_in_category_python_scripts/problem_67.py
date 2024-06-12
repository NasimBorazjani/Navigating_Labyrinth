
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, ())
    goal_sum = 384

    # Define the coins and their tax values
    coins = [8, 13, 16, 4, 35, 2, 19, 2, 21, 26, 28, 12, 58, 28, 12, 35, 33, 4, 19, 27, 61, 30, 17, 20, 27, 25, 30, 31, 9, 15, 4, 13, 11, 29]
    tax = {13: 1, 4: 1, 61: 2, 30: 19, 12: 4, 20: 16, 29: 10, 2: 2, 35: 17, 31: 17, 19: 15, 25: 11, 21: 8, 27: 16, 17: 17, 11: 7, 58: 12, 26: 4, 15: 14, 28: 10, 8: 5, 16: 5, 9: 8, 33: 13}

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, state = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state[1] == goal_sum:
            return list(state[3])

        # Generate all valid actions from the current state, which includes adding any of the coins to the current sum
        for coin in coins:
            # Check if the new state would be valid, ie if the coin is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
            if (coin < state[2] and coin % 2 == 0) or (coin >= state[2] and coin % 2 == 1):
                # The actions is valid, generate the new state
                new_state = (state[0] + 1, state[1] + coin, coin, state[3] + (coin,))
                # The cost so far is the sum of the tax values of the coins chosen
                new_cost = g + tax[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the difference between the goal sum and the current sum
    # The heuristic relaxes the constraint that the coins must be unique and presumes we can reach the goal sum by adding the difference to the current sum
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of adding a coin to the current sum is always the tax value of the coin, which is exactly the decrease in the difference between the goal sum and the current sum, if the coin is added to the current sum, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the difference between the goal sum and the current sum would be 0 in the goal state.
    return goal - state[1]

print(a_star())
