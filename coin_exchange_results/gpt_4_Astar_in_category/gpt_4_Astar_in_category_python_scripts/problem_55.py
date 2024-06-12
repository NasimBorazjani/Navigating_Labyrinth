
import heapq


def a_star():
   # Define the initial state of the problem, which is an empty list of coins
   initial_state = []
   # Define the goal state of the problem, which is a list of coins that sum up to 325
   goal_sum = 325
   # Define the list of coins and their tax values
   coins = [12, 26, 9, 14, 11, 25, 28, 17, 18, 18, 9, 16, 2, 11, 31, 25, 4, 23, 9, 3, 24, 22, 3, 14, 32, 30, 19, 7, 4, 22, 33, 13, 25, 15, 14, 28, 20, 3, 4, 3, 32, 10, 6, 29, 25]
   tax_values = {29: 2, 9: 7, 17: 4, 18: 9, 26: 6, 33: 11, 16: 12, 4: 3, 31: 12, 6: 2, 11: 8, 23: 14, 7: 1, 30: 8, 12: 8, 13: 2, 20: 13, 24: 16, 14: 8, 19: 8, 10: 8, 32: 14, 3: 2, 2: 2, 25: 19, 22: 18, 15: 5, 28: 9}

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

       # Generate all possible actions from the current state, which includes adding any of the remaining coins to the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin must not already be in the list and the sum of the coins in the new state must not exceed the goal sum
           if coin not in state and sum(state) + coin <= goal_sum:
               # The coin must be smaller than the previous one and have an even value, or be larger than or equal to the previous coin and have an odd value
               if (not state or (coin < state[-1] and coin % 2 == 0) or (coin >= state[-1] and coin % 2 == 1)):
                   # Generate the new state
                   new_state = state + [coin]
                   # The cost so far is the sum of the tax values of the coins in the list
                   new_cost = g + tax_values[coin]

                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                   if tuple(new_state) not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                       visited_costs[tuple(new_state)] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal_sum):
   # An admissible and consistent heuristic is the difference between the goal sum and the sum of the coins in the current state
   # The heuristic is admissible because it never overestimates the cost to reach the goal, as the sum of the coins in the goal state must equal the goal sum
   # The heuristic is consistent because the cost of adding a coin to the list is the tax value of the coin, which is always greater than or equal to the decrease in the heuristic, ie the value of the coin
   return goal_sum - sum(state)


print(a_star())
