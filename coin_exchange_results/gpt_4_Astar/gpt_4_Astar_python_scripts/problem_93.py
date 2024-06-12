
import heapq

def a_star():
    # Define the initial state of the problem
    coins = [43, 41, 23, 24, 40, 11, 12, 9, 32, 32, 6, 15, 16, 20, 6, 39, 9, 12, 4, 251, 43, 24, 27, 20, 39, 37, 7, 43, 9, 13, 45, 27, 9, 15, 41, 25]
    taxes = {9: 7, 32: 17, 24: 17, 15: 11, 4: 3, 39: 18, 41: 9, 25: 14, 27: 5, 40: 5, 43: 8, 11: 9, 20: 1, 45: 2, 16: 15, 251: 12, 37: 10, 13: 1, 23: 1, 7: 1, 12: 1, 6: 5}
    goal_sum = 471
    initial_state = (0, 0, [], tuple(coins))

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
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
            # Check if the new state would be valid, ie if the coin is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
            if (not actions or coin < actions[-1]) and coin % 2 == 0 or (actions and coin >= actions[-1]) and coin % 2 == 1:
                # Generate the new state
                new_state = (state[0] + coin, state[1] + taxes[coin], tuple(coin for coin in state[3] if coin != coin))
                # The cost so far is the sum of the taxes of the chosen coins, as our objective is to minimize the total tax paid
                new_cost = g + taxes[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the difference between the goal sum and the current sum of the chosen coins
    # The heuristic relaxes the constraints that the coins must be unique and that the coins must satisfy the even-odd rule, and presumes we can choose any coin to reach the goal sum
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax of the coin, which is always greater than or equal to 1, the decrease in the difference between the goal sum and the current sum, if the coin is chosen
    return goal - state[0]

print(a_star())
