
import heapq

def a_star():
    # Define the initial state of the problem
    initial_state = (0, 0, 0, 0, [])
    # Define the goal state of the problem
    goal_sum = 267
    # Define the coins and their taxes
    coins = [26, 19, 7, 24, 27, 15, 9, 9, 9, 26, 15, 23, 6, 6, 24, 8, 21, 6, 6, 7, 25, 22, 8, 2, 7, 5, 8, 18, 14, 15, 24, 10, 4, 23, 21, 8, 18, 12, 16]
    taxes = {24: 14, 27: 10, 22: 14, 16: 7, 14: 12, 6: 3, 8: 7, 23: 6, 18: 18, 5: 3, 25: 8, 7: 6, 12: 3, 15: 8, 9: 2, 19: 15, 2: 1, 4: 1, 26: 15, 10: 8, 21: 19}
    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0
    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, initial_state)]
    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, state = heapq.heappop(queue)
        # If the current state is the goal state, return the actions taken to reach it
        if state[0] == goal_sum:
            return state[4]
        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for coin in coins:
            # Check if the new state would be valid, ie if the sum of the coins chosen so far and the new coin does not exceed the goal sum, and if the new coin follows the rules of the problem
            if state[0] + coin <= goal_sum and (coin >= state[1] and coin % 2 == 1 or coin < state[1] and coin % 2 == 0):
                # Generate the new state
                new_state = (state[0] + coin, coin, state[2] + taxes[coin], state[3] + 1, state[4] + [coin])
                # The cost so far is the total tax paid, as our objective is to minimize the total tax paid
                new_cost = g + taxes[coin]
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The heuristic is the remaining sum to reach the goal, as we are trying to minimize the total tax paid
                    h = goal_sum - new_state[0]
                    heapq.heappush(queue, (g + h, new_cost, new_state))
    return None

print(a_star())
