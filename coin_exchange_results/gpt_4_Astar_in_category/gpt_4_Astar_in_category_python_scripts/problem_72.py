
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, ())
    goal_sum = 384

    # Define the coins and their tax values
    coins = [13, 3, 34, 36, 19, 31, 6, 7, 10, 24, 92, 3, 24, 33, 33, 22, 93, 13, 17, 28, 25, 16, 21, 16, 20, 26, 24, 16, 11, 18, 2, 30, 25, 23, 28, 21]
    tax = {3: 1, 23: 1, 34: 8, 17: 14, 20: 16, 11: 5, 28: 7, 13: 3, 22: 19, 16: 4, 26: 20, 93: 7, 31: 11, 6: 2, 36: 12, 33: 15, 18: 1, 19: 2, 7: 7, 21: 7, 10: 9, 24: 11, 30: 4, 25: 7, 2: 2, 92: 19}

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

        # Generate all possible actions from the current state, which includes adding any of the coins to the current sum
        for coin in coins:
            # Check if the new state would be valid, ie the sum of the coins does not exceed the goal sum and the coin follows the rules of being even or odd
            if state[0] + coin <= goal_sum and (state[1] < coin and coin % 2 == 1) or (state[1] > coin and coin % 2 == 0):
                # Generate the new state
                new_state = (state[0] + coin, coin, state[2] + tax[coin], state[3] + (coin,))
                # The cost so far is the sum of the tax values of the coins chosen
                new_cost = g + tax[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The heuristic is the remaining sum to reach the goal, as we are trying to minimize the tax paid
                    h = goal_sum - new_state[0]
                    heapq.heappush(queue, (new_cost + h, new_cost, new_state))

    return None

print(a_star())
