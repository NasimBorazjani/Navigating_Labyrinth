
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the chosen coins equaling 301
   goal_sum = 301
   # Define the tax values for each coin
   tax_values = {15: 2, 17: 10, 10: 3, 12: 10, 21: 12, 4: 2, 22: 1, 11: 6, 26: 9, 14: 7, 24: 12, 161: 16, 20: 15, 9: 8, 8: 1, 13: 10, 28: 6, 7: 6, 25: 6, 19: 15}
   # Define the list of coins
   coins = [22, 4, 12, 26, 4, 9, 4, 28, 28, 8, 28, 19, 15, 20, 9, 161, 11, 28, 17, 10, 25, 15, 7, 28, 21, 24, 10, 13, 22, 4, 10, 14]
   # Define the set of coins with the same tax value
   coins_same_tax = {15, 17, 10, 12, 4, 22, 11, 26, 14, 24, 161, 20, 9, 8, 13, 28, 7, 25, 19}
   # Define the set of coins with the same tax value and are smaller than the previous coin
   coins_smaller = {4, 10, 22, 4, 10, 22, 4, 14}
   # Define the set of coins with the same tax value and are larger than or equal to the previous coin
   coins_larger = {15, 17, 12, 26, 20, 28, 28, 28, 19, 21, 24, 25, 28, 161}


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if sum(state[0]) == goal_sum:
           return actions


       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the total sum of the chosen coins does not exceed the goal sum
           if coin not in state[0] and sum(state[0]) + coin <= goal_sum:
               # Generate the new state
               new_state = (state[0] | {coin}, state[1] + tax_values[coin])
               # The cost so far is the total tax paid so far, as the task is to minimize the total tax paid
               new_cost = g + tax_values[coin]


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum, tax_values, coins_same_tax, coins_smaller, coins_larger), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal_sum, tax_values, coins_same_tax, coins_smaller, coins_larger):
   # An admissible and consistent heuristic for this problem is the sum of the tax values of the remaining coins to be chosen, plus the tax value of the largest coin that can be chosen to reach the goal sum
   # This heuristic relaxes the constraint that the coin chosen must have an even value if it is smaller than the previous coin chosen and an odd value if it is larger than or equal to the previous coin chosen
   # It is admissible because it never overestimates the cost to reach the goal, as each remaining coin must be chosen at least once
   # It's consistent because moving a coin from the remaining set to the chosen set reduces the heuristic cost of the successor node by a max of the tax value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax value of the moved coin) + h(n)
   remaining_coins = set(coins) - state[0]
   h = sum(tax_values[coin] for coin in remaining_coins)
   # Find the largest coin that can be chosen to reach the goal sum
   for coin in sorted(remaining_coins, reverse=True):
       if sum(state[0]) + coin <= goal_sum:
           h += tax_values[coin]
           break
   return h


print(a_star())
