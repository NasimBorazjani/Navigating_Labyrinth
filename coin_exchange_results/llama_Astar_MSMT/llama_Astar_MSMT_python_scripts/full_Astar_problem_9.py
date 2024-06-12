
import heapq


def initialize():
   # Define the list of coins and their tax values
   coins = [3, 6, 9, 10, 13, 15, 18, 5, 21, 19, 12, 15, 5, 9, 4, 16, 8, 4, 7, 7, 7, 2, 16, 14, 18, 3, 89, 21, 12, 10, 7, 14, 4, 11, 6, 20]
   tax_values = {14: 1, 89: 13, 2: 2, 5: 2, 4: 4, 6: 6, 8: 2, 16: 5, 21: 4, 20: 2, 18: 9, 11: 10, 10: 3, 12: 12, 15: 5, 13: 1, 3: 1, 19: 19, 7: 7, 9: 3}
   # Define the target sum
   target_sum = 229
   # Define the previous coin chosen
   prev_coin = None


   visited_costs = {}
   visited_costs[()] = 0


   queue = [(0, 0, [], ())]
  
   return coins, tax_values, target_sum, prev_coin, visited_costs, queue
  
def a_star():
  
   coins, tax_values, target_sum, prev_coin, visited_costs, queue = initialize()


   while queue:
       _, g, coins_chosen, state = heapq.heappop(queue)


       # If the sum of the chosen coins equals the target sum, return the chosen coins
       if sum(coins_chosen) == target_sum:
           return coins_chosen


       # Generate all possible actions from the current state, which includes choosing the next coin from the list
       for coin in coins:
           # Check if the new state is valid, ie the coin is not already chosen and the sum of the chosen coins does not exceed the target sum
           if coin not in state and sum(coins_chosen) + coin <= target_sum:
               # Check if the coin is smaller than the previous coin chosen, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
               if prev_coin is not None and coin < prev_coin and coin % 2 != 0:
                   continue
               elif prev_coin is not None and coin >= prev_coin and coin % 2 == 0:
                   continue
               # Generate the new state
               new_state = state + (coin,)
               # The additional cost of this state is the tax value of the chosen coin
               new_cost = g + tax_values[coin]
              
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, target_sum), new_cost, coins_chosen + [coin], new_state))
   return None




def heuristic(state, target_sum):
   # The heuristic function can be a simulation of choosing the next coin greedily, using the next largest coin as long as the sum of the chosen coins does not exceed the target sum
   # This heuristic is admissible because it is greedy, always opting for the action that minimizes the total tax paid, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a coin is removed from the chosen coins, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of tax that can be saved by choosing the next coin in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the coins by decreasing value
   coins = sorted(state, reverse=True)
   # Iterate through the chosen coins
   for coin in coins:
       # Check if the coin is smaller than the previous coin chosen, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
       if prev_coin is not None and coin < prev_coin and coin % 2 != 0:
           continue
       elif prev_coin is not None and coin >= prev_coin and coin % 2 == 0:
           continue
       # The coin is valid, subtract its value from the target sum
       target_sum -= coin
       # If the target sum is reached, return the heuristic
       if target_sum == 0:
           return h
       # If the target sum is not reached, increment the estimated cost to the goal by 1 actions
       h += 1
   return h


print(a_star())
