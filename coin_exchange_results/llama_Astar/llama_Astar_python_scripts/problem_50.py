
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the chosen coins equaling 351
   goal_sum = 351
   # Define the tax values for each coin
   tax_values = {15: 6, 29: 12, 19: 3, 30: 18, 14: 2, 77: 3, 6: 5, 17: 1, 32: 16, 9: 8, 22: 15, 31: 17, 25: 10, 24: 1, 28: 11, 2: 2, 7: 4, 8: 7, 11: 7, 23: 19, 10: 2, 16: 2}
   # Define the list of coins
   coins = [19, 14, 29, 19, 29, 9, 17, 16, 25, 7, 8, 2, 23, 11, 28, 6, 29, 16, 19, 31, 30, 15, 7, 16, 23, 23, 10, 32, 8, 14, 7, 9, 6, 23, 77, 24, 22, 24, 22]
   # Define the dictionary of coin values and their tax values
   coin_tax = {coin: tax for coin, tax in zip(coins, [tax_values[coin] for coin in coins])}
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
       if sum(chosen_coins) == goal_sum:
           return chosen_coins
       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the total tax paid does not exceed the goal tax
           if coin not in state[0] and g + coin_tax[coin] <= goal_sum:
               # Generate the new state
               new_state = (state[0] | {coin}, g + coin_tax[coin])
               # The cost so far is the total tax paid so far, as the task is to minimize the total tax paid
               new_cost = g
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum, coin_tax, coin_indices), new_cost, chosen_coins + [coin], new_state))
   return None


def heuristic(state, goal_sum, coin_tax, coin_indices):
   # An admissible and consistent heuristic for this problem is the sum of the remaining coins to be chosen, minus the sum of their tax values
   # This heuristic relaxes the constraint that the coins must be chosen in order, as it only considers the remaining coins to be chosen and their tax values
   # It is admissible because it never overestimates the cost to reach the goal, as each remaining coin must be chosen at least once
   # It's consistent because moving a coin from the remaining coins to the chosen coins reduces the heuristic cost of the successor node by a max of the tax value of the moved coin
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax value of the moved coin) + h(n)
   remaining_coins = [coin for coin in coin_tax if coin not in state[0]]
   remaining_coins.sort(key=lambda coin: coin_indices[coin])
   h = sum(remaining_coins) - sum(coin_tax[coin] for coin in remaining_coins)
   return h


print(a_star())
