
import heapq


def initialize():
   # Define the list of coins and their tax values
   coins = [13, 10, 12, 10, 16, 7, 9, 14, 13, 18, 36, 11, 7, 14, 7, 8, 19, 7, 39, 13, 3, 18, 20, 4, 3, 18, 15, 2, 19, 16]
   tax_values = {15: 5, 36: 15, 39: 9, 9: 8, 13: 3, 2: 2, 18: 10, 12: 12, 3: 3, 8: 8, 11: 6, 10: 4, 4: 4, 14: 10, 7: 3, 16: 16, 20: 18, 19: 17}
   # The target sum of the chosen coins
   target_sum = 203
   # The initial state is an empty list of chosen coins
   initial_state = []


   visited_costs = {}
   visited_costs[tuple(initial_state)] = 0


   queue = [(0, 0, [], initial_state)]
  
   return coins, tax_values, target_sum, visited_costs, queue
  
def a_star():
  
   coins, tax_values, target_sum, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the sum of the chosen coins in the current state equals the target sum, return the actions taken
       if sum(state) == target_sum:
           return actions


       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the coin can be added to the current state, ie the coin is not already chosen and the sum of the chosen coins does not exceed the target sum
           if coin not in state and sum(state) + coin <= target_sum:
               # Generate the new state
               new_state = state + [coin]
               # The cost so far is the sum of the tax values of the chosen coins, as the task is to minimize the total tax paid
               new_cost = g + tax_values[coin]


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[tuple(new_state)] = new_cost
                   h = heuristic(new_state, target_sum, tax_values)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [coin], new_state))
   return None




def heuristic(state, target_sum, tax_values):
   # The heuristic function can be a simulation of choosing coins greedily, using the next largest coin as long as the sum of the chosen coins does not exceed the target sum
   # This heuristic is admissible because it is greedy, always opting for the coin that minimizes the total tax paid, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a coin is removed from the state, or equal or less by at most the tax of the coin used, as the maximum amount of tax that can be added to the state is by using the largest coin that won't cause an overflow, which is exactly the coin used to fill the state in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to the tax of the coin used) + h(n’)
   h = 0
   # Sort the coins by decreasing value
   coins = sorted(coins, reverse=True)
   # Iterate through the coins
   for coin in coins:
       # Check if the coin can be added to the state
       if coin not in state and sum(state) + coin <= target_sum:
           # Add the coin to the state
           state.append(coin)
           # Increment the estimated cost to the goal by the tax of the coin
           h += tax_values[coin]
   return h


print(a_star())
