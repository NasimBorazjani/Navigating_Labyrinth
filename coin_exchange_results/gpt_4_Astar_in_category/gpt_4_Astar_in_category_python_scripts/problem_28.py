
import heapq


def a_star():
   # Define the initial state of the problem, which is an empty list of coins
   initial_state = []
   # Define the goal state of the problem, which is a sum of 267
   goal_sum = 267
   # Define the list of coins and their tax values
   coins = [26, 19, 7, 24, 27, 15, 9, 9, 9, 26, 15, 23, 6, 6, 24, 8, 21, 6, 6, 7, 25, 22, 8, 2, 7, 5, 8, 18, 14, 15, 24, 10, 4, 23, 21, 8, 18, 12, 16]
   tax_values = {24: 14, 27: 10, 22: 14, 16: 7, 14: 12, 6: 3, 8: 7, 23: 6, 18: 18, 5: 3, 25: 8, 7: 6, 12: 3, 15: 8, 9: 2, 19: 15, 2: 1, 4: 1, 26: 15, 10: 8, 21: 19}
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
           # Check if the new state would be valid, ie the coin must not already be in the state and the sum of the coins in the new state must not exceed the goal sum
           if coin not in state and sum(state) + coin <= goal_sum:
               # The coin must be smaller than the previous one and have an even value, or be larger than or equal to the previous coin and have an odd value
               if (not state or (coin < state[-1] and coin % 2 == 0) or (coin >= state[-1] and coin % 2 == 1)):
                   # Generate the new state
                   new_state = state + [coin]
                   # The cost so far is the sum of the tax values of the coins in the state
                   new_cost = g + tax_values[coin]
                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                   if tuple(new_state) not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                       visited_costs[tuple(new_state)] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal_sum):
   # An admissible and consistent heuristic is the difference between the goal sum and the sum of the coins in the current state
   # The heuristic is admissible because it never overestimates the cost to reach the goal, as the sum of the coins in the state can only increase
   # The heuristic is consistent because the cost of adding a coin to the state is the tax value of the coin, which is always greater than or equal to the decrease in the heuristic, ie the increase in the sum of the coins in the state
   return goal_sum - sum(state)


print(a_star())
