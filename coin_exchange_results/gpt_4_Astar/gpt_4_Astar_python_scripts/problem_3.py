
import heapq

def a_star():
    # Define the initial state of the problem
    coins = [13, 19, 9, 4, 18, 17, 2, 14, 17, 17, 8, 6, 4, 10, 19, 37, 20, 19, 14, 7, 6, 11, 21, 9, 3, 10, 21, 20, 2, 17, 2]
    taxes = {14: 2, 18: 9, 11: 10, 9: 6, 10: 9, 13: 10, 37: 9, 6: 5, 2: 2, 4: 1, 8: 3, 19: 10, 17: 7, 7: 6, 3: 3, 21: 3, 20: 4}
    goal_sum = 215
    initial_state = (0, 0, [], 0)  # (sum_so_far, last_coin, coins_chosen, total_tax)

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
        if state[0] == goal_sum:
            return actions

        # Generate all valid actions from the current state, which includes choosing any of the remaining coins
        for coin in coins:
            if coin not in actions:
                # Check if the new state would be valid, ie if the sum of the coins chosen so far and the new coin does not exceed the goal sum
                # and if the new coin is smaller than the last one chosen, it must be even, otherwise, if it's larger or equal, it must be odd
                if state[0] + coin <= goal_sum and ((coin < state[1] and coin % 2 == 0) or (coin >= state[1] and coin % 2 == 1)):
                    # Generate the new state
                    new_state = (state[0] + coin, coin, actions + [coin], state[3] + taxes[coin])
                    # The cost so far is the total tax paid, as our objective is to minimize the total tax paid
                    new_cost = g + taxes[coin]

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the difference between the goal sum and the sum of the coins chosen so far
    # The heuristic relaxes the constraint that the coins chosen must follow the rules about their order and parity, and presumes we can choose any of the remaining coins to reach the goal sum
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax of the coin, which is always greater than or equal to 1, the decrease in the difference between the goal sum and the sum of the coins chosen so far, if the coin is chosen toward the goal sum
    return goal - state[0]

print(a_star())
