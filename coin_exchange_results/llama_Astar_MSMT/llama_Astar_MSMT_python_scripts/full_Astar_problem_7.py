
import heapq


def initialize():
   # Define the list of coins and their tax values
   coins = [41, 4, 22, 8, 5, 5, 20, 4, 3, 19, 4, 13, 3, 18, 20, 9, 15, 3, 3, 14, 3, 14, 9, 4, 15, 19, 6, 15, 22, 19, 3, 3, 20, 9, 20, 11, 22, 15, 20]
   tax_values = {20: 11, 15: 13, 9: 7, 8: 3, 3: 1, 6: 3, 5: 2, 13: 11, 4: 4, 22: 11, 19: 19, 11: 1, 14: 2, 41: 16, 18: 18}
   # Define the target sum of the chosen coins
   target_sum = 220
   # Define the initial state of the problem, with no coins chosen and the total tax paid as 0
   initial_state = ([], 0)
   # Initialize the visited_costs dictionary and the priority queue
   visited_costs = {}
   visited_costs[initial_state] = 0
   queue = [(0, 0, [], initial_state)]
  
   return coins, tax_values, target_sum, initial_state, visited_costs, queue
  
def a_star():
  
   coins, tax_values, target_sum, initial_state, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the sum of the chosen coins in the current state equals the target sum, return the actions taken
       if sum(state[0]) == target_sum:
           return actions


       # Generate all possible actions from the current state, which includes choosing each coin from the list
       for coin in coins:
           # Check if the coin can be added to the current state, ie the coin is not already chosen and the total tax paid after adding the coin does not exceed the total tax paid in the current state
           if coin not in state[0] and g + tax_values[coin] <= state[1]:
               # Generate the new state
               new_state = (state[0] + [coin], g + tax_values[coin])
               # The cost so far is the total tax paid in the new state
               new_cost = new_state[1]
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic is the difference between the target sum and the sum of the chosen coins in the new state
                   h = target_sum - sum(new_state[0])
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [coin], new_state))
   return None


print(a_star())
