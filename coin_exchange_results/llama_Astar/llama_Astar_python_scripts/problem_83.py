
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the chosen coins equaling 411
   goal_sum = 411
   # Define the tax values for each coin
   tax_values = {10: 7, 2: 2, 14: 12, 15: 8, 13: 10, 9: 1, 38: 17, 117: 2, 16: 13, 25: 11, 31: 3, 32: 2, 22: 10, 7: 4, 12: 3, 4: 1, 40: 2, 34: 4, 41: 9, 30: 8, 11: 10, 26: 13, 28: 6, 3: 2, 37: 17, 5: 5, 21: 3, 24: 13}
   # Define the list of coins
   coins = [12, 5, 22, 10, 4, 26, 26, 31, 13, 30, 37, 14, 14, 38, 9, 30, 7, 16, 21, 37, 4, 24, 10, 41, 13, 16, 3, 40, 24, 10, 41, 13, 16, 3, 28, 31, 22, 30, 32, 38, 25, 10, 4, 30]
   # Define the additional constraints on the coins
   constraints = [(10, 7), (2, 2), (14, 12), (15, 8), (13, 10), (9, 1), (38, 17), (117, 2), (16, 13), (25, 11), (31, 3), (32, 2), (22, 10), (7, 4), (12, 3), (4, 1), (40, 2), (34, 4), (41, 9), (30, 8), (11, 10), (26, 13), (28, 6), (3, 2), (37, 17), (5, 5), (21, 3), (24, 13)]
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in a list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]
  
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie the sum of the chosen coins equals the goal sum
       if sum(state[0]) == goal_sum:
           return actions


       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the sum of the chosen coins does not exceed the goal sum
           if coin not in state[0] and sum(state[0]) + coin <= goal_sum:
               # Generate the new state
               new_state = (state[0] | {coin}, g + tax_values[coin])
               # The cost so far is the tax paid so far, as the task is to minimize the tax paid
               new_cost = g + tax_values[coin]


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum, tax_values), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal_sum, tax_values):
   # An admissible and consistent heuristic for this problem is the sum of the tax values of the remaining coins to be chosen, plus the tax value of the largest coin that can be chosen to reach the goal sum
   # This heuristic relaxes the constraint that the tax for coins of the same value is the same
   # It is admissible because it never overestimates the cost to reach the goal, as each remaining coin must be chosen at least once
   # It's consistent because moving a coin from the remaining coins to the chosen coins reduces the heuristic cost of the successor node by a max of the tax value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax value of the moved coin) + h(n)
   remaining_coins = [coin for coin in tax_values if coin not in state[0]]
   remaining_coins.sort(reverse=True)
   h = sum(tax_values[coin] for coin in remaining_coins)
   for coin in remaining_coins:
       if sum(state[0]) + coin <= goal_sum:
           h -= tax_values[coin]
           break
   return h


print(a_star())
