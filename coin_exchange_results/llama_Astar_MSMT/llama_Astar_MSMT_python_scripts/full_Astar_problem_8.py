
import heapq


def initialize():
   # Define the list of coins and their tax values
   coins = [4, 17, 8, 15, 6, 14, 2, 4, 16, 10, 6, 5, 14, 8, 18, 2, 17, 9, 17, 59, 3, 10, 21, 4, 9, 14, 14, 20, 14, 8, 14, 18, 5, 16, 14, 17, 5, 3]
   tax_values = {15: 6, 5: 5, 17: 1, 14: 4, 2: 2, 8: 2, 10: 9, 59: 9, 16: 8, 4: 3, 18: 10, 20: 11, 21: 8, 6: 6, 9: 9, 3: 3}
   target_sum = 214
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
           # Check if the new state is valid, ie the sum of the chosen coins does not exceed the target sum
           if sum(chosen_coins) + coin <= target_sum:
               # Generate the new state
               new_chosen_coins = chosen_coins + (coin,)
               # The cost of the new state is the tax value of the coin added
               new_cost = g + tax_values[coin]


               if new_chosen_coins not in visited_costs or new_cost < visited_costs[new_chosen_coins]:
                   visited_costs[new_chosen_coins] = new_cost
                   # The heuristic is the difference between the target sum and the sum of the chosen coins in the new state
                   h = target_sum - sum(new_chosen_coins)
                   heapq.heappush(queue, (new_cost + h, new_cost, new_chosen_coins))
   return None


print(a_star())
