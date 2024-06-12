
import heapq

def initialize():
   # Define the list of coins and their corresponding tax values
   coins = [14, 2, 5, 8, 65, 5, 16, 2, 5, 2, 12, 17, 16, 15, 20, 4, 19, 9, 10, 64, 2, 10, 14, 2, 17]
   tax_values = {20: 13, 4: 2, 17: 16, 19: 8, 64: 4, 5: 3, 14: 10, 10: 9, 65: 11, 16: 2, 12: 7, 8: 5, 2: 2, 15: 14, 9: 8}
   target_sum = 208

   visited_costs = {}
   visited_costs[(0, 0, 0)] = 0

   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   queue = [(0, 0, [], (0, 0, 0))]
  
   return coins, tax_values, target_sum, visited_costs, queue
  
def a_star():
  
   coins, tax_values, target_sum, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # Unpack the information encoded in each state
       total_value, prev_coin, total_tax = state

       # If the total value of the chosen coins equals the target sum, return the list of coins chosen
       if total_value == target_sum:
           return actions

       # Generate all possible actions from the current state, which includes choosing the next coin from the list
       for coin in coins:
           # Check if the coin has not been chosen yet and the total value of the chosen coins plus the new coin does not exceed the target sum
           if coin not in actions and total_value + coin <= target_sum:
               # Check if the coin follows the rules of being even if smaller than the previous coin and odd if larger or equal to the previous coin
               if (coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0):
                   # Calculate the tax for the current coin
                   coin_tax = tax_values[coin]
                   # Calculate the total tax paid so far
                   new_total_tax = total_tax + coin_tax
                   # Generate the new state
                   new_state = (total_value + coin, coin, new_total_tax)
                   # The cost of the new state is the total tax paid so far
                   new_cost = g + coin_tax
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (g + new_total_tax, new_cost, actions + [coin], new_state))
   return None

print(a_star())
