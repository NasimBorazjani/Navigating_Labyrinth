
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the coins to be chosen, which is 324
   goal_sum = 324
   # Define the tax values for each coin
   tax_values = {27: 18, 6: 2, 22: 12, 18: 11, 4: 3, 12: 4, 28: 6, 147: 10, 32: 6, 19: 3, 29: 12, 31: 19, 20: 4, 2: 2, 30: 17, 3: 2, 11: 10, 9: 2}
   # Define the list of coins
   coins = [11, 6, 147, 6, 19, 29, 28, 32, 18, 20, 12, 22, 4, 20, 27, 3, 3, 18, 19, 9, 2, 28, 31, 20, 2, 27, 22, 30, 3]
   # Define the dictionary of coin values and their indices in the list
   coin_indices = {coin: i for i, coin in enumerate(coins)}
   # Define the dictionary of coin values and their tax values
   coin_taxes = {coin: tax_values[coin] for coin in coins}
   # Define the dictionary of coin values and their next coin values
   next_coin_values = {coin: coins[i + 1] if i + 1 < len(coins) else None for i, coin in enumerate(coins)}
   # Define the dictionary of coin values and their previous coin values
   prev_coin_values = {coin: coins[i - 1] if i > 0 else None for i, coin in enumerate(coins)}


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
           if coin not in state[0] and g + coin_taxes[coin] <= goal_sum:
               # Generate the new state
               new_state = (state[0] | {coin}, g + coin_taxes[coin])
               # The cost so far is the total tax paid so far
               new_cost = g
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum, coin_taxes, coin_indices, next_coin_values, prev_coin_values), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal_sum, coin_taxes, coin_indices, next_coin_values, prev_coin_values):
   # An admissible and consistent heuristic for this problem is the sum of the tax values of the remaining coins to be chosen, plus the tax value of the next coin to be chosen minus the tax value of the previous coin chosen
   # This heuristic relaxes the constraint that the tax value of a coin must be greater than the tax value of the previous coin chosen, and the tax value of a coin must be less than the tax value of the next coin to be chosen
   # It is admissible because it never overestimates the cost to reach the goal, as each remaining coin must be chosen at least once
   # It's consistent because moving a coin from the remaining coins to the chosen coins reduces the heuristic cost of the successor node by a max of the tax value of the coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax value of the coin) + h(n)
   h = 0
   for coin in coin_taxes:
       if coin not in state[0]:
           h += coin_taxes[coin]
   # If there are no remaining coins to choose, the heuristic cost of the goal state is 0
   if not h:
       return 0
   # Otherwise, add the tax value of the next coin to be chosen minus the tax value of the previous coin chosen
   else:
       next_coin = next_coin_values[max(state[0], key=lambda coin: coin_indices[coin])]
       prev_coin = prev_coin_values[max(state[0], key=lambda coin: coin_indices[coin])]
       if next_coin is not None and prev_coin is not None:
           h += coin_taxes[next_coin] - coin_taxes[prev_coin]
   return h


print(a_star())
