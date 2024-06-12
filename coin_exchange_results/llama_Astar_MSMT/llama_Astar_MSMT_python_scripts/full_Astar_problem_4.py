
import heapq


def initialize():
   # Define the list of coins and their tax values
   coins = [14, 19, 3, 8, 5, 107, 4, 10, 9, 2, 11, 7, 11, 11, 4, 10, 17, 14, 18, 10, 21, 13, 2, 13, 19, 5, 8, 4, 7, 6, 10]
   tax_values = {17: 9, 107: 7, 13: 11, 10: 7, 19: 12, 9: 2, 4: 4, 14: 8, 21: 14, 6: 2, 5: 3, 2: 2, 3: 3, 7: 6, 18: 6, 8: 4, 11: 11}
   target_sum = 215
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
       for coin in coins:
           # Check if the coin can be added to the current state, ie the state does not already contain the coin, and the sum of the chosen coins does not exceed the target sum
           if coin not in state and sum(state) + coin <= target_sum:
               # Generate the new state
               new_state = state + (coin,)
               # The cost so far is the sum of the tax values of the chosen coins, as the task is to minimize the total tax paid
               new_cost = g + tax_values[coin]


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, target_sum, tax_values)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [coin], new_state))
   return None




def heuristic(state, target_sum, tax_values):
   # The heuristic function can be a simulation of choosing coins greedily, using the next largest coin as long as the sum of the chosen coins does not exceed the target sum
   # This heuristic is admissible because it is greedy, always opting for the coin that minimizes the total tax paid, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a coin is removed from the state, or equal or less by at most the tax of the coin used to fill the state in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to the tax of the coin used to fill the state in the heuristic) + h(n’)
   h = 0
   # Sort the coins by decreasing value
   coins = sorted(state, reverse=True)
   # Iterate through the coins
   for coin in coins:
       # Check if the coin can be added to the state
       if sum(state) + coin <= target_sum:
           # Add the coin to the state
           state = state + (coin,)
           # Increment the estimated cost to the goal by the tax of the coin
           h += tax_values[coin]
   return h


print(a_star())
