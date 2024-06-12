
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, ())
    goal_state = 359

    # Define the coins and their tax values
    coins = [23, 10, 22, 30, 5, 16, 2, 28, 25, 26, 30, 25, 35, 32, 10, 4, 24, 32, 34, 12, 11, 5, 5, 18, 16, 24, 3, 12, 11, 5, 2, 7, 19, 34, 7, 30, 17, 11, 16, 10, 31, 31, 34, 27, 3, 24]
    tax = {24: 9, 26: 11, 17: 7, 7: 4, 12: 4, 35: 18, 5: 5, 31: 8, 2: 2, 3: 1, 27: 14, 34: 3, 30: 1, 23: 6, 4: 2, 10: 8, 18: 18, 25: 15, 28: 4, 32: 19, 11: 7, 16: 6, 19: 11, 22: 5}

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

        # Generate all valid actions from the current state, which includes adding any of the coins to the total
        for coin in coins:
            # Check if the new state would be valid, ie if the coin is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
            if (state[1] > coin and coin % 2 == 0) or (state[1] <= coin and coin % 2 == 1):
                # The actions is valid, generate the new state
                new_state = (state[0] + coin, coin, state[2] + tax[coin], state[3] + (coin,))
                # The cost so far is the total tax paid, as our objective is to minimize the total tax paid
                new_cost = g + tax[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the difference between the goal state and the current state
    # The heuristic relaxes the constraint that the coins must be unique and presumes we can reach the goal state by adding the difference to the current state
    # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
    # The heuristic is consistent because the cost of moving to a successor node is always 1, which is exactly the decrease in the heuristic, if the successor node is closer to the goal state, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the difference between the goal state and itself would be 0.
    return goal - state[0]

print(a_star())
