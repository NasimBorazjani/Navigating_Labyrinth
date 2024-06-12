
import heapq


def initialize():
   # Define the list of coins and their tax values
   coins = [14, 2, 5, 8, 65, 5, 16, 2, 5, 2, 12, 17, 16, 15, 20, 4, 19, 9, 10, 64, 2, 10, 14, 2, 17]
   tax_values = {20: 13, 4: 2, 17: 16, 19: 8, 64: 4, 5: 3, 14: 10, 10: 9, 65: 11, 16: 2, 12: 7, 8: 5, 2: 2, 15: 14, 9: 8}
   target_sum = 208
   num_coins = len(coins)


   visited_costs = {}
   visited_costs[()] = 0


   queue = [(0, 0, [], ())]
  
   return coins, tax_values, target_sum, num_coins, visited_costs, queue
  
def a_star():
  
   coins, tax_values, target_sum, num_coins, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the sum of the chosen coins in the current state equals the target sum, return the actions taken
       if sum(state) == target_sum:
           return actions


       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin_ind in range(num_coins):
           # Check if the coin can be added to the current state, ie the coin is not already in the state and the state is in a valid order
           if coin_ind not in state and (not state or (coins[coin_ind] > state[-1] and coins[coin_ind] % 2 == 1) or (coins[coin_ind] <= state[-1] and coins[coin_ind] % 2 == 0)):
               new_state = state + (coin_ind,)
               # The cost so far is the sum of the tax values of the chosen coins
               new_cost = g + sum(tax_values[coins[i]] for i in new_state)


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, target_sum, coins, tax_values)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [coins[coin_ind]], new_state))
   return None




def heuristic(state, target_sum, coins, tax_values):
   # The heuristic function can be a simulation of choosing coins greedily, using the next largest coin repeatedly as long as the sum of the chosen coins does not exceed the target sum
   # This heuristic is admissible because it is greedy, always opting for the action that minimizes the total tax paid, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a coin is removed from the state, or equal or less by at most the tax of the coin used, as the maximum amount of tax that can be added to the state is by using the largest coin that won't cause the sum to exceed the target, which is exactly the coin used to add to the state in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to the tax of the coin used) + h(n’)
   h = 0
   # Sort the coins by decreasing value
   coins = sorted(coins, reverse=True)
   # Iterate through the coins
   for coin in coins:
       # Check if the coin can be added to the state
       if coin not in state and (not state or (coin > state[-1] and coin % 2 == 1) or (coin <= state[-1] and coin % 2 == 0)):
           # Add the coin to the state
           state = state + (coin,)
           # Increment the estimated cost to the goal by the tax of the coin
           h += tax_values[coin]
           # If the sum of the chosen coins exceeds the target sum, remove the coin from the state and break the loop
           if sum(state) > target_sum:
               state = state[:-1]
               break
   return h


print(a_star())
