
import heapq


def a_star():
   # Define the initial state of the problem, which is an empty list of coins
   initial_state = []
   # Define the goal state of the problem, which is a sum of 264
   goal_sum = 264
   # Define the list of coins and their tax values
   coins = [19, 2, 25, 9, 6, 24, 4, 26, 17, 11, 11, 2, 17, 2, 5, 6, 3, 3, 3, 18, 26, 18, 21, 3, 5, 8, 12, 15, 8, 18, 24, 5, 19, 7, 18, 25, 12, 13, 12, 2, 25, 16, 17, 16, 3, 3]
   tax_values = {26: 12, 25: 20, 17: 13, 13: 4, 16: 13, 11: 10, 24: 5, 5: 4, 8: 6, 7: 5, 4: 4, 12: 9, 18: 12, 3: 2, 21: 17, 19: 7, 2: 2, 9: 9, 6: 2, 15: 4}
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(initial_state)] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)
       # If the sum of the coins in the current state equals the goal sum, return the actions taken to reach this state
       if sum(state) == goal_sum:
           return actions
       # Generate all possible actions from the current state, which includes adding any of the remaining coins to the current state
       for coin in coins:
           # Check if the new state would be valid, ie the sum of the coins in the new state must not exceed the goal sum and the coin must satisfy the even-odd condition
           if sum(state) + coin <= goal_sum and (not state or (coin >= state[-1] and coin % 2 == 1) or (coin < state[-1] and coin % 2 == 0)):
               # Generate the new state
               new_state = state + [coin]
               # The cost so far is the sum of the tax values of the coins in the new state
               new_cost = g + tax_values[coin]
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if tuple(new_state) not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                   visited_costs[tuple(new_state)] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal_sum):
   # An admissible and consistent heuristic is the difference between the goal sum and the sum of the coins in the current state
   # The heuristic is admissible because it never overestimates the cost to reach the goal state, as the sum of the coins in the goal state must equal the goal sum
   # The heuristic is consistent because the cost of adding a coin to the current state is the tax value of the coin, which is always greater than or equal to the decrease in the heuristic, ie the value of the coin
   return goal_sum - sum(state)


print(a_star())
