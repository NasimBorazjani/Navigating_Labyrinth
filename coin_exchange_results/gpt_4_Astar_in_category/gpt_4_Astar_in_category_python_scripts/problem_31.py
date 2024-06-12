
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, ())
    goal_state = 260

    # Define the coins and their tax values
    coins = [12, 23, 57, 18, 6, 5, 21, 15, 14, 23, 5, 16, 9, 8, 19, 8, 19, 6, 8, 3, 12, 2, 14, 3, 3, 4, 26, 6, 6, 25, 9, 13, 20, 24, 6, 26, 14, 25, 5, 26]
    tax_values = {6: 2, 12: 3, 9: 2, 2: 1, 14: 1, 16: 12, 21: 10, 4: 1, 8: 5, 26: 7, 23: 7, 57: 11, 15: 15, 19: 13, 25: 15, 13: 4, 5: 3, 24: 4, 3: 3, 18: 4, 20: 10}

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
        if state[0] == goal_state:
            return list(state[3])

        # Generate all valid actions from the current state, which includes adding any of the coins to the current sum
        for coin in coins:
            # Check if the coin is valid, ie if the coin is not already used and if it satisfies the even/odd condition
            if coin not in state[3] and (state[1] == 0 or (state[1] < coin and coin % 2 == 1) or (state[1] >= coin and coin % 2 == 0)):
                # The action is valid, generate the new state
                new_state = (state[0] + coin, coin, state[2] + tax_values[coin], state[3] + (coin,))
                # The cost so far is the tax paid, as our objective is to minimize the tax paid
                new_cost = g + tax_values[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the remaining sum to reach the goal
    # The heuristic relaxes the constraint that a coin can only be used once and presumes we can reach the goal sum without paying any tax
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of adding a coin to the sum is always the tax of the coin, which is exactly the decrease in the remaining sum, if the coin is added to the sum, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the remaining sum to reach the goal would be 0 in the goal state.
    return goal - state[0]

print(a_star())
