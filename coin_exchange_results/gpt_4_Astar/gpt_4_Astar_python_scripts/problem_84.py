
import heapq

def a_star():
    # Define the initial state of the problem
    initial_state = (0, 0, 0, [])
    # Define the goal state of the problem
    goal_sum = 426
    # Define the coins and their tax values
    coins = [17, 4, 35, 10, 42, 11, 10, 11, 2, 14, 29, 31, 33, 3, 38, 4, 32, 9, 19, 14, 4, 39, 6, 36, 31, 25, 40, 8, 33, 31, 11, 34, 18, 2, 32, 40, 4, 16, 1, 36, 37, 3, 33, 20, 10, 8, 9, 20, 14, 35, 36, 22, 35, 4]
    tax_values = {37: 11, 10: 3, 36: 8, 32: 3, 3: 1, 18: 16, 14: 5, 35: 5, 16: 15, 8: 5, 42: 20, 29: 4, 6: 1, 25: 9, 11: 4, 20: 15, 39: 6, 38: 14, 34: 6, 40: 11, 9: 2, 17: 6, 19: 8, 4: 4, 22: 20, 31: 3, 1: 1, 33: 18, 2: 2}
    # Define the visited costs dictionary
    visited_costs = {}
    visited_costs[initial_state] = 0
    # Define the priority queue
    queue = [(0, 0, [], initial_state)]
    # While there are states in the queue
    while queue:
        # Pop the state with the lowest cost from the queue
        _, g, actions, state = heapq.heappop(queue)
        # If the current state is the goal state, return the actions
        if state[0] == goal_sum:
            return actions
        # Generate all possible actions from the current state
        for coin in coins:
            # Check if the coin can be added to the current state
            if coin + state[0] <= goal_sum and (state[1] == 0 or (coin >= state[1] and coin % 2 == 1) or (coin < state[1] and coin % 2 == 0)):
                # Generate the new state
                new_state = (coin + state[0], coin, state[2] + tax_values[coin], actions + [coin])
                # Calculate the cost of the new state
                new_cost = g + tax_values[coin]
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost, new_cost, actions + [coin], new_state))
    return None

print(a_star())
