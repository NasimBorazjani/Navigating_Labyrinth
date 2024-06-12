
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total value of the coins that adds up to 210
   goal_value = 210
   # Define the tax values for each coin
   tax_values = {9: 9, 6: 1, 13: 4, 2: 1, 16: 3, 14: 4, 19: 16, 20: 2, 15: 3, 7: 3, 18: 14, 17: 15, 4: 2, 5: 5, 8: 8, 21: 10, 12: 11, 11: 7, 3: 2}
   # Define the list of coins
   coins = [17, 19, 5, 17, 13, 2, 12, 4, 4, 15, 19, 7, 18, 15, 4, 6, 9, 2, 4, 11, 21, 17, 20, 4, 8, 2, 19, 16, 2, 12, 8, 16, 18, 3, 18, 13, 3, 15, 7, 18, 4, 14, 3, 5, 8, 7, 19, 9, 17, 5, 17, 6, 3, 5, 15]
   # Define the dictionary of coin values and their tax values
   coin_tax_values = {coin: tax_values[coin] for coin in coins}
   # Define the dictionary of coin values and their indices in the coins list
   coin_indices = {coin: index for index, coin in enumerate(coins)}
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in a list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]
  
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, chosen_coins, state = heapq.heappop(queue)
       # Check if the current state is the goal state
       if sum(state[0]) == goal_value:
           return chosen_coins
       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the total value of the chosen coins does not exceed the goal value
           if coin not in state[0] and sum(state[0]) + coin <= goal_value:
               # Generate the new state
               new_state = (state[0] | {coin}, state[1] + coin_tax_values[coin])
               # The cost so far is the total tax paid so far, as the task is to minimize the total tax paid
               new_cost = g + coin_tax_values[coin]
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_value, coin_tax_values, coin_indices), new_cost, chosen_coins + [coin], new_state))
   return None


def heuristic(state, goal_value, coin_tax_values, coin_indices):
   # An admissible and consistent heuristic for this problem is the sum of the tax values of the remaining coins to be chosen, plus the tax value of the largest coin that can be chosen to reach the goal value
   # This heuristic relaxes the constraint that the coins must be chosen in increasing order of their values
   # It is admissible because it never overestimates the cost to reach the goal, as each remaining coin must be chosen at least once
   # It's consistent because moving a coin from the remaining coins to the chosen coins reduces the heuristic cost of the successor node by a max of the tax value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax value of the moved coin) + h(n)
   remaining_coins = [coin for coin in coin_tax_values if coin not in state[0]]
   remaining_coins.sort(reverse=True)
   h = sum(coin_tax_values[coin] for coin in remaining_coins)
   for coin in remaining_coins:
       if sum(state[0]) + coin <= goal_value:
           h -= coin_tax_values[coin]
           break
   return h


print(a_star())
