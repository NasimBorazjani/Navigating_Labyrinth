
import heapq


def initialize():
   # Define the list of coins and their tax values
   coins = [20, 10, 16, 21, 15, 21, 13, 6, 19, 9, 7, 5, 2, 6, 9, 22, 4, 13, 3, 16, 22, 18, 6, 5, 14, 7, 7, 2, 17, 9, 8, 83, 14]
   tax_values = {22: 18, 21: 1, 14: 12, 10: 8, 8: 6, 17: 9, 6: 4, 7: 6, 9: 3, 20: 13, 19: 12, 5: 3, 13: 8, 4: 3, 83: 14, 3: 2, 18: 1, 2: 1, 16: 2, 15: 3}
   target_sum = 239
   num_coins = len(coins)


   # Initialize the visited_costs dictionary and the priority queue
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
       for coin in coins:
           # Check if the new state is valid, ie the sum of the chosen coins does not exceed the target sum
           if sum(chosen_coins) + coin <= target_sum:
               # Generate the new state
               new_chosen_coins = chosen_coins + (coin,)
               # The cost so far is the sum of the tax values of the chosen coins, as the task is to minimize the total tax paid
               new_cost = g + tax_values[coin]


               if new_chosen_coins not in visited_costs or new_cost < visited_costs[new_chosen_coins]:
                   visited_costs[new_chosen_coins] = new_cost
                   # The heuristic is the difference between the target sum and the sum of the chosen coins, as we are trying to minimize the sum of the chosen coins
                   h = target_sum - sum(new_chosen_coins)
                   heapq.heappush(queue, (new_cost + h, new_cost, new_chosen_coins))
   return None


print(a_star())
