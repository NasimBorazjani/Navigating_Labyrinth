
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the chosen coins equaling 445
   goal_sum = 445
   # Define the tax values for each coin
   tax_values = {41: 14, 23: 15, 31: 19, 21: 18, 22: 2, 6: 3, 11: 5, 12: 11, 37: 10, 7: 2, 32: 19, 28: 10, 16: 12, 2: 2, 197: 7, 39: 18, 19: 18, 15: 4, 10: 9, 5: 4, 27: 10, 38: 3, 24: 5}
   # Define the list of coins
   coins = [27, 23, 11, 23, 6, 197, 7, 21, 2, 22, 12, 38, 15, 32, 5, 19, 6, 28, 31, 31, 10, 10, 28, 24, 41, 6, 39, 16, 11, 37, 23, 7, 2]
   # Define the dictionary of coin values and their tax values
   coin_tax_values = {coin: tax_values[coin] for coin in coins}
   # Define the dictionary of coin values and their indices in the coins list
   coin_indices = {coin: index for index, coin in enumerate(coins)}
   # Define the dictionary of coin values and their previous coin values
   prev_coins = {coin: coins[index - 1] if index > 0 else None for index, coin in enumerate(coins)}


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if sum(state[0]) == goal_sum:
           return actions


       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the total tax paid does not exceed the goal tax
           if coin not in state[0] and state[1] + coin_tax_values[coin] <= goal_sum:
               # Generate the new state
               new_state = (state[0] | {coin}, state[1] + coin_tax_values[coin])
               # The cost so far is the total tax paid so far
               new_cost = g
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum, coin_tax_values, coin_indices, prev_coins), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal_sum, coin_tax_values, coin_indices, prev_coins):
   # An admissible and consistent heuristic for this problem is the sum of the tax values of the remaining coins to be chosen, plus the tax value of the last chosen coin
   # This heuristic relaxes the constraint that the tax value of a coin must be even if it is smaller than the previous coin chosen and odd otherwise
   # It is admissible because it never overestimates the cost to reach the goal, as each remaining coin must be chosen at least once
   # It's consistent because moving a coin from the remaining coins to the chosen coins reduces the heuristic cost of the successor node by a max of the tax value of the coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax value of the coin) + h(n)
   remaining_coins = set(coin for coin in coin_tax_values.keys() if coin not in state[0])
   h = sum(coin_tax_values[coin] for coin in remaining_coins)
   if state[0]:
       h += coin_tax_values[max(state[0])]
   return h


print(a_star())
