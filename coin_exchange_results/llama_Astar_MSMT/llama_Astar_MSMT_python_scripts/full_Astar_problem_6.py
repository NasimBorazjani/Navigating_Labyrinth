
import heapq


def initialize():
   # Define the list of coins and their tax values
   coins = [20, 25, 10, 4, 13, 3, 10, 17, 5, 25, 17, 2, 19, 24, 25, 10, 19, 8, 2, 20, 15, 84, 23, 87, 19, 8, 12, 17, 23, 6]
   tax_values = {12: 12, 19: 8, 84: 20, 24: 1, 5: 1, 3: 1, 4: 2, 87: 7, 10: 5, 25: 7, 6: 5, 20: 5, 15: 7, 23: 17, 13: 4, 17: 16, 2: 1, 8: 5}
   target_sum = 250
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
       for coin in coins:
           # Check if the new state is valid, ie the new sum of the chosen coins does not exceed the target sum
           if sum(chosen_coins) + coin <= target_sum:
               # Generate the new state
               new_chosen_coins = chosen_coins + (coin,)
               # The cost so far is the sum of the tax values of the chosen coins, as the task is to minimize the total tax paid
               new_cost = g + tax_values[coin]


               if new_chosen_coins not in visited_costs or new_cost < visited_costs[new_chosen_coins]:
                   visited_costs[new_chosen_coins] = new_cost
                   # The heuristic is the difference between the target sum and the sum of the new state, as we are trying to minimize the sum of the chosen coins
                   h = target_sum - sum(new_chosen_coins)
                   heapq.heappush(queue, (new_cost + h, new_cost, new_chosen_coins))
   return None


print(a_star())
