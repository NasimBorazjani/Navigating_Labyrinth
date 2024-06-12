
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the chosen coins equaling 348
   goal_sum = 348
   # Define the tax values for each coin
   tax_values = {20: 18, 16: 6, 19: 2, 27: 12, 25: 2, 6: 2, 26: 16, 23: 9, 28: 12, 49: 16, 33: 13, 30: 12, 8: 6, 21: 18, 31: 16, 48: 5, 15: 5, 10: 2, 3: 1, 29: 14, 32: 15, 5: 3, 4: 4, 34: 3, 17: 14, 12: 11, 7: 3, 9: 9, 14: 7, 24: 14, 18: 15, 2: 1}
   # Define the list of coins
   coins = [12, 12, 5, 32, 25, 3, 23, 49, 31, 6, 12, 23, 20, 14, 34, 17, 16, 16, 21, 18, 7, 30, 7, 27, 29, 14, 5, 9, 48, 33, 5, 18, 15, 29, 2, 28, 29, 25, 26, 6, 4, 4, 6, 8, 16, 5, 4, 4, 20, 25, 10, 6, 3, 24, 19]
   # Define the set of unique coins
   unique_coins = set(coins)
   # Define the dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in the list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, chosen_coins, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie the sum of the chosen coins equals the goal sum
       if sum(state[0]) == goal_sum:
           return chosen_coins


       # Generate all possible actions from the current state, which includes choosing a coin from the list of unique coins
       for coin in unique_coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the sum of the chosen coins does not exceed the goal sum
           if coin not in state[0] and sum(state[0]) + coin <= goal_sum:
               # Generate the new state
               new_state = (state[0].copy(), state[1])
               new_state[0].add(coin)
               # The cost so far is the total tax paid so far plus the tax of the chosen coin
               new_cost = g + tax_values[coin]
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum, tax_values), new_cost, chosen_coins + [coin], new_state))
   return None


def heuristic(state, goal_sum, tax_values):
   # An admissible and consistent heuristic for this problem is the sum of the tax values of the coins not chosen, plus the tax of the largest coin that can be chosen to reach the goal sum
   # This heuristic relaxes the constraint that the tax for coins of the same value is the same
   # It is admissible because it never overestimates the cost to reach the goal, as each coin not chosen must be taxed at least once
   # It's consistent because moving a coin from the chosen set to the not chosen set reduces the heuristic cost of the successor node by a max of the tax of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax of the moved coin) + h(n)
   h = 0
   not_chosen_coins = unique_coins - state[0]
   for coin in not_chosen_coins:
       h += tax_values[coin]
   # Find the largest coin that can be chosen to reach the goal sum
   remaining_sum = goal_sum - sum(state[0])
   for coin in sorted(not_chosen_coins, reverse=True):
       if coin <= remaining_sum:
           h += tax_values[coin]
           break
   return h


print(a_star())
