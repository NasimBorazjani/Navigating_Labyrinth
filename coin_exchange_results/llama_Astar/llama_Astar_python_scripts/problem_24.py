
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the coins that need to be chosen
   goal_sum = 305
   # Define the tax values for each coin
   tax_values = {24: 5, 26: 16, 28: 20, 2: 1, 22: 16, 25: 11, 27: 7, 11: 4, 6: 3, 99: 17, 8: 5, 7: 5, 5: 3, 23: 5, 4: 4, 98: 16, 16: 3, 29: 5, 20: 19}
   # Define the list of coins
   coins = [25, 29, 8, 11, 8, 25, 20, 16, 6, 4, 98, 7, 28, 24, 27, 16, 23, 26, 26, 99, 2, 7, 22, 7, 5, 24, 2]
   # Define the dictionary of coin values and their tax values
   coin_tax = {coin: tax for coin, tax in zip(coins, tax_values[25]*len(coins))}
   # Define the dictionary of coin values and their indices in the coins list
   coin_indices = {coin: index for index, coin in enumerate(coins)}
   # Define the dictionary of coin values and their previous coin values
   coin_prev = {coin: coins[index - 1] if index > 0 else None for index, coin in enumerate(coins)}
   # Define the dictionary of coin values and their next coin values
   coin_next = {coin: coins[index + 1] if index < len(coins) - 1 else None for index, coin in enumerate(coins)}


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if sum(chosen_coins) == goal_sum:
           return actions


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
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum, coin_tax, coin_prev, coin_next), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal_sum, coin_tax, coin_prev, coin_next):
   # An admissible and consistent heuristic for this problem is the sum of the tax values of the remaining coins to be chosen
   # This heuristic relaxes the constraint that the tax for coins of the same value is the same
   # It is admissible because it never overestimates the cost to reach the goal, as each remaining coin must be chosen at least once
   # It's consistent because moving a coin from one state to another reduces the heuristic cost of the successor node by a max of the tax value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax value of the moved coin) + h(n)
   remaining_coins = set(coin for coin in coin_tax if coin not in state[0])
   h = sum(coin_tax[coin] for coin in remaining_coins)
   return h


print(a_star())
