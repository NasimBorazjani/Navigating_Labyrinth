
import heapq


def a_star():
   # Define the initial state of the problem, which is an empty list of coins
   initial_state = []
   # Define the goal state of the problem, which is a list of coins that sum up to 412
   goal_sum = 412
   # Define the list of coins and their tax values
   coins = [13, 30, 19, 13, 34, 12, 16, 21, 24, 39, 37, 32, 3, 5, 30, 37, 29, 20, 15, 23, 30, 24, 12, 21, 19, 10, 26, 29, 3, 23, 20, 40, 22, 13, 2, 36, 8, 40, 6, 24, 24, 11, 26, 37, 16, 57, 39, 21, 17]
   tax_values = {2: 2, 21: 6, 24: 9, 26: 2, 5: 3, 29: 10, 10: 7, 13: 13, 30: 17, 36: 15, 3: 1, 32: 7, 8: 5, 20: 2, 22: 3, 57: 19, 40: 8, 6: 4, 23: 8, 39: 3, 16: 5, 37: 6, 12: 9, 11: 11, 34: 6, 17: 2, 15: 10, 19: 17}
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(initial_state)] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)
       # If the sum of the coins in the current state equals the goal sum, return the actions taken
       if sum(state) == goal_sum:
           return actions
       # Generate all possible actions from the current state, which includes adding any of the remaining coins to the list of chosen coins
       for coin in coins:
           # Check if the new state would be valid, ie the coin must not already be in the list of chosen coins
           if coin not in state:
               # And the coin must be smaller than the previous one and have an even value, or be larger than or equal to the previous coin and have an odd value
               if (not state or (coin < state[-1] and coin % 2 == 0) or (coin >= state[-1] and coin % 2 == 1)):
                   # Generate the new state
                   new_state = state + [coin]
                   # The cost so far is the sum of the tax values of the chosen coins, as the task is to minimize the total tax paid
                   new_cost = g + tax_values[coin]
                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                   if tuple(new_state) not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                       visited_costs[tuple(new_state)] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal_sum):
   # An admissible and consistent heuristic is the difference between the goal sum and the sum of the coins in the current state
   # The heuristic is admissible because it never overestimates the cost to reach the goal, as each coin added to the list of chosen coins increases the sum of the coins by its value
   # The heuristic is consistent because the cost of adding a coin to the list of chosen coins is the tax value of the coin, which is always greater than or equal to the decrease in the heuristic, which is the value of the coin
   return goal_sum - sum(state)


print(a_star())
