
import heapq


def a_star():
   # Define the initial state of the problem, which is an empty list of coins
   initial_state = []
   # Define the goal state of the problem, which is a sum of 230
   goal_state = 230
   # Define the list of coins and their tax values
   coins = [9, 2, 23, 20, 13, 4, 15, 16, 12, 21, 13, 9, 2, 14, 13, 14, 4, 19, 12, 6, 21, 23, 4, 18, 2, 23, 23, 6, 18, 23, 3, 16, 7, 2, 22, 16, 8, 10, 23, 17, 3, 18, 8]
   tax_values = {9: 1, 17: 6, 2: 2, 22: 9, 13: 13, 16: 8, 12: 4, 4: 1, 21: 14, 14: 10, 19: 9, 10: 7, 7: 6, 8: 7, 6: 2, 23: 16, 18: 3, 20: 2, 3: 1, 15: 2}
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(initial_state)] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   queue = [(0, 0, [], initial_state)]
   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)
       # If the sum of the coins in the current state is equal to the goal state, return the actions taken
       if sum(state) == goal_state:
           return actions
       # Generate all possible actions from the current state, which includes adding any of the remaining coins to the current state
       for coin in coins:
           # Check if the new state would be valid, ie the coin must not already be in the state, and the sum of the coins in the new state must not exceed the goal state
           if coin not in state and sum(state) + coin <= goal_state:
               # Check if the coin is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
               if (not state or coin < state[-1]) and coin % 2 == 0 or (state and coin >= state[-1]) and coin % 2 == 1:
                   # Generate the new state
                   new_state = state + [coin]
                   # The cost so far is the sum of the tax values of the coins in the state
                   new_cost = g + tax_values[coin]
                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                   if tuple(new_state) not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                       visited_costs[tuple(new_state)] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the difference between the goal state and the sum of the coins in the current state
   # The heuristic is admissible because it never overestimates the cost to reach the goal state, as the sum of the coins in the state can never exceed the goal state
   # The heuristic is consistent because the cost of adding a coin to the state is always less than or equal to the decrease in the heuristic, which is the value of the coin
   return goal - sum(state)


print(a_star())
