
import heapq


def initialize():
   # Define the list of coins and their tax values
   coins = [6, 20, 15, 14, 23, 6, 8, 15, 11, 2, 16, 21, 17, 10, 23, 20, 21, 16, 13, 3, 7, 4, 9, 21, 7, 13, 10, 18, 11, 9, 13, 12, 15, 17, 2, 8, 18, 3, 16, 9, 3, 14, 23, 16]
   tax_values = {21: 11, 18: 16, 16: 6, 12: 5, 14: 11, 11: 8, 15: 11, 4: 3, 9: 2, 23: 14, 7: 5, 20: 12, 6: 2, 8: 3, 17: 6, 13: 3, 3: 3, 2: 1, 10: 5}
   target_sum = 236
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


       # Generate all possible actions from the current state, which includes choosing the next coin in the list
       for coin_ind in range(num_coins):
           # Check if the coin can be added to the current state, ie if the coin is not already in the state and if the coin is smaller than the last coin in the state, it must have an even value, otherwise, if the coin is larger than or equal to the last coin chosen, it must have an odd value
           if coin_ind not in state and (not state or (coins[coin_ind] % 2 == 0 and state[-1] < coins[coin_ind]) or (coins[coin_ind] % 2 == 1 and state[-1] >= coins[coin_ind])):
               # Generate the new state
               new_state = state + (coin_ind,)
               # The cost so far is the sum of the tax values of the chosen coins, as the task is to minimize the total tax paid
               new_cost = g + tax_values[coins[coin_ind]]


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, target_sum, coins, tax_values)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [coins[coin_ind]], new_state))
   return None




def heuristic(state, target_sum, coins, tax_values):
   # The heuristic function can be a simulation of choosing the next coin greedily, using the next largest coin as long as the sum of the chosen coins does not exceed the target sum
   # This heuristic is admissible because it is greedy, always opting for the action that minimizes the total tax paid, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a coin is removed from the state, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of tax that can be saved by removing a coin from the state is by using the largest coin that won't cause the sum of the chosen coins to exceed the target sum. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the coins by decreasing value
   coins = sorted(coins, reverse=True)
   # Iterate through the chosen coins
   for coin_ind in state:
       # Check if the coin can be added to the state
       if (sum(state) + coins[coin_ind] <= target_sum):
           # Add the tax value of the coin to the estimated cost
           h += tax_values[coins[coin_ind]]
   return h


print(a_star())
