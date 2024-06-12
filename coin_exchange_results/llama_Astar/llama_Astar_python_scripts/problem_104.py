
import heapq


def a_star():
   # Define the initial state of the problem, as an empty list representing the chosen coins
   initial_state = []
   # Define the goal sum, as 441
   goal_sum = 441
   # Define the tax values for each coin
   tax_values = {6: 4, 18: 3, 38: 1, 23: 2, 16: 8, 12: 2, 4: 2, 24: 13, 28: 17, 30: 17, 1: 1, 9: 9, 27: 8, 11: 4, 37: 16, 41: 19, 13: 3, 31: 8, 44: 8, 22: 7, 43: 13, 10: 3, 17: 8, 36: 7, 39: 3, 25: 17, 40: 10, 8: 6, 32: 16, 14: 4, 2: 1, 42: 3, 3: 2, 5: 2}
   # Define the list of coins
   coins = [18, 23, 23, 36, 27, 10, 25, 14, 6, 43, 6, 31, 5, 43, 3, 13, 16, 8, 11, 6, 39, 44, 41, 28, 12, 8, 1, 14, 22, 23, 11, 24, 37, 9, 2, 31, 27, 10, 9, 38, 37, 4, 4, 17, 18, 36, 18, 32, 3, 12, 4, 42, 8, 4, 4, 16, 30, 40, 13, 41]
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(initial_state)] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in the list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie the sum of the chosen coins equals the goal sum
       if sum(state) == goal_sum:
           return actions


       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the sum of the chosen coins does not exceed the goal sum
           if coin not in state and sum(state) + coin <= goal_sum:
               # Generate the new state
               new_state = state + [coin]
               # The cost so far is the sum of the chosen coins, as our objective is to minimize the sum of the chosen coins
               new_cost = g + coin
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if tuple(new_state) not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                   visited_costs[tuple(new_state)] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum, tax_values), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal_sum, tax_values):
   # An admissible and consistent heuristic for this problem is the sum of the tax values of the coins not chosen, plus the tax value of the largest coin chosen
   # This heuristic relaxes the constraint that the tax for coins of the same value is the same
   # It is admissible because it never overestimates the cost to reach the goal, as each coin not chosen must be chosen at least once
   # It's consistent because moving a coin from the chosen set to the not chosen set reduces the heuristic cost of the successor node by a max of the tax value of the coin moved, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax value of the coin moved) + h(n)
   h = 0
   for coin in set(tax_values.keys()) - set(state):
       h += tax_values[coin]
   if state:
       h += max(tax_values[coin] for coin in state)
   return h


print(a_star())
