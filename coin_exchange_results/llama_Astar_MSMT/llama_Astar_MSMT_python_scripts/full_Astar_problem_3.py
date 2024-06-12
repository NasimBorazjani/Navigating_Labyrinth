
import heapq


def initialize():
   # Define the list of coins and their tax values
   coins = [13, 19, 9, 4, 18, 17, 2, 14, 17, 17, 8, 6, 4, 10, 19, 37, 20, 19, 14, 7, 6, 11, 21, 9, 3, 10, 21, 20, 2, 17, 2]
   tax_values = {14: 2, 18: 9, 11: 10, 9: 6, 10: 9, 13: 10, 37: 9, 6: 5, 2: 2, 4: 1, 8: 3, 19: 10, 17: 7, 7: 6, 3: 3, 21: 3, 20: 4}
   target_sum = 215
   num_coins = len(coins)


   visited_costs = {}
   visited_costs[()] = 0


   queue = [(0, 0, ())]
  
   return coins, tax_values, target_sum, num_coins, visited_costs, queue
  
def a_star():
  
   coins, tax_values, target_sum, num_coins, visited_costs, queue = initialize()


   while queue:
       _, g, chosen_coins = heapq.heappop(queue)


       # If the sum of the chosen coins equals the target sum, return the chosen coins
       if sum(chosen_coins) == target_sum:
           return chosen_coins


       # Generate all possible actions from the current state, which includes adding the next coin to the chosen coins
       for coin_index in range(num_coins):
           coin = coins[coin_index]
           # Check if the coin can be added to the chosen coins, ie the sum of the chosen coins plus the coin does not exceed the target sum
           if sum(chosen_coins) + coin <= target_sum:
               # Generate the new state
               new_chosen_coins = chosen_coins + (coin,)
               # The cost of the new state is the tax value of the coin added
               new_cost = g + tax_values[coin]


               if new_chosen_coins not in visited_costs or new_cost < visited_costs[new_chosen_coins]:
                   visited_costs[new_chosen_coins] = new_cost
                   # The heuristic is the difference between the target sum and the sum of the chosen coins, as we are trying to minimize the sum of the chosen coins
                   h = target_sum - sum(new_chosen_coins)
                   heapq.heappush(queue, (new_cost + h, new_cost, new_chosen_coins))
   return None


print(a_star())
