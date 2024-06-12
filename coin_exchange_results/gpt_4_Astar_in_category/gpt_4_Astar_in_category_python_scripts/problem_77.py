
import heapq


def a_star():
   # Define the initial state of the problem, which is an empty list of coins
   initial_state = []
   # Define the goal state of the problem, which is a sum of 396
   goal_state = 396
   # Define the coins and their tax values
   coins = [26, 32, 14, 36, 14, 8, 9, 3, 8, 18, 7, 23, 6, 20, 34, 8, 37, 19, 15, 6, 2, 13, 37, 7, 31, 2, 7, 4, 17, 9, 4, 22, 7, 16, 33, 14, 11, 30, 36, 14, 34, 37, 36, 37, 32, 38, 15, 17, 19, 14]
   tax_values = {17: 16, 4: 2, 15: 2, 8: 1, 19: 5, 9: 4, 23: 7, 3: 2, 16: 13, 2: 1, 38: 13, 11: 2, 31: 6, 7: 6, 36: 8, 14: 8, 37: 17, 32: 5, 6: 1, 13: 11, 22: 9, 20: 8, 18: 4, 30: 6, 34: 2, 33: 1, 26: 3}
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(initial_state)] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   queue = [(0, 0, [], initial_state)]
   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)
       # If the sum of the coins in the current state equals the goal state, return the actions taken
       if sum(state) == goal_state:
           return actions
       # Generate all possible actions from the current state, which includes adding any of the remaining coins to the state
       for coin in coins:
           # Check if the new state would be valid, ie the sum of the coins in the new state must not exceed the goal state
           # And the coin must satisfy the constraints on the value of the coin relative to the previous coin chosen
           if (sum(state) + coin <= goal_state and
               (not state or (state[-1] <= coin and coin % 2 == 1) or (state[-1] > coin and coin % 2 == 0))):
               # Generate the new state
               new_state = state + [coin]
               # The cost so far is the sum of the tax values of the coins chosen, as the task is to minimize the total tax paid
               new_cost = g + tax_values[coin]
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if tuple(new_state) not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                   visited_costs[tuple(new_state)] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the difference between the goal state and the sum of the coins in the current state
   # The heuristic is admissible because it never overestimates the cost to reach the goal state, as the minimum tax value of a coin is 1, and thus the minimum cost to add a coin to the state is 1
   # The heuristic is consistent because the cost of adding a coin to the state is always greater than or equal to 1, which is exactly the decrease in the heuristic, if the coin is added to the state
   return goal - sum(state)


print(a_star())
