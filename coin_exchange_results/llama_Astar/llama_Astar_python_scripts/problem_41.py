
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the coins that need to be chosen
   goal_sum = 284
   # Define the tax values for each coin
   tax_values = {14: 7, 15: 15, 2: 2, 22: 7, 7: 1, 25: 7, 10: 4, 11: 11, 16: 11, 27: 8, 3: 2, 13: 5, 19: 10, 8: 5, 23: 18, 5: 4, 12: 4, 28: 6, 6: 4, 21: 3, 20: 15, 26: 1, 4: 4, 9: 9, 24: 6, 17: 13}
   # Define the list of coins
   coins = [20, 27, 20, 26, 2, 19, 25, 5, 14, 28, 7, 4, 20, 25, 9, 7, 3, 9, 27, 23, 2, 17, 25, 19, 10, 2, 8, 15, 3, 6, 24, 6, 22, 3, 10, 3, 2, 24, 7, 16, 2, 24, 21, 5, 23, 25, 10, 5, 20, 14, 24, 12, 11, 11, 13]
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in a list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]
  
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie the total sum of the chosen coins equals the goal sum
       if sum(state[0]) == goal_sum:
           return actions


       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the total tax paid does not exceed the goal tax
           if coin not in state[0] and g + tax_values[coin] <= goal_sum:
               # Generate the new state
               new_state = (state[0].copy(), g + tax_values[coin])
               new_state[0].add(coin)
               # The cost so far is the total tax paid so far, as the task is to minimize the total tax paid
               new_cost = g + tax_values[coin]


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the values of the remaining coins to be chosen, minus the goal sum
   # This heuristic relaxes the constraint that the coins must be chosen in increasing or decreasing order, and the tax values must be paid
   # It is admissible because it never overestimates the cost to reach the goal, as each remaining coin must be chosen at least once
   # It's consistent because moving a coin from the remaining coins to the chosen coins reduces the heuristic cost of the successor node by a max of the value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax value of the moved coin) + h(n)
   remaining_coins = goal_sum - sum(state[0])
   return remaining_coins


print(a_star())
