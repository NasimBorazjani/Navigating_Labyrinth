
import heapq


def a_star():
   # Define the initial state of the problem, which is an empty list of coins
   initial_state = []
   # Define the goal state of the problem, which is a list of coins that sum up to 309
   goal_sum = 309
   # Define the coins and their tax values
   coins = [84, 2, 8, 16, 21, 10, 15, 4, 17, 16, 4, 85, 30, 13, 28, 2, 2, 11, 18, 9, 25, 5, 24, 14, 20, 30, 6]
   tax_values = {15: 2, 18: 9, 28: 4, 84: 10, 2: 1, 24: 19, 30: 12, 5: 2, 9: 9, 21: 9, 11: 10, 16: 14, 4: 2, 17: 2, 85: 18, 6: 5, 8: 6, 13: 2, 10: 4, 25: 11, 20: 19, 14: 2}
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(initial_state)] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   queue = [(0, 0, [], initial_state)]
   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)
       # If the sum of the coins in the current state equals the goal sum, return the actions taken
       if sum(state) == goal_sum:
           return actions
       # Generate all possible actions from the current state, which includes adding any of the remaining coins to the current state
       for coin in coins:
           # Check if the new state would be valid, ie the coin must be smaller than the previous one and have an even value, or be larger than or equal to the previous coin and have an odd value
           if (not state or (coin < state[-1] and coin % 2 == 0) or (coin >= state[-1] and coin % 2 == 1)) and coin not in state:
               # Generate the new state
               new_state = state + [coin]
               # The cost so far is the sum of the tax values of the coins in the state, as the task is to minimize the total tax paid
               new_cost = g + tax_values[coin]
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if tuple(new_state) not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                   visited_costs[tuple(new_state)] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal_sum):
   # An admissible and consistent heuristic is the difference between the goal sum and the sum of the coins in the current state
   # The heuristic is admissible because it never overestimates the cost to reach the goal, as each coin added to the state increases the sum of the coins in the state by at least 1
   # The heuristic is consistent because the cost of adding a coin to the state is the tax value of the coin, which is always greater than or equal to 1, which is the maximum decrease in the heuristic cost, if the coin is added to the state
   return goal_sum - sum(state)


print(a_star())
