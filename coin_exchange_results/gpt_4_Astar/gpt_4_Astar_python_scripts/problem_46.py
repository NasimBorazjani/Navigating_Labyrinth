
import heapq

def a_star():
    # Define the initial state of the problem
    coins = [11, 6, 147, 6, 19, 29, 28, 32, 18, 20, 12, 22, 4, 20, 27, 3, 3, 18, 19, 9, 2, 28, 31, 20, 2, 27, 22, 30, 3]
    taxes = {27: 18, 6: 2, 22: 12, 18: 11, 4: 3, 12: 4, 28: 6, 147: 10, 32: 6, 19: 3, 29: 12, 31: 19, 20: 4, 2: 2, 30: 17, 3: 2, 11: 10, 9: 2}
    target_sum = 324
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

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state[0] == target_sum:
            return actions

        # Generate all valid actions from the current state, which includes choosing any of the remaining coins
        for coin in state[3]:
            # Check if the new state would be valid, ie if the coin is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
            if (not actions or coin < actions[-1] and coin % 2 == 0) or (coin >= actions[-1] and coin % 2 == 1):
                # Generate the new state
                new_state = (state[0] + coin, state[1] + taxes[coin], tuple(coin for coin in state[3] if coin != coin))
                # The cost so far is the sum of the taxes of the chosen coins, as our objective is to minimize the total tax paid
                new_cost = g + taxes[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, target_sum), new_cost, actions + [coin], new_state))

    return None

def heuristic(state, target_sum):
    # An admissible and consistent heuristic is the difference between the target sum and the sum of the chosen coins so far
    # The heuristic relaxes the constraints that the coins must be unique and that the coins must satisfy the even-odd rule, and presumes we can choose any coin to reach the target sum
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of choosing a coin is the tax of the coin, which is always greater than or equal to 1, the decrease in the difference between the target sum and the sum of the chosen coins
    return target_sum - state[0]

print(a_star())
